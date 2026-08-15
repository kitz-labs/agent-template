# Versioning

Use semantic versioning `MAJOR.MINOR.PATCH`.

- MAJOR: incompatible contract, schema, path or permission change.
- MINOR: backward-compatible capability or optional field.
- PATCH: correction with no contract break.

Every released change updates `CHANGELOG` or an equivalent release record. Production consumers pin a compatible version instead of silently following an unbounded latest version.
