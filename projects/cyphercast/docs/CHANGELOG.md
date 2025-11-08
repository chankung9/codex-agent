# Cyphercast Change Log

Document notable changes to the cyphercast program across HQ and downstream repositories.  
Follow [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) + Semantic Versioning.

## [Unreleased]

### Added
- Initial Codex HQ governance and engineering scaffolding (upskill guide, best practices, software policy, RACI).
- Integration record updated with doc parity evidence and downstream checklist.
- ADR-0001 documenting wallet adapter stack decision.
- Development roadmap (`DEV_ROADMAP.md`) and phased task YAMLs for frontend, wallet integration, prediction UX, and release readiness.
- Link verification tooling (`projects/cyphercast/scripts/check_links.sh`) and policy updates requiring `pnpm check:links` in CI.
- Next.js frontend workspace scaffolded with marketing/dashboard/stake routes, shadcn tokens, and Storybook baseline.
- Wallet adapter provider + RPC helpers added (env scaffolding, Surfpool-ready configuration).

### Pending
- Execute integration smoke checklist post doc-sync parity.
- Establish staging release workflow and smoke suite results.
