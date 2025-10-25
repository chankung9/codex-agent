# hello-agent Sandbox Test Outline

## Objectives and Success Criteria
- **Validate integration workflows:** Confirm that registry entries and integration checklists in `docs/PROJECTS.md` and `docs/INTEGRATION_HELLO_AGENT.md` remain accurate as work progresses.
- **Exercise cross-persona collaboration:** Ensure engineer, product, and HR agents can coordinate around shared deliverables such as the MVP plan and status reviews.
- **Demonstrate document and reporting readiness:** Prepare the groundwork needed to close the outstanding checklist items for document sync and automated reporting.

### Test Use Cases
- **Commit and document synchronization:** Engineer agent drafts or updates artifacts in the sandbox repo and mirrors the changes back to Codex HQ records.
- **Weekly product review loop:** Product agent reviews sandbox progress and records decisions or follow-ups in HQ documentation.
- **Performance tracking hand-off:** HR agent captures agreed metrics from the sandbox activities and feeds them into reporting channels.

### Acceptance Criteria
- Objectives from `docs/INTEGRATION_HELLO_AGENT.md` are reflected in a shared MVP plan with explicit owners and next steps.
- At least one review cycle between engineer and product agents is documented with outcomes and follow-up tasks.
- Reporting touchpoints for HR are defined, including where metrics will be logged once automation is available.

## Resource Inventory
| Artifact | Location | Purpose | Readiness | Gaps / Notes |
| --- | --- | --- | --- | --- |
| Integration record | `docs/INTEGRATION_HELLO_AGENT.md` | Tracks linkage between HQ and sandbox | ✅ Complete | Needs updates once sync/reporting validated |
| Project registry entry | `docs/PROJECTS.md` | Catalog entry with ownership/status | ✅ Complete | Keep status aligned with testing progress |
| Workspace README | `projects/hello-agent/README.md` | Directory overview and future enhancements | ⚠️ Basic | Expand with links to active plans when created |
| Task registry guide | `projects/hello-agent/tasks/README.md` | Defines YAML task structure | ✅ Ready | Create actual task files per initiative |
| Task template | `projects/hello-agent/tasks/task_template.yaml` | Starting point for structured tasks | ✅ Ready | Instantiate for MVP plan and subsequent tasks |
| Pending artifacts | *(not yet created)* | Specs, dependency manifest, release notes | ❌ Missing | Produce during test to cover documentation pipeline |
