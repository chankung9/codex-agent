# Project Registry

Each entry defines a project integrated with the Codex-Agent organization.
Fields: name, purpose, owner, repo, status, notes

## Repository Coordination Policy

- All downstream project repositories (e.g., `hello-agent`) **must live side-by-side** with the `codex-agent` repo on each engineer's workstation (e.g., `/workspace/codex-agent` and `/workspace/hello-agent`).
- Do **not** nest downstream repos inside `codex-agent`; this prevents accidental commits, submodule drift, and mixing Git histories.
- Shared tooling (like `projects/<project>/scripts/doc_sync_diff.sh`) assumes this layout and accepts a path argument such as `../hello-agent`.
- After any documentation update that affects a downstream project, engineers rerun the doc-sync helper against the side-by-side clone and log the evidence in `audit/logs/YYYY-MM-DD.md`.
- All audit/report timestamps recorded during coordination **must use Asia/Bangkok (UTC+07:00)** via `./scripts/current_time.sh` to keep humans and agents aligned on a single clock source.

## Entries

### hello-agent

- **Purpose:** Sandbox and development testbed for Codex-Agent orchestration.
- **Owner:** engineer_agent
- **Repository:** [https://github.com/chankung9/hello-agent](https://github.com/chankung9/hello-agent)
- **Status:** Active
- **Notes:** Used to validate manual handoff between ChatGPT Workspace and Codex.
- **Integration Status:** linked (see `docs/INTEGRATION_HELLO_AGENT.md`)

### cyphercast

- **Purpose:** Interactive streaming and live prediction platform built on Solana with Anchor PDAs and SPL-token rewards.
- **Owner:** product_agent
- **Repository:** [https://github.com/chankung9/cyphercast](https://github.com/chankung9/cyphercast)
- **Status:** Incubating
- **Notes:** Local clone expected at `../cyphercast`; Phase 2 delivers token vault and staking flow used for Codex-led showcases.
- **Integration Status:** in_progress (see `projects/cyphercast/docs/INTEGRATION_CYPHERCAST.md`; downstream doc parity pending)
