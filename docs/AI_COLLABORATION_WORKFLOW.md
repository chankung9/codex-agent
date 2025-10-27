# AI Collaboration Workflow Blueprint

## Task Structure
- **Active tasks** live in `projects/<project>/tasks/` and follow the YAML template (`task_template.yaml`). Each task tracks `summary`, `owner`, `status`, `links`, and measurable `acceptance_criteria`.
- **Backlog snapshots** reside under `projects/<project>/backlogs/<task_id>/<YYYY-MM-DD-##>.yaml`. These freeze a point-in-time plan or review for traceability.
- When a task moves to `completed`, relocate the YAML file to `projects/<project>/tasks/completed/` to keep the active queue small while retaining history.

## Discuss & Review Flow
1. Open the relevant task file (for example `projects/hello-agent/tasks/frontend_color_controls_001.yaml`) so your IDE extensions inherit context.
2. Trigger a short-form prompt in the target assistant:
   - **Codex / Copilot Chat:** `@codex discuss <task_file> in <project>`
   - **GLM via Cline:** `@glm discuss <task_file> in <project>`
3. Capture the AI recommendations by updating or creating a backlog snapshot under `projects/<project>/backlogs/<task_id>/`.
   - Append structured notes (summary, decisions, next steps) so reviewers can trace how the plan evolved.
   - Include follow-up actions or risks so downstream reviewers can track decisions.
4. Reference the latest backlog snapshot inside the task YAML `links` array. This keeps the live task aligned with conversation history.

## Applying Outcomes
- Convert actionable advice into explicit checklist items in the task or backlog snapshot.
- Update project plans or feature specifications with any new requirements.
- When debate leads to a decision, log it both in the discussion file and the relevant documentation that governs the workstream.

## Tips
- Keep prompts concise; the open file provides context.
- If working offline or without API access, copy the assistant’s response directly into the backlog snapshot so the repository still records the discussion.
