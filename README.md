# Codex-Agent Organization

Codex-Agent coordinates multiple specialized agents (product, engineering, HR, audit) to bootstrap and operate AI-assisted workstreams for the Solana ecosystem. The repository captures shared governance artifacts, cross-team plans, and integration guides for downstream sandboxes like `hello-agent`.

## Executive Overview

- **Mission:** Provide a structured workspace where autonomous and human operators can plan, implement, audit, and report on Codex-led initiatives.
- **Scope:** Organization-wide templates, project registry, integration notes, and workspace branches (`main`, `dev`, `codex/auto`) that enable manual and automated contributions.
- **Key Assets:** Agent prompt packs, organization design blueprint, project registry, and integration playbooks across docs, audit, finance, and reports directories.
- **Branching Policy:** `main` stays stable for consumers landing in the repo; all day-to-day work must happen on `dev` (or feature branches that merge into `dev`) before promotion back to `main`.
- **Next Actions:** Maintain the project registry, document new integrations in `docs/`, keep the workspace directory aligned with active implementation tasks, and only fast-forward `main` once `dev` is validated.

### Working in This Repo
> ℹ️ The organization is currently **testing whether Codex-Agent can govern a full software-production process**.  
> The `main` branch stays stable for observers; switch to `dev` to see work-in-progress.

1. Clone the repository and immediately switch to the development branch:
   ```bash
   git checkout dev
   ```
2. Create feature branches from `dev` as needed, then open PRs targeting `dev`.
3. After review + validation, merge into `dev`, and only then promote to `main` via the release process.

## Automation Router

Use `workspace/agent_router.py` (Python) or the new Rust binary in `workspace/agent_router_rs/` to mirror agent chat commands into the correct files:

| Command | Action | Target |
| --- | --- | --- |
| `@finance summary` | Ensures the current month's finance summary exists (auto-filled from `finance/summary_TEMPLATE.md`) and appends an Automation Notes entry. | `finance/summary_<YYYY-MM>.md` |
| `@compliance audit` | Creates/appends the daily audit log entry with timestamped context. | `audit/logs/<YYYY-MM-DD>.md` |

Python example:

```bash
python3 workspace/agent_router.py "@finance summary" -c "DPD approvals still pending."
python3 workspace/agent_router.py "@compliance audit" -c "Verified hello-agent DPD captured controls."
```

Rust example (run from repo root):

```bash
cargo run --manifest-path workspace/agent_router_rs/Cargo.toml -- "@finance summary" -c "Rust router note."
cargo run --manifest-path workspace/agent_router_rs/Cargo.toml -- "@compliance audit" -c "Rust router audit."
```

Extend the router with additional handlers whenever new agent commands need deterministic storage.
