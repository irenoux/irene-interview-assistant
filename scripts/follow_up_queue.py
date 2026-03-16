#!/usr/bin/env python3
"""
Follow-up queue: scan Application Tracker in coaching_state.md
and show applications with F/U 1 or F/U 2 due today or overdue.

Usage:
    python follow_up_queue.py              # show today + overdue
    python follow_up_queue.py --all        # include all pending future F/Us too
"""

import re
import sys
from datetime import datetime, date

COACHING_STATE = "./coaching_state.md"


def parse_date(s):
    s = s.strip().replace('~', '').replace('*', '')
    if not s or s in ('—', 'N/A', 'N/A (pre-tracker)', '-', ''):
        return None
    try:
        return datetime.strptime(s, '%Y-%m-%d').date()
    except ValueError:
        return None


def is_done(s):
    s = s.strip()
    return s not in ('—', '', 'N/A', 'N/A (pre-tracker)', '-')


def main():
    show_all = '--all' in sys.argv

    with open(COACHING_STATE, 'r') as f:
        content = f.read()

    # Extract the Application Tracker table
    tracker_match = re.search(
        r'## Application Tracker\n.*?\n\|[-| ]+\|\n(.*?)(?=\n## |\Z)',
        content, re.DOTALL
    )
    if not tracker_match:
        print("Could not find Application Tracker in coaching_state.md")
        return

    rows_text = tracker_match.group(1)
    today = date.today()

    due_today = []
    overdue = []
    upcoming = []

    for line in rows_text.strip().split('\n'):
        if not line.startswith('|'):
            continue
        cols = [c.strip() for c in line.split('|')[1:-1]]
        if len(cols) < 14:
            continue

        # Column positions (0-indexed after splitting):
        # 0=ID, 1=Date, 2=Company, 3=Role, 4=Resume, 5=Method, 6=CL,
        # 7=Status, 8=RespDate, 9=RespType, 10=FU1Due, 11=FU1Done,
        # 12=FU2Due, 13=FU2Done, 14=Notes
        try:
            id_ = cols[0]
            company = cols[2]
            role = cols[3]
            status = cols[7]
            fu1_due = parse_date(cols[10])
            fu1_done = is_done(cols[11])
            fu2_due = parse_date(cols[12]) if len(cols) > 12 else None
            fu2_done = is_done(cols[13]) if len(cols) > 13 else False
        except IndexError:
            continue

        # Skip closed/rejected/withdrawn unless pending F/Us explicitly set
        if status in ('Rejected', 'Withdrawn', 'Offer'):
            continue

        label = f"[{id_}] {company} — {role}"

        if fu1_due and not fu1_done:
            if fu1_due == today:
                due_today.append((label, 'F/U 1', fu1_due, status))
            elif fu1_due < today:
                overdue.append((label, 'F/U 1', fu1_due, status))
            elif show_all:
                upcoming.append((label, 'F/U 1', fu1_due, status))

        if fu2_due and not fu2_done:
            if fu2_due == today:
                due_today.append((label, 'F/U 2', fu2_due, status))
            elif fu2_due < today:
                overdue.append((label, 'F/U 2', fu2_due, status))
            elif show_all:
                upcoming.append((label, 'F/U 2', fu2_due, status))

    print(f"\n{'='*55}")
    print(f"  Follow-up Queue — {today}")
    print(f"{'='*55}\n")

    if overdue:
        print("🔴 OVERDUE:")
        for label, wave, due, status in sorted(overdue, key=lambda x: x[2]):
            days_late = (today - due).days
            print(f"  {label}")
            print(f"     {wave} was due {due} ({days_late}d ago) — Status: {status}\n")

    if due_today:
        print("🟡 DUE TODAY:")
        for label, wave, due, status in due_today:
            print(f"  {label}")
            print(f"     {wave} due today — Status: {status}\n")

    if upcoming and show_all:
        print("🟢 UPCOMING:")
        for label, wave, due, status in sorted(upcoming, key=lambda x: x[2]):
            days_until = (due - today).days
            print(f"  {label}")
            print(f"     {wave} due {due} (in {days_until}d) — Status: {status}\n")

    if not overdue and not due_today:
        print("✓ Nothing due today.\n")
        if not show_all:
            print("  Run with --all to see upcoming F/Us.\n")


if __name__ == '__main__':
    main()
