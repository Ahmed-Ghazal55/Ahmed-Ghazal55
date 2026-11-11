# Hosting integration status — 2026-11-11

**Prepared, intentionally deferred.** No deployment target has owner approval. The engineering repository is a CI template library and does not need empty deployment environments. Environments list is empty, deployments list is empty, and Pages returned 404. No environment, secret, account connection, domain, tunnel, server, database or paid resource was created.

Provider account and installation state is **unverified**, not absent. `user/installations` cannot be enumerated with this OAuth token. Vercel, Railway, Wrangler, Cloudflared and Azure CLIs are not installed; this does not prove account absence. Docker is already installed and was not replaced or reconfigured. GHCR package listing requires `read:packages`; publication was not attempted.

| Provider | Appropriate use after target approval | Exact owner entry point | Authorization boundary |
|---|---|---|---|
| Vercel | Next.js PR preview | https://vercel.com/login then https://vercel.com/new | Inspect existing GitHub connection first; selected repository only; contents read and only provider-documented deployment/check permissions |
| Railway | NestJS / Node API | https://railway.com/login then https://railway.com/dashboard | Inspect existing connection; select one approved API repo; confirm costs before creating any service/database |
| Cloudflare Pages | Appropriate static website | https://dash.cloudflare.com/ → Workers & Pages → Create → Pages → Connect to Git | Select approved static repo; review requested content/metadata/check/deployment permissions in the actual authorization screen |
| Cloudflare Tunnel + Access | Protected Ubuntu demonstration | https://one.dash.cloudflare.com/ | Explicit separate approval; restricted app port and Access policy; no public database or Docker socket |
| Azure App Service | Suitable .NET application | https://portal.azure.com/ → App Services; existing app → Deployment Center | Verify tenant/subscription and existing resources before authorization; no subscription-wide role or resource creation implied |
| Docker / GHCR | Container build and approved image publication | https://github.com/Ahmed-Ghazal55?tab=packages | Future publisher uses least-privilege `packages: write`; no package authorization added now |

Inspect current authorizations at https://github.com/settings/installations and https://github.com/settings/applications. A live OAuth authorization URL includes provider-generated state and must come from the owner's selected provider flow; none was fabricated or initiated. The URLs above are login/connection entry points, not claims that OAuth completed. Do not grant All Repositories access. Choose one hosting provider per application role instead of connecting redundant providers.

## Deployment-ready repository checklist
Only after an actual target is selected: create preview/staging/production in that repository; separate environment secrets and data; restrict production to the approved release branch; configure human approval where supported, and no automatic production promotion. If the plan cannot enforce the intended approval, leave production workflow absent. Do not copy secrets into this report.

Rollback must name the last known-good artifact/image digest or provider release, health checks, authorized operator and credential revocation steps. Database rollback requires tested restore/migration procedures on staging. None of those runtime validations can be claimed without a selected application and deployment target.
