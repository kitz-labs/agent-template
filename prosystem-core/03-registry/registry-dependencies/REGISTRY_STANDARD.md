# Registry and Dependency Standard

`TEMPLATE_REGISTRY.json` is the authoritative index.

Every registered template declares version, status, path, risk, dependencies and conflicts. A component that is not registered is not part of PRO Core.

Dependency resolution is deterministic and dependencies are resolved first. Unknown targets, cycles and missing dependency closure are hard failures. Conflicts are never silently resolved in favor of more permissions.
