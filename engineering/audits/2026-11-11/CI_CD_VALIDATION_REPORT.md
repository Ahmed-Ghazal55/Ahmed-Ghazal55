# CI/CD validation — 2026-11-11

## Changes
- Pilot and CodeQL workflows now run on every pull request and on pushes to main. Removing workflow path filters prevents documentation-only changes from leaving required checks pending.
- Existing reusable workflow check names were preserved. The reviewed main ruleset was activated only after owner approval, a verified PR merge and successful main runs; the import-safe proposal JSON remains disabled.
- .NET CI writes TRX to a newly created temporary directory, rejects no report and rejects zero executed tests in any returned run. Fresh directories prevent stale results from qualifying a build.
- Eight regression cases execute the actual workflow shell blocks against isolated synthetic inputs: missing lockfile, missing required npm script, missing static entrypoint, invalid JavaScript, tracked archive, tracked dependencies, empty .NET suite, and plain library without a test SDK.
- Existing action versions pinned to upstream commit SHAs. Node requires `lint`, `build`, `test:ci` and a lockfile; lifecycle scripts remain disabled at installation.

## Local evidence
| Check | Observed result | Scope |
|---|---|---|
| CI guard regressions | 8 passed | Real shell failure cases, isolated temporary fixtures |
| Node fixture | Install, lint, build succeeded; 1 test passed | Plain JavaScript fixture; syntax build only |
| .NET fixture | Restore/build succeeded; 1 real xUnit test executed; fresh TRX guard passed | .NET 10, Test SDK 18.11.1, VS adapter 4.0.1 |
| Static fixture | 1 HTML file parsed and JavaScript syntax passed | No CSS standards validator or browser E2E |
| npm audit | Zero known vulnerabilities | Fixture has no external dependencies |
| NuGet audit | No vulnerable packages from current sources | Includes fixture transitive dependencies |

GitHub CI results and reviewed PR links are recorded in [EXECUTION_SUMMARY.md](EXECUTION_SUMMARY.md). Check the exact PR head before treating a run as current; historical successful runs on 678216b were baseline evidence only.

## Missing coverage and adoption limits
| Target | Current support | Remaining evidence |
|---|---|---|
| JavaScript / Node | Reusable workflow + real fixture and rejection cases | Application-specific integration coverage |
| TypeScript | Required scripts can invoke the caller's real compiler | No dedicated TypeScript compiler fixture in this repository |
| React / Next.js / NestJS | Caller pattern and Node workflow available | No real framework build/browser/API fixture; do not claim framework validation |
| C# / .NET | Real xUnit fixture and discovery/execution guard | Application SDK/matrix, real SQL Server/PostgreSQL tests |
| Static HTML/CSS/JS | HTML parsing, JS syntax and entrypoint checks | Browser, accessibility, CSS/HTML standards and UI behavior |
| Repository hygiene | Existing gate + synthetic archive/dependency rejection | Malware, deleted history and dependency supply-chain audit |
| Deployment / containers | Planning only | Approved target, image scan, staging health and rollback; no production automation |

## Reproduce
```bash
python3 engineering/scripts/test-ci-guards.py
npm --prefix engineering/fixtures/node ci --ignore-scripts
npm --prefix engineering/fixtures/node run lint
npm --prefix engineering/fixtures/node run build
npm --prefix engineering/fixtures/node run test:ci
dotnet test engineering/fixtures/dotnet/Smoke.Tests/Smoke.Tests.csproj --configuration Release
gh pr checks --repo Ahmed-Ghazal55/Ahmed-Ghazal55 <PR-number>
```

The ordinary dotnet command above runs the fixture; use the reusable workflow to verify the fresh-TRX enforcement. There is no production release in these workflows.

## Verified remote execution
- [PR #11](https://github.com/Ahmed-Ghazal55/Ahmed-Ghazal55/pull/11) final head `a401668072b3a4e899dca1de5494c86f078cbdfa`: all seven workflow jobs and the aggregate CodeQL check succeeded.
- Merged as `d922e09b650c83b8f8aab4c521118073cdb3c3b6`; post-merge runs below succeeded on that exact commit.
- [Pilot shared workflows](https://github.com/Ahmed-Ghazal55/Ahmed-Ghazal55/actions/runs/43055071054): success.
- [CodeQL - pilot source](https://github.com/Ahmed-Ghazal55/Ahmed-Ghazal55/actions/runs/43055070838): success.
- Final readback documentation uses a separate documentation-only PR under active rules. Its required checks and normal merge are the acceptance check for documentation-only triggers and usable solo maintenance. The PR/check URLs are linked from the final GitHub handoff.
