"""Regenerate the auto-built parts of README.md and docs/data.json from /data.

Usage:
    python -m scripts.build          # write files
    python -m scripts.build --check  # exit 1 if files are out of date (used in CI)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from urllib.parse import urlparse

from scripts.lib import ROOT, load_changelog, load_checks, load_tools

README = ROOT / "README.md"
DATA_JSON = ROOT / "docs" / "data.json"
DATA_JS = ROOT / "docs" / "data.js"  # lets the site work from file:// too
LATEST_CHANGES = 10

VERDICT_BADGE = {
    "true": "✅ True",
    "partly-true": "🟡 Partly true",
    "misleading": "🟠 Misleading",
    "false": "❌ False",
    "unproven": "❔ Unproven",
}
STUDENT = {True: "✅", False: "❌", "partial": "🟡", "unknown": "❔"}
FREE = {True: "✅", False: "❌", "unknown": "❔"}
IMPACT = {"high": "🔴", "medium": "🟠", "low": "⚪", "low-for-users": "⚪"}


def _md(text: str) -> str:
    return " ".join(str(text).split()).replace("|", "\\|")


def _domain(url: str) -> str:
    return urlparse(url).netloc.removeprefix("www.")


def _links(urls: list[str], limit: int = 2) -> str:
    return " ".join(f"[{_domain(u)}]({u})" for u in urls[:limit])


def tools_table(tools: list[dict]) -> str:
    rows = [
        "| Tool | Best for | Free tier | Students | Plans | Verified |",
        "|---|---|:-:|:-:|---|---|",
    ]
    for t in tools:
        plans = "; ".join(f"{p['plan']}: {p['price']}" for p in t["pricing"])
        rows.append(
            f"| [**{_md(t['name'])}**](data/tools/{t['id']}.yaml) | {_md(t['best_for'][0])} "
            f"| {FREE.get(t.get('free_tier', 'unknown'), '❔')} "
            f"| {STUDENT.get(t['student_friendly'], '❔')} | {_md(plans)} | {t['last_verified']} |"
        )
    return "\n".join(rows)


def changes_list(entries: list[dict]) -> str:
    lines = []
    for e in entries[:LATEST_CHANGES]:
        lines.append(
            f"- {IMPACT.get(e['impact'], '⚪')} **{e['date']}** · {_md(e['title'])}. "
            f"{_md(e['summary'])} ({_links(e['sources'], 1)})"
        )
    return "\n".join(lines) or "_No changes recorded yet._"


def checks_list(checks: list[dict]) -> str:
    blocks = []
    for c in checks:
        blocks.append(
            f"<details>\n<summary><b>{VERDICT_BADGE[c['verdict']]}</b>: “{_md(c['claim'])}”</summary>\n\n"
            f"{_md(c['explanation'])}\n\n"
            + (f"**What it means for you:** {_md(c['what_it_means_for_you'])}\n\n" if c.get("what_it_means_for_you") else "")
            + f"Sources: {_links(c['sources'], 3)} · checked {c['date']}\n</details>"
        )
    return "\n\n".join(blocks) or "_No reality checks yet._"


def replace_block(text: str, name: str, body: str) -> str:
    pattern = re.compile(rf"(<!-- {name}:START -->)(.*?)(<!-- {name}:END -->)", re.S)
    if not pattern.search(text):
        raise SystemExit(f"README is missing the <!-- {name}:START/END --> markers")
    return pattern.sub(lambda m: f"{m.group(1)}\n{body}\n{m.group(3)}", text)


def render() -> tuple[str, str]:
    tools, changes, checks = load_tools(), load_changelog(), load_checks()
    readme = README.read_text(encoding="utf-8")
    readme = replace_block(readme, "TOOLS", tools_table(tools))
    readme = replace_block(readme, "CHANGES", changes_list(changes))
    readme = replace_block(readme, "CHECKS", checks_list(checks))
    data = json.dumps({"tools": tools, "changes": changes, "checks": checks}, indent=2, ensure_ascii=False) + "\n"
    return readme, data


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    readme, data = render()
    data_js = f"window.ARC_DATA = {data.rstrip()};\n"

    def current(path):
        return path.read_text(encoding="utf-8") if path.exists() else ""

    if args.check:
        stale = [n for n, new, old in (("README.md", readme, current(README)),
                                        ("docs/data.json", data, current(DATA_JSON)),
                                        ("docs/data.js", data_js, current(DATA_JS))) if new != old]
        if stale:
            print("Out of date: " + ", ".join(stale) + ". Run: python -m scripts.build")
            return 1
        print("Generated files are up to date.")
        return 0

    README.write_text(readme, encoding="utf-8")
    DATA_JSON.write_text(data, encoding="utf-8")
    DATA_JS.write_text(data_js, encoding="utf-8")
    print("Built README.md, docs/data.json and docs/data.js")
    return 0


if __name__ == "__main__":
    sys.exit(main())
