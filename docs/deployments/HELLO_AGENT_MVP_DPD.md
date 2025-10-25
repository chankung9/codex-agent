# Deployment Plan — hello-agent MVP Link

## 1. Overview & Objectives
- **Feature:** Establish MVP workflow between codex-agent HQ and hello-agent repo.
- **Objectives:**
  - Ensure integration docs, task pipeline, and finance reporting stay in sync.
  - Validate manual deployment handoff before enabling automation.
- **Success Metrics:**
  - MVP plan committed in hello-agent repo.
  - Release checklist items mapped to compliance + finance sign-offs.

## 2. Infrastructure Diagram
- **Components:**
  - Codex-Agent HQ repo (`codex-agent`).
  - Downstream sandbox repo (`hello-agent`).
  - Manual command layer (ChatGPT Workspace + Codex CLI).
- **Dependencies:**
  - `.codex/plan.yaml` for orchestration.
  - `pipeline.yaml` gates for reviews.
  - `reports/` + `finance/` for telemetry.
- **Diagram Reference:** Initial text topology (diagram TODO once tooling available).

## 3. Rollback Strategy
- If MVP tasks introduce regressions, revert commits on `dev` branch.
- Disable downstream instructions until integration note is updated.
- Restore previous documentation snapshots from Git history (tag `pre-mvp-plan`).

## 4. Test & Validation Plan
| Test | Owner | Evidence |
| --- | --- | --- |
| Documentation completeness | Product Agent | `docs/INTEGRATION_HELLO_AGENT.md` updated checklist |
| Pipeline guardrails | Engineer Agent | `pipeline.yaml` includes hello-agent gates |
| Finance readiness | Finance Agent | `finance/summary_2025-10.md` reflects MVP budget |
| Compliance trace | Compliance Agent | Audit log entry + release checklist mapping |

## 5. Approval Sign-off
- **Product Lead:** _pending_
- **Engineer Lead:** _pending_
- **Legal/Compliance:** _pending_
- **Finance:** _pending_

> Prepared 2025-10-25. Update sign-off fields as approvals are recorded.
