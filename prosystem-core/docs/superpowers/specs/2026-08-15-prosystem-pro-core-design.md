# Pro System PRO Core Design

## Goal
Create one authoritative, modular and machine-validatable foundation for all future Pro System templates.

## Scope
Exactly five mandatory components: Core Standard, Production Agent, Security + Permissions, Registry + Dependencies, Validator + Tests.

## Architecture
The root registry is authoritative. Each component owns one directory with a machine-readable descriptor and human documentation. The production agent composes the other four components. Security is deny-by-default and cannot be weakened by composition. A zero-dependency Python validator enforces structural, graph, version, security and secret invariants.

## Data flow
Template selection -> registry lookup -> dependency closure -> conflict checks -> security invariants -> required-file checks -> secret scan -> tests -> release gate.

## Failure handling
Unknown dependencies, cycles, conflicts, missing files, invalid versions, security-baseline weakening and likely secrets are hard failures. Unknown side-effect state escalates rather than retries blindly.

## Testing
Test-first unit coverage for valid repository, missing files, cycles, unknown dependencies, conflicts, secret detection, semantic versioning, production-agent dependencies, repository control files and security invariants. Whole-repository validation is the final integration test.
