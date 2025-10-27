# Codex-Agent Organization

Codex-Agent coordinates multiple specialized agents (product, engineering, HR, audit) to bootstrap and operate AI-assisted workstreams for the Solana ecosystem. The repository captures shared governance artifacts, cross-team plans, and integration guides for downstream sandboxes like `hello-agent`.

## Main Branch Snapshot

Codex-Agent is actively testing whether it can govern an end-to-end software-production workflow. The `main` branch stays stable for observers, while active work streams live on `dev`.

### View Work in Progress
1. Clone the repository and switch to `dev`:
   ```bash
   git clone <repo-url>
   cd codex-agent
   git checkout dev
   ```
2. Create feature branches from `dev`, open PRs back to `dev`, and promote to `main` only after validation/tagging.

### What to Expect on `main`
- High-level documentation and previously released artifacts.
- Links to downstream projects (such as hello-agent) and governance templates.
- Release tags that have passed the review pipeline; active pilots (e.g., hello-agent) are tracked on `dev` or in `reports/releases/`.

## Executive Overview

- **Mission:** Provide a structured workspace where autonomous and human operators can plan, implement, audit, and report on Codex-led initiatives.
- **Scope:** Organization-wide templates, project registry, integration notes, and workspace branches (`main`, `dev`, `codex/auto`) that enable manual and automated contributions.
- **Key Assets:** Agent prompt packs, organization design blueprint, project registry, and integration playbooks across docs, audit, finance, and reports directories.
- **Branching Policy:** `main` stays stable for consumers landing in the repo; all day-to-day work must happen on `dev` (or feature branches that merge into `dev`) before promotion back to `main`.
- **Next Actions:** Maintain the project registry, document new integrations in `docs/`, keep the workspace directory aligned with active implementation tasks, and only fast-forward `main` once `dev` is validated.

### Working in This Repo
1. Clone the repository and immediately switch to the development branch:
   ```bash
   git checkout dev
   ```
2. Create feature branches from `dev` as needed, then open PRs targeting `dev`.
3. After review + validation, merge into `dev`, and only then promote to `main` via the release process.

## Timekeeping Standard

- All Codex-Agent records (audit logs, staff reports, release notes, plan manifests) **must use Asia/Bangkok (UTC+07:00)** as the canonical timezone.
- Before writing any timestamped content, call `./scripts/current_time.sh` (or import its logic) to capture an ISO-8601 value, then store both the `timezone` and `timestamp` fields in the document.
- Automation pipelines and downstream repos should reference this script instead of relying on host clock defaults to avoid cloud/on-prem drift.

## AI Collaboration & Logging

- Follow `docs/AI_COLLABORATION_WORKFLOW.md` for the canonical flow to capture AI-assisted discussions.
- After running a short prompt in your preferred extension (Codex, Copilot Chat, GLM/Cline, etc.), create or update the relevant backlog snapshot under `projects/<project>/backlogs/` with the key outcomes.
- Link the snapshot from the active task YAML so reviewers can trace decisions, risks, and next steps without relying on external chat logs.
