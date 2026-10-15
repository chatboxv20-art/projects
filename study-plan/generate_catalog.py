"""Regenerate course-catalog.csv from the catalog tables in README.md."""
import csv
import re
from pathlib import Path

text = Path(__file__).with_name("README.md").read_text(encoding="utf-8")

row_re = re.compile(r"^\|\s*([A-Z]{3}\s\d{3})\s*\|\s*([^|]+?)\s*\|\s*(\d)\s*\|(.*)$")
section_re = re.compile(r"^### 10\.(\d) (.+)")
track_re = re.compile(r"^\*\*(.+?) track\*\*")

category = track = None
rows = []
for line in text.splitlines():
    s = section_re.match(line)
    if s:
        title = s.group(2)
        if "University" in title:
            category = "University"
        elif "Core" in title:
            category = "Faculty core"
        elif "Major" in title:
            category = "Major"
        else:
            category = "Elective"
        continue
    t = track_re.match(line)
    if t:
        track = t.group(1)
        continue
    m = row_re.match(line)
    if not m or category is None:
        continue
    code, name, ch, rest = m.group(1), m.group(2).strip(), m.group(3), m.group(4)
    cells = [c.strip() for c in rest.strip().strip("|").split("|")]
    prereq, semester = "", ""
    if len(cells) >= 2 and cells[-1].isdigit():
        prereq, semester = cells[-2], cells[-1]
    elif len(cells) == 1 and cells[0].isdigit():
        semester = cells[0]
    rows.append([code, name, ch, category, track or "", prereq, semester])

out = Path(__file__).with_name("course-catalog.csv")
with out.open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Code", "Course", "Credit_Hours", "Category", "Track",
                "Prerequisite", "Semester"])
    w.writerows(rows)
print(f"Wrote {len(rows)} rows to {out.name}")
