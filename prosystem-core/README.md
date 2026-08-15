# Pro System Templates — PRO Core

Version 1.0.0 is the mandatory foundation for new Pro System agents and template-driven projects.

## Five mandatory components

1. `core-standard` — naming, lifecycle, versioning, quality gates and composition rules.
2. `production-agent` — complete production-ready agent contract aligned with the existing Pro System agent structure.
3. `security-baseline` — deny-by-default security, risk levels, approvals, secret handling and permission profiles.
4. `registry-dependencies` — one authoritative registry with dependency and conflict rules.
5. `validator-tests` — zero-dependency validator, tests and continuous validation contract.

## Golden rule

No template is production-ready unless the validator passes and all required quality gates are satisfied.

## Local validation

```bash
python3 tools/validate_templates.py .
python3 -m unittest discover -s tests -v
```

## Production-agent composition validation

```bash
python3 tools/validate_templates.py . --select core-standard security-baseline registry-dependencies validator-tests production-agent
```

The core never stores real secrets. `.env.example` may contain names only, never secret values.
