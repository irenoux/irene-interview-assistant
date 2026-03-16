#!/usr/bin/env python3
"""
ATS keyword scorer: check how well a resume file matches a keyword list.

Claude extracts the keywords once per JD (saves the turn); this script
does the counting without needing Claude to re-read the resume every time.

Usage:
    python ats_score.py --resume PATH_TO_RESUME --keywords "keyword1, keyword2, ..."
    python ats_score.py --resume PATH_TO_RESUME --keywords-file keywords.txt
    python ats_score.py --resume PATH_TO_RESUME --jd-id A101

The --jd-id flag looks up saved keywords from coaching_state.md
(under the JD Analysis section for that application ID).

Examples:
    python ats_score.py --resume ~/Documents/resume_general_v4.3.txt \
        --keywords "product strategy, stakeholder alignment, OKRs, A/B testing, SQL"

    python ats_score.py --resume ~/Documents/resume_general_v4.3.txt \
        --jd-id A101
"""

import re
import sys
import argparse
from pathlib import Path

COACHING_STATE = "./coaching_state.md"


def load_resume(path: str) -> str:
    p = Path(path).expanduser()
    if not p.exists():
        print(f"ERROR: Resume file not found: {p}")
        sys.exit(1)
    return p.read_text(encoding='utf-8', errors='ignore').lower()


def parse_keywords_string(s: str) -> list[str]:
    """Parse comma-separated keyword string into cleaned list."""
    return [kw.strip().lower() for kw in s.split(',') if kw.strip()]


def load_keywords_file(path: str) -> list[str]:
    p = Path(path).expanduser()
    if not p.exists():
        print(f"ERROR: Keywords file not found: {p}")
        sys.exit(1)
    lines = p.read_text().splitlines()
    keywords = []
    for line in lines:
        line = line.strip().lstrip('-•*').strip()
        if line:
            # Handle comma-separated lines too
            keywords.extend(parse_keywords_string(line))
    return keywords


def extract_keywords_from_state(jd_id: str) -> list[str]:
    """
    Look up keywords saved in coaching_state.md for a given application ID.
    Looks in JD Analysis sections for top competencies / keyword lists.
    Also checks the Application Tracker notes for the ID.
    """
    try:
        content = Path(COACHING_STATE).read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"ERROR: coaching_state.md not found at {COACHING_STATE}")
        sys.exit(1)

    keywords = []

    # Try to find JD Analysis section — match by company name from tracker first
    tracker_match = re.search(
        r'## Application Tracker\n.*?\n\|[-| ]+\|\n(.*?)(?=\n## |\Z)',
        content, re.DOTALL
    )
    company_name = None
    role_name = None
    if tracker_match:
        for line in tracker_match.group(1).strip().split('\n'):
            if not line.startswith('|'):
                continue
            cols = [c.strip() for c in line.split('|')[1:-1]]
            if len(cols) >= 4 and cols[0] == jd_id:
                company_name = cols[2]
                role_name = cols[3]
                break

    if company_name:
        # Find JD Analysis section for this company
        jd_section = re.search(
            rf'## JD Analysis: {re.escape(company_name)}.*?\n(.*?)(?=\n## |\Z)',
            content, re.DOTALL | re.IGNORECASE
        )
        if jd_section:
            section_text = jd_section.group(1)
            # Extract top competencies line
            comp_match = re.search(r'- Top competencies:\s*(.+)', section_text)
            if comp_match:
                raw = comp_match.group(1)
                keywords.extend(parse_keywords_string(raw))
            # Also grab any keyword lines
            kw_matches = re.findall(r'(?:keyword|skill|competency)[s]?[:\s]+([^\n]+)', section_text, re.IGNORECASE)
            for m in kw_matches:
                keywords.extend(parse_keywords_string(m))

    if not keywords:
        print(f"No saved keywords found for {jd_id}"
              + (f" ({company_name})" if company_name else "")
              + ".\nProvide keywords manually with --keywords or --keywords-file.")
        sys.exit(1)

    return keywords


def score_resume(resume_text: str, keywords: list[str]) -> dict:
    found = []
    missing = []

    for kw in keywords:
        # Match whole phrase; handle multi-word keywords
        pattern = re.escape(kw.lower())
        if re.search(r'\b' + pattern + r'\b', resume_text):
            found.append(kw)
        else:
            # Softer match: all individual words present (for phrases)
            words = kw.lower().split()
            if len(words) > 1 and all(re.search(r'\b' + re.escape(w) + r'\b', resume_text) for w in words):
                found.append(kw + ' [partial]')
            else:
                missing.append(kw)

    total = len(keywords)
    matched = len(found)
    pct = round(matched / total * 100) if total > 0 else 0

    return {
        'total': total,
        'matched': matched,
        'pct': pct,
        'found': found,
        'missing': missing,
    }


def main():
    parser = argparse.ArgumentParser(description='ATS keyword scorer')
    parser.add_argument('--resume', required=True, help='Path to resume text file')
    parser.add_argument('--keywords', help='Comma-separated keyword list')
    parser.add_argument('--keywords-file', help='Path to file with one keyword per line')
    parser.add_argument('--jd-id', help='Application ID (e.g. A101) — looks up keywords from coaching_state.md')
    parser.add_argument('--threshold', type=int, default=75,
                        help='Target match %% to highlight (default: 75)')
    args = parser.parse_args()

    # Load keywords from whichever source was provided
    if args.keywords:
        keywords = parse_keywords_string(args.keywords)
    elif args.keywords_file:
        keywords = load_keywords_file(args.keywords_file)
    elif args.jd_id:
        keywords = extract_keywords_from_state(args.jd_id)
    else:
        print("ERROR: Provide one of --keywords, --keywords-file, or --jd-id")
        parser.print_help()
        sys.exit(1)

    if not keywords:
        print("ERROR: No keywords to score against.")
        sys.exit(1)

    # Deduplicate while preserving order
    seen = set()
    unique_keywords = []
    for kw in keywords:
        if kw.lower() not in seen:
            seen.add(kw.lower())
            unique_keywords.append(kw)
    keywords = unique_keywords

    resume_text = load_resume(args.resume)
    result = score_resume(resume_text, keywords)

    threshold = args.threshold
    status_icon = '✅' if result['pct'] >= threshold else ('⚠️' if result['pct'] >= threshold - 15 else '🔴')

    print(f"\n{'='*55}")
    print(f"  ATS Keyword Score")
    print(f"{'='*55}\n")
    print(f"  Resume:    {args.resume}")
    if args.jd_id:
        print(f"  JD ID:     {args.jd_id}")
    print(f"\n  Score:     {result['matched']}/{result['total']} = {result['pct']}%  {status_icon}")
    print(f"  Target:    {threshold}%+\n")

    if result['found']:
        print(f"✅ FOUND ({len(result['found'])}):")
        for kw in sorted(result['found']):
            print(f"   • {kw}")

    if result['missing']:
        print(f"\n❌ MISSING ({len(result['missing'])}):")
        for kw in sorted(result['missing']):
            print(f"   • {kw}")

    print()

    # Quick action line
    if result['missing']:
        top_missing = result['missing'][:3]
        print(f"  → Priority adds: {', '.join(top_missing)}\n")


if __name__ == '__main__':
    main()
