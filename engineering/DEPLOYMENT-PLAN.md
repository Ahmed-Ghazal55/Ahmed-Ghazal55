# Controlled Preview and Deployment Plan

Status (2026-11-11): PLAN ONLY. Provider account/installations are unverified; no deployment target is approved for this pilot. No production deployments enabled by this sprint. See [hosting integration status](audits/2026-11-11/HOSTING_INTEGRATION_STATUS.md).

| Stack | Preview option | Release target |
| --- | --- | --- |
| Static JS/HTML | GitHub Pages or Cloudflare Pages | approved static host |
| React / Next.js | Vercel PR preview | Vercel |
| NestJS / Node.js | Railway staging | Railway or audited VPS |
| ASP.NET Core / .NET | Azure staging or Docker | Azure / VPS |
| PostgreSQL / SQL Server | isolated private test DB | managed private DB |
| React Native | device test build artifact | mobile distribution |
| Ubuntu local demo | protected Cloudflare Tunnel | no production by default |

## External connection checklist
- Account owner authorizes one hosting GitHub App with only selected repositories.
- Validate provider cost, region, build command, environmental secrets and data sensitivity.
- Create preview, staging and production environment approvals; never copy production secrets into PRs.
- Separate frontend URL and API domain, TLS, CORS, auth cookies, sanitized logging and backups.
- Test deploy and rollback in staging before production; require manual approval.
- Do not expose Docker socket, local database or personal workstation through an unrestricted tunnel.
