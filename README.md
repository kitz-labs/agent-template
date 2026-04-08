# 🤖 Agent Template

> A reusable premium AI agent template for building production-ready agents with prompts, tools, API bindings, configs, tests, Docker, and documentation.

<p align="center">
  <strong>Build powerful AI agents faster, cleaner, and more consistently.</strong>
</p>

<p align="center">
  <a href="https://kitzlabs.ai">
    <img alt="Visit kitzlabs.ai" src="https://img.shields.io/badge/Visit-kitzlabs.ai-111827?style=for-the-badge" />
  </a>
</p>

<p align="center">
  <a href="bitcoin:37Ndnsy6GcNWCZjX4aDmtSBBzaehpkkuNA">
    <img alt="Buy me a coffee with Bitcoin" src="https://img.shields.io/badge/☕%20Buy%20me%20a%20coffee-Bitcoin-F7931A?style=for-the-badge" />
  </a>
</p>

---

## ✨ What is this?

**Agent Template** is a reusable, structured foundation for creating new AI agents.

It is designed for:
- ⚡ fast agent creation
- 🧱 clean architecture
- 🛡️ strong safety and approval rules
- 🔌 tool integrations and API bindings
- 🧪 tests and production readiness
- 📚 documentation that other developers can actually use

This repository is ideal if you want to:
- build internal AI agents
- standardize how agents are created
- hand a complete blueprint to Codex or other coding agents
- create repeatable, scalable agent projects

---

## 🚀 Quickstart

### 1. Clone the repository

```bash
git clone https://github.com/kitz-labs/agent-template.git
cd agent-template
```

### 2. Copy the template into a new agent project

```bash
cp -R agent-template my-new-agent
cd my-new-agent
```

### 3. Fill out the input brief

Open and complete:

```text
02_INPUT_BRIEF_TEMPLATE.md
```

### 4. Use the coding-agent prompt

Send these to Codex or another coding agent:
- the `agent-template/` folder
- your completed `02_INPUT_BRIEF_TEMPLATE.md`
- `03_CODING_AGENT_MASTER_PROMPT.md`

### 5. Generate your full agent

The coding agent should create:
- full source code
- prompt files
- tool wiring
- API bindings
- tests
- Docker setup
- docs
- runbook

---

## 🧠 Core idea

The formula is simple:

```text
Template + Input Brief + Master Prompt = Complete AI Agent
```

Instead of explaining your full architecture every single time, you use a **repeatable template system**.

---

## 📦 What’s inside?

```text
agent-template/
├── configs/
├── prompts/
├── api/
├── tools/
├── src/
├── tests/
├── docs/
├── scripts/
└── data/
```

Top-level helper files include:
- `00_START_HERE.md`
- `02_INPUT_BRIEF_TEMPLATE.md`
- `03_CODING_AGENT_MASTER_PROMPT.md`
- `04_ABNAHME_CHECKLISTE.md`
- `08_PREMIUM_GOVERNANCE.md`
- `09_AGENT_ERSTELLUNG_SCHRITT_FUER_SCHRITT.md`
- `10_COPY_PASTE_PROMPT_FUER_CODEX.md`

---

## 🛠️ What this template covers

### Prompt system
- system prompts
- safety prompts
- style guide prompts
- approval prompts
- runtime prompts
- task prompts
- few-shot examples

### Tooling
- tool registry
- tool schemas
- tool implementations
- validation hooks
- approval handling for high-risk actions

### API integrations
- API client registry
- REST client templates
- auth handler templates
- request / response schemas
- config-driven API bindings

### Engineering setup
- FastAPI scaffold
- modular agent orchestration
- config files
- environment variables
- tests
- Docker
- Makefile
- docs and runbook

---

## 🔐 Premium governance

This repo includes an ultra-strict premium structure.

That means:
- no hidden prompts in code
- no tools without registry entries
- no APIs without binding files
- no secrets in source code
- no unsafe write actions without approval rules
- no production release without tests

See:
- `08_PREMIUM_GOVERNANCE.md`
- `agent-template/configs/approval_matrix.yaml`
- `agent-template/prompts/system/approval_policy.md`

---

## 🧭 How to create a new agent

### Step 1
Copy `agent-template/` into a fresh project folder.

### Step 2
Complete the business and technical requirements in:

```text
02_INPUT_BRIEF_TEMPLATE.md
```

### Step 3
Give a coding agent these 3 things:
- the template folder
- the completed input brief
- the master prompt

### Step 4
Let the coding agent replace all placeholders and generate the final implementation.

### Step 5
Validate the result with:

```text
04_ABNAHME_CHECKLISTE.md
```

---

## 📚 Documentation

Additional docs:
- [`docs/GETTING_STARTED.md`](docs/GETTING_STARTED.md)
- [`docs/HOW_TO_USE_TEMPLATE.md`](docs/HOW_TO_USE_TEMPLATE.md)
- [`docs/TEMPLATE_STRUCTURE.md`](docs/TEMPLATE_STRUCTURE.md)
- [`docs/BEST_PRACTICES.md`](docs/BEST_PRACTICES.md)
- [`docs/MONETIZATION.md`](docs/MONETIZATION.md)
- [`docs/SUPPORT.md`](docs/SUPPORT.md)

---

## 💼 Can I monetize this?

Yes.

Common models:
- offer the base template publicly
- sell premium packs or advanced agent kits
- offer setup / implementation services
- offer done-for-you custom agent builds
- offer support, onboarding, and consulting

See:
- [`docs/MONETIZATION.md`](docs/MONETIZATION.md)

---

## 👥 Who is this for?

- founders
- AI builders
- agencies
- internal product teams
- automation engineers
- developers working with Codex or coding agents

---

## ✅ Recommended workflow

1. define the agent scope
2. complete the input brief
3. pass template + brief + prompt to a coding agent
4. review generated files
5. run tests
6. validate against the checklist
7. deploy safely

---

## 🌍 Why this repository exists

Most people don’t fail because they lack ideas.  
They fail because they rebuild the same agent architecture from scratch every time.

This template solves that.

It gives you a **repeatable system** for building agents that are:
- structured
- safer
- easier to maintain
- easier to hand off
- easier to scale

---

## ☕ Support This Project

If this repository helps you, you can support the work with **Bitcoin**.

<p align="center">
  <a href="bitcoin:37Ndnsy6GcNWCZjX4aDmtSBBzaehpkkuNA">
    <img alt="Buy me a coffee with Bitcoin" src="https://img.shields.io/badge/☕%20Buy%20me%20a%20coffee-Bitcoin-F7931A?style=for-the-badge" />
  </a>
</p>

<p align="center">
  <strong>Bitcoin Address</strong><br/>
  <code>37Ndnsy6GcNWCZjX4aDmtSBBzaehpkkuNA</code>
</p>

More details:
- [`docs/SUPPORT.md`](docs/SUPPORT.md)

---

## 🤝 Contributing

Contributions, improvements, and premium extensions are welcome.

Please read:
- [`CONTRIBUTING.md`](CONTRIBUTING.md)

---

## 📄 License

This repository is licensed under the MIT License unless noted otherwise.

---

## ⭐ Support the project

If this template helps you, consider:
- starring the repo
- forking it
- using it in your own AI agent workflows
- reaching out for premium implementations

---

<p align="center">
  <strong>Built by AI Kitz Art & Labs</strong><br/>
  Reusable systems for next-generation AI agents.
</p>
