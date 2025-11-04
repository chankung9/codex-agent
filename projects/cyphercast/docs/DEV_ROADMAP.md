# Cyphercast Development Roadmap

This roadmap converts existing governance artifacts, Phase 2 documentation, and integration requirements into an actionable sequence of milestones.  
Use it to coordinate frontend work, align with the Solana program, and prepare testing + release activities.

## Phase 0 — Alignment & Foundations (Completed)

- **Scope:** Establish HQ workspace, ingest Phase 2 documentation, publish engineering policies, and sync with downstream repo.  
- **Deliverables:** `FRONTEND_UPSKILL_GUIDE.md`, `ENGINEERING_BEST_PRACTICES.md`, `SOFTWARE_ENGINEERING_POLICY.md`, doc parity audit (`audit/logs/2025-10-31.md`).  
- **Status:** Complete — reference integration record for evidence.

## Phase 1 — Frontend Scaffold

- **Objectives:**
  - Initialize Next.js (or Vite) TypeScript app with pnpm workspace support.
  - Apply linting/formatting/type-check tooling per `ENGINEERING_BEST_PRACTICES.md`.
  - Bring in Tailwind + shadcn/ui design system, Storybook (or Ladle), and base layout routes.
- **Dependencies:** FRONTEND_UPSKILL_GUIDE, ADR-0001 (wallet stack) for project configuration expectations.
- **Exit Criteria:**
  - Repository builds successfully (`pnpm build`) with CI lint/typecheck scripts.
  - Component playground running (Storybook) with at least wallet button mock.
  - Documentation updated under `docs/CHANGELOG.md` and doc-sync evidence recorded.

## Phase 2 — Wallet & Solana Integration Enablement

- **Objectives:**
  - Implement wallet provider stack per `ADR-0001-wallet-adapter-stack`.
  - Configure Surfpool/localnet connection utilities and environment management.
  - Generate Anchor IDL typings and RPC client helpers (`lib/solana/*`).
  - Provide mock adapters + service layer for unit tests.
- **Dependencies:** Phase 1 scaffold complete; Solana program (Phase 2 features) on local validator; `docs/ARCHITECTURE.md` from downstream for module mapping.
- **Exit Criteria:**
  - Wallet connect/disconnect flow works against TestAdapter in dev.
  - Transaction builder library submits join/predict requests to local validator (mock data acceptable).
  - Integration documentation updated; CLI quick ref referenced from UI help.

## Phase 3 — Prediction & Claims Experience

- **Objectives:**
  - Build UX for stream selection, prediction submission, result viewing, and reward claim.
  - Wire real program accounts (Stream, TokenVault, Prediction) using data loaders (TanStack Query).
  - Handle error/display states, staking precision, tip presentation, and receipts.
- **Dependencies:** Wallet integration deliverables and on-chain program behavior documented in `PHASE2-IMPLEMENTATION.md`, `rewards.md`.
- **Exit Criteria:**
  - End-to-end user journey completes on localnet using real transactions.
  - Accessibility and responsive checks pass for primary flows.
  - Analytics/logging hooks instrumented for stake/claim events.

## Phase 4 — Quality & Testing Maturation

- **Objectives:**
  - Lock down unit + component test coverage (Vitest/Jest + React Testing Library).
  - Stand up Playwright integration suite with Surfpool automation (per `docs/TESTING.md` once synced).
  - Prepare integration smoke runbook (`INTEGRATION_SMOKE_CHECKLIST.md`) for execution.
- **Dependencies:** Stable UI flows (Phase 3) and local validator automation from Phase 2.
- **Exit Criteria:**
  - CI pipeline runs lint, unit tests, component tests, and Playwright headless sequence.
  - Documentation link checker (`pnpm check:links` or `scripts/check_links.sh`) runs green in CI and PRs.
  - Evidence of at least one dry-run recorded in `audit/logs/<date>.md`.
  - Smoke checklist marked ready to execute (frontend support confirmed).

## Phase 5 — Release & Compliance Readiness

- **Objectives:**
  - Align with `SOFTWARE_ENGINEERING_POLICY.md` release gates: code review, audit logging, documentation sync.
  - Prepare staging/devnet smoke suite (slim scenario) and track tx signatures.
  - Complete roadmap of documentation updates (`DEV_ROADMAP.md`, `CHANGELOG.md`, integration record).
- **Dependencies:** Testing maturity from Phase 4, Product approvals, Finance/Compliance checkpoints.
- **Exit Criteria:**
  - Release candidate checklist signed (Product + Finance + Compliance).
  - Doc-sync diff clean; audit log captures release decision.
  - Tag + changelog entry issued with references to completed tasks and testing evidence.

## Tracking & Next Actions

- Corresponding tasks are published under `projects/cyphercast/tasks/roadmap_*.yaml`.
- Progress updates should feed into `.codex/plan.yaml` entries and be logged via `./scripts/current_time.sh` in `audit/logs/`.
- Upon completion of each phase, update `projects/cyphercast/docs/CHANGELOG.md` and adjust `INTEGRATION_CYPHERCAST.md` checklist items.
