# Owner actions required — 2026-11-11

## 1. Main protection is complete
Owner approved activation after verified PR #11 merge. [Ruleset 27044588](https://github.com/Ahmed-Ghazal55/Ahmed-Ghazal55/rules/27044588) is **active** on main only. Its independent API readback confirms seven required GitHub Actions checks, PRs, resolved conversations, blocked deletion/force pushes, zero approvals and no bypass actors. The extra unattributed-change approval flag is explicitly false. Main reports `protected: true`.

No further protection authorization is required for this pilot. Review the existing ruleset at [Settings → Rules → protect-main](https://github.com/Ahmed-Ghazal55/Ahmed-Ghazal55/settings/rules/27044588); do not create another one. The JSON proposal remains disabled as an import-safe template; it does not describe live enforcement. Future changes to other repositories still need separate scope and approval.

## 2. Hosting/account visibility
Open https://github.com/settings/installations and https://github.com/settings/applications to inspect the existing Vercel/Railway/Cloudflare/Azure connections and repository access. The CLI OAuth token cannot enumerate installations. Do not install an App or expand repository access just for inventory. Select a single application and provider before any OAuth/install flow, and review the actual permissions at that point. Exact provider entry URLs and target-specific steps are in [HOSTING_INTEGRATION_STATUS.md](HOSTING_INTEGRATION_STATUS.md).

Optional GHCR inventory is blocked by missing `read:packages`. If package inventory becomes necessary, owner approval precedes `gh auth refresh -h github.com -s read:packages`. It is not needed for the current CI work. Projects authorization was already approved and completed; no new token or repeat login is needed.

## 3. Existing security investigation
Continue [issue #6](https://github.com/Ahmed-Ghazal55/Ahmed-Ghazal55/issues/6) with a separately approved isolated static/hash/history investigation of the 20 archive paths across 10 public repositories. Shopping also has 24,094 tracked dependency-tree paths. No malware conclusion is established. Do not install dependencies, execute or remove archive contents, rewrite history, or assume the GitHub copies match local projects. Any discovered credential exposure needs its own controlled rotation.

## 4. Remaining application validation
Choose a clean non-client TypeScript/React/Next.js/NestJS application before framework-level CI, browser/API testing or preview deployment. No application rollout is authorized by this pilot sprint. The .NET fixture has a newer Test SDK 18.12.0 available; let Dependabot propose it and verify compatibility before merge. Do not duplicate CodeQL advanced setup with default setup.

## 5. Optional board grouping
Both requested view layouts work. For additional grouping, open [Engineering table](https://github.com/users/Ahmed-Ghazal55/projects/1/views/2) → view options → Group by → Workstream → Save. No extra Projects permission is required.
