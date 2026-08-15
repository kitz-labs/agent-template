# Lifecycle

Template lifecycle:

`draft -> experimental -> stable -> deprecated -> archived`

Generated production system lifecycle:

`design -> configured -> testing -> staging -> approved -> production -> monitored -> deprecated -> archived`

A transition to `approved` requires evidence for tests, security and rollback readiness. A transition to `production` requires explicit deployment authorization where side effects exist.
