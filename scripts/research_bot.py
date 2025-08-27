#!/usr/bin/env python3
import datetime as dt
import argparse
import json
import logging
import os
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from typing import Dict, List, Set, Tuple, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


ARXIV_API = "http://export.arxiv.org/api/query"
MARKER_START = "<!-- research-bot:start -->"
MARKER_END = "<!-- research-bot:end -->"


def load_config(path: str) -> Dict[str, any]:
    cfg = {
        "queries": [
            "\"isaac gym\"",
            "omniisaac",
            "\"isaac lab\"",
            "\"omni isaac\"",
        ],
        "days_back": 14,
        "max_results": 25,
        "output_count": 10,
        "readme_path": "README.md",
        "section_title": "## 🧠 Latest Research (auto-updated)",
    }
    if os.path.exists(path):
        try:
            import yaml  # type: ignore
        except ImportError:
            logger.warning("PyYAML not available, using default configuration")
            return cfg
        else:
            try:
                with open(path, "r", encoding="utf-8") as f:
                    user_cfg = yaml.safe_load(f) or {}
                cfg.update({k: v for k, v in user_cfg.items() if v is not None})
            except yaml.YAMLError as e:
                logger.error(f"Failed to parse YAML config: {e}")
                return cfg
            except IOError as e:
                logger.error(f"Failed to read config file: {e}")
                return cfg
    return cfg


def iso_date(s: str) -> Optional[dt.date]:
    """Parse ISO date string from arXiv (e.g., 2024-08-21T12:34:56Z)."""
    try:
        return dt.datetime.fromisoformat(s.replace("Z", "+00:00")).date()
    except (ValueError, AttributeError) as e:
        logger.warning(f"Failed to parse date '{s}': {e}")
        return None


def parse_arxiv_feed(xml_bytes: bytes) -> List[Dict[str, any]]:
    """Parse arXiv Atom feed XML and extract paper information."""
    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError as e:
        logger.error(f"Failed to parse XML: {e}")
        return []
    
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    papers: List[Dict[str, any]] = []
    for entry in root.findall("atom:entry", ns):
        eid = entry.findtext("atom:id", default="", namespaces=ns)
        title = (entry.findtext("atom:title", default="", namespaces=ns) or "").strip()
        published = entry.findtext("atom:published", default="", namespaces=ns) or ""
        published_date = iso_date(published) if published else None
        authors = [
            (a.findtext("atom:name", default="", namespaces=ns) or "").strip()
            for a in entry.findall("atom:author", ns)
        ]
        abs_url = eid or ""
        arxiv_id = None
        if "arxiv.org" in abs_url:
            m = re.search(r"arxiv\.org/abs/([0-9.]+)(v\d+)?", abs_url)
            if m:
                arxiv_id = m.group(1)
        if not arxiv_id:
            for link in entry.findall("atom:link", ns):
                href = link.attrib.get("href", "")
                m = re.search(r"arxiv\.org/abs/([0-9.]+)(v\d+)?", href)
                if m:
                    arxiv_id = m.group(1)
                    abs_url = href
                    break
        if not arxiv_id:
            continue
        abs_url = f"https://arxiv.org/abs/{arxiv_id}"
        pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
        papers.append(
            {
                "id": arxiv_id,
                "title": title,
                "published": published_date.isoformat() if published_date else "",
                "authors": authors,
                "abs_url": abs_url,
                "pdf_url": pdf_url,
            }
        )
    return papers


def fetch_arxiv(query: str, max_results: int) -> List[Dict[str, any]]:
    params = {
        "search_query": f"all:{query}",
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": str(max_results),
    }
    """Fetch papers from arXiv API for the given query."""
    url = f"{ARXIV_API}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": "research-bot/1.0"})
    
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
        return parse_arxiv_feed(data)
    except urllib.error.URLError as e:
        logger.error(f"Network error fetching arXiv data for query '{query}': {e}")
        return []
    except TimeoutError as e:
        logger.error(f"Timeout fetching arXiv data for query '{query}': {e}")
        return []


def load_seen(path: str) -> Set[str]:
    if not os.path.exists(path):
        return set()
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        logger.warning(f"Failed to load state file: {e}")
        return set()
    return set(data.get("arxiv_ids", []))


def save_seen(path: str, ids: Set[str]) -> None:
    """Save seen paper IDs to state file."""
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump({"arxiv_ids": sorted(ids)}, f, indent=2)
    except IOError as e:
        logger.error(f"Failed to save state file: {e}")


def extract_existing_ids_from_readme(readme_text: str) -> Set[str]:
    # Capture IDs like 2401.00001 possibly followed by version or .pdf, but only keep the ID
    pattern = re.compile(r"arxiv\.org/(?:abs|pdf)/([0-9]+\.[0-9]+)(?:v\d+)?(?:\.pdf)?")
    return set(m.group(1) for m in pattern.finditer(readme_text))


def render_bullets(papers: List[Dict[str, any]]) -> str:
    lines = []
    for p in papers:
        authors = ", ".join(p.get("authors", [])[:3])
        if len(p.get("authors", [])) > 3:
            authors += ", et al."
        date = p.get("published", "")
        lines.append(
            f"- [{p['title']}]({p['abs_url']}) — {authors} ({date}) [pdf]({p['pdf_url']})"
        )
    return "\n".join(lines)


def update_readme(readme_path: str, section_title: str, bullets_block: str) -> Tuple[str, bool]:
    changed = False
    if not os.path.exists(readme_path):
        return "", False
    with open(readme_path, "r", encoding="utf-8") as f:
        text = f.read()

    if MARKER_START in text and MARKER_END in text:
        pattern = re.compile(
            re.escape(MARKER_START) + r"[\s\S]*?" + re.escape(MARKER_END), re.MULTILINE
        )
        new_block = f"{MARKER_START}\n{bullets_block}\n{MARKER_END}"
        new_text = pattern.sub(new_block, text)
        changed = new_text != text
        text = new_text
    else:
        # Append a new section at the end
        addition = (
            f"\n\n{section_title}\n\n{MARKER_START}\n{bullets_block}\n{MARKER_END}\n"
        )
        text = text.rstrip() + addition
        changed = True

    return text, changed


def main() -> int:
    parser = argparse.ArgumentParser(description="Update README with latest arXiv research.")
    parser.add_argument("--dry-run", action="store_true", help="Do not write files; just print.")
    parser.add_argument("--readme-path", default=None, help="Override README path.")
    parser.add_argument("--state-path", default=None, help="Override state JSON path.")
    parser.add_argument("--days-back", type=int, default=None, help="Override days_back window.")
    parser.add_argument("--output-count", type=int, default=None, help="Override output_count.")
    args = parser.parse_args()

    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    os.chdir(repo_root)

    cfg = load_config(".research-bot.yaml")
    readme_path = args.readme_path or cfg.get("readme_path", "README.md")
    queries = cfg.get("queries", [])
    max_results = int(cfg.get("max_results", 25))
    days_back = int(args.days_back or cfg.get("days_back", 14))
    output_count = int(args.output_count or cfg.get("output_count", 10))
    section_title = cfg.get("section_title", "## 🧠 Latest Research (auto-updated)")

    # Collect papers for all queries
    collected: dict[str, dict] = {}
    for q in queries:
        try:
            papers = fetch_arxiv(q, max_results)
            for p in papers:
                collected[p["id"]] = p
            logger.info(f"Fetched {len(papers)} papers for query '{q}'")
        except Exception as e:
            logger.error(f"Unexpected error for query '{q}': {e}", exc_info=True)

    if not collected:
        print("No papers fetched; exiting.")
        return 0

    today = dt.date.today()
    cutoff = today - dt.timedelta(days=days_back)
    papers = [p for p in collected.values() if p.get("published")]
    papers = [p for p in papers if dt.date.fromisoformat(p["published"]) >= cutoff]
    papers.sort(key=lambda p: p.get("published", ""), reverse=True)

    # Load seen IDs and existing README IDs to avoid dupes
    state_path = args.state_path or os.path.join(".bot", "state.json")
    seen = load_seen(state_path)
    with open(readme_path, "r", encoding="utf-8") as f:
        readme_text = f.read()
    existing = extract_existing_ids_from_readme(readme_text)
    known = seen | existing

    new_papers = [p for p in papers if p["id"] not in known]
    new_papers = new_papers[:output_count]

    if not new_papers:
        print("No new papers detected in the time window.")
        return 0

    bullets = render_bullets(new_papers)
    new_text, changed = update_readme(readme_path, section_title, bullets)
    if not changed:
        print("README unchanged.")
        return 0

    if args.dry_run:
        print(f"DRY RUN: would update README with {len(new_papers)} new papers.")
        print(bullets)
        return 0

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_text)

    # Update seen state
    for p in new_papers:
        seen.add(p["id"])
    save_seen(state_path, seen)

    print(f"Updated README with {len(new_papers)} new papers.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
