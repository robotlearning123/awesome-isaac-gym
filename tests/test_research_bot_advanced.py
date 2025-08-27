"""Advanced test cases for research_bot with edge cases and error handling."""
import os
import sys
import json
import textwrap
from pathlib import Path
from unittest.mock import patch, MagicMock
import urllib.error
import xml.etree.ElementTree as ET

# Make the repo's scripts/ importable
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.research_bot import (  # type: ignore
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
def test_fetch_arxiv_handles_network_errors(mock_urlopen):
    """Test that fetch_arxiv handles network errors gracefully."""
    # Test URLError
    mock_urlopen.side_effect = urllib.error.URLError("Connection refused")
    papers = fetch_arxiv("test query", 10)
    assert papers == []
    
    # Test timeout
    mock_urlopen.side_effect = TimeoutError("Request timeout")
    papers = fetch_arxiv("test query", 10)
    assert papers == []
    
    # Test HTTP error
    mock_urlopen.side_effect = urllib.error.HTTPError(
        url="http://example.com",
        code=503,
        msg="Service Unavailable",
        hdrs={},
        fp=None
    )
    papers = fetch_arxiv("test query", 10)
    assert papers == []


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