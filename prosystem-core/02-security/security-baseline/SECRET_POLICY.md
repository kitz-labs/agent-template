# Secret Policy

Allowed in templates: environment-variable names and empty examples.

Forbidden: tokens, passwords, private keys, session cookies, database credentials and copied production `.env` files.

Logs must redact secret values. Agents must not print environment contents to troubleshoot authentication. Rotation is treated as a privileged operation and requires explicit authorization.
