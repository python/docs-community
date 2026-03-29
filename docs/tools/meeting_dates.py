"""Sphinx extension to generate a list of upcoming meeting dates."""

import datetime as dt
import os

from docutils import nodes
from sphinx.util.docutils import SphinxDirective


def utc_hour(date):
    if 4 <= date.month <= 10:
        # Daylight saving time in Europe and the US
        return 19 if date.month % 2 == 0 else 16
    else:
        # Winter time in Europe and the US
        return 20 if date.month % 2 == 0 else 17


def first_tuesday(year, month):
    first = dt.date(year, month, 1)
    days_ahead = (1 - first.weekday()) % 7
    return first + dt.timedelta(days=days_ahead)


def upcoming_meetings(today, count):
    meetings = []
    year, month = today.year, today.month
    while len(meetings) < count:
        meeting_date = first_tuesday(year, month)
        if meeting_date >= today:
            meetings.append((meeting_date, utc_hour(meeting_date)))
        month += 1
        if month > 12:
            month = 1
            year += 1
    return meetings


def past_meetings(today, count):
    meetings = []
    year, month = today.year, today.month
    while len(meetings) < count:
        meeting_date = first_tuesday(year, month)
        if meeting_date < today:
            meetings.append((meeting_date, utc_hour(meeting_date)))
        month -= 1
        if month < 1:
            month = 12
            year -= 1
    meetings.reverse()
    return meetings


class MeetingDatesDirective(SphinxDirective):
    has_content = False

    def run(self):
        bullets = nodes.bullet_list()
        for date, hour in upcoming_meetings(dt.date.today(), 6):
            item = nodes.list_item()
            text = f"{date.strftime('%B %d, %Y')} - {hour:02d}:00 UTC"
            url = f"https://arewemeetingyet.com/UTC/{date.isoformat()}/{hour}:00/Docs Community Meeting"

            paragraph = nodes.paragraph()
            ref = nodes.reference("", text, refuri=url)
            paragraph += ref
            item += paragraph
            bullets += item

        return [bullets]


def generate_ics(app, exception):
    if exception:
        return

    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Python Docs WG//Meeting dates//EN",
        "X-WR-CALDESC:Python Docs WG meetings from https://docs-community.readthedocs.io/",
        "X-WR-CALNAME:Python Docs WG meetings",
    ]
    today = dt.date.today()
    meetings = past_meetings(today, 12) + upcoming_meetings(today, 12)
    for date, hour in meetings:
        start = dt.datetime(date.year, date.month, date.day, hour, 0, 0)
        end = start + dt.timedelta(hours=1)
        lines += [
            "BEGIN:VEVENT",
            f"UID:{start.strftime('%Y%m%dT%H%M%SZ')}@python-docs-community",
            f"DTSTAMP:{dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ')}",
            f"DTSTART:{start.strftime('%Y%m%dT%H%M%SZ')}",
            f"DTEND:{end.strftime('%Y%m%dT%H%M%SZ')}",
            "SUMMARY:Python Docs WG",
            "DESCRIPTION:Agenda: https://hackmd.io/@encukou/pydocswg1"
            "\\nDiscord event: https://discord.gg/yhvN2ECXSM?event=1389130476555337908",
            "END:VEVENT",
        ]
    lines += ["END:VCALENDAR"]
    ics = "\r\n".join(lines) + "\r\n"

    with open(os.path.join(app.outdir, "docs-community-meetings.ics"), "w") as f:
        f.write(ics)


def setup(app):
    app.add_directive("meeting-dates", MeetingDatesDirective)
    app.connect("build-finished", generate_ics)
    return {"version": "1.0", "parallel_read_safe": True}
