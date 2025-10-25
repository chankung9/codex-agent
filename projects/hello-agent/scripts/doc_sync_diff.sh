#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage: doc_sync_diff.sh <path-to-hello-agent-repo> [relative-docs-path]

Compares Codex HQ docs under projects/hello-agent/docs with the downstream
hello-agent repository docs to ensure they are in sync.

Arguments:
  path-to-hello-agent-repo  Absolute or relative path to the downstream repo.
  relative-docs-path        Optional docs subdirectory inside the downstream repo (default: docs).
EOF
}

if [[ $# -lt 1 || $# -gt 2 ]]; then
  usage
  exit 1
fi

SANDBOX_REPO="$(cd "$1" && pwd)"
SANDBOX_DOCS_SUBDIR="${2:-docs}"
SANDBOX_DOCS="${SANDBOX_REPO}/${SANDBOX_DOCS_SUBDIR}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HQ_DOCS_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)/docs"

if [[ ! -d "$SANDBOX_DOCS" ]]; then
  echo "error: downstream docs directory not found at ${SANDBOX_DOCS}" >&2
  exit 2
fi

echo "Comparing:"
echo "  HQ docs       : ${HQ_DOCS_DIR}"
echo "  Downstream doc: ${SANDBOX_DOCS}"
echo

diff -ruN "${HQ_DOCS_DIR}" "${SANDBOX_DOCS}"
