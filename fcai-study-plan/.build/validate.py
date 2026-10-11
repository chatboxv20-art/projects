# -*- coding: utf-8 -*-
"""Compliance sweep for the business study plan (prompt.md format)."""
import os, re, sys, glob

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "study-plan")
AR_LABEL = "**Egyptian Arabic (اللهجة المصرية):**"
END_BLOCKS = ["Lesson Summary", "Key Takeaways", "Common Mistakes", "Quiz",
              "Quiz Answers", "Practice Exercise", "Homework", "Recommended Revision",
              "Preview of the Next Lesson", "Important Terms"]
TEACH = [f"{w:02d}" for w in [1,2,3,4,5,6,9,10,11,12,13,14]]

problems = []

# 1. week lesson files
for sem in range(1, 9):
    for wk in TEACH:
        p = os.path.join(ROOT, f"semester-{sem}", f"week-{wk}.md")
        if not os.path.exists(p):
            problems.append(f"MISSING {p}")
            continue
        t = open(p, encoding="utf-8").read()
        n_def_en = t.count("English Definition:")
        n_def_ar = t.count("Egyptian Arabic Definition:")
        if n_def_en < 6 or n_def_ar < 6:
            problems.append(f"{p}: definitions en={n_def_en} ar={n_def_ar}")
        if t.count(AR_LABEL) < 40:
            problems.append(f"{p}: arabic blocks={t.count(AR_LABEL)}")
        for b in END_BLOCKS:
            if f"### {b} (" not in t:
                problems.append(f"{p}: missing end block {b}")
        if t.count("**Primary Resource (") < 6:
            problems.append(f"{p}: primary resources < 6")
        if t.count("**Optional Resource (") < 6:
            problems.append(f"{p}: optional resources < 6")
        if t.count("**Practice Platform (") < 6:
            problems.append(f"{p}: practice platforms < 6")

# 2. exam files
for sem in range(1, 9):
    for f in ["midterm-exam.md", "midterm-answers.md", "final-exam.md", "final-answers.md"]:
        p = os.path.join(ROOT, f"semester-{sem}", "exams", f)
        if not os.path.exists(p):
            problems.append(f"MISSING {p}")

# 3. required docs
for f in ["README.md", "00-overview/degree-map.md", "00-overview/style-guide-ar.md",
          "00-overview/cairo-university-system.md", "00-overview/glossary.md",
          "curriculum/course-inventory.md", "curriculum/prerequisite-graph.md"]:
    p = os.path.join(ROOT, f)
    if not os.path.exists(p):
        problems.append(f"MISSING {p}")

# 4. no placeholder links and no known typos
for p in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True):
    t = open(p, encoding="utf-8").read()
    for bad in ["TODO", "PLACEHOLDER", "[UNVERIFIED", "example.com", "http://example"]:
        if bad in t:
            problems.append(f"{p}: contains {bad}")
    if "نطام" in t:
        problems.append(f"{p}: typo نطام (should be نظام)")

# 4b. MCQ answer keys: varied letters and aligned with the exam options
OPT = ["أ", "ب", "ج", "د"]
for sem in range(1, 9):
    for kind in ("midterm", "final"):
        ep = os.path.join(ROOT, f"semester-{sem}", "exams", f"{kind}-exam.md")
        ap = os.path.join(ROOT, f"semester-{sem}", "exams", f"{kind}-answers.md")
        if not (os.path.exists(ep) and os.path.exists(ap)):
            continue
        ex = open(ep, encoding="utf-8").read()
        an = open(ap, encoding="utf-8").read()
        key = {m.group(1): m.group(2)
               for m in re.finditer(r"\*\*(\d+)\.\*\* الإجابة \*\*([أبجد])\*\*", an)}
        letters = set(key.values())
        if len(letters) < 2:
            problems.append(f"{ap}: MCQ answers not varied (all {letters})")
        blocks = re.split(r"\n\*\*(\d+)\.\*\* ", ex)
        for i in range(1, len(blocks), 2):
            num, body = blocks[i], blocks[i + 1]
            opts = re.findall(r"- ([أبجد])\) (.+)", body)
            if len(opts) != 4:
                continue
            chosen = [txt for lab, txt in opts if lab == key.get(num)]
            if not chosen or "أداة شغّالة" not in chosen[0]:
                problems.append(f"{ep}: answer key for Q{num} does not match options")

# 5. count files
allmd = glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True)
print(f"Total markdown files: {len(allmd)}")
print(f"Problems: {len(problems)}")
for x in problems[:60]:
    print(" -", x)
