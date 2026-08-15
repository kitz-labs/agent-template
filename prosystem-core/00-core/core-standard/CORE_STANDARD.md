# PRO Core Standard

## Mandatory invariants

1. Every template has a unique lowercase kebab-case identifier.
2. Every stable template has an owner, semantic version, risk level and explicit required files.
3. Machine-readable configuration is canonical; documentation explains it but never overrides it.
4. Dependencies are explicit. Hidden dependencies are forbidden.
5. Conflicts are explicit and block composition.
6. Security is deny-by-default. A more permissive child template may never silently weaken the baseline.
7. Production status requires validation, tests, security review and evidence of completion.
8. Templates contain no real secrets, customer credentials or unrestricted production data.
9. Changes that break consumers require a major version increase and a migration note.
10. Generated systems must remain understandable without reading generator internals.

## Required template states

`draft -> experimental -> stable -> deprecated -> archived`

Only `stable` templates may be selected automatically for production.
