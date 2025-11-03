# Cyphercast Integration Smoke Checklist

## Purpose

Define the minimal test pass we will execute once the frontend wallet flow is available.  
The goal is to validate HQ ↔ downstream wiring and critical Solana flows before heavier test suites run.

## Prerequisites

- Frontend implementation supports connect → stake (prediction) → claim flow.
- Local validator instructions ready (Surfpool or Anchor localnet).
- Environment variables documented (`SOLANA_RPC_URL`, `KEYPAIR`, wallet adapter config).

## Test Steps

1. Checkout latest `main` branches for both HQ and downstream repos.
2. Provision local validator (Surfpool container or Anchor localnet) following `docs/TESTING.md`.
3. Fund a developer wallet via `solana airdrop 4`.
4. Launch the cyphercast frontend in staging/test configuration.
5. Connect wallet using the configured adapter (TestAdapter or Phantom dev wallet); verify balance display.
6. Submit a staking prediction transaction; capture signature and confirm on validator.
7. Resolve the stream via CLI/oracle script; ensure totals update.
8. Claim rewards; verify frontend reflects credited balance and transaction succeeds.

## Evidence to Capture

- RPC transaction signatures and validator logs (Surfpool output).
- Frontend console or UI screenshots for key steps.
- Any Playwright/Test runner reports if automation is used.
- Summary entry in `audit/logs/<date>.md` stating checklist execution and outcomes.

## Ownership & Tracking

- **Owner:** Engineer agent.
- **Trigger:** Add task entry to `.codex/plan.yaml` when frontend milestone kicks off.
- **Completion:** Update `projects/cyphercast/docs/INTEGRATION_CYPHERCAST.md` and relevant audit logs once checklist passes.
