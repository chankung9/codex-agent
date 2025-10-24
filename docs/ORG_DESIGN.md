# Codex-Agent Organization Design

Codex-Agent mirrors a lightweight multi-agent organization where each functional unit (product, engineering, HR, finance, audit) collaborates through shared artifacts. The design emphasizes:

1. **Clear ownership:** Each directory inside `agents/` holds prompts, SOPs, and context for a dedicated agent persona.
2. **Documentation-first flow:** All initiatives originate in `.codex/plan.yaml`, with execution notes captured in `docs/` and operational evidence archived under `audit/` and `reports/`.
3. **Branch hygiene:** `main` remains the stable reference, `dev` aggregates day-to-day work, and `codex/auto` is reserved for automated commits or tool-generated changes.
4. **Integration hooks:** External sandboxes (for example, `hello-agent`) register via `docs/PROJECTS.md`, and each integration receives its own playbook under `docs/INTEGRATION_*.md`.

This blueprint ensures the organization can grow by simply adding new agent directories, templates, or registry entries without reworking the base structure.
