#!/usr/bin/env bash
set -euo pipefail

# Lightweight wrapper around markdown-link-check for consistent CI and local runs.

usage() {
  cat <<'USAGE'
Usage: check_links.sh [paths...]

Runs markdown-link-check against the provided markdown files. If no paths are
supplied, the script scans all Markdown files under projects/cyphercast/docs/
and the top-level docs/ directory.

Dependencies:
  - Node.js 18+
  - npx (ships with Node.js)

Configuration:
  - projects/cyphercast/.markdown-link-check.json
USAGE
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../../.." && pwd)"
CONFIG_FILE="${REPO_ROOT}/projects/cyphercast/.markdown-link-check.json"

mapfile -t TARGETS < <(
  if [[ $# -gt 0 ]]; then
    for path in "$@"; do
      if [[ -d "$path" ]]; then
        find "$path" -type f -name '*.md'
      else
        echo "$path"
      fi
    done
  else
    find "${REPO_ROOT}/projects/cyphercast/docs" -type f -name '*.md'
    find "${REPO_ROOT}/docs" -maxdepth 1 -type f -name '*.md'
  fi |
  sort -u
)

if [[ ${#TARGETS[@]} -eq 0 ]]; then
  echo "No markdown files found." >&2
  exit 1
fi

STATUS=0
for file in "${TARGETS[@]}"; do
  echo "Checking links in ${file}"
  if ! npx -y markdown-link-check "${file}" -q -p -c "${CONFIG_FILE}"; then
    STATUS=1
  fi
done

exit ${STATUS}
