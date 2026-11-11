#!/usr/bin/env bash
# READ-ONLY inventory of Git repositories and known unexpected ZIP filenames.
# Does not checkout, pull, reset, delete, extract, execute archives or change files.
set -uo pipefail
ROOT="${1:-$HOME/Projects}"
if [[ ! -d "$ROOT" ]]; then printf 'Directory not found: %s\n' "$ROOT" >&2; exit 1; fi
printf '=== Git working trees ===\n'
while IFS= read -r -d '' gitdir; do
  repo="${gitdir%/.git}"
  printf '\n=== %s ===\n' "$repo"
  git -C "$repo" status --short --branch || true
  git -C "$repo" remote -v || true
  printf 'Tracked node_modules count: '
  git -C "$repo" ls-files | awk '/(^|\/)node_modules\// {count++} END {print count+0}'
done < <(find "$ROOT" -type d -name .git -prune -print0 2>/dev/null)
printf '\n=== Known archive-name candidates (including node_modules, excluding .git) ===\n'
while IFS= read -r -d '' file; do
  printf '%s\n' "$file"
  sha256sum -- "$file" || true
done < <(find "$ROOT" -type d -name .git -prune -o -type f \( \
  -iname '*nsfw*.zip' -o -iname '*hungerer*.zip' -o \
  -iname 'portfolio-3.8.zip' -o -iname 'Software-v*.zip' -o \
  -iname '*leads*tracker*.zip' \) -print0 2>/dev/null)
printf '\nFinished. No files were changed. Hashes are not a malware verdict.\n'
