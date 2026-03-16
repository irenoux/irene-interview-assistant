#!/usr/bin/env python3
"""
Weekly job search insights: parse Application Tracker in coaching_state.md
and output analytics by method, source, CL style, and timeline.

Run every Monday (or any time with --full for full history).

Usage:
    python weekly_insights.py              # last 7 days
    python weekly_insights.py --weeks 2    # last 2 weeks
    python weekly_insights.py --full       # all time
    python weekly_insights.py --cl-experiment  # CL experiment summary only
"""

import re
import sys
import argparse
from datetime import datetime, date, timedelta
from collections import defaultdict


COACHING_STATE = "./coaching_state.md"

# CL style tags expected in Notes field
CL_STYLE_TAGS = {
    'Style-A': 'Earned Insight',
    'Style-B': 'Mirror',
    'Style-C': 'Problem Statement',
    'Style-D': 'No CL (control)',
}


def parse_date(s):
    s = s.strip().replace('~', '').replace('*', '')
    if not s or s in ('—', 'N/A', 'N/A (pre-tracker)', '-', ''):
        return None
    try:
        return datetime.strptime(s, '%Y-%m-%d').date()
    except ValueError:
        return None


def extract_cl_style(notes: str) -> str:
    """
    Extract CL style tag from Notes field.
    Handles both 'Style-A' and 'CL Style A' formats, plus 'CL N/A'.
    """
    n = notes.lower()
    # Explicit no-CL signals
    if 'cl n/a' in n or 'no cl' in n or 'no cover' in n or 'style d' in n or 'style-d' in n:
        return 'Style-D'
    # Style tags — match 'Style A', 'Style-A', 'CL Style A', etc.
    for tag, label in CL_STYLE_TAGS.items():
        letter = tag[-1]  # 'A', 'B', 'C', 'D'
        patterns = [f'style-{letter.lower()}', f'style {letter.lower()}']
        if any(p in n for p in patterns):
            return tag
    if notes.strip() in ('—', '', '-'):
        return 'unknown'
    return 'unknown'


def extract_job_source(notes: str) -> str:
    """Extract job source from Notes field (e.g. 'src:LinkedIn', 'src:jobs-command')."""
    m = re.search(r'src:([^\s,|]+)', notes, re.IGNORECASE)
    if m:
        return m.group(1)
    # Fallback keywords
    for kw in ('linkedin', 'indeed', 'jobs-command', 'referral', 'direct', 'recruiter'):
        if kw.lower() in notes.lower():
            return kw
    return 'unknown'


def load_tracker_rows():
    """Read and parse all Application Tracker rows from coaching_state.md."""
    try:
        with open(COACHING_STATE, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"ERROR: coaching_state.md not found at {COACHING_STATE}")
        sys.exit(1)

    tracker_match = re.search(
        r'## Application Tracker\n.*?\n\|[-| ]+\|\n(.*?)(?=\n## |\Z)',
        content, re.DOTALL
    )
    if not tracker_match:
        print("Could not find Application Tracker in coaching_state.md")
        sys.exit(1)

    rows = []
    for line in tracker_match.group(1).strip().split('\n'):
        if not line.startswith('|'):
            continue
        cols = [c.strip() for c in line.split('|')[1:-1]]
        if len(cols) < 14:
            continue

        try:
            row = {
                'id':           cols[0],
                'date':         parse_date(cols[1]),
                'company':      cols[2],
                'role':         cols[3],
                'resume':       cols[4],
                'method':       cols[5],
                'cl':           cols[6],
                'status':       cols[7],
                'resp_date':    parse_date(cols[8]),
                'resp_type':    cols[9],
                'fu1_due':      parse_date(cols[10]),
                'fu1_done':     cols[11] not in ('—', '', '-', 'N/A'),
                'fu2_due':      parse_date(cols[12]) if len(cols) > 12 else None,
                'fu2_done':     cols[13] not in ('—', '', '-', 'N/A') if len(cols) > 13 else False,
                'notes':        cols[14] if len(cols) > 14 else '',
            }
            rows.append(row)
        except IndexError:
            continue

    return rows


def pct(numerator, denominator):
    if denominator == 0:
        return '—'
    return f"{round(numerator / denominator * 100)}%"


def print_section(title):
    print(f"\n{'─'*50}")
    print(f"  {title}")
    print(f"{'─'*50}")


def response_received(row):
    return row['status'] not in ('Applied', 'Likely Closed') and row['resp_type'] not in ('—', '', '-', 'N/A')


def print_cl_experiment(rows):
    print_section("CL Style Experiment")

    by_style = defaultdict(list)
    for row in rows:
        style = extract_cl_style(row['notes'])
        by_style[style].append(row)

    has_data = False
    for tag, label in CL_STYLE_TAGS.items():
        group = by_style.get(tag, [])
        if not group:
            continue
        has_data = True
        responded = [r for r in group if response_received(r)]
        advanced = [r for r in group if r['status'] in ('Screen Scheduled', 'Phone Screen Done', 'Loop Scheduled', 'Offer')]

        print(f"\n  {tag} — {label}")
        print(f"    Applications : {len(group)}")
        print(f"    Any response : {len(responded)} ({pct(len(responded), len(group))})")
        print(f"    Advanced     : {len(advanced)} ({pct(len(advanced), len(group))})")
        companies = ', '.join(r['company'] for r in group)
        print(f"    Companies    : {companies}")

    unknown = by_style.get('unknown', [])
    if unknown:
        print(f"\n  ⚠️  {len(unknown)} row(s) without a CL style tag — add Style-A/B/C/D to Notes for tracking.")

    if not has_data:
        print("\n  No CL-tagged rows yet. Add Style-A/B/C/D to Notes field when logging applications.")


def main():
    parser = argparse.ArgumentParser(description='Weekly job search insights')
    parser.add_argument('--weeks', type=int, default=1, help='Number of weeks back to include (default: 1)')
    parser.add_argument('--full', action='store_true', help='Include all-time data')
    parser.add_argument('--cl-experiment', action='store_true', help='Show CL experiment summary only')
    args = parser.parse_args()

    rows = load_tracker_rows()
    today = date.today()

    # Filter by window
    if args.full:
        window_rows = rows
        window_label = "All Time"
    else:
        cutoff = today - timedelta(weeks=args.weeks)
        window_rows = [r for r in rows if r['date'] and r['date'] >= cutoff]
        window_label = f"Last {args.weeks * 7} Days (since {cutoff})"

    print(f"\n{'='*50}")
    print(f"  Weekly Insights — {today}")
    print(f"  Window: {window_label}")
    print(f"{'='*50}")

    if args.cl_experiment:
        # All-time for experiment regardless of window
        print_cl_experiment(rows)
        print()
        return

    # ── Overview ────────────────────────────────────────
    print_section("Overview")
    total = len(window_rows)
    responded = [r for r in window_rows if response_received(r)]
    advanced = [r for r in window_rows if r['status'] in ('Screen Scheduled', 'Phone Screen Done', 'Loop Scheduled', 'Offer')]
    rejected = [r for r in window_rows if r['status'] in ('Rejected', 'Withdrawn')]

    print(f"  Applications   : {total}")
    print(f"  Any response   : {len(responded)} ({pct(len(responded), total)})")
    print(f"  Advanced       : {len(advanced)} ({pct(len(advanced), total)})")
    print(f"  Rejected       : {len(rejected)} ({pct(len(rejected), total)})")
    pending = [r for r in window_rows if r['status'] == 'Applied']
    print(f"  Still pending  : {len(pending)}")

    # ── By Method ───────────────────────────────────────
    print_section("Response Rate by Application Method")
    by_method = defaultdict(list)
    for r in window_rows:
        by_method[r['method'] or 'unknown'].append(r)

    print(f"  {'Method':<22} {'Apps':>4}  {'Resp':>4}  {'Adv':>4}  {'Resp%':>6}  {'Adv%':>6}")
    print(f"  {'─'*22}  {'─'*4}  {'─'*4}  {'─'*4}  {'─'*6}  {'─'*6}")
    for method, group in sorted(by_method.items(), key=lambda x: -len(x[1])):
        resp = sum(1 for r in group if response_received(r))
        adv  = sum(1 for r in group if r['status'] in ('Screen Scheduled', 'Phone Screen Done', 'Loop Scheduled', 'Offer'))
        print(f"  {method:<22} {len(group):>4}  {resp:>4}  {adv:>4}  {pct(resp, len(group)):>6}  {pct(adv, len(group)):>6}")

    # ── By Job Source ────────────────────────────────────
    print_section("Response Rate by Job Source")
    by_source = defaultdict(list)
    for r in window_rows:
        source = extract_job_source(r['notes'])
        by_source[source].append(r)

    has_sources = any(s != 'unknown' for s in by_source)
    if not has_sources:
        print("  ⚠️  No src: tags found in Notes. Add 'src:LinkedIn', 'src:jobs-command', etc. to track this.")
    else:
        print(f"  {'Source':<22} {'Apps':>4}  {'Resp':>4}  {'Resp%':>6}")
        print(f"  {'─'*22}  {'─'*4}  {'─'*4}  {'─'*6}")
        for source, group in sorted(by_source.items(), key=lambda x: -len(x[1])):
            resp = sum(1 for r in group if response_received(r))
            print(f"  {source:<22} {len(group):>4}  {resp:>4}  {pct(resp, len(group)):>6}")

    # ── CL Experiment ────────────────────────────────────
    print_cl_experiment(window_rows)

    # ── Resume Version ───────────────────────────────────
    print_section("Response Rate by Resume Version")
    by_resume = defaultdict(list)
    for r in window_rows:
        by_resume[r['resume'] or 'unknown'].append(r)

    if len(by_resume) == 1:
        print(f"  Only one resume version in use: {list(by_resume.keys())[0]}")
    else:
        print(f"  {'Version':<30} {'Apps':>4}  {'Resp':>4}  {'Resp%':>6}")
        print(f"  {'─'*30}  {'─'*4}  {'─'*4}  {'─'*6}")
        for ver, group in sorted(by_resume.items(), key=lambda x: -len(x[1])):
            resp = sum(1 for r in group if response_received(r))
            print(f"  {ver:<30} {len(group):>4}  {resp:>4}  {pct(resp, len(group)):>6}")

    # ── Response Time ────────────────────────────────────
    print_section("Response Time")
    times = []
    for r in window_rows:
        if r['date'] and r['resp_date'] and response_received(r):
            delta = (r['resp_date'] - r['date']).days
            times.append(delta)
    if times:
        avg = round(sum(times) / len(times), 1)
        print(f"  Average time to first response: {avg} calendar days (n={len(times)})")
        print(f"  Range: {min(times)}–{max(times)} days")
    else:
        print("  Not enough response data yet.")

    # ── Follow-up Queue Status ───────────────────────────
    print_section("Follow-up Status (all tracked, not windowed)")
    fu_pending = []
    fu_overdue = []
    for r in rows:
        if r['status'] in ('Rejected', 'Withdrawn', 'Offer'):
            continue
        for wave, due, done in [('F/U 1', r['fu1_due'], r['fu1_done']),
                                  ('F/U 2', r['fu2_due'], r['fu2_done'])]:
            if due and not done:
                if due <= today:
                    fu_overdue.append((r['company'], wave, due))
                else:
                    fu_pending.append((r['company'], wave, due))

    if fu_overdue:
        print(f"  🔴 Overdue: {len(fu_overdue)}")
        for company, wave, due in sorted(fu_overdue, key=lambda x: x[2]):
            print(f"     {company} — {wave} (was due {due})")
    if fu_pending:
        print(f"  🟢 Upcoming: {len(fu_pending)}")
        for company, wave, due in sorted(fu_pending, key=lambda x: x[2]):
            days = (due - today).days
            print(f"     {company} — {wave} due {due} (in {days}d)")
    if not fu_overdue and not fu_pending:
        print("  ✓ No open follow-ups.")

    # ── Suggested Tweaks ────────────────────────────────
    print_section("Suggested Tweaks")
    tweaks = []

    if total < 5:
        tweaks.append("Volume is low — need 5+ applications before rate comparisons are meaningful.")

    if len(responded) == 0 and total >= 3:
        tweaks.append("0% response rate — check: ATS keyword coverage, resume version, application method.")

    # Method signal
    if len(by_method) > 1:
        best_method = max(by_method.items(),
                          key=lambda x: sum(1 for r in x[1] if response_received(r)) / len(x[1]))
        if sum(1 for r in best_method[1] if response_received(r)) > 0:
            tweaks.append(f"Best-performing method so far: '{best_method[0]}' — consider weighting more applications here.")

    # CL experiment signal
    cl_by_tag = defaultdict(list)
    for r in rows:
        tag = extract_cl_style(r['notes'])
        cl_by_tag[tag].append(r)
    cl_with_data = {t: g for t, g in cl_by_tag.items() if t in CL_STYLE_TAGS and len(g) >= 2}
    if len(cl_with_data) >= 2:
        best_cl = max(cl_with_data.items(),
                      key=lambda x: sum(1 for r in x[1] if response_received(r)) / len(x[1]))
        best_cl_resp = sum(1 for r in best_cl[1] if response_received(r))
        if best_cl_resp > 0:
            tweaks.append(f"CL experiment early signal: {best_cl[0]} ({CL_STYLE_TAGS[best_cl[0]]}) leads on response rate. Watch for n≥5 to confirm.")

    if fu_overdue:
        tweaks.append(f"{len(fu_overdue)} overdue follow-up(s) — run `python follow_up_queue.py` and send today.")

    if not tweaks:
        tweaks.append("Not enough data for pattern-based suggestions yet. Keep logging.")

    for t in tweaks:
        print(f"  → {t}")

    print()


if __name__ == '__main__':
    main()
