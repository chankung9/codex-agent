# Task Registry

Store structured tasks synced with `.codex/plan.yaml`. Naming convention: `<epic>_<sequence>.yaml`.

Each YAML should include:
- `id`
- `summary`
- `owner`
- `status`
- `links` (docs, repos)

## Archiving
- Active tasks live directly under `projects/hello-agent/tasks/`.
- When a task reaches `completed`, move the YAML into `projects/hello-agent/tasks/completed/` to keep the active queue lean while preserving history.
