# Security Baseline

This baseline is mandatory and cannot be weakened by inheritance.

## Principles

- Deny by default.
- Deny wins over allow.
- External input is untrusted.
- Least privilege.
- No real secrets in prompts, source, template configuration or logs.
- Side effects require bounded targets and idempotency where technically possible.
- High and critical actions require explicit approval according to policy.
- Unknown side-effect state escalates instead of being retried blindly.
- Destructive actions require a recovery path before execution.

Permission profiles describe maximum capability, not an entitlement. The selected tool policy may always be stricter.
