# GitHub engineering audit — 2026-11-11

Scope: `Ahmed-Ghazal55/Ahmed-Ghazal55` only for writes. All other repositories were inventoried read-only. Existing local applications and original archives were not modified. Raw API evidence stays outside this public repository; private repository identities/content and credentials are omitted.

## Authentication and capability report
| Capability | Verified result |
|---|---|
| Identity | `Ahmed-Ghazal55`; repository admin/push permissions confirmed through REST |
| Toolchain | GitHub CLI 2.46.0; Git 2.53.0; Node 24.18.0; .NET SDK 10.0.402 on Ubuntu 26.04 |
| Existing CLI scopes | `gist`, `read:org`, `repo`, `workflow`; owner approved refresh adding `project`; subsequent Projects queries/mutations succeeded |
| Projects | Existing private project 1 reused; exact fields and three linked issues read back |
| GitHub Apps | OAuth token cannot enumerate `user/installations` (403); empty repository webhooks do not prove no installed Apps |
| GHCR | Package inventory denied without `read:packages`; no authorization added or packages published |
| Permissions | Actions default token read-only; automated PR approval disabled; no secrets inherited by reusable CI |

## Discovery and gap analysis before writes
| Area | Discovery | Sprint response |
|---|---|---|
| Existing infrastructure | Six workflows, fixtures, Dependabot, templates and policies already exist | Reused; no rebuild or redundant tools installed |
| PRs #7–#10 | All merged; latest fixture runs successful | Verified through issues/PR metadata and check runs |
| Board | Projects scope absent initially; one empty private release board after authorization | Reused project 1, renamed and configured; no new board |
| CI triggers | Path filters skip documentation-only PRs and leave future required checks pending | Remove filters from pilot and CodeQL; PRs always run; push runs limited to main |
| .NET tests | `dotnet test` can succeed for a library or empty test suite | Require fresh TRX files and a positive executed count per test run |
| Vulnerability alerts | Disabled; alert-list 403 and enabled-status 404 | Enabled once; independent GET 204, alert list empty |
| Branch protection | Rulesets/effective rules empty; legacy protection reports unprotected | API-validated disabled ruleset 27044588; owner approved activation after verified PR #11 merge |
| Deployment | No environments, deployments or Pages site | Prepared and intentionally deferred; no approved target |
| Legacy provenance | 10 public repos have 20 archive paths; shopping has 24,094 dependency-tree paths | Read-only inventory; no archives opened and no cleanup |

## Repository inventory and suggested CI adoption
Classification reflects observed risk, not a malware diagnosis or a definitive statement of project age. No repository was assumed identical to a local Ubuntu project. No repository is assigned Legacy without owner evidence.

| Repository | Classification | CI adoption | Evidence |
|---|---|---|---|
| [Ahmed-Ghazal55](https://github.com/Ahmed-Ghazal55/Ahmed-Ghazal55) | Pilot | Existing Node, .NET, static and hygiene workflows; this sprint only | 0 archives; 0 dependency-tree paths |
| [ai-coding-prompt-java](https://github.com/Ahmed-Ghazal55/ai-coding-prompt-java) | Requires security investigation | Hold install/build/adoption until provenance review; static CI later where applicable | 2 archives; 0 dependency-tree paths |
| [BootStrap-Demo](https://github.com/Ahmed-Ghazal55/BootStrap-Demo) | Requires security investigation | Hold install/build/adoption until provenance review; static CI later where applicable | 2 archives; 0 dependency-tree paths |
| [cart-page](https://github.com/Ahmed-Ghazal55/cart-page) | Requires security investigation | Hold install/build/adoption until provenance review; static CI later where applicable | 2 archives; 0 dependency-tree paths |
| [Chrome-Extension-Leads-Tracker](https://github.com/Ahmed-Ghazal55/Chrome-Extension-Leads-Tracker) | Requires security investigation | Hold install/build/adoption until provenance review; static CI later where applicable | 2 archives; 0 dependency-tree paths |
| Withheld private repository (1) | Active / Protected | Metadata only; documentation controls after owner review | None |
| [gate-payroll](https://github.com/Ahmed-Ghazal55/gate-payroll) | Active / Protected | Existing deployment workflow; separate application review; no changes | 0 archives; 0 dependency-tree paths |
| [Keeta-Poartel](https://github.com/Ahmed-Ghazal55/Keeta-Poartel) | Ready for audit | Review ownership, manifest and scripts before choosing Node/static CI | 0 archives; 0 dependency-tree paths |
| [Modern.Fix](https://github.com/Ahmed-Ghazal55/Modern.Fix) | Requires security investigation | Hold install/build/adoption until provenance review; static CI later where applicable | 2 archives; 0 dependency-tree paths |
| [Parachute](https://github.com/Ahmed-Ghazal55/Parachute) | Requires security investigation | Hold install/build/adoption until provenance review; static CI later where applicable | 2 archives; 0 dependency-tree paths |
| [portfolio](https://github.com/Ahmed-Ghazal55/portfolio) | Requires security investigation | Hold install/build/adoption until provenance review; static CI later where applicable | 2 archives; 0 dependency-tree paths |
| [shopping](https://github.com/Ahmed-Ghazal55/shopping) | Requires security investigation | Hold install/build/adoption until provenance review; static CI later where applicable | 2 archives; 24094 dependency-tree paths |
| [To-Do-List](https://github.com/Ahmed-Ghazal55/To-Do-List) | Requires security investigation | Hold install/build/adoption until provenance review; static CI later where applicable | 2 archives; 0 dependency-tree paths |
| [YouTube-Frontend](https://github.com/Ahmed-Ghazal55/YouTube-Frontend) | Requires security investigation | Hold install/build/adoption until provenance review; static CI later where applicable | 2 archives; 0 dependency-tree paths |

Inventory pagination: 14 accessible repositories in a 100-item page; public recursive trees all reported `truncated=false`. The one private repository was inspected at metadata level only. Archive and dependency counts describe tree entries, not executed files.

## Verification boundaries
CodeQL covers JavaScript/TypeScript and C# in the pilot. Passing scans and zero returned alerts are scoped evidence, not proof of no vulnerabilities. React/Next.js/NestJS builds, databases, browsers, deployments, archives and Git history were not validated by the smoke fixtures. Provider account state remains unverified.
