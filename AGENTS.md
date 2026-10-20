# AGENTS.md — repository knowledge

## What this repo is

A self-contained Markdown **study-guide** for a 4-year / 8-semester university
degree that mirrors the real **Business Administration track** at the Faculty of
Business (Faculty of Commerce & Business Administration), Cairo University.

Everything lives under `business-study-plan/`:

- `business-study-plan/study-plan/` — the guide itself (175 Markdown files).
- `business-study-plan/.build/` — the generator that produces the guide.

## Format contract ("prompt_v2" bilingual-block system)

Every lesson section is a **full bilingual block**:

1. the complete English section first, then
2. the label `**Egyptian Arabic (اللهجة المصرية):**` followed by the complete
   same section in natural Egyptian colloquial Arabic (عامية مصرية, not فصحى).

Never mix languages line-by-line. Each topic opens immediately under its heading
with a Definition block:

```
Topic Name (اسم عربي)
English Definition: ...
Egyptian Arabic Definition: ...
```

Untranslated on purpose: links/URLs, code, and the Resource
Name/Type/Link/Difficulty/Estimated Time fields, plus course codes and table
structure. Each lesson ends with ten mandatory blocks in a fixed order
(Lesson Summary, Key Takeaways, Common Mistakes, Quiz, Quiz Answers, Practice
Exercise, Homework, Recommended Revision, Preview of the Next Lesson, Important
Terms) and carries a per-course resource triad (1 primary + 1 optional + 1
practice platform).

## Structure of the guide

- `00-overview/` — style guide, Cairo University credit-hour/exam system,
  degree map, glossary.
- `curriculum/` — full course inventory and prerequisite graph.
- `semester-1/` … `semester-8/` — semester calendar + 16 weekly lessons
  (`week-01.md` … `week-16.md`) + an `exams/` folder.
- `semester-N/exams/` — midterm and final papers **with model answers**.

Teaching weeks are `[1,2,3,4,5,6,9,10,11,12,13,14]`; week 7 = review,
week 8 = midterm, weeks 15–16 = review. Topic index = `TEACH_WEEKS.index(week)`.

## Curriculum summary

8 semesters, 48 courses, **128 credit hours** (16 CH per semester, 6 courses
each), reconciling to a standard Faculty of Business total. Level progression:
Freshman (1–2) → Sophomore (3–4) → Junior (5–6) → Senior (7–8).

## How the guide is generated

It is generated, not hand-written. `business-study-plan/.build/`:

- `curriculum_data.py` — single source of truth (semesters, courses, codes,
  credit hours, splits, prerequisites).
- `topics.py` + `topics2.py` — 12 teaching-week topics per course.
- `domains_a.py` / `domains_b.py` / `domains_c.py` — reusable bilingual domain
  content bundles (accounting, management, economics, marketing, finance, …).
- `course_domain.py` — maps course codes to domain bundles.
- `terms.py` — supporting vocabulary for the "Important Terms" block.
- `generator.py` — bilingual lesson/topic/resource/end-of-lesson renderer.
- `generator_build.py` — week files + semester READMEs.
- `generator_exams.py` — midterm/final papers + model answers.
- `generator_docs.py` — overview docs, curriculum docs, root/top READMEs.
- `run_build.py` — run this to regenerate everything.
- `validate.py` — compliance sweep; must report 0 problems.

Regenerate with:

```
cd business-study-plan/.build && python3 run_build.py && python3 validate.py
```

## Conventions / gotchas

- Exam MCQ answer keys are shuffled with `random.Random(f"{code}:{q_index}")`
  so the correct option varies by question and stays deterministic across
  rebuilds; `validate.py` checks the key letters vary and point at the correct
  option.
- Exam score totals must equal the sum of their sections (midterm 84, final 96).
- Arabic prose must use `نظام`, never the typo `نطام`.
- Adding a course requires: an entry in `curriculum_data.py`, 12 topics in
  `topics*.py`, a `course_domain.py` mapping, and (if a new domain) a bundle in
  `domains_*.py` plus terms in `terms.py`.
- Source-data note: real Cairo Faculty of Commerce/Business plans vary by
  program (128–132 CH); this plan standardises on 128 CH over 8 equal 16-CH
  semesters. Official reference: `https://www.foc.cu.edu.eg/`.
