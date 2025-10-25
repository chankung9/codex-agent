# Security Checklist — Codex-Agent Organization

version: 1.0  
maintained_by: Engineer Agent  
approved_by: Compliance Agent  
last_reviewed: YYYY-MM-DD

---

## 1) Purpose

This checklist ensures all releases, deployments, and merges comply with the organization's Security Policy (`/docs/SECURITY_POLICY.md`).  
It must be completed and attached to every pull request or release candidate.

---

## 2) Project Information

| Field        | Description                      |
| ------------ | -------------------------------- |
| Project Name |                                  |
| Branch       |                                  |
| Reviewer     |                                  |
| Date         |                                  |
| Review Type  | [Pre-Deploy / Pre-Merge / Audit] |

---

## 3) Access Control

| #   | Check                                                          | Status | Notes |
| --- | -------------------------------------------------------------- | ------ | ----- |
| 1   | All credentials and secrets are stored securely (not in repo). | [ ]    |       |
| 2   | Repository permissions verified (no excess access).            | [ ]    |       |
| 3   | MFA enabled for all contributors.                              | [ ]    |       |

---

## 4) Dependency & Code Security

| #   | Check                                                                           | Status | Notes |
| --- | ------------------------------------------------------------------------------- | ------ | ----- |
| 1   | Dependencies scanned for vulnerabilities (npm audit / cargo audit / pip-audit). | [ ]    |       |
| 2   | No deprecated or unmaintained packages used.                                    | [ ]    |       |
| 3   | Static code analysis performed (e.g., `cargo clippy`, `eslint`).                | [ ]    |       |
| 4   | Secrets and keys scanned (`trufflehog`, `gitleaks`).                            | [ ]    |       |
| 5   | Code signed or checksum verified (if applicable).                               | [ ]    |       |

---

## 5) Data Handling

| #   | Check                                            | Status | Notes |
| --- | ------------------------------------------------ | ------ | ----- |
| 1   | Sensitive data encrypted in transit and at rest. | [ ]    |       |
| 2   | No PII or confidential data hardcoded.           | [ ]    |       |
| 3   | Backups verified for integrity.                  | [ ]    |       |

---

## 6) Infrastructure & Network

| #   | Check                                     | Status | Notes |
| --- | ----------------------------------------- | ------ | ----- |
| 1   | Environment separated (dev/staging/prod). | [ ]    |       |
| 2   | HTTPS enforced everywhere.                | [ ]    |       |
| 3   | Firewall and IP restrictions validated.   | [ ]    |       |
| 4   | Monitoring and alerting configured.       | [ ]    |       |

---

## 7) CI/CD Pipeline

| #   | Check                                           | Status | Notes |
| --- | ----------------------------------------------- | ------ | ----- |
| 1   | CI runs all tests and lint checks before merge. | [ ]    |       |
| 2   | Secrets masked in CI logs.                      | [ ]    |       |
| 3   | Build artifacts signed and verified.            | [ ]    |       |
| 4   | Rollback plan documented.                       | [ ]    |       |

---

## 8) Incident Preparedness

| #   | Check                                           | Status | Notes |
| --- | ----------------------------------------------- | ------ | ----- |
| 1   | Incident contact list available and up to date. | [ ]    |       |
| 2   | Recovery scripts tested.                        | [ ]    |       |
| 3   | `/reports/incidents/` template linked.          | [ ]    |       |

---

## 9) Compliance Review

| #   | Check                                                                     | Status | Notes |
| --- | ------------------------------------------------------------------------- | ------ | ----- |
| 1   | Policy version verified (`/docs/POLICY.md` & `/docs/SECURITY_POLICY.md`). | [ ]    |       |
| 2   | Security checklist reviewed by Compliance Agent.                          | [ ]    |       |
| 3   | Findings logged in `/reports/audit/`.                                     | [ ]    |       |

---

## 10) Final Approval

| Field         | Description          |
| ------------- | -------------------- |
| Approved By   |                      |
| Date          |                      |
| Sign-off Type | [Manual / Automated] |

---

> **Usage:**  
> Attach this file to every PR or release branch.  
> Mark all checks `[x]` when verified.  
> Store final version under `/reports/audit/` if used in an audit cycle.
