# 🚀 Getting Started

Welcome to **Agent Template**.

This guide helps you go from repository clone to your first generated AI agent.

---

## 1. Clone the repository

```bash
git clone https://github.com/kitz-labs/agent-template.git
cd agent-template
```

## 2. Understand the structure

Important files:
- `README.md`
- `00_START_HERE.md`
- `02_INPUT_BRIEF_TEMPLATE.md`
- `03_CODING_AGENT_MASTER_PROMPT.md`
- `04_ABNAHME_CHECKLISTE.md`
- `09_AGENT_ERSTELLUNG_SCHRITT_FUER_SCHRITT.md`
- `10_COPY_PASTE_PROMPT_FUER_CODEX.md`

Important folder:
- `agent-template/`

## 3. Create a new agent project

```bash
cp -R agent-template my-agent
cd my-agent
```

## 4. Fill out the Input Brief

Use:

```text
02_INPUT_BRIEF_TEMPLATE.md
```

Describe:
- the agent goal
- target users
- tools
- APIs
- boundaries
- approvals
- tests
- deployment

## 5. Use a coding agent

Send the following to Codex or another coding agent:
- the template folder
- the completed input brief
- the master prompt

## 6. Validate the output

Use:

```text
04_ABNAHME_CHECKLISTE.md
```
