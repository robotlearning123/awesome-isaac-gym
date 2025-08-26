import os
import sys
from pathlib import Path

import textwrap

# Make the repo's scripts/ importable
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.research_bot import (  # type: ignore
    parse_arxiv_feed,
    update_readme,
    extract_existing_ids_from_readme,
    render_bullets,
)


def test_parse_arxiv_feed_parses_entries():
    xml = textwrap.dedent(
        """
        <feed xmlns="http://www.w3.org/2005/Atom">
          <entry>
            <id>http://arxiv.org/abs/2401.00001v1</id>
            <updated>2024-01-01T12:00:00Z</updated>
            <published>2024-01-01T12:00:00Z</published>
            <title>Test Paper One</title>
            <author><name>Alice</name></author>
            <author><name>Bob</name></author>
            <link rel="alternate" type="text/html" href="https://arxiv.org/abs/2401.00001v1"/>
          </entry>
          <entry>
            <id>http://arxiv.org/abs/2401.00002v2</id>
            <updated>2024-01-02T12:00:00Z</updated>
            <published>2024-01-02T12:00:00Z</published>
            <title>Test Paper Two</title>
            <author><name>Carol</name></author>
            <link rel="alternate" type="text/html" href="https://arxiv.org/abs/2401.00002v2"/>
          </entry>
        </feed>
        """
    ).encode()

    papers = parse_arxiv_feed(xml)
    assert len(papers) == 2
    assert papers[0]["id"] == "2401.00001"
    assert papers[0]["title"] == "Test Paper One"
    assert papers[0]["abs_url"] == "https://arxiv.org/abs/2401.00001"
    assert papers[0]["pdf_url"].endswith("2401.00001.pdf")


def test_update_readme_appends_when_markers_absent(tmp_path: Path):
    readme = tmp_path / "README.md"
    readme.write_text("# Title\n\nSome content\n", encoding="utf-8")
    bullets = "- [A](http://example.com) — A (2024-01-01) [pdf](http://example.com/a.pdf)"

    new_text, changed = update_readme(str(readme), "## Section", bullets)
    assert changed is True
    assert "<!-- research-bot:start -->" in new_text
    assert bullets in new_text


def test_update_readme_replaces_between_markers(tmp_path: Path):
    readme = tmp_path / "README.md"
    original = textwrap.dedent(
        """
        # Title

        <!-- research-bot:start -->
        old text
        <!-- research-bot:end -->
        """
    )
    readme.write_text(original, encoding="utf-8")
    bullets = "- [B](http://example.com) — B (2024-01-02) [pdf](http://example.com/b.pdf)"

    new_text, changed = update_readme(str(readme), "## Section", bullets)
    assert changed is True
    assert "old text" not in new_text
    assert bullets in new_text


def test_extract_existing_ids_from_readme():
    text = (
        "See https://arxiv.org/abs/2401.00001 and also https://arxiv.org/pdf/2401.00002.pdf"
    )
    ids = extract_existing_ids_from_readme(text)
    assert ids == {"2401.00001", "2401.00002"}


def test_render_bullets_format():
    papers = [
        {
            "id": "2401.00001",
            "title": "X",
            "published": "2024-01-01",
            "authors": ["A", "B", "C", "D"],
            "abs_url": "https://arxiv.org/abs/2401.00001",
            "pdf_url": "https://arxiv.org/pdf/2401.00001.pdf",
        }
    ]
    s = render_bullets(papers)
    assert "X" in s and "(2024-01-01)" in s and "et al." in s
