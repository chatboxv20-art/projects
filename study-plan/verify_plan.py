"""Consistency checks for the Cairo University Business Administration study plan.

Parses the course-catalog tables in README.md and verifies:
  1. Requirement-group credit totals (15 / 36 / 72 / 21 = 144)
  2. Per-semester credit totals (18 / 17 / 20 / 18 / 18 / 18 / 17 / 18)
  3. Every prerequisite is scheduled in an earlier semester than its course
"""
import re
import sys
from pathlib import Path

README = Path(__file__).with_name("README.md")
text = README.read_text(encoding="utf-8")

# ---- Parse catalog tables (sections 10.1 - 10.4) -------------------------------
# Rows look like: | CODE | Course | CH | [extra cols...] |
row_re = re.compile(r"^\|\s*([A-Z]{3}\s\d{3})\s*\|\s*([^|]+?)\s*\|\s*(\d)\s*\|(.*)$")
section_re = re.compile(r"^### 10\.(\d) (.+)")

courses = {}  # code -> dict(ch, semester, prereq, category)
category = None
for line in text.splitlines():
    sec = section_re.match(line)
    if sec:
        title = sec.group(2)
        if "University" in title:
            category = "University"
        elif "Core" in title:
            category = "Faculty core"
        elif "Major" in title:
            category = "Major"
        elif "Elective" in title:
            category = "Elective"
        continue
    m = row_re.match(line)
    if not m or category is None:
        continue
    code, name, ch, rest = m.group(1), m.group(2).strip(), int(m.group(3)), m.group(4)
    if code in courses:  # keep first occurrence
        continue
    cells = [c.strip() for c in rest.strip().strip("|").split("|")]
    prereq, semester = "", None
    if len(cells) >= 2 and cells[-1].isdigit():
        prereq = cells[-2]
        semester = int(cells[-1])
    elif len(cells) == 1 and cells[0].isdigit():
        semester = int(cells[0])
    courses[code] = {"name": name, "ch": ch, "prereq": prereq,
                     "sem": semester, "category": category}

errors = []

# ---- 1. Requirement-group totals ----------------------------------------------
# The catalog lists an elective *menu* larger than what a student takes, so the
# degree total counts only 21 elective credit hours (7 electives x 3 CH).
ELECTIVE_CH_TAKEN = 21
by_cat = {}
for c in courses.values():
    by_cat[c["category"]] = by_cat.get(c["category"], 0) + c["ch"]
required = sum(ch for cat, ch in by_cat.items() if cat != "Elective")
group_total = required + ELECTIVE_CH_TAKEN
print(f"[1] Requirement groups: {by_cat}")
print(f"    Required (non-elective) = {required}, electives taken = {ELECTIVE_CH_TAKEN}")
print(f"    Degree total = {group_total} (expected 144)")
print(f"    Courses parsed: {len(courses)} (menu includes elective surplus)")
if group_total != 144:
    errors.append(f"Degree total = {group_total}, expected 144")

# ---- 2. Per-semester totals from the curriculum section -----------------------
sem_tables = re.findall(r"#### Semester (\d) — (\d+) CH", text)
if len(sem_tables) != 8:
    errors.append(f"Found {len(sem_tables)} semester headers, expected 8")
sem_sum = sum(int(ch) for _, ch in sem_tables)
print(f"[2] Semester headers: {[int(s) for s, _ in sem_tables]}")
print(f"    Sum of stated semester totals: {sem_sum} (expected 144)")
if sem_sum != 144:
    errors.append(f"Sum of semester totals = {sem_sum}, expected 144")

# ---- 2b. Each semester's course rows must sum to its stated total --------------
# Course rows in section 6 include regular codes and bold "*Elective I*" slots.
block_re = re.compile(r"#### Semester (\d) — (\d+) CH(.*?)(?=#### Semester|### Credit-Hour)", re.S)
cur_row_re = re.compile(
    r"^\|\s*\*{0,2}([A-Z]{3}\s\d{3}|Elective [IVX]+)\*{0,2}\s*\|\s*([^|]+?)\s*\|\s*(\d)\s*\|",
    re.M,
)
print("[2b] Per-semester course-row sums:")
for sem, stated, body in block_re.findall(text):
    body = body.split("**Exam plan")[0]
    total = sum(int(ch) for _, _, ch in cur_row_re.findall(body))
    flag = "OK" if total == int(stated) else "MISMATCH"
    print(f"     Semester {sem}: rows sum {total:2d}, header {stated:>2} -> {flag}")
    if total != int(stated):
        errors.append(f"Semester {sem} rows sum {total} != stated {stated}")

# ---- 3. Prerequisite ordering -------------------------------------------------
print("[3] Prerequisite ordering:")
for code, c in courses.items():
    if not c["prereq"] or c["sem"] is None:
        continue
    for p in re.findall(r"[A-Z]{3}\s\d{3}", c["prereq"]):
        p = p.strip()
        if p not in courses:
            errors.append(f"{code}: unknown prerequisite {p}")
            continue
        if courses[p]["sem"] is None or c["sem"] is None:
            continue
        if courses[p]["sem"] >= c["sem"]:
            errors.append(
                f"{code} (sem {c['sem']}) has prereq {p} (sem {courses[p]['sem']}) "
                "not in an earlier semester"
            )

# ---- Report -------------------------------------------------------------------
if errors:
    print("\nFAILED checks:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print("\nAll consistency checks passed.")
