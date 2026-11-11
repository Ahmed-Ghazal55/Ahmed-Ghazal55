# Examples: invoke shared workflows in an approved repository

These are **examples**, not files to paste unchanged into active projects.

## Node / TypeScript (.github/workflows/ci.yml)
```yaml
name: CI
on:
  pull_request:
  push:
    branches: [main]
permissions:
  contents: read
jobs:
  node:
    uses: Ahmed-Ghazal55/Ahmed-Ghazal55/.github/workflows/reusable-node-ci.yml@main
    with:
      node-version: '24'
      working-directory: '.'
```

Requirements: checked-in package-lock.json, reviewed dependencies and supported npm scripts. CI uses `npm ci --ignore-scripts` to avoid lifecycle scripts in untrusted code; framework-specific tools requiring lifecycle scripts need separate review before changing this behavior.

## .NET / C# (.github/workflows/ci.yml)
```yaml
name: CI
on:
  pull_request:
  push:
    branches: [main]
permissions:
  contents: read
jobs:
  dotnet:
    uses: Ahmed-Ghazal55/Ahmed-Ghazal55/.github/workflows/reusable-dotnet-ci.yml@main
    with:
      dotnet-version: '10.0.x'
      target: './MySolution.sln'
```

Replace SDK and target with versions/paths actually supported by the project. The reusable workflow requires fresh VSTest TRX output and at least one executed test in every returned test run. A plain library or zero-test suite fails. Projects using Microsoft.Testing.Platform or a different result format need a separately reviewed adapter; this VSTest workflow must not silently skip that validation.

## Security and release governance
- Prefer pinning callers to a reviewed commit SHA rather than tracking `@main` in production projects.
- Never expose secrets to workflows for untrusted pull requests.
- Do not run `pull_request_target` workflows that execute untrusted PR code.
- Never combine automated PR analysis with unrestricted write permissions.
- Separate publication from build checks; require manual approval and server/service connection.

## Static HTML / JavaScript (no package.json)
```yaml
name: Static CI
on:
  pull_request:
  push:
    branches: [main]
permissions:
  contents: read
jobs:
  static:
    uses: Ahmed-Ghazal55/Ahmed-Ghazal55/.github/workflows/reusable-static-web-ci.yml@main
    with:
      working-directory: '.'
```

Requires an `index.html` at the selected working directory and checks JavaScript syntax. This is *not* an end-to-end/browser or a full HTML standards audit. Pin the reusable workflow by reviewed commit SHA when a deployment-ready repository adopts it.
