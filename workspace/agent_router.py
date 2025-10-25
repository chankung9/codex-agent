#!/usr/bin/env python3
"""Simple command router that maps agent commands to workspace files.

Usage examples:
  python workspace/agent_router.py "@finance summary" -c "MVP planning still within budget."
  python workspace/agent_router.py "@compliance audit" -c "Verified release checklist alignment."

The script keeps all updates inside the repo so manual + automated flows stay in sync.
"""
from __future__ import annotations

import argparse
import datetime as dt
from pathlib import Path
from typing import Callable, Dict

ROOT = Path(__file__).resolve().parent.parent
FINANCE_DIR = ROOT / "finance"
AUDIT_LOG_DIR = ROOT / "audit" / "logs"
FINANCE_TEMPLATE = FINANCE_DIR / "summary_TEMPLATE.md"
AUTOMATION_HEADING = "## Automation Notes"


class CommandHandler:
    def __init__(self, func: Callable[[str], None]):
        self.func = func

    def __call__(self, content: str) -> None:
        self.func(content.strip())


def timestamp() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def ensure_finance_file(month: str) -> Path:
    target = FINANCE_DIR / f"summary_{month}.md"
    if target.exists():
        return target

    FINANCE_DIR.mkdir(parents=True, exist_ok=True)
    template_text = FINANCE_TEMPLATE.read_text() if FINANCE_TEMPLATE.exists() else ""
    month_label = dt.datetime.strptime(month, "%Y-%m").strftime("%B %Y")
    filled = (
        template_text
        .replace("<Month YYYY>", month_label)
        .replace("<YYYY-MM>", month)
    ) or f"# Monthly Finance Summary — {month_label}\n\n- Draft created automatically."
    target.write_text(filled.rstrip() + "\n")
    return target


def append_automation_note(path: Path, line: str) -> None:
    existing = path.read_text().rstrip()
    if AUTOMATION_HEADING not in existing:
        existing = existing + f"\n\n{AUTOMATION_HEADING}\n"
    elif not existing.endswith("\n"):
        existing += "\n"
    new_text = existing + f"- {line}\n"
    path.write_text(new_text)


def handle_finance_summary(content: str) -> None:
    month = dt.date.today().strftime("%Y-%m")
    path = ensure_finance_file(month)
    note = content or "No additional context provided."
    append_automation_note(path, f"{timestamp()} — {note}")
    print(f"Logged finance summary note in {path.relative_to(ROOT)}")


def ensure_audit_file(day: str) -> Path:
    path = AUDIT_LOG_DIR / f"{day}.md"
    if path.exists():
        return path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"# Audit Log — {day}\n")
    return path


def handle_compliance_audit(content: str) -> None:
    day = dt.date.today().strftime("%Y-%m-%d")
    path = ensure_audit_file(day)
    entry = content or "No additional context provided."
    with path.open("a", encoding="utf-8") as fh:
        fh.write(
            f"- Event: {entry}\n"
            f"  - Owner: Compliance Agent\n"
            f"  - Timestamp: {timestamp()}\n"
        )
    print(f"Logged compliance audit event in {path.relative_to(ROOT)}")


HANDLERS: Dict[str, CommandHandler] = {
    "@finance summary": CommandHandler(handle_finance_summary),
    "@compliance audit": CommandHandler(handle_compliance_audit),
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Route agent commands to repo artifacts.")
    parser.add_argument("command", help="Agent command, e.g., '@finance summary'.")
    parser.add_argument("-c", "--content", default="", help="Text appended to the relevant file.")
    args = parser.parse_args()

    command = args.command.strip()
    handler = HANDLERS.get(command)
    if not handler:
        available = ", ".join(HANDLERS.keys())
        raise SystemExit(f"Unknown command '{command}'. Available: {available}")

    handler(args.content)


if __name__ == "__main__":
    main()
