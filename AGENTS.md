# AGENTS.md — repository knowledge

## What this repo is
Three parallel, self-contained Markdown study-guide projects for Cairo University
programs (4 years / 8 semesters), each mirroring a real faculty curriculum with
16 teaching weeks per semester, midterm (week 8) + final exam papers with model answers:

- `study-plan/` — Communication & Computer Engineering (CCE), Faculty of Engineering.
  Content is **Egyptian-Arabic only** (format contract from `/workspace/prompt_en.md`).
- `business-study-plan/` — Business Administration track, Faculty of Business /
  Faculty of Commerce & Business Administration. Content is **fully bilingual**
  (complete English block then complete Egyptian-Arabic block), following the
  format contract in `prompt.md` (repo-root `prompt.md`, also at
  `/home/openhands/workspace/project/prompt.md`).
- `fcai-study-plan/` — Computer Science track, Faculty of Computers and Artificial
  Intelligence (FCAI), Cairo University. Content is **fully bilingual** in the same
  `prompt.md` format. 8 semesters / 48 courses / **136 credit hours** (17 CH each),
  mirroring the real FCAI credit-hour system (135–138 CH) with courses such as
  CS111, CS112, CS113, CS114, CS211, CS213, AI201, AI301.

## Prompt.md format contract (business-study-plan and fcai-study-plan)
Every lesson section must be a *full bilingual block*: the whole English section
first, then `**Egyptian Arabic (اللهجة المصرية):**` and the whole same section in
natural Egyptian colloquial Arabic (عامية مصرية, not فصحى). Never mix languages
line-by-line. Each topic opens with `Topic Name (اسم عربي)` + `English Definition:`
+ `Egyptian Arabic Definition:` immediately under the heading. Links, URLs, code,
Resource Name/Type/Link/Difficulty/Estimated Time fields, and table structure stay
untranslated. Ten mandatory end-of-lesson blocks in a fixed order, plus a
per-course resource triad (1 primary + 1 optional + 1 practice platform).

## How business-study-plan is generated
It is generated, not hand-written. Everything lives in `business-study-plan/.build/`:

- `curriculum_data.py` — single source of truth: 8 semesters, 48 courses,
  codes, credit hours, splits, prerequisites (128 CH total, 16/semester).
- `topics.py` + `topics2.py` — 12 teaching-week topics per course (weeks 1–6, 9–14).
- `domains_a.py`, `domains_b.py`, `domains_c.py` — 24 reusable bilingual domain
  content bundles (accounting, management, economics, marketing, finance, etc.).
- `course_domain.py` — maps course codes to domain bundles.
- `terms.py` — supporting vocabulary per domain for the "Important Terms" block.
- `generator.py` — bilingual lesson/topic/resource/end-of-lesson renderer.
- `generator_build.py` — week files + semester READMEs.
- `generator_exams.py` — midterm/final exam papers + model answers.
- `generator_docs.py` — overview docs, curriculum docs, root/top READMEs.
- `run_build.py` — run this to regenerate everything: `python3 run_build.py`.
- `validate.py` — compliance sweep (definitions, bilingual blocks, end blocks,
  resource triads, missing files, placeholder links). Must report 0 problems.

Regenerate with: `cd business-study-plan/.build && python3 run_build.py && python3 validate.py`

## How fcai-study-plan is generated
Same pipeline shape as `business-study-plan`, living in `fcai-study-plan/.build/`:
`curriculum_data.py` (8 semesters / 48 courses / 136 CH), `topics.py` + `topics2.py`
(12 teaching-week topics per course), `domains_a.py`/`domains_b.py`/`domains_c.py`
(CS/AI domain bundles: programming, data structures, algorithms, OS, networks,
databases, ML, deep learning, NLP, vision, RL, security, cloud, graphics, etc.),
`course_domain.py`, `terms.py`, `generator.py`, `generator_build.py`,
`generator_exams.py`, `generator_docs.py`, `run_build.py`, `validate.py`.
Regenerate with: `cd fcai-study-plan/.build && python3 run_build.py && python3 validate.py`

## Conventions / gotchas
- Teaching weeks are `[1,2,3,4,5,6,9,10,11,12,13,14]`; week 7 = review,
  week 8 = midterm, weeks 15–16 = review. Topic index = `TEACH_WEEKS.index(week)`.
- Exam MCQ answer keys in `generator_exams.py` are shuffled with
  `random.Random(f"{code}:{q_index}")` so the correct option varies by question
  and stays deterministic across rebuilds; `validate.py` checks the key letters
  vary and point at the correct option, and flags the Arabic typo `نطام`.
- Arabic prose must use `نظام`, never `نطام` (a typo that once appeared 1280×
  across the weekly lessons).
- Adding a course requires: entry in `curriculum_data.py`, 12 topics in `topics*.py`,
  a `course_domain.py` mapping, and (if a new domain) a bundle in `domains_*.py`
  plus terms in `terms.py`.
- Source-data note: real Cairo Faculty of Commerce/Business plans vary by program
  (128–132 CH); this plan standardises on 128 CH over 8 equal 16-CH semesters.
  Official reference: `https://www.foc.cu.edu.eg/`.
