# Project Registry

Each entry defines a project integrated with the Codex-Agent organization.
Fields: name, purpose, owner, repo, status, notes

## Repository Coordination Policy

- All downstream project repositories (e.g., `hello-agent`) **must live side-by-side** with the `codex-agent` repo on each engineer's workstation (e.g., `/workspace/codex-agent` and `/workspace/hello-agent`).
- Do **not** nest downstream repos inside `codex-agent`; this prevents accidental commits, submodule drift, and mixing Git histories.
- Shared tooling (like `projects/<project>/scripts/doc_sync_diff.sh`) assumes this layout and accepts a path argument such as `../hello-agent`.
- After any documentation update that affects a downstream project, engineers rerun the doc-sync helper against the side-by-side clone and log the evidence in `audit/logs/YYYY-MM-DD.md`.

## Entries

### hello-agent

- **Purpose:** Sandbox and development testbed for Codex-Agent orchestration.
- **Owner:** engineer_agent
- **Repository:** [https://github.com/chankung9/hello-agent](https://github.com/chankung9/hello-agent)
- **Status:** Active
- **Notes:** Used to validate manual handoff between ChatGPT Workspace and Codex.
- **Integration Status:** linked (see `docs/INTEGRATION_HELLO_AGENT.md`)
