#!/usr/bin/env python3
"""Execute the actual reusable-workflow shell steps against isolated fixtures.

No third-party Python packages, archives, client projects or deployment credentials.
The .NET negative fixture deliberately has a test SDK but no test methods.
"""
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]


def step_script(filename, step_name):
    lines = (ROOT / '.github/workflows' / filename).read_text().splitlines()
    start = lines.index('      - name: ' + step_name)
    run = next(i for i in range(start + 1, len(lines)) if lines[i].strip() == 'run: |')
    script = []
    for line in lines[run + 1:]:
        if line.strip() and not line.startswith('          '):
            break
        script.append(line[10:])
    return '\n'.join(script) + '\n'


def command(args, cwd, env=None):
    return subprocess.run(args, cwd=cwd, env={**os.environ, **(env or {})},
                          text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


class CIGuards(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='engineering-ci-guard-')
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name)

    def shell(self, filename, step_name, env=None):
        return command(['bash', '-e', '-o', 'pipefail', '-c', step_script(filename, step_name)], self.path, env)

    def test_missing_lockfile_is_rejected(self):
        (self.path / 'package.json').write_text('{}')
        result = self.shell('reusable-node-ci.yml', 'Install locked dependencies', {'PROJECT_DIR': str(self.path)})
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn('package-lock.json is required', result.stdout)

    def test_missing_required_npm_script_is_rejected(self):
        (self.path / 'package.json').write_text(json.dumps({'scripts': {'lint': 'node --version', 'build': 'node --version'}}))
        result = self.shell('reusable-node-ci.yml', 'Require lint, build and test:ci scripts', {'PROJECT_DIR': str(self.path)})
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn('Missing required npm script: test:ci', result.stdout)

    def test_static_site_requires_entrypoint(self):
        result = self.shell('reusable-static-web-ci.yml', 'Inspect static website source', {'WEB_DIR': str(self.path)})
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn('Missing index.html', result.stdout)

    def test_static_site_rejects_invalid_javascript(self):
        (self.path / 'index.html').write_text('<!doctype html><title>Fixture</title>')
        (self.path / 'broken.js').write_text('function {')
        result = self.shell('reusable-static-web-ci.yml', 'Inspect static website source', {'WEB_DIR': str(self.path)})
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn('SyntaxError', result.stdout)

    def test_hygiene_rejects_archive(self):
        command(['git', 'init', '-q'], self.path)
        (self.path / 'payload.zip').write_text('synthetic marker; not an archive')
        command(['git', 'add', '--', 'payload.zip'], self.path)
        result = self.shell('reusable-repo-hygiene.yml', 'Reject tracked dependencies and archive payloads')
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn('BLOCKED: tracked archives', result.stdout)

    def test_hygiene_rejects_tracked_dependencies(self):
        command(['git', 'init', '-q'], self.path)
        (self.path / 'node_modules').mkdir()
        (self.path / 'node_modules/marker.js').write_text('// synthetic')
        command(['git', 'add', '--', 'node_modules/marker.js'], self.path)
        result = self.shell('reusable-repo-hygiene.yml', 'Reject tracked dependencies and archive payloads')
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn('BLOCKED: tracked node_modules', result.stdout)

    def test_dotnet_project_without_tests_is_rejected(self):
        shutil.copyfile(ROOT / 'engineering/fixtures/dotnet/Smoke.Tests/Smoke.Tests.csproj', self.path / 'Empty.Tests.csproj')
        (self.path / 'Empty.cs').write_text('public class Empty { }')
        restore = command(['dotnet', 'restore', 'Empty.Tests.csproj', '--verbosity', 'quiet'], self.path)
        self.assertEqual(restore.returncode, 0, restore.stdout)
        result = self.shell('reusable-dotnet-ci.yml', 'Run tests and require executed results',
                            {'DOTNET_TARGET': str(self.path / 'Empty.Tests.csproj'), 'RUNNER_TEMP': str(self.path)})
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn('zero tests', result.stdout)

    def test_dotnet_library_without_test_sdk_is_rejected(self):
        (self.path / 'Library.csproj').write_text('<Project Sdk="Microsoft.NET.Sdk"><PropertyGroup><TargetFramework>net10.0</TargetFramework></PropertyGroup></Project>')
        restore = command(['dotnet', 'restore', 'Library.csproj', '--verbosity', 'quiet'], self.path)
        self.assertEqual(restore.returncode, 0, restore.stdout)
        result = self.shell('reusable-dotnet-ci.yml', 'Run tests and require executed results',
                            {'DOTNET_TARGET': str(self.path / 'Library.csproj'), 'RUNNER_TEMP': str(self.path)})
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn('No TRX results', result.stdout)


if __name__ == '__main__':
    unittest.main(verbosity=2)
