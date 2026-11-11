# GitHub Projects status — 2026-11-11

Verified board: [Engineering Delivery & Release Board](https://github.com/users/Ahmed-Ghazal55/projects/1). Visibility: **private**. Reused the existing empty `Gate Payroll & Release Board`; no duplicate project was created and no existing items were removed.

| Field | Exact options |
|---|---|
| Status | Backlog; Ready; In Progress; Review; Verify; Preview; Done |
| Workstream | Frontend / React / Next.js; Backend / Node.js / NestJS; C# / .NET; Database; Security; DevOps / Deployment; Documentation / Learning |
| Project classification | Pilot; Active / Protected; Legacy; Learning |

| Existing issue | Status | Workstream | Classification | Reason |
|---|---|---|---|---|
| [#1 Infrastructure Sprint 01](https://github.com/Ahmed-Ghazal55/Ahmed-Ghazal55/issues/1) | In Progress | DevOps / Deployment | Pilot | Infrastructure works; governance authorization and application/deployment work remain |
| [#5 Governance](https://github.com/Ahmed-Ghazal55/Ahmed-Ghazal55/issues/5) | In Progress | DevOps / Deployment | Pilot | Board and owner-approved main protection complete; provider visibility/application rollout remain |
| [#6 Security audit](https://github.com/Ahmed-Ghazal55/Ahmed-Ghazal55/issues/6) | Ready | Security | Pilot | Archive path inventory complete; separate isolated investigation not executed |

Verified views:
- [Delivery board](https://github.com/users/Ahmed-Ghazal55/projects/1/views/1): Board layout, columns grouped by Status.
- [Engineering table](https://github.com/users/Ahmed-Ghazal55/projects/1/views/2): Table layout.
- Both display Title, Status, Repository, Workstream and Project classification.

REST user-project/view routes returned 404. GraphQL advertised `createProjectV2View` and `updateProjectV2View`; both worked and were independently read back. No view setup is blocked. Optional table grouping: open Engineering table → view options → Group by → Workstream → Save. This optional grouping was not configured by the available view input (visible fields only).

The three issues remain open because their remaining work is real. Main protection is active as ruleset 27044588 after owner approval and verified merges. Issue #5's misleading environment/integration checkboxes were corrected, and all three issues received a verified latest-status section. Environments remain intentionally deferred until an application and deployment target are approved.
