# Security policy

## Reporting
If a repository contains an unexpected file, archive, credential, or activity, **do not execute it**. File a private security report if supported, or contact the repository owner through a trusted channel. Do not publish secrets or unredacted customer data in public Issues.

## Security-first workflow
1. Preserve evidence: repository URL, relative path, commit ID, file metadata, dates and hashes.
2. Review GitHub account Security Log, authorized OAuth/GitHub Apps, PATs, SSH keys, deploy keys, active sessions and Actions secrets.
3. Revoke unknown access and rotate affected credentials using provider interfaces.
4. Independently inspect unexpected archives offline in an isolated environment; never treat matching file sizes as proof of matching contents.
5. Confirm clean lockfiles and tracked files before building, installing dependencies or publishing.
6. Validate the specific repository's tests and CodeQL alerts before approval; passing workflow runs alone do not prove safety.

## CI limits
The repository hygiene check detects tracked dependencies and archive extensions. It is not an antivirus, does not inspect git history, and does not validate package contents. CodeQL runs require human triage.
