# GitHub engineering operating model (v0.1)

This is a **template library**, not an automatic deployment system. All production and local-server releases are disabled until each project has passed its own review and received explicit approval.

## 1. Development lifecycle
Backlog -> Triage -> Ready -> In Progress -> Review -> Verify -> Preview -> Done.
Use one GitHub Issue per actionable task, associate PRs with Issues, and prefer small vertical slices. Each sprint has a goal and acceptance criteria; no sprint is equivalent to permission to deploy.

### Roles
- Codex: architecture, implementation, backend, tests and technical plans.
- Claude: optional second reviewer; do not give automatic merge or deployment authority.
- Cursor / Antigravity: editor and UI-focused workflows where appropriate.
- Human: owns approvals, secrets, repository access, merging and deployments.

## 2. Branch and review policy
- Use feature branches (e.g. feat/issue-123), submit PRs, and require CI before merge where repository settings allow.
- No force pushes, repository deletion, automated mass changes, or publishing client/private data.
- Use least-privilege tokens, read-only CI for PRs, and GitHub-hosted runners for untrusted code.
- Do not attach self-hosted runners from personal Ubuntu machines to public PR workflows.

## 3. Supported build workflows
- Node.js, React, Next.js, NestJS, React Native and TypeScript use reusable-node-ci.yml when npm lockfile and scripts are verified.
- ASP.NET Core, C# and EF Core use reusable-dotnet-ci.yml after choosing project-specific SDK version and solution path.
- Database migrations and real database integration tests require isolated disposable test environments and are NOT run by default.
- JavaScript frontends without package.json can use a separate static validation workflow in their own repos.

## 4. Deployment mapping (not yet enabled)
- Static HTML/CSS/JS: GitHub Pages or Cloudflare Pages.
- Next.js frontend: Vercel previews, then approved production.
- NestJS / Node API: Railway or audited Docker/VPS.
- ASP.NET Core: Azure App Service or audited Docker/VPS.
- PostgreSQL/SQL Server: managed private instances or local dev containers; never expose directly to the Internet.
- Ubuntu-local demonstrations: authenticated Cloudflare Tunnel, not a publicly exposed privileged runner.

Environments: development -> preview -> staging -> production. Use environment protections, approval gates, per-environment secrets, and database backups/migration rollback plans.

## 5. Repository readiness gate
Before enabling build/install, review provenance, suspicious ZIP archives, tracked node_modules, credential leaks, licenses, dependency lockfiles, available tests, and legal authorization to publish. A workflow success does not mean security audit or usability testing is complete.

## 6. Adoption sequence
1. Inventory every repository and mark protected/active/legacy.
2. Choose one verified clean non-production pilot repository.
3. Adapt caller workflow to the repository's actual framework and SDK versions.
4. Run CI on a PR, inspect logs and fix blockers.
5. Set up a preview environment and secrets through provider-authorized UI.
6. Approve rollout repo by repo, then configure GitHub Projects and branch protection.
7. Review deployment safety, rollback procedures, access scopes and costs.

## 7. Known limitations
No GitHub Project board, hosting app, API secrets, production deploy, code scanning settings or local Ubuntu files are created by this document.
