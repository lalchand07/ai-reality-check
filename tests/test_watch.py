import json

from scripts import watch


PAGE_V1 = "<html><head><title>x</title></head><body><nav>Home</nav><p>Pro plan costs twenty dollars per month for individuals.</p><script>var x=1</script></body></html>"
PAGE_V2 = PAGE_V1.replace("</body>", "<p>New: the Student plan now includes 300 monthly AI credits.</p></body>")


def test_visible_text_strips_noise():
    text = watch.visible_text(PAGE_V1)
    assert "twenty dollars" in text
    assert "var x" not in text
    assert "Home" not in text  # short nav lines dropped


def test_added_lines_only_reports_new_text():
    old, new = watch.visible_text(PAGE_V1), watch.visible_text(PAGE_V2)
    assert watch.added_lines(old, new) == ["New: the Student plan now includes 300 monthly AI credits."]


def test_run_detects_change_and_writes_draft(tmp_path, monkeypatch):
    monkeypatch.setattr(watch, "DRAFTS", tmp_path / "drafts")
    monkeypatch.setattr(watch, "SNAPSHOTS", tmp_path / "snaps")
    monkeypatch.setattr(watch, "ROOT", tmp_path)
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    src = [{"id": "demo", "tool": "demo", "url": "https://example.com"}]

    state, changed = watch.run(src, {}, "2026-09-29", fetcher=lambda u: PAGE_V1)
    assert changed == [] and "demo" in state  # first run only stores a snapshot

    state, changed = watch.run(src, state, "2026-09-30", fetcher=lambda u: PAGE_V2)
    assert changed == ["demo"]
    draft = (tmp_path / "drafts" / "2026-09-30-demo.md").read_text()
    assert "300 monthly AI credits" in draft and "needs human verification" in draft

    _, changed = watch.run(src, state, "2026-10-01", fetcher=lambda u: PAGE_V2)
    assert changed == []


def test_fetch_failure_does_not_crash(tmp_path, monkeypatch):
    monkeypatch.setattr(watch, "SNAPSHOTS", tmp_path / "snaps")
    def boom(url):
        raise OSError("network down")
    state, changed = watch.run([{"id": "d", "tool": "d", "url": "https://x"}], {}, "2026-09-29", fetcher=boom)
    assert state == {} and changed == []
