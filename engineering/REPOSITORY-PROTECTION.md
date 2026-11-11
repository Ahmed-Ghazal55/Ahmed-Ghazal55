# GitHub Branch Protection and Environment Policy

Status (2026-11-11): [private engineering board](https://github.com/users/Ahmed-Ghazal55/projects/1) configured. Main protection is [active ruleset 27044588](https://github.com/Ahmed-Ghazal55/Ahmed-Ghazal55/rules/27044588) after explicit owner approval and verified CI/merge. The [JSON proposal](protect-main.proposal.json) stays disabled as a safe import template. Environments are intentionally deferred until a deployment target is approved. See the [current audit](audits/2026-11-11/EXECUTION_SUMMARY.md).

## Branch rules for approved repositories
- Protect main from deletion and force pushes.
- Require pull requests and conversation resolution. The solo pilot requires zero approvals; teams may add independent reviewers when available.
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
Use GitHub Settings -> Rules -> Rulesets after CI verification and explicit activation approval. The authenticated CLI has repository administration access; the separate connected app may have narrower access. Configure Environments only for an approved deployment-ready application.
