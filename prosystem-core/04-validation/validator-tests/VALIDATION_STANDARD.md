# Validation Standard

The validator is intentionally zero-dependency Python so it can run before project dependencies are installed.

Hard failures include:

- missing repository control files;
- invalid semantic versions;
- unknown or cyclic dependencies;
- selected composition without dependency closure;
- explicit template conflicts;
- descriptor/registry mismatches;
- missing required files;
- unsafe relative paths;
- violation of deny-by-default security invariants;
- likely committed secrets or forbidden secret-bearing filenames.

A failing validator blocks release.
