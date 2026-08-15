#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

SEMVER = re.compile(r'^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$')
STATUS = {'draft','experimental','stable','deprecated','archived'}
RISK = {'low','medium','high','critical'}
CONTROL = ('README.md','VERSION','TEMPLATE_REGISTRY.json','tools/validate_templates.py','tests/test_validator.py')
PROD_DEPS = {'core-standard','security-baseline','registry-dependencies','validator-tests'}
CONFIRM = {'payments','refunds','dns_changes','database_writes','production_deploy','service_restart','nginx_reload','file_delete','env_change','secret_rotation','customer_data_export'}
SECRET = [re.compile(r'\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b'), re.compile(r'\bgh[pousr]_[A-Za-z0-9]{20,}\b'), re.compile(r'\bAKIA[0-9A-Z]{16}\b'), re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----')]
TEXT = {'.md','.txt','.json','.yaml','.yml','.toml','.ini','.env','.py','.sh','.js','.ts'}

class ValidationError(Exception):
    pass

@dataclass
class ValidationReport:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    @property
    def ok(self) -> bool:
        return not self.errors

def _load(path: Path, errors: list[str]) -> dict:
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except FileNotFoundError:
        errors.append(f'Missing file: {path}')
    except json.JSONDecodeError as exc:
        errors.append(f'Invalid JSON in {path}: line {exc.lineno}')
    return {}

def _safe(value: object) -> bool:
    if not isinstance(value, str) or not value.strip():
        return False
    path = Path(value)
    return not path.is_absolute() and '..' not in path.parts

def _cycles(graph: dict[str, list[str]]) -> list[list[str]]:
    found, stack = [], []
    state = {node: 0 for node in graph}
    def visit(node: str) -> None:
        state[node] = 1
        stack.append(node)
        for nxt in graph.get(node, []):
            if nxt not in state:
                continue
            if state[nxt] == 0:
                visit(nxt)
            elif state[nxt] == 1:
                found.append(stack[stack.index(nxt):] + [nxt])
        stack.pop()
        state[node] = 2
    for node in graph:
        if state[node] == 0:
            visit(node)
    return found

def _scan_secrets(root: Path, errors: list[str]) -> None:
    for path in root.rglob('*'):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        if any(part in {'.git','__pycache__'} for part in rel.parts):
            continue
        if path.name in {'.env','id_rsa','id_ed25519'}:
            errors.append(f'Forbidden secret-bearing filename: {rel}')
            continue
        if path.name == '.env.example':
            continue
        if path.suffix.lower() not in TEXT and path.name != 'VERSION':
            continue
        if path.stat().st_size > 1_000_000:
            continue
        text = path.read_text(encoding='utf-8', errors='replace')
        if any(pattern.search(text) for pattern in SECRET):
            errors.append(f'Potential secret detected in {rel}')

def validate_repository(root: str | Path, selected: Iterable[str] | None = None) -> ValidationReport:
    root = Path(root).resolve()
    report = ValidationReport()
    if not root.is_dir():
        report.errors.append(f'Root directory does not exist: {root}')
        return report
    for rel in CONTROL:
        if not (root / rel).is_file():
            report.errors.append(f'Missing repository control file: {rel}')
    try:
        version = (root / 'VERSION').read_text(encoding='utf-8').strip()
    except FileNotFoundError:
        version = ''
    if version and not SEMVER.fullmatch(version):
        report.errors.append(f'VERSION is not valid semver: {version!r}')
    registry = _load(root / 'TEMPLATE_REGISTRY.json', report.errors)
    templates = registry.get('templates', {}) if isinstance(registry, dict) else {}
    if registry and registry.get('schema_version') != 1:
        report.errors.append('TEMPLATE_REGISTRY.json schema_version must be 1')
    if not isinstance(templates, dict) or not templates:
        report.errors.append('TEMPLATE_REGISTRY.json templates must be a non-empty object')
        templates = {}
    graph: dict[str, list[str]] = {}
    for template_id, entry in templates.items():
        if not isinstance(entry, dict):
            report.errors.append(f'Registry entry {template_id} must be an object')
            continue
        missing = {'version','status','path','risk','dependencies','conflicts'} - set(entry)
        if missing:
            report.errors.append(f'Registry entry {template_id} missing fields: {", ".join(sorted(missing))}')
            continue
        if not SEMVER.fullmatch(str(entry['version'])):
            report.errors.append(f'Registry entry {template_id} has invalid semver: {entry["version"]!r}')
        if entry['status'] not in STATUS:
            report.errors.append(f'Registry entry {template_id} has invalid status')
        if entry['risk'] not in RISK:
            report.errors.append(f'Registry entry {template_id} has invalid risk')
        if not _safe(entry['path']):
            report.errors.append(f'Registry entry {template_id} has unsafe path')
            continue
        deps = entry['dependencies'] if isinstance(entry['dependencies'], list) else []
        conflicts = entry['conflicts'] if isinstance(entry['conflicts'], list) else []
        graph[template_id] = [dep for dep in deps if isinstance(dep, str)]
        for dep in deps:
            if dep not in templates:
                report.errors.append(f'Template {template_id} has unknown dependency: {dep}')
        for conflict in conflicts:
            if conflict not in templates:
                report.errors.append(f'Template {template_id} has unknown conflict target: {conflict}')
        descriptor = _load(root / entry['path'] / 'template.json', report.errors)
        if descriptor:
            for key in ('id','version','status','risk','owner','required_files'):
                if key not in descriptor:
                    report.errors.append(f'Template {template_id} descriptor missing field: {key}')
            if descriptor.get('id') != template_id:
                report.errors.append(f'Template ID mismatch: {template_id}')
            if descriptor.get('version') != entry['version']:
                report.errors.append(f'Version mismatch for {template_id}')
            if descriptor.get('status') != entry['status']:
                report.errors.append(f'Status mismatch for {template_id}')
            if descriptor.get('risk') != entry['risk']:
                report.errors.append(f'Risk mismatch for {template_id}')
            for rel_file in descriptor.get('required_files', []):
                if not _safe(rel_file) or not (root / entry['path'] / rel_file).is_file():
                    report.errors.append(f'Template {template_id} missing required file: {rel_file}')
        if entry.get('kind') == 'production-agent':
            for dep in sorted(PROD_DEPS - set(deps)):
                report.errors.append(f'Production agent {template_id} must depend on {dep}')
        if entry.get('kind') == 'security-baseline':
            policy = _load(root / entry['path'] / 'security-policy.json', report.errors)
            if policy:
                if policy.get('default_decision') != 'deny':
                    report.errors.append('Security baseline default_decision must be deny')
                if policy.get('deny_wins') is not True:
                    report.errors.append('Security baseline deny_wins must be true')
                if policy.get('secrets_in_prompt_or_config') is not False:
                    report.errors.append('Security baseline secrets_in_prompt_or_config must be false')
                if set(policy.get('risk_levels', [])) != RISK:
                    report.errors.append('Security baseline risk_levels must contain low, medium, high, critical')
                missing_confirm = CONFIRM - set(policy.get('confirmation_required_for', []))
                if missing_confirm:
                    report.errors.append('Security baseline confirmation_required_for missing: ' + ', '.join(sorted(missing_confirm)))
    for cycle in _cycles(graph):
        report.errors.append('Dependency cycle detected: ' + ' -> '.join(cycle))
    if selected is not None:
        chosen = set(selected)
        for unknown in chosen - set(templates):
            report.errors.append(f'Selected unknown template: {unknown}')
        for template_id in chosen & set(templates):
            entry = templates[template_id]
            for conflict in entry.get('conflicts', []):
                if conflict in chosen:
                    report.errors.append(f'Template conflict: {template_id} conflicts with {conflict}')
            for dep in entry.get('dependencies', []):
                if dep not in chosen:
                    report.errors.append(f'Selected template {template_id} requires missing dependency {dep}')
    _scan_secrets(root, report.errors)
    return report

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description='Validate Pro System Templates')
    parser.add_argument('root', nargs='?', default='.')
    parser.add_argument('--select', nargs='*')
    args = parser.parse_args(argv)
    report = validate_repository(args.root, args.select)
    for error in report.errors:
        print('ERROR:', error)
    print('OK: Pro System template validation passed' if report.ok else f'FAILED: {len(report.errors)} error(s)')
    return 0 if report.ok else 1

if __name__ == '__main__':
    raise SystemExit(main())
