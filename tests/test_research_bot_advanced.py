"""Advanced test cases for research_bot with edge cases and error handling."""
import os
import sys
import json
import textwrap
from pathlib import Path
from unittest.mock import patch, MagicMock
import urllib.error

import pytest
import xml.etree.ElementTree as ET

# Make the repo's scripts/ importable
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.research_bot import (  # type: ignore
    main,
    parse_arxiv_feed,
    fetch_arxiv,
    load_config,
    load_seen,
    save_seen,
    iso_date,
)


def test_iso_date_handles_invalid_input():
    """Test that iso_date handles invalid date strings gracefully."""
    assert iso_date("") is None
    assert iso_date("invalid-date") is None
    assert iso_date("2024-13-45") is None  # Invalid month/day
    assert iso_date(None) is None  # type: ignore


def test_parse_arxiv_feed_handles_malformed_xml():
    """Test that parse_arxiv_feed handles malformed XML gracefully."""
    malformed_xml = b"<feed>unclosed tag"
    papers = parse_arxiv_feed(malformed_xml)
    assert papers == []
    
    invalid_xml = b"not xml at all"
    papers = parse_arxiv_feed(invalid_xml)
    assert papers == []


def test_parse_arxiv_feed_handles_empty_fields():
    """Test that parse_arxiv_feed handles missing/empty fields."""
    xml = textwrap.dedent(
        """
        <feed xmlns="http://www.w3.org/2005/Atom">
          <entry>
            <id></id>
            <title></title>
            <published></published>
          </entry>
        </feed>
        """
    ).encode()
    
    papers = parse_arxiv_feed(xml)
    assert len(papers) == 0  # Should skip entries without valid arxiv_id


@patch('urllib.request.urlopen')
def test_fetch_arxiv_propagates_network_errors(mock_urlopen):
    """fetch_arxiv must raise on errors so callers can tell them from empty results."""
    errors = [
        urllib.error.URLError("Connection refused"),
        TimeoutError("Request timeout"),
        urllib.error.HTTPError(
            url="http://example.com", code=503, msg="Service Unavailable", hdrs={}, fp=None
        ),
    ]
    for err in errors:
        mock_urlopen.side_effect = err
        with pytest.raises(type(err)):
            fetch_arxiv("test query", 10)


@patch('urllib.request.urlopen')
def test_fetch_arxiv_success(mock_urlopen):
    """Test successful arXiv API fetch."""
    valid_xml = textwrap.dedent(
        """
        <feed xmlns="http://www.w3.org/2005/Atom">
          <entry>
            <id>http://arxiv.org/abs/2401.00001v1</id>
            <published>2024-01-01T12:00:00Z</published>
            <title>Test Paper</title>
            <author><name>Test Author</name></author>
          </entry>
        </feed>
        """
    ).encode()
    
    mock_response = MagicMock()
    mock_response.read.return_value = valid_xml
    mock_response.__enter__ = MagicMock(return_value=mock_response)
    mock_response.__exit__ = MagicMock(return_value=None)
    mock_urlopen.return_value = mock_response
    
    papers = fetch_arxiv("test query", 10)
    assert len(papers) == 1
    assert papers[0]["id"] == "2401.00001"
    assert papers[0]["title"] == "Test Paper"


def test_load_config_with_missing_yaml(tmp_path: Path):
    """Test load_config when PyYAML is not available."""
    config_path = tmp_path / "config.yaml"
    config_path.write_text("queries: ['test']")
    
    with patch.dict(sys.modules, {'yaml': None}):
        config = load_config(str(config_path))
        assert config["queries"] == ["\"isaac gym\"", "omniisaac", "\"isaac lab\"", "\"omni isaac\""]


def test_load_config_with_invalid_yaml(tmp_path: Path):
    """Test load_config with invalid YAML content."""
    config_path = tmp_path / "config.yaml"
    config_path.write_text("invalid: yaml: content: [")
    
    config = load_config(str(config_path))
    # Should return defaults on parse error
    assert config["days_back"] == 14


def test_load_seen_with_corrupted_json(tmp_path: Path):
    """Test load_seen with corrupted JSON file."""
    state_path = tmp_path / "state.json"
    state_path.write_text("{invalid json}")
    
    seen = load_seen(str(state_path))
    assert seen == set()


def test_load_seen_with_missing_file():
    """Test load_seen when file doesn't exist."""
    seen = load_seen("/nonexistent/path/state.json")
    assert seen == set()


def test_save_seen_handles_write_errors(tmp_path: Path):
    """Test save_seen handles write errors gracefully."""
    # Try to write to a read-only directory
    ro_path = tmp_path / "readonly"
    ro_path.mkdir()
    state_path = ro_path / "subdir" / "state.json"
    
    # Make directory read-only
    os.chmod(ro_path, 0o444)
    
    try:
        save_seen(str(state_path), {"2401.00001", "2401.00002"})
        # Should not raise exception
    finally:
        # Restore permissions for cleanup
        os.chmod(ro_path, 0o755)


def test_parse_arxiv_feed_with_versioned_ids():
    """Test handling of versioned arXiv IDs (e.g., v1, v2)."""
    xml = textwrap.dedent(
        """
        <feed xmlns="http://www.w3.org/2005/Atom">
          <entry>
            <id>http://arxiv.org/abs/2401.00001v3</id>
            <published>2024-01-01T12:00:00Z</published>
            <title>Versioned Paper</title>
            <author><name>Author</name></author>
          </entry>
        </feed>
        """
    ).encode()
    
    papers = parse_arxiv_feed(xml)
    assert len(papers) == 1
    assert papers[0]["id"] == "2401.00001"  # Should strip version


def test_parse_arxiv_feed_with_many_authors():
    """Test handling of papers with many authors."""
    xml = textwrap.dedent(
        """
        <feed xmlns="http://www.w3.org/2005/Atom">
          <entry>
            <id>http://arxiv.org/abs/2401.00001</id>
            <published>2024-01-01T12:00:00Z</published>
            <title>Multi-Author Paper</title>
            <author><name>Author 1</name></author>
            <author><name>Author 2</name></author>
            <author><name>Author 3</name></author>
            <author><name>Author 4</name></author>
            <author><name>Author 5</name></author>
          </entry>
        </feed>
        """
    ).encode()
    
    papers = parse_arxiv_feed(xml)
    assert len(papers) == 1
    assert len(papers[0]["authors"]) == 5


def _run_main(monkeypatch, tmp_path, fetch, queries=("q1", "q2")):
    readme = tmp_path / "README.md"
    readme.write_text("# Title\n", encoding="utf-8")
    monkeypatch.setattr("scripts.research_bot.fetch_arxiv", fetch)
    monkeypatch.setattr(
        "scripts.research_bot.load_config",
        lambda path: {"queries": list(queries), "max_results": 5, "days_back": 14,
                      "output_count": 10, "readme_path": str(readme)},
    )
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(sys, "argv", [
        "research_bot.py", "--dry-run", "--readme-path", str(readme),
        "--state-path", str(tmp_path / "state.json"),
    ])
    return main()


def _paper():
    import datetime as dt
    return {
        "id": "2401.00001", "title": "T", "published": dt.date.today().isoformat(),
        "authors": ["A"], "abs_url": "https://arxiv.org/abs/2401.00001",
        "pdf_url": "https://arxiv.org/pdf/2401.00001.pdf",
    }


def test_main_exits_nonzero_when_all_fetches_error(monkeypatch, tmp_path, capsys):
    def boom(q, n):
        raise urllib.error.URLError("down")

    assert _run_main(monkeypatch, tmp_path, boom) == 1
    err = capsys.readouterr().err
    assert "2 of 2 queries failed" in err


def test_main_exits_zero_on_empty_successful_fetch(monkeypatch, tmp_path, capsys):
    assert _run_main(monkeypatch, tmp_path, lambda q, n: []) == 0
    captured = capsys.readouterr()
    assert "No papers fetched" in captured.out
    assert captured.err == ""


def test_main_partial_error_still_succeeds_with_warning(monkeypatch, tmp_path, capsys):
    def flaky(q, n):
        if q == "q1":
            raise urllib.error.URLError("down")
        return [_paper()]

    assert _run_main(monkeypatch, tmp_path, flaky) == 0
    captured = capsys.readouterr()
    assert "query 'q1' failed" in captured.err
    assert "would update README with 1 new papers" in captured.out


def test_main_partial_error_with_no_papers_exits_nonzero(monkeypatch, tmp_path):
    def flaky(q, n):
        if q == "q1":
            raise urllib.error.URLError("down")
        return []

    assert _run_main(monkeypatch, tmp_path, flaky) == 1
