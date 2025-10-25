# Release Summary Reports — Codex-Agent Organization

---

version: 1.0  
maintained_by: Compliance Agent  
approved_by: CEO  
last_updated: YYYY-MM-DD

---

## Purpose

This directory stores **aggregated release summaries** (monthly and quarterly) that consolidate metrics, incidents, and compliance data across multiple releases.  
Each summary aligns with audit, KPI, and policy review cycles.

---

## Directory Layout

```
reports/releases/summary/
├── README.md # This file
├── SUMMARY_TEMPLATE.md # Template for new summaries
├── SUMMARY-2025-10.md # Example monthly summary
└── SUMMARY-Q4-2025.md # Example quarterly summary
```

---

## Summary Workflow

### 1. Input Sources

Each summary compiles data from:

- `/reports/releases/YYYY-MM/REL-vX.Y.Z.md` (individual release reports)
- `/reports/kpi/YYYY-WW.md` (weekly KPIs)
- `/reports/incidents/INC-*.md` (incident reports)
- `/reports/audit/AUDIT_LOG_TEMPLATE.md` (audit logs)
- `/docs/POLICY_CHANGELOG.md` (policy context)

### 2. Compilation Steps

1. Create a new summary file using `SUMMARY_TEMPLATE.md`
2. Aggregate:
   - Total releases
   - Success/failure ratio
   - Deployment and incident metrics
   - Compliance check results
3. Review with Engineer, Product, and Compliance agents
4. Submit for CEO approval

### 3. Output Format

- **Monthly summaries:** `SUMMARY-YYYY-MM.md`
- **Quarterly summaries:** `SUMMARY-Q#.md`
- Each file must include:
  - Overview
  - Key metrics
  - KPI and compliance sections
  - Approvals and signatures

---

## Automation Option

Future workflow (`.github/workflows/summary-aggregate.yml`) may:

- Parse all release reports for the current month
- Generate a summary draft automatically
- Commit to this directory for manual approval

---

## Review & Archiving

- Summaries retained for **at least 24 months**
- Archive old summaries in `/reports/releases/archive/`
- Quarterly summaries feed into:
  - `/reports/audit/`
  - `/docs/POLICY_REVIEW_FORM.md`

---

> **Note:**  
> Each summary file should be written in UTF-8 Markdown and reference all linked release and incident documents.  
> Never overwrite historical summaries—always create a new version with timestamped ID.
