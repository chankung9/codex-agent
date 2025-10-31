# Task Registry

Use this directory to store structured task manifests aligned with `.codex/plan.yaml`.  
Naming convention: `<epic>_<sequence>.yaml`.

Each YAML should include:
- `id`
- `summary`
- `owner`
- `status`
- `links` (docs, repos, tickets)

## Archiving
- Active tasks live directly under `projects/cyphercast/tasks/`.
- When a task reaches `completed`, move the YAML into `projects/cyphercast/tasks/completed/` to keep the active queue lean while preserving history.
