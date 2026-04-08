# How to Create a New Agent

## Formula
Template + Input Brief + Master Prompt = finished agent

## Workflow
1. Copy `agent-template/` into a new project folder.
2. Complete `02_INPUT_BRIEF_TEMPLATE.md`.
3. Send the template folder, the completed brief, and `03_CODING_AGENT_MASTER_PROMPT.md` to Codex or another coding agent.
4. Let the coding agent replace all placeholders and generate the full implementation.
5. Validate the result with `04_ABNAHME_CHECKLISTE.md`.
6. Only then move toward production use.

## What to send to a coding agent
- the full `agent-template/` folder
- the completed input brief
- the master prompt

## What should come back
- full codebase
- prompt files
- tool registry
- API bindings
- tests
- docs
- run instructions
