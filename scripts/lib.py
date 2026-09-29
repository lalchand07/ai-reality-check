"""Shared helpers for loading and normalising repo data."""
from __future__ import annotations

import datetime as dt
import json
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SCHEMA = ROOT / "schema"


def _stringify_dates(obj: Any) -> Any:
    """YAML turns 2026-09-29 into a date object; keep everything as ISO strings."""
    if isinstance(obj, (dt.date, dt.datetime)):
        return obj.isoformat()[:10]
    if isinstance(obj, dict):
        return {k: _stringify_dates(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_stringify_dates(v) for v in obj]
    return obj


def load_yaml(path: Path) -> Any:
    with path.open(encoding="utf-8") as fh:
        return _stringify_dates(yaml.safe_load(fh))


def _visible(paths):
    return sorted(p for p in paths if not p.name.startswith("_"))


def tool_files() -> list[Path]:
    return _visible((DATA / "tools").glob("*.yaml"))


def changelog_files() -> list[Path]:
    return _visible((DATA / "changelog").glob("*.yaml"))


def check_files() -> list[Path]:
    return _visible((DATA / "reality-checks").glob("*.yaml"))


def load_tools() -> list[dict]:
    return sorted((load_yaml(p) for p in tool_files()), key=lambda t: t["name"].lower())


def load_changelog() -> list[dict]:
    entries = []
    for p in changelog_files():
        entries.extend(load_yaml(p).get("entries", []))
    return sorted(entries, key=lambda e: e["date"], reverse=True)


def load_checks() -> list[dict]:
    return sorted((load_yaml(p) for p in check_files()), key=lambda c: c["date"], reverse=True)


def load_schema(name: str) -> dict:
    return json.loads((SCHEMA / f"{name}.schema.json").read_text(encoding="utf-8"))
