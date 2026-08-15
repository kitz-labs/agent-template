# Production Agent Acceptance Checklist

- [ ] All required source files exist.
- [ ] `agent.yaml` matches the intended role and risk.
- [ ] Permission profile is least-privilege.
- [ ] Tools and Model Context Protocol access are explicit.
- [ ] Handoffs are bounded and schema-based.
- [ ] Memory has provenance, scope and retention rules.
- [ ] Approval gates cover dangerous side effects.
- [ ] Automated test suite passes.
- [ ] Evaluation criteria are defined.
- [ ] Observability does not leak secrets.
- [ ] Rollback or recovery is documented for state changes.
- [ ] Release evidence exists before production status.
