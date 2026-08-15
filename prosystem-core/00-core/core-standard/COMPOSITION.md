# Composition Rules

Composition is dependency-driven.

- Resolve dependencies before consumers.
- Reject unknown dependencies.
- Reject dependency cycles.
- Reject explicit conflicts.
- Require the full dependency closure for a selected production composition.
- Security rules merge using the stricter result; deny wins.
- Permission expansion is never implicit.
- A production agent always includes core, security, registry and validator components.
