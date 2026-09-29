"""Validate every data file against its schema plus repo-specific rules.

Usage:
    python -m scripts.validate            # errors fail, stale data warns
    python -m scripts.validate --strict   # stale data also fails
"""
from __future__ import annotations

import argparse
import datetime as dt
import sys

from jsonschema import Draft202012Validator

from scripts.lib import changelog_files, check_files, load_schema, load_yaml, tool_files

STALE_AFTER_DAYS = 60


def _schema_errors(validator, doc, path) -> list[str]:
    return [
        f"{path}: {'/'.join(map(str, e.absolute_path)) or '<root>'}: {e.message}"
        for e in sorted(validator.iter_errors(doc), key=lambda e: list(e.absolute_path))
    ]


def validate(today: dt.date | None = None) -> tuple[list[str], list[str]]:
    today = today or dt.date.today()
    errors: list[str] = []
    warnings: list[str] = []

    tool_v = Draft202012Validator(load_schema("tool"))
    ids = set()
    for path in tool_files():
        doc = load_yaml(path)
        errors += _schema_errors(tool_v, doc, path.name)
        if not isinstance(doc, dict):
            continue
        if doc.get("id") != path.stem:
            errors.append(f"{path.name}: id '{doc.get('id')}' must match file name '{path.stem}'")
        if doc.get("id") in ids:
            errors.append(f"{path.name}: duplicate id '{doc.get('id')}'")
        ids.add(doc.get("id"))
        try:
            age = (today - dt.date.fromisoformat(doc["last_verified"])).days
            if age > STALE_AFTER_DAYS:
                warnings.append(f"{path.name}: last verified {age} days ago, please re-check")
            if age < -1:  # allow one day for time zones
                errors.append(f"{path.name}: last_verified is in the future")
        except (KeyError, ValueError):
            pass

    log_v = Draft202012Validator(load_schema("changelog"))
    for path in changelog_files():
        doc = load_yaml(path)
        errors += _schema_errors(log_v, doc, path.name)
        if isinstance(doc, dict) and doc.get("month") != path.stem:
            errors.append(f"{path.name}: month '{doc.get('month')}' must match file name")
        for i, entry in enumerate((doc or {}).get("entries", []) or []):
            if isinstance(entry, dict) and not str(entry.get("date", "")).startswith(path.stem):
                errors.append(f"{path.name}: entry {i} date {entry.get('date')} is outside {path.stem}")

    check_v = Draft202012Validator(load_schema("reality-check"))
    for path in check_files():
        doc = load_yaml(path)
        errors += _schema_errors(check_v, doc, path.name)
        if isinstance(doc, dict) and doc.get("id") != path.stem:
            errors.append(f"{path.name}: id must match file name")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true", help="treat stale data as an error")
    args = parser.parse_args()

    errors, warnings = validate()
    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    failed = bool(errors) or (args.strict and bool(warnings))
    print("Validation failed." if failed else f"All data valid ({len(warnings)} warnings).")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
