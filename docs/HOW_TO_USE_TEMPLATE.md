# 🧩 How to Use This Template

This repository is designed to help you create **new AI agents in a repeatable way**.

## The 3 building blocks

Every new agent should be created from these 3 inputs:

1. **The template folder**
2. **The completed input brief**
3. **The master prompt for the coding agent**

## Step-by-step

### 1. Copy the template folder
Create a new project from `agent-template/`.

### 2. Define the business goal
Open `02_INPUT_BRIEF_TEMPLATE.md` and describe:
- what the agent should do
- who it serves
- what it must never do
- which tools it may use
- which APIs it needs
- which approvals are required

### 3. Hand everything to a coding agent
Provide:
- `agent-template/`
- `02_INPUT_BRIEF_TEMPLATE.md`
- `03_CODING_AGENT_MASTER_PROMPT.md`

### 4. Generate the final implementation
The coding agent should replace all placeholders and create the final project.

### 5. Validate before use
Use `04_ABNAHME_CHECKLISTE.md` before production or sharing.

## Best use cases

This template works especially well for:
- research agents
- support agents
- sales agents
- operations agents
- internal workflow agents
- API-integrated business agents
