"""Watch official pages for changes and draft changelog entries for human review.

For each page in data/sources.yaml:
  1. fetch it and reduce it to normalised visible text
  2. compare its hash with .watch-state.json
  3. if it changed, write data/changelog/_drafts/<date>-<id>.md with the new lines
     and (optionally) an AI-written draft summary

Drafts are never published automatically. A maintainer verifies each one against
the source and moves the facts into data/changelog/YYYY-MM.yaml.

Environment:
  ANTHROPIC_API_KEY   optional, enables AI draft summaries
  WATCH_MODEL         optional, model id for summaries (default below)
"""
from __future__ import annotations

import datetime as dt
import difflib
import hashlib
import html
import json
import os
import re
import sys
import urllib.error
import urllib.request

from scripts.lib import DATA, ROOT, load_yaml

STATE_FILE = ROOT / ".watch-state.json"
DRAFTS = DATA / "changelog" / "_drafts"
SNAPSHOTS = ROOT / ".watch-snapshots"
USER_AGENT = "ai-reality-check-watcher/1.0 (+https://github.com/)"
DEFAULT_MODEL = "claude-sonnet-5"
MAX_DIFF_LINES = 80


def fetch(url: str, timeout: int = 30) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        return resp.read().decode(charset, errors="replace")


def visible_text(raw_html: str) -> str:
    """Strip scripts, styles and tags; keep one meaningful line per block."""
    text = re.sub(r"(?is)<(script|style|noscript|svg|head)[^>]*>.*?</\1>", " ", raw_html)
    text = re.sub(r"(?i)<br\s*/?>|</(p|div|li|h[1-6]|tr|td|section|article|nav|header|footer|main|ul|ol|table|blockquote|pre)>", "\n", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    lines = (re.sub(r"\s+", " ", line).strip() for line in text.splitlines())
    # Drop very short lines (nav items, buttons) that change often and mean little.
    return "\n".join(line for line in lines if len(line) >= 25)


def added_lines(old: str, new: str) -> list[str]:
    diff = difflib.unified_diff(old.splitlines(), new.splitlines(), lineterm="", n=0)
    return [l[1:] for l in diff if l.startswith("+") and not l.startswith("+++")][:MAX_DIFF_LINES]


def ai_summary(source: dict, lines: list[str]) -> str | None:
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key or not lines:
        return None
    prompt = (
        "You help maintain a neutral, source-backed tracker of AI developer tools.\n"
        f"New text appeared on {source['url']} (tool: {source['tool']}).\n"
        "Summarise ONLY concrete changes a developer or student would care about "
        "(pricing, limits, models, features, deprecations). No hype, no speculation. "
        "If nothing meaningful changed, reply exactly: NO_MEANINGFUL_CHANGE.\n\n"
        + "\n".join(lines)
    )
    body = json.dumps({
        "model": os.environ.get("WATCH_MODEL", DEFAULT_MODEL),
        "max_tokens": 600,
        "messages": [{"role": "user", "content": prompt}],
    }).encode()
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=body,
        headers={"content-type": "application/json", "x-api-key": key, "anthropic-version": "2023-06-01"},
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.load(resp)
        return "".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text").strip()
    except (urllib.error.URLError, json.JSONDecodeError, TimeoutError) as exc:
        print(f"  AI summary failed: {exc}")
        return None


def write_draft(source: dict, lines: list[str], summary: str | None, today: str) -> None:
    DRAFTS.mkdir(parents=True, exist_ok=True)
    path = DRAFTS / f"{today}-{source['id']}.md"
    parts = [
        f"# Draft: possible change on `{source['id']}`",
        f"- Tool: `{source['tool']}`",
        f"- Source: {source['url']}",
        f"- Detected: {today}",
        "- Status: **needs human verification**",
        "",
        "## AI draft summary (verify before using)",
        summary or "_No AI summary (no API key configured)._",
        "",
        "## New text on the page",
        "```text",
        *lines,
        "```",
    ]
    path.write_text("\n".join(parts) + "\n", encoding="utf-8")
    print(f"  draft written: {path.relative_to(ROOT)}")


def run(sources: list[dict], state: dict, today: str, fetcher=fetch) -> tuple[dict, list[str]]:
    changed = []
    SNAPSHOTS.mkdir(exist_ok=True)
    for src in sources:
        print(f"- {src['id']}: {src['url']}")
        try:
            text = visible_text(fetcher(src["url"]))
        except Exception as exc:  # network errors must never break the whole run
            print(f"  fetch failed: {exc}")
            continue
        digest = hashlib.sha256(text.encode()).hexdigest()
        snap = SNAPSHOTS / f"{src['id']}.txt"
        previous = state.get(src["id"])
        if previous is None:
            print("  first snapshot stored")
        elif previous != digest:
            old = snap.read_text(encoding="utf-8") if snap.exists() else ""
            lines = added_lines(old, text)
            summary = ai_summary(src, lines)
            if summary and summary.strip() == "NO_MEANINGFUL_CHANGE":
                print("  changed, but AI judged it cosmetic")
            elif lines:
                write_draft(src, lines, summary, today)
                changed.append(src["id"])
        else:
            print("  unchanged")
        state[src["id"]] = digest
        snap.write_text(text, encoding="utf-8")
    return state, changed


def main() -> int:
    sources = load_yaml(DATA / "sources.yaml")["watch"]
    state = json.loads(STATE_FILE.read_text()) if STATE_FILE.exists() else {}
    today = dt.date.today().isoformat()
    state, changed = run(sources, state, today)
    STATE_FILE.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n")
    print(f"\n{len(changed)} source(s) changed: {', '.join(changed) or 'none'}")
    if gh_out := os.environ.get("GITHUB_OUTPUT"):
        with open(gh_out, "a", encoding="utf-8") as fh:
            fh.write(f"changed={','.join(changed)}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
