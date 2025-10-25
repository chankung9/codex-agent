# Releases Directory — Codex-Agent Organization

---

version: 1.1
maintained_by: Engineer Agent
approved_by: Product & Compliance Agents
last_updated: YYYY-MM-DD

---

# Releases Directory — Codex-Agent Organization

## Purpose

This directory stores all **release-related documents** for Codex-Agent projects, including:

- Individual release reports
- Monthly and quarterly summaries
- Templates used for report generation

All files here provide traceability between deployment activity, incidents, and policy compliance.

## Directory Layout

```
reports/releases/
├── README.md # This file
├── RELEASE_TEMPLATE.md # Standard release report template
├── 2025-10/ # Folder for release reports by month
│ ├── REL-v1.0.0.md
│ └── REL-v1.1.0.md
└── summary/ # Optional summaries
└── SUMMARY-Q4-2025.md
```

---

## File Naming

| Type              | Format          | Example              |
| ----------------- | --------------- | -------------------- |
| Release Report    | `REL-vX.Y.Z.md` | `REL-v1.0.0.md`      |
| Folder (by month) | `YYYY-MM`       | `2025-10`            |
| Summary           | `SUMMARY-Q#.md` | `SUMMARY-Q4-2025.md` |

---

## Workflow

### 1. Pre-Release

1. Complete required checklists:
   - `/docs/RELEASE_CHECKLIST.md`
   - `/docs/SECURITY_CHECKLIST.md`
2. Confirm branch → `main`
3. Tag the version (`vX.Y.Z`)

### 2. During Release

1. Copy `RELEASE_TEMPLATE.md` into the correct month folder.
2. Fill all sections (overview, validation, metrics, approvals).
3. Link related files:
   - `/reports/audit/AUDIT_LOG_TEMPLATE.md`
   - `/reports/incidents/INCIDENT_TEMPLATE.md`
   - `/docs/POLICY_CHANGELOG.md`

### 3. Post-Release

1. Verify performance metrics and incident data.
2. File signed report under `/reports/releases/YYYY-MM/`.
3. Summarize in `/reports/releases/summary/`.

---

## Retention Policy

- Keep all release records for **at least 24 months**.
- Older reports may be archived under `/reports/archive/` with checksum verification.
- Each release report must include digital signatures from Product, Engineer, and Compliance agents.

---

## Related Documents

- `/docs/RELEASE_CHECKLIST.md`
- `/docs/SECURITY_CHECKLIST.md`
- `/reports/audit/AUDIT_LOG_TEMPLATE.md`
- `/reports/incidents/INCIDENT_TEMPLATE.md`

---

> **Note:**  
> Each release report must be UTF-8 encoded and Markdown-linted before commit.  
> Workflow automation may validate structure and cross-references automatically.
