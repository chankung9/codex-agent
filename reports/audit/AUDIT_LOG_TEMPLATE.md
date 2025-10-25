header

# Audit Log Template — Codex-Agent Organization

version: 1.0
created_at: YYYY-MM-DD
auditor: Compliance Agent
approved_by: Legal / CEO

---

## 1) Audit Overview

| Field          | Description                                     |
| -------------- | ----------------------------------------------- |
| Audit ID       | AUD-YYYY-###                                    |
| Scope          | e.g. Security, Data Handling, Finance, Process  |
| Type           | [Internal / External / Automated]               |
| Period Covered | YYYY-MM-DD → YYYY-MM-DD                         |
| Status         | [In Progress / Completed / Reviewed / Approved] |

---

## 2) Objectives

- Verify compliance with organizational policies.
- Validate execution of workflows and reports.
- Ensure data integrity and process transparency.

---

## 3) Evidence Summary

| Evidence ID | Source      | Description | Verified | Link / Path |
| ----------- | ----------- | ----------- | -------- | ----------- |
| EV-001      | System Logs |             | [Y/N]    | /logs/...   |
| EV-002      | Reports     |             |          |             |
|             |             |             |          |             |

---

## 4) Findings

| Finding ID | Category | Severity | Description | Impact | Recommendation |
| ---------- | -------- | -------- | ----------- | ------ | -------------- |
| F-001      | Policy   | Medium   |             |        |                |
| F-002      | Security | High     |             |        |                |
|            |          |          |             |        |                |

---

## 5) Corrective Actions

| Action ID | Owner    | Target Date | Status         | Notes |
| --------- | -------- | ----------- | -------------- | ----- |
| A-001     | Engineer |             | [Pending/Done] |       |
| A-002     | HR       |             |                |       |

---

## 6) Reviewer Comments

- Reviewer:
- Review Date:
- Comments:

---

## 7) Attachments

- Related incident reports: `/reports/incidents/INC-*.md`
- KPI references: `/reports/kpi/YYYY-WW.md`
- Policy documents: `/docs/ORG_DESIGN.md`, `/docs/POLICY.md`

---

> **Note:**  
> Each audit file must be stored under `reports/audit/logs/` and named `AUD-YYYY-MM-DD.md`.  
> Keep immutable copies for at least 12 months.
