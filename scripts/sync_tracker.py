#!/usr/bin/env python3
"""
sync_tracker.py: Pull Status updates from Google Sheets → coaching_state.md

One-directional: Google Sheets is the source of truth for Status.
Matches rows by Company name. Only updates the Status column.
Logs all changes (and no-changes) to stdout.

Usage:
    python3 scripts/sync_tracker.py              # pull + apply changes
    python3 scripts/sync_tracker.py --dry-run    # preview without writing

Expected Google Sheet columns:
    Company | Title | Cover Letter Submitted | Application Method | Status |
    Application Date | Reach out to Company Contact | Who | Notes
"""

import re
import csv
import sys
import argparse
import urllib.request
from datetime import date
from io import StringIO
from typing import Optional

SHEET_ID = "158MbpIe6TYyQeU_7cFhklXXWxkLrendo"
CSV_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv"

COACHING_STATE = "/Users/irene/Downloads/interview-coach-skill-main/coaching_state.md"

# ── Status mapping ────────────────────────────────────────────────────────────
# Map your Google Sheet status values → coaching_state.md values.
# Keys are lowercase (the script lowercases before lookup).
# If a value isn't in this map, it's passed through as-is.
# Add or edit entries to match whatever you type in the sheet.
STATUS_MAP = {
    'applied':                'Applied',
    'application submitted':  'Applied',
    'submitted':              'Applied',
    'phone screen scheduled': 'Screen Scheduled',
    'screen scheduled':       'Screen Scheduled',
    'recruiter screen':       'Screen Scheduled',
    'phone screen':           'Phone Screen Done',
    'phone screen done':      'Phone Screen Done',
    'phone screen complete':  'Phone Screen Done',
    'interview scheduled':    'Loop Scheduled',
    'loop scheduled':         'Loop Scheduled',
    'interviewing':           'Loop Scheduled',
    'offer':                  'Offer',
    'offer received':         'Offer',
    'rejected':               'Rejected',
    'rejection':              'Rejected',
    'no':                     'Rejected',
    'withdrawn':              'Withdrawn',
    'withdrew':               'Withdrawn',
    'ghosted':                'Likely Closed',
    'likely closed':          'Likely Closed',
    'no response':            'Likely Closed',
    'denied':                 'Rejected',
    '1st round interview':    'Loop Scheduled',
    'first round interview':  'Loop Scheduled',
    'interviewing':           'Loop Scheduled',
}


# Words to strip before fuzzy matching company names
_NOISE_WORDS = {
    'inc', 'inc.', 'llc', 'llc.', 'ltd', 'ltd.', 'corp', 'corp.',
    'co', 'co.', 'the', 'and', '&', 'group', 'global', 'solutions',
    'services', 'technologies', 'technology', 'tech',
}

# Manual aliases: sheet name (lowercase) → tracker name (lowercase)
# Add entries here if auto-matching still misses after fuzzy logic.
# Example: 'zen educate limited': 'zen educate'
COMPANY_ALIASES = {
    # tracker name (lowercase) → sheet key (lowercase, as it appears in the sheet)
    'transcarent':   'transacrent',
    'human ventures': 'human ventrues',
    # Add more as needed: 'tracker name (lowercase)': 'sheet name (lowercase)'
}


def normalize(s: str) -> str:
    """Lowercase, strip whitespace for matching."""
    return s.strip().lower()


def significant_words(name: str) -> frozenset[str]:
    """Extract meaningful words from a company name, dropping noise words."""
    words = re.sub(r'[^\w\s]', '', name.lower()).split()
    return frozenset(w for w in words if w not in _NOISE_WORDS and len(w) > 1)


def fuzzy_match(sheet_names, tracker_company):
    # type: (dict, str) -> Optional[str]
    """
    Try to match a tracker company name against sheet names.
    Strategy (in order):
      1. Exact match (after normalize)
      2. Manual alias lookup
      3. Significant-word overlap — all words of the shorter name appear in the longer
    Returns matched sheet key or None.
    """
    norm = normalize(tracker_company)

    # 1. Exact
    if norm in sheet_names:
        return norm

    # 2. Manual alias
    alias = COMPANY_ALIASES.get(norm)
    if alias and alias in sheet_names:
        return alias

    # 3. Significant-word overlap
    tracker_words = significant_words(tracker_company)
    if not tracker_words:
        return None

    candidates = []
    for sheet_key in sheet_names:
        sheet_words = significant_words(sheet_key)
        if not sheet_words:
            continue
        # All words from the smaller set must appear in the larger set
        smaller, larger = (tracker_words, sheet_words) if len(tracker_words) <= len(sheet_words) \
                          else (sheet_words, tracker_words)
        if smaller.issubset(larger):
            candidates.append(sheet_key)

    if len(candidates) == 1:
        return candidates[0]
    if len(candidates) > 1:
        # Multiple fuzzy matches — return the one with highest word overlap
        return max(candidates, key=lambda k: len(significant_words(k) & tracker_words))

    return None


def map_status(raw: str) -> str:
    """Map sheet status to tracker status. Passthrough if not in map."""
    mapped = STATUS_MAP.get(normalize(raw))
    return mapped if mapped else raw.strip()


def fetch_sheet_statuses():
    """
    Download CSV from Google Sheets and return {normalized_company: mapped_status}.
    Skips blank rows and header row.
    """
    try:
        with urllib.request.urlopen(CSV_URL, timeout=10) as response:
            raw = response.read().decode('utf-8')
    except Exception as e:
        print(f"ERROR: Could not fetch Google Sheet — {e}")
        print(f"  Check that the sheet is shared as 'Anyone with the link can view'.")
        print(f"  URL attempted: {CSV_URL}")
        sys.exit(1)

    reader = csv.DictReader(StringIO(raw))

    # Validate expected columns exist
    fieldnames = set(reader.fieldnames or [])
    required = {'Status'}
    # Accept either 'Company' or 'CompanyTitle'
    has_company_col = 'Company' in fieldnames or 'CompanyTitle' in fieldnames
    if not required.issubset(fieldnames) or not has_company_col:
        found = reader.fieldnames or []
        print(f"ERROR: Sheet must have a 'Company' (or 'CompanyTitle') column and a 'Status' column.")
        print(f"  Found columns: {found}")
        sys.exit(1)

    company_col = 'Company' if 'Company' in fieldnames else 'CompanyTitle'

    result = {}
    unmapped_warn = set()

    for row in reader:
        company = row.get(company_col, '').strip()
        status_raw = row.get('Status', '').strip()

        if not company or not status_raw:
            continue

        mapped = map_status(status_raw)
        if mapped == status_raw and normalize(status_raw) not in STATUS_MAP:
            unmapped_warn.add(status_raw)

        result[normalize(company)] = mapped

    if unmapped_warn:
        print(f"⚠️  Unmapped status values (passed through as-is): {', '.join(sorted(unmapped_warn))}")
        print(f"   Add them to STATUS_MAP in sync_tracker.py if you want canonical names.\n")

    return result


def parse_tracker_rows(content: str):
    """
    Extract Application Tracker rows from coaching_state.md.
    Returns list of (line_index, company, current_status).
    """
    lines = content.split('\n')
    in_tracker = False
    rows = []

    for i, line in enumerate(lines):
        if line.startswith('## Application Tracker'):
            in_tracker = True
            continue
        if in_tracker and re.match(r'^## ', line):
            break

        if not in_tracker or not line.startswith('|'):
            continue

        parts = [p.strip() for p in line.split('|')]
        # parts[0] is '' (before first |), data starts at parts[1]
        # Layout: ID(1) Date(2) Company(3) Role(4) ResumeVer(5) Method(6) CL(7) Status(8) ...
        if len(parts) < 10:
            continue

        company = parts[3]
        status = parts[8]

        # Skip header and separator rows
        if not company or company in ('Company',) or set(company) <= set('- '):
            continue
        if '---' in company or set(status) <= set('- '):
            continue

        rows.append((i, company, status))

    return rows, lines


def apply_updates(lines: list, line_idx: int, new_status: str) -> None:
    """Update the Status cell (parts[8]) of a tracker row in-place."""
    parts = lines[line_idx].split('|')
    if len(parts) < 10:
        return
    parts[8] = f' {new_status} '
    lines[line_idx] = '|'.join(parts)


def main():
    parser = argparse.ArgumentParser(description='Sync Google Sheets status → coaching_state.md')
    parser.add_argument('--dry-run', action='store_true', help='Preview changes without writing')
    args = parser.parse_args()

    today = date.today()

    print(f"\n{'='*55}")
    print(f"  Tracker Sync — {today}")
    if args.dry_run:
        print(f"  DRY RUN — no changes will be written")
    print(f"{'='*55}\n")

    # 1. Fetch sheet data
    print("Fetching Google Sheet...", end=' ', flush=True)
    sheet_statuses = fetch_sheet_statuses()
    print(f"✓  {len(sheet_statuses)} companies found\n")

    # 2. Read coaching_state.md
    try:
        with open(COACHING_STATE, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"ERROR: coaching_state.md not found at {COACHING_STATE}")
        sys.exit(1)

    # 3. Parse tracker rows
    tracker_rows, lines = parse_tracker_rows(content)

    if not tracker_rows:
        print("No Application Tracker rows found in coaching_state.md")
        sys.exit(0)

    # 4. Compare and collect changes
    changes = []      # (line_idx, company, old_status, new_status)
    no_change = []    # (company, status)
    not_in_sheet = [] # companies in tracker but not in sheet

    for line_idx, company, current_status in tracker_rows:
        matched_key = fuzzy_match(sheet_statuses, company)
        if matched_key is None:
            not_in_sheet.append(company)
            continue

        sheet_status = sheet_statuses[matched_key]
        # Show fuzzy match note if names differ
        match_note = f" [matched: '{matched_key}']" if matched_key != normalize(company) else ""

        if sheet_status != current_status:
            changes.append((line_idx, company, current_status, sheet_status, match_note))
        else:
            no_change.append((company, current_status, match_note))

    # 5. Report
    if changes:
        verb = "Would update" if args.dry_run else "Updated"
        print(f"✅ {verb} ({len(changes)}):")
        for _, company, old, new, note in changes:
            print(f"   {company}: {old} → {new}{note}")
        print()

    if no_change:
        print(f"✓  No change ({len(no_change)}):")
        for company, status, note in no_change:
            print(f"   {company} ({status}){note}")
        print()

    if not_in_sheet:
        print(f"⚠️  In tracker but not found in sheet ({len(not_in_sheet)}):")
        for company in not_in_sheet:
            print(f"   {company}")
        print(f"   → Company names may differ between sheet and tracker. Check spelling.\n")

    # 6. Apply changes
    if changes and not args.dry_run:
        for line_idx, _, _, new_status, _ in changes:
            apply_updates(lines, line_idx, new_status)

        updated_content = '\n'.join(lines)
        with open(COACHING_STATE, 'w') as f:
            f.write(updated_content)

        print(f"coaching_state.md updated. {len(changes)} status change(s) applied.")
    elif not changes:
        print("Nothing to update — tracker is in sync with sheet.")
    elif args.dry_run:
        print(f"Dry run complete. Run without --dry-run to apply {len(changes)} change(s).")

    print()


if __name__ == '__main__':
    main()
