# Incident Report Template — Codex-Agent Organization

version: 1.0
created_at: YYYY-MM-DD
updated_at: YYYY-MM-DD
prepared_by: Engineer Agent
approved_by: CTO / CEO

---

## 1) Incident Summary

| Field            | Description                                                    |
| ---------------- | -------------------------------------------------------------- |
| Incident ID      | INC-YYYY-###                                                   |
| Severity         | [Critical / High / Medium / Low]                               |
| Status           | [Open / Investigating / Mitigated / Resolved / Closed]         |
| Detection Method | [Monitoring / User Report / Audit / Other]                     |
| Affected Systems | e.g. hello-agent, token-vault, pipeline                        |
| Impact Summary   | Short, factual description of what broke and who was affected. |

---

## 2) Timeline

| Timestamp        | Event       | Owner         |
| ---------------- | ----------- | ------------- |
| YYYY-MM-DD HH:MM | Description | Engineer name |
|                  |             |               |

---

## 3) Root Cause Analysis (RCA)

**Problem Statement:**  
Describe what went wrong technically.

**Immediate Cause:**  
Identify the triggering failure or bug.

**Contributing Factors:**

- Environment issues
- Configuration errors
- Communication gaps

**Root Cause (5 Whys):**

1. Why?
2. Why?
3. Why?
4. Why?
5. Why?

---

## 4) Resolution

| Step | Action | Owner | Timestamp |
| ---- | ------ | ----- | --------- |
| 1    |        |       |           |
| 2    |        |       |           |

**Verification Result:**  
✅ Confirmed fix applied and validated.

---

## 5) Prevention & Follow-up

| Area          | Preventive Action | Owner | Due Date |
| ------------- | ----------------- | ----- | -------- |
| Code          |                   |       |          |
| Monitoring    |                   |       |          |
| Communication |                   |       |          |
| Documentation |                   |       |          |

---

## 6) Lessons Learned

- What went well:
- What went poorly:
- What to change next time:

---

## 7) Attachments

- Log snapshots: `/reports/audit/logs/YYYY-MM-DD.md`
- Related tasks: `/projects/.../tasks/...`
- Evidence: URLs, screenshots, etc.

---

> Use this template for every production or staging incident.  
> Commit each file as `reports/incidents/INC-YYYY-###.md` with a clear message.
