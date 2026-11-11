# GitHub owner setup: exact UI steps

**Current state (2026-11-11):** CI, CodeQL and Dependabot exist. The [private engineering board](https://github.com/users/Ahmed-Ghazal55/projects/1) is configured with both Board and Table views. Vulnerability alerts are enabled. Restrictive rules await explicit approval; deployment environments are deferred. Use [current owner actions](audits/2026-11-11/OWNER_ACTIONS_REQUIRED.md) before the generic instructions below. Never create a second board or duplicate ruleset.

## A. Reuse the configured GitHub Projects board
1. Sign in to GitHub as Ahmed-Ghazal55.
2. Open https://github.com/users/Ahmed-Ghazal55/projects/1; do not create a new project.
3. Confirm **Engineering Delivery & Release Board** remains **Private**.
4. Existing **Status** options: Backlog, Ready, In Progress, Review, Verify, Preview, Done. Do not add a duplicate Stage field.
5. Existing **Workstream** options: Frontend / React / Next.js; Backend / Node.js / NestJS; C# / .NET; Database; Security; DevOps / Deployment; Documentation / Learning.
6. Existing **Project classification** options: Pilot, Active / Protected, Legacy, Learning. Avoid secrets or client data in issue text.
7. Issues #1, #5 and #6 are already linked; do not add duplicate items.
8. Current Status: #1 and #5 In Progress; #6 Ready. Change only after remaining work is verified.
9. Delivery board groups by Status; Engineering table displays the same fields. Optional: group the table by Workstream. Do not create empty recurring sprints.
10. Confirm the three Issues are visible and the private board has only approved collaborators.

## B. Configure branch protection / rulesets
1. Open https://github.com/Ahmed-Ghazal55/Ahmed-Ghazal55/settings/rules (requires repository admin and plan-supported rulesets).
2. Click **New ruleset > New branch ruleset** or use **Branch protection** if that is your interface.
3. Review `engineering/protect-main.proposal.json`, target `main`, and keep it disabled until the owner explicitly approves activation.
4. Block force pushes and branch deletion; require pull requests before merging, and require conversation resolution.
5. Choose checks after verifying their exact names in a recent successful PR run: Pilot shared workflows / hygiene-smoke / inventory, Pilot shared workflows / node-smoke / verify-node, Pilot shared workflows / dotnet-smoke / verify-dotnet. Check names can appear differently in the UI: use the literal GitHub-provided entries rather than assuming these examples.
6. Require review count only if you have another independent reviewer; a solo account can otherwise deadlock its own merges. Prefer a practical documented solo exception.
7. Preview the effective rules and confirm you can still merge a reviewed test PR before extending to other repositories.

## C. Configure environments
1. When a specific deployment-ready repository is selected, open that repository's **Settings > Environments**.
2. Create **preview**, **staging**, **production**.
3. For production, configure required reviewers / protection rules if supported by the account and repo plan.
4. Configure deployment branches and environment-scoped secrets; never use production credentials in a preview PR.
5. Prefer provider OIDC where supported. Only then add a deployment workflow; nothing deploys from this template library.
6. Test staging, rollback, credential revocation and logs before enabling production.

## D. Review Dependabot and CodeQL
1. Open https://github.com/Ahmed-Ghazal55/Ahmed-Ghazal55/pulls and filter author `dependabot[bot]`.
2. For each update PR, read the changelog, supported Node/runtime requirements, licenses, permissions and workflow modifications.
3. Inspect successful PR checks and consider merging one update at a time; never auto-merge a major update without compatibility review.
4. Open https://github.com/Ahmed-Ghazal55/Ahmed-Ghazal55/security/code-scanning if visible and review alerts individually, not just the Actions run status. This repository already uses a custom CodeQL workflow (advanced setup): do NOT enable default setup on top without deliberately migrating, because it may disable or duplicate the custom scan.
5. Inspect https://github.com/Ahmed-Ghazal55/Ahmed-Ghazal55/actions and confirm the last CodeQL and Pilot runs succeeded.
6. Check Settings > Security & analysis / Advanced Security for features available on your plan.

## E. Connect hosting apps (one repository at a time)
1. Create or sign in to Vercel (Next.js previews), Railway (Node/NestJS), Cloudflare (static preview and protected tunnel), and optionally Azure (.NET deployment).
2. Open the provider dashboard; select **New project / Import from GitHub / Connect GitHub**.
3. In GitHub's authorization screen, confirm app publisher, requested OAuth/App permissions, and select **Only select repositories**.
4. Choose a sanitized non-client pilot repo; never grant unrestricted access to legacy repos with unverified ZIP files.
5. Set build root, framework/runtime version, preview branch, region and budget controls in the provider.
6. Add provider environment variables through the provider UI. Do not store secrets in Git or chat.
7. Produce and verify a preview URL; test frontend API origin/CORS, access control, smoke tests and server logs.
8. Disable automatic production promotion; add guarded staging and rollback. Record deployment URL only after a successful preview.

## F. Ubuntu local / remote servers
1. Avoid self-hosted Actions runners on your normal desktop for public repositories.
2. For a local demo, use a separately reviewed **Cloudflare Tunnel** with Cloudflare Access authentication and a restricted app port, not an open database connection.
3. For Docker deployment, use a dedicated server with limited SSH deploy account and secrets outside Git; publish images to GHCR only after container scanning.
4. For PostgreSQL / SQL Server, keep DB ports private, require backups and a tested restore procedure, and run migrations only in approved staging/production release workflows.

## G. Local repository inventory (read-only)
Run this in your Ubuntu terminal and review output before syncing any project:

```bash
ROOT="$HOME/Projects"
find "$ROOT" -type d -name .git -prune -print |
while IFS= read -r gitdir; do
  repo="${gitdir%/.git}"
  echo "=== $repo ==="
  git -C "$repo" status --short --branch || true
  git -C "$repo" remote -v || true
done
```

Do **not** run git pull, reset --hard, clean -fd, or delete archives before the provenance review.
