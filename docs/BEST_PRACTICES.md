# 🏆 Best Practices

Use these principles when creating agents from this template.

## 1. Keep scope explicit
Every agent should have:
- a clear purpose
- clear target users
- clear allowed actions
- clear forbidden actions

## 2. Treat prompts as files
Do not hide key system behavior in code.
Store prompts, policies, and runtime instructions in real files.

## 3. Use approval rules for risky actions
Anything that writes, sends, deletes, publishes, or triggers side effects should have approval logic.

## 4. Prefer config over hardcoding
Models, APIs, tools, thresholds, and routing should be configurable.

## 5. Validate tool inputs
Tool calls should be schema-checked or validated before execution.

## 6. Design for handoff
A good agent project should be understandable by someone new to the codebase.

## 7. Test more than the happy path
At minimum, test:
- prompt presence
- tool registry loading
- API binding setup
- guardrails
- end-to-end flow

## 8. Separate responsibilities
Keep prompts, tools, APIs, agent orchestration, safety, and observability modular.
