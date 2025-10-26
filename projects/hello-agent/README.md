# hello-agent Project Workspace

Artifacts specific to the hello-agent sandbox live here.

- `tasks/` holds YAML task definitions referenced by `pipeline.yaml`.
- Future enhancements: specs, dependency manifests, release notes.

## Working With The Downstream Repo
- Follow the global side-by-side cloning policy described in `docs/PROJECTS.md` (keep `hello-agent` next to `codex-agent`, not nested).
  - The doc-sync helper (`projects/hello-agent/scripts/doc_sync_diff.sh`) expects a path argument, so `../hello-agent` stays the default example.
- After each documentation change, run the sync script against the side-by-side clone and log the result in `audit/logs/YYYY-MM-DD.md`.
