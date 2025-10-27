#!/usr/bin/env python3
"""Simple command router that maps agent commands to workspace files.

Usage examples:
  python workspace/agent_router.py "@finance summary" -c "MVP planning still within budget."
  python workspace/agent_router.py "@compliance audit" -c "Verified release checklist alignment."
  python workspace/agent_router.py "@copilot plan" -c "Drafted rollout checklist."
  python workspace/agent_router.py "@codex review" -c "Flagged missing test coverage."
  python workspace/agent_router.py "@glm discuss" -c "Finalized launch timeline." --scope "product design engineering"

The script keeps all updates inside the repo so manual + automated flows stay in sync.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
from pathlib import Path
from typing import Any, Callable, Dict
import copy

ROOT = Path(__file__).resolve().parent.parent
FINANCE_DIR = ROOT / "finance"
AUDIT_LOG_DIR = ROOT / "audit" / "logs"
TEAMS_DIR = ROOT / "teams"
ENGINEERING_DISCUSSIONS_DIR = TEAMS_DIR / "engineering" / "discussions"
CROSS_FUNCTIONAL_DISCUSSIONS_DIR = TEAMS_DIR / "cross-functional" / "discussions"
CONFIG_DIR = ROOT / "workspace" / "config"
AGENT_CONFIG_PATH = CONFIG_DIR / "agents.json"
FINANCE_TEMPLATE = FINANCE_DIR / "summary_TEMPLATE.md"
AUTOMATION_HEADING = "## Automation Notes"
DISCUSSION_HEADING = "## Notes"
ENV_CONFIG_JSON_KEY = "CODEX_AGENT_CONFIG_JSON"
ENV_AGENT_PREFIX = "CODEX_AGENT"
DEFAULT_ACTION_DIRECTORIES = {
    "plan": ENGINEERING_DISCUSSIONS_DIR,
    "review": ENGINEERING_DISCUSSIONS_DIR,
    "discuss": CROSS_FUNCTIONAL_DISCUSSIONS_DIR,
}


class CommandHandler:
    def __init__(self, func: Callable[[str, argparse.Namespace], None]):
        self.func = func

    def __call__(self, content: str, args: argparse.Namespace) -> None:
        self.func(content.strip(), args)


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


def handle_finance_summary(content: str, _: argparse.Namespace) -> None:
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


def handle_compliance_audit(content: str, _: argparse.Namespace) -> None:
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


def ensure_discussion_file(base_dir: Path, filename: str, title: str) -> Path:
    path = base_dir / filename
    if path.exists():
        return path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"# {title}\n\n")
    return path


def append_discussion_entry(path: Path, platform_label: str, entry: str) -> None:
    note = entry or "No additional context provided."
    existing = path.read_text().rstrip()
    if DISCUSSION_HEADING not in existing:
        existing = existing + f"\n\n{DISCUSSION_HEADING}\n"
    elif not existing.endswith("\n"):
        existing += "\n"
    update = f"- {timestamp()} — {platform_label}: {note}\n"
    path.write_text(existing + update)


def slugify_scope(scope: str) -> str:
    slug = re.sub(r"[^a-z0-9-]", "-", scope.lower().strip())
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug or "general"


def format_scope_label(scope: str) -> str:
    if not scope:
        return "General"
    return " ".join(part.capitalize() for part in scope.split())


AI_AGENT_LABELS = {
    "copilot": "GitHub Copilot",
    "codex": "Codex",
    "glm": "GLM 4.6",
}

SUPPORTED_AI_ACTIONS = {"plan", "review", "discuss"}


HANDLERS: Dict[str, CommandHandler] = {
    "@finance summary": CommandHandler(handle_finance_summary),
    "@compliance audit": CommandHandler(handle_compliance_audit),
}


def handle_ai_command(
    agent_key: str,
    action: str,
    content: str,
    args: argparse.Namespace,
    agent_settings: Dict[str, Dict[str, Any]],
) -> None:
    agent_label = AI_AGENT_LABELS[agent_key]
    day = dt.date.today().strftime("%Y-%m-%d")
    settings = agent_settings.get(agent_key, {})

    if action == "discuss":
        scope_raw = getattr(args, "scope", "") or settings.get("default_scope", "")
        slug = slugify_scope(scope_raw)
        base_path = settings.get("actions", {}).get("discuss")
        base_dir = (ROOT / base_path) if base_path else DEFAULT_ACTION_DIRECTORIES["discuss"]
        subdir = base_dir / slug
        title_scope = format_scope_label(scope_raw)
        filename = f"{agent_key}_discussion_{day}.md"
        title = f"Cross-Team Discussion ({title_scope}) — {day}"
        path = ensure_discussion_file(subdir, filename, title)
        entry_label = f"{agent_label} Discussion"
    else:
        base_path = settings.get("actions", {}).get(action)
        base_dir = (ROOT / base_path) if base_path else DEFAULT_ACTION_DIRECTORIES[action]
        filename = f"{agent_key}_{action}_{day}.md"
        title = f"{agent_label} {action.capitalize()} — {day}"
        path = ensure_discussion_file(base_dir, filename, title)
        entry_label = f"{agent_label} {action.capitalize()}"

    append_discussion_entry(path, entry_label, content)
    relative = path.relative_to(ROOT)
    print(f"Logged {entry_label} update in {relative}")


def ensure_agent_config_file() -> Path:
    if AGENT_CONFIG_PATH.exists():
        return AGENT_CONFIG_PATH

    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    default_payload = {
        agent: {
            "api_key": f"<SET_{agent.upper()}_TOKEN>",
            "actions": {
                "plan": "teams/engineering/discussions/",
                "review": "teams/engineering/discussions/",
                "discuss": "teams/cross-functional/discussions/",
            },
            "default_scope": "general",
        }
        for agent in AI_AGENT_LABELS
    }
    AGENT_CONFIG_PATH.write_text(json.dumps(default_payload, indent=2) + "\n", encoding="utf-8")
    print(
        "Initialized agent configuration template at "
        f"{AGENT_CONFIG_PATH.relative_to(ROOT)}. Update this file with real credentials."
    )
    return AGENT_CONFIG_PATH


def env_agent_key(agent: str, *parts: str) -> str:
    joined = "_".join(part.upper() for part in parts)
    return f"{ENV_AGENT_PREFIX}_{agent.upper()}_{joined}" if joined else f"{ENV_AGENT_PREFIX}_{agent.upper()}"


def apply_env_overrides(settings: Dict[str, Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:

    # Work on a deep copy to avoid mutating the caller's object.
    result = copy.deepcopy(settings)

    for agent in AI_AGENT_LABELS:
        agent_settings = result.setdefault(agent, {})
        actions = agent_settings.setdefault("actions", {})

        api_key_env = os.getenv(env_agent_key(agent, "api", "key"))
        if api_key_env:
            agent_settings["api_key"] = api_key_env

        default_scope_env = os.getenv(env_agent_key(agent, "default", "scope"))
        if default_scope_env:
            agent_settings["default_scope"] = default_scope_env

        for action in SUPPORTED_AI_ACTIONS:
            action_env = os.getenv(env_agent_key(agent, action, "dir"))
            if action_env:
                actions[action] = action_env

    return result


def load_agent_settings() -> Dict[str, Dict[str, Any]]:
    def _validate_and_normalize(raw: Any) -> Dict[str, Dict[str, Any]]:
        if not isinstance(raw, dict):
            raise SystemExit(f"Agent configuration must be a JSON object mapping agent keys to settings.")

        normalized: Dict[str, Dict[str, Any]] = {}
        # Defaults matching ensure_agent_config_file()
        default_actions = {
            "plan": "teams/engineering/discussions/",
            "review": "teams/engineering/discussions/",
            "discuss": "teams/cross-functional/discussions/",
        }

        for agent in AI_AGENT_LABELS:
            entry = raw.get(agent, {})
            if not isinstance(entry, dict):
                if agent in raw:
                    raise SystemExit(f"Invalid settings for agent '{agent}': expected an object.")
                entry = {}

            api_key = entry.get("api_key", f"<SET_{agent.upper()}_TOKEN>")
            if not isinstance(api_key, str):
                raise SystemExit(f"'api_key' for agent '{agent}' must be a string.")

            default_scope = entry.get("default_scope", "general")
            if not isinstance(default_scope, str):
                raise SystemExit(f"'default_scope' for agent '{agent}' must be a string.")

            actions_raw = entry.get("actions", {})
            if not isinstance(actions_raw, dict):
                raise SystemExit(f"'actions' for agent '{agent}' must be an object mapping action->path.")

            actions: Dict[str, str] = {}
            for k, v in actions_raw.items():
                if not isinstance(k, str) or not isinstance(v, str):
                    raise SystemExit(f"Action mapping for agent '{agent}' contains non-string key/value.")
                actions[k] = v

            # Ensure supported actions exist with sensible defaults if omitted.
            for act, default_dir in default_actions.items():
                actions.setdefault(act, default_dir)

            normalized[agent] = {
                "api_key": api_key,
                "default_scope": default_scope,
                "actions": actions,
            }

        return normalized

    env_payload = os.getenv(ENV_CONFIG_JSON_KEY)
    if env_payload:
        try:
            data = json.loads(env_payload)
        except json.JSONDecodeError as exc:
            raise SystemExit(
                f"Failed to parse JSON from {ENV_CONFIG_JSON_KEY}: {exc}"
            ) from exc
        validated = _validate_and_normalize(data)
        return apply_env_overrides(validated)

    path = ensure_agent_config_file()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(
            f"Failed to parse agent configuration at {path.relative_to(ROOT)}: {exc}"
        ) from exc

    validated = _validate_and_normalize(data)
    return apply_env_overrides(validated)


def main() -> None:
    parser = argparse.ArgumentParser(description="Route agent commands to repo artifacts.")
    parser.add_argument("command", help="Agent command, e.g., '@finance summary'.")
    parser.add_argument("-c", "--content", default="", help="Text appended to the relevant file.")
    parser.add_argument(
        "--scope",
        default="",
        help=(
            "Optional scope for discussion commands, such as 'product design engineering'. "
            "Used to group cross-functional sessions across AI agents."
        ),
    )
    args = parser.parse_args()

    agent_settings = load_agent_settings()
    command = args.command.strip()
    handler = HANDLERS.get(command)
    if handler:
        handler(args.content, args)
        return

    match = re.fullmatch(r"@([a-z0-9_-]+)\s+([a-z0-9_-]+)", command)
    if match:
        agent_key, action = match.groups()
        if agent_key in AI_AGENT_LABELS and action in SUPPORTED_AI_ACTIONS:
            handle_ai_command(agent_key, action, args.content, args, agent_settings)
            return

    available_core = ", ".join(HANDLERS.keys())
    ai_options = ", ".join(
        f"@{agent} {action}" for agent in AI_AGENT_LABELS for action in sorted(SUPPORTED_AI_ACTIONS)
    )
    raise SystemExit(
        f"Unknown command '{command}'. Available: {', '.join(filter(None, [available_core, ai_options]))}"
    )


if __name__ == "__main__":
    main()
