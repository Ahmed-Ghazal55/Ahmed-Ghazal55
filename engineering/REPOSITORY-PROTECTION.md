# GitHub Branch Protection and Environment Policy

Status: Prepared policy. GitHub rulesets, Projects boards and Environments have NOT been created or changed.

## Branch rules for approved repositories
- Protect main from deletion and force pushes.
- Require pull request reviews and conversation resolution for teams.
- Require successful CI checks only after verifying real job names and results.
- Require admins to follow rules where supported; document emergency bypass.
- Apply these settings per repository; never blindly change protected client projects.

## Environments
- preview: isolated test data and nonproduction credentials
- staging: separate secrets, tests, health checks, restore/rollback plan
- production: required human reviewers, approved branches and recovery process

## GitHub security
- Least privilege, short-lived OIDC where supported, no secrets in source.
- Scan tracked vendor trees, unknown archives, tokens and license provenance before publishing.
- Never run public PRs on a personal Ubuntu self-hosted runner.
- Keep database ports, Docker daemon sockets and admin endpoints private.

## Owner actions
Use GitHub Settings -> Rules -> Rulesets and Settings -> Environments in the relevant repository after CI verification. The connected GitHub app cannot create or modify those settings.
