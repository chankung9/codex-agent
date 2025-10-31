# cyphercast Project Workspace

Codex HQ artifacts for the `cyphercast` downstream repository live here.  
Use this workspace to coordinate tasks, documentation, and integration checklists before publishing updates to the sandbox repo.

- `tasks/` keeps YAML task manifests aligned with `.codex/plan.yaml`.
- `docs/` hosts Codex-maintained specs and playbooks that sync to the downstream repo.
- `scripts/` bundles helper utilities such as doc-diff tooling.

## Downstream Repository Layout

- Follow the HQ side-by-side policy: keep `codex-agent` and `cyphercast` cloned next to each other (e.g., `/workspace/codex-agent` and `/workspace/cyphercast`).
- Do **not** nest the downstream repo inside this workspace; automation assumes the relative path `../cyphercast`.

## Document Sync

- Run `projects/cyphercast/scripts/doc_sync_diff.sh ../cyphercast` after updating HQ docs to verify parity.
- Capture timestamped evidence (Asia/Bangkok via `./scripts/current_time.sh`) inside `audit/logs/<date>.md` whenever sync checks are executed.
