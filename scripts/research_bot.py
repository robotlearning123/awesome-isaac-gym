#!/usr/bin/env python3
"""
Research Bot for Isaac Gym - Fetches latest papers from arXiv
"""
import datetime as dt
import argparse
import json
import os
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET


ARXIV_API = "http://export.arxiv.org/api/query"
MARKER_START = "<!-- research-bot:start -->"
MARKER_END = "<!-- research-bot:end -->"


def load_config(path):
    """Load configuration from YAML file with defaults."""
    cfg = {
        "queries": ['"isaac gym"', 'omniisaac', '"isaac lab"', '"omni isaac"'],
        "days_back": 14,
        "max_results": 25,
        "output_count": 10,
        "readme_path": "README.md",
        "section_title": "## 🧠 Latest Research (auto-updated)",
    }
    
    if os.path.exists(path):
        try:
            import yaml
            with open(path, "r", encoding="utf-8") as f:
                user_cfg = yaml.safe_load(f) or {}
            cfg.update({k: v for k, v in user_cfg.items() if v is not None})
        except Exception:
            pass  # Use defaults if config fails to load
    
    return cfg


def iso_date(s):
    """Parse ISO date string from arXiv."""
    try:
        return dt.datetime.fromisoformat(s.replace("Z", "+00:00")).date()
    except Exception:
        return None


def parse_arxiv_feed(xml_bytes):
    """Parse arXiv Atom feed XML and extract paper information."""
    try:
        root = ET.fromstring(xml_bytes)
    except Exception:
        return []
    
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    papers = []
    
    for entry in root.findall("atom:entry", ns):
        eid = entry.findtext("atom:id", default="", namespaces=ns)
        title = (entry.findtext("atom:title", default="", namespaces=ns) or "").strip()
        published = entry.findtext("atom:published", default="", namespaces=ns) or ""
        published_date = iso_date(published) if published else None
        
        authors = [
            (a.findtext("atom:name", default="", namespaces=ns) or "").strip()
            for a in entry.findall("atom:author", ns)
        ]
        
        # Extract arXiv ID
        arxiv_id = None
        if "arxiv.org" in eid:
            m = re.search(r"arxiv\.org/abs/([0-9.]+)(v\d+)?", eid)
            if m:
                arxiv_id = m.group(1)
        
        if not arxiv_id:
            for link in entry.findall("atom:link", ns):
                href = link.attrib.get("href", "")
                m = re.search(r"arxiv\.org/abs/([0-9.]+)(v\d+)?", href)
                if m:
                    arxiv_id = m.group(1)
                    break
        
        if arxiv_id:
            papers.append({
                "id": arxiv_id,
                "title": title,
                "published": published_date.isoformat() if published_date else "",
                "authors": authors,
                "abs_url": f"https://arxiv.org/abs/{arxiv_id}",
                "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}.pdf",
            })
    
    return papers


def fetch_arxiv(query, max_results):
    """Fetch papers from arXiv API for the given query."""
    params = {
        "search_query": f"all:{query}",
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": str(max_results),
    }
    url = f"{ARXIV_API}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": "research-bot/1.0"})
    
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return parse_arxiv_feed(resp.read())
    except Exception:
        return []


def load_seen(path):
    """Load previously seen paper IDs."""
    if not os.path.exists(path):
        return set()
    
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return set(data.get("arxiv_ids", []))
    except Exception:
        return set()


def save_seen(path, ids):
    """Save seen paper IDs to state file."""
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump({"arxiv_ids": sorted(ids)}, f, indent=2)
    except Exception:
        pass


def extract_existing_ids_from_readme(readme_text):
    """Extract arXiv IDs already present in README."""
    pattern = re.compile(r"arxiv\.org/(?:abs|pdf)/([0-9]+\.[0-9]+)(?:v\d+)?(?:\.pdf)?")
    return set(m.group(1) for m in pattern.finditer(readme_text))


def render_bullets(papers):
    """Render papers as markdown bullet points."""
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


def update_readme(readme_path, section_title, bullets_block):
    """Update README with new papers between markers."""
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
    else:
        # Append new section at the end
        addition = f"\n\n{section_title}\n\n{MARKER_START}\n{bullets_block}\n{MARKER_END}\n"
        new_text = text.rstrip() + addition
        changed = True
    
    return new_text, changed


def main():
    parser = argparse.ArgumentParser(description="Update README with latest arXiv research.")
    parser.add_argument("--dry-run", action="store_true", help="Do not write files; just print.")
    parser.add_argument("--readme-path", default=None, help="Override README path.")
    parser.add_argument("--state-path", default=None, help="Override state JSON path.")
    parser.add_argument("--days-back", type=int, default=None, help="Override days_back window.")
    parser.add_argument("--output-count", type=int, default=None, help="Override output_count.")
    args = parser.parse_args()
    
    # Change to repository root
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    os.chdir(repo_root)
    
    # Load configuration
    cfg = load_config(".research-bot.yaml")
    readme_path = args.readme_path or cfg.get("readme_path", "README.md")
    queries = cfg.get("queries", [])
    max_results = int(cfg.get("max_results", 25))
    days_back = int(args.days_back or cfg.get("days_back", 14))
    output_count = int(args.output_count or cfg.get("output_count", 10))
    section_title = cfg.get("section_title", "## 🧠 Latest Research (auto-updated)")
    
    # Collect papers for all queries
    collected = {}
    for q in queries:
        try:
            for p in fetch_arxiv(q, max_results):
                collected[p["id"]] = p
        except Exception as e:
            print(f"Warning: query '{q}' failed: {e}", file=sys.stderr)
    
    if not collected:
        print("No papers fetched; exiting.")
        return 0
    
    # Filter by date
    today = dt.date.today()
    cutoff = today - dt.timedelta(days=days_back)
    papers = [p for p in collected.values() if p.get("published")]
    papers = [p for p in papers if dt.date.fromisoformat(p["published"]) >= cutoff]
    papers.sort(key=lambda p: p.get("published", ""), reverse=True)
    
    # Load seen IDs and existing README IDs to avoid duplicates
    state_path = args.state_path or os.path.join(".bot", "state.json")
    seen = load_seen(state_path)
    with open(readme_path, "r", encoding="utf-8") as f:
        readme_text = f.read()
    existing = extract_existing_ids_from_readme(readme_text)
    known = seen | existing
    
    # Find new papers
    new_papers = [p for p in papers if p["id"] not in known]
    new_papers = new_papers[:output_count]
    
    if not new_papers:
        print("No new papers detected in the time window.")
        return 0
    
    # Render and update
    bullets = render_bullets(new_papers)
    new_text, changed = update_readme(readme_path, section_title, bullets)
    
    if not changed:
        print("README unchanged.")
        return 0
    
    if args.dry_run:
        print(f"DRY RUN: would update README with {len(new_papers)} new papers.")
        print(bullets)
        return 0
    
    # Save updates
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