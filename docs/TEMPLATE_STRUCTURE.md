# 🗂️ Template Structure

This repository contains two layers:

## 1. Top-level project guidance
These files explain how to use the template:
- `00_START_HERE.md`
- `01_TEMPLATE_UEBERSICHT.md`
- `02_INPUT_BRIEF_TEMPLATE.md`
- `03_CODING_AGENT_MASTER_PROMPT.md`
- `04_ABNAHME_CHECKLISTE.md`
- `08_PREMIUM_GOVERNANCE.md`
- `09_AGENT_ERSTELLUNG_SCHRITT_FUER_SCHRITT.md`
- `10_COPY_PASTE_PROMPT_FUER_CODEX.md`

## 2. The technical scaffold
The `agent-template/` folder contains the reusable engineering foundation.

```text
agent-template/
├── configs/
├── prompts/
├── api/
├── tools/
├── src/
├── tests/
├── scripts/
├── docs/
└── data/
```

## Folder overview

### `configs/`
Central configuration for models, tools, memory, security, routing, approvals, and APIs.

### `prompts/`
All prompt files such as system prompts, safety rules, approval policy, runtime prompts, task prompts, and few-shot examples.

### `api/`
API binding templates, schemas, and OpenAPI helpers.

### `tools/`
Tool registry, tool schemas, and tool implementations.

### `src/`
Application logic, orchestration, web layer, integrations, memory, safety, and observability.

### `tests/`
Prompt, tooling, routing, guardrail, and end-to-end tests.
