[เนื้อหาด้านบน]

# Reports Directory — Codex-Agent Organization

This directory contains all organizational reporting templates and generated reports used by HR, Engineering, Product, and Compliance agents.

## Structure

| Path              | Description                                             | Owner             |
| ----------------- | ------------------------------------------------------- | ----------------- |
| `KPI_TEMPLATE.md` | Weekly performance and operational KPI report template. | HR Agent          |
| `audit/`          | Compliance and audit logs (auto-generated).             | Compliance Agent  |
| `incidents/`      | Incident reports and post-mortems.                      | Engineering Agent |
| `training/`       | Learning and upskilling progress.                       | HR Agent          |
| `finance/`        | Budget and cost summaries (optional).                   | Finance Agent     |

## Usage

1. **Weekly Reports**

   - HR agent generates a new report each week by copying `KPI_TEMPLATE.md`.
   - File name format: `reports/kpi/YYYY-WW.md`
   - Example:
     ```
     reports/kpi/2025-W43.md
     ```

2. **Incident Reports**

   - Engineering agent creates a new file under `reports/incidents/` per event.
   - Example:
     ```
     reports/incidents/INC-2025-001.md
     ```

3. **Audit Logs**

   - Compliance agent stores verification results in `reports/audit/`.
   - Format: `audit/logs/YYYY-MM-DD.md`

4. **Linking to Other Systems**
   - Each report should reference related entities:
     - `/docs/ORG_DESIGN.md` — structural context
     - `/agents/` — responsible agents
     - `/projects/` — linked projects

## hello-agent MVP Reporting Alignment

- Finance + product reviewers must summarize MVP metrics using `reports/summary_TEMPLATE.md` before approvals.
- Reference `projects/hello-agent/docs/MVP_PLAN.md` milestones in each summary to ensure cadence consistency.
- When filing monthly updates, include links to audit entries documenting doc-sync tests and reporting sign-offs.

## Workflow Integration

When automated workflows are enabled:

- New reports will be checked for UTF-8 encoding and Markdown integrity.
- KPI updates can trigger summary sync to `/reports/summary/latest.md`.

## Versioning

Each report file is committed individually for auditability.  
Keep historical versions — do not overwrite past reports.

---

> **Note:** Follow the `KPI_TEMPLATE.md` structure strictly to ensure compatibility with future analytics automation.
