import datetime as dt

from scripts import build, validate
from scripts.lib import load_changelog, load_checks, load_tools


def test_repository_data_is_valid():
    errors, _ = validate.validate(today=dt.date(2026, 9, 29))
    assert errors == []


def test_every_tool_has_https_sources():
    for tool in load_tools():
        assert tool["sources"], tool["id"]
        assert all(u.startswith("https://") for u in tool["sources"])


def test_changelog_sorted_newest_first():
    dates = [e["date"] for e in load_changelog()]
    assert dates == sorted(dates, reverse=True)


def test_reality_checks_need_two_sources():
    for check in load_checks():
        assert len(check["sources"]) >= 2, check["id"]


def test_staleness_warning(tmp_path, monkeypatch):
    _, warnings = validate.validate(today=dt.date(2027, 6, 1))
    assert warnings, "old data should produce staleness warnings"


def test_generated_files_up_to_date():
    readme, data = build.render()
    assert readme == build.README.read_text(encoding="utf-8")
    assert data == build.DATA_JSON.read_text(encoding="utf-8")


def test_table_escapes_pipes():
    tool = {
        "id": "x", "name": "A|B", "best_for": ["c|d"], "free_tier": True,
        "student_friendly": "partial", "pricing": [{"plan": "p", "price": "$1"}],
        "last_verified": "2026-09-29",
    }
    row = build.tools_table([tool]).splitlines()[-1]
    assert "A\\|B" in row and "c\\|d" in row
