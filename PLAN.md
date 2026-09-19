# PLAN.md — 4-Year / 8-Semester CCE Study-Plan

## 1. OBJECTIVE

Build a complete, self-contained **Markdown study-guide repository** for a 4-year / 8-semester
engineering degree that mirrors the **Communication & Computer Engineering (CCE)** track at the
Faculty of Engineering, Cairo University.

The repository must contain:

- A faithful **8-semester curriculum skeleton** (every course, code, credit hours, prerequisites,
  16 teaching weeks + midterm week + final exam period per semester).
- **Midterm and final exam papers** for every semester, with questions *and* model answers.
- **Week-by-week lesson content** authored strictly in the format defined by `/workspace/prompt_en.md`
  — i.e. every lesson written entirely in natural Egyptian colloquial Arabic (عامية مصرية), each
  topic opening with a Definition block, plus practical examples, resources, quiz + answers,
  homework, and end-of-lesson sections.
- **One fully-written, gold-standard sample lesson** produced first so the style can be verified
  before generating the rest in batches.

## 2. CONTEXT SUMMARY

- **Source of truth:** the official Cairo University CCE program specification — course codes,
  titles, credit hours, prerequisites, and the 180 CH total — rather than invented structure.
- **Sequence tension:** the official sample plan spreads the program over 10 terms (including
  summers), while the request is for **8 semesters / 4 years**; the course sequence therefore has
  to be re-sequenced.
- **Language contract (from `prompt_en.md`):** lessons are Egyptian Arabic only. The only things
  that stay untranslated are links/URLs, code/terminal commands/config snippets, and the Resource
  Name / Type / Link / Difficulty / Estimated Time fields.
- **Scale reality:** ~68 courses × 16 weeks is far more than can be generated in one pass, which is
  why the approach is gated and batched.

## 3. APPROACH OVERVIEW

**Skeleton → gold-standard sample → batch generate.**

This is deliberate: writing all ~68 courses × 16 weeks at full `prompt_en.md` depth in one go is not
achievable, so the plan freezes the curriculum data first, gets one perfect lesson approved as the
style contract, then generates the rest semester by semester.

## 4. IMPLEMENTATION STEPS

1. **Create the repo tree** (`study-plan/`) plus an Egyptian-Arabic style guide encoding the
   `prompt_en.md` rules.
2. **Build the authoritative course inventory** (codes, CH, prereqs) and re-sequence it into exactly
   8 semesters, reconciling to 180 CH — preserving credit-hour totals, level progression, and
   prerequisite order; explicitly merge/drop the summer terms the official sample plan uses and note
   any course that must move.
3. **Lay out 8 semester calendars:** 16 teaching weeks, **week 8 = midterm**, then the final exam
   period.
4. **Gold-standard lesson** = `semester-1/week-01.md`, full format, self-checked, awaiting approval.
5. **Semester 1: weeks 2–16** lessons.
6. **Semester 1: midterm + final exam papers** with model answers.
7. **Repeat for semesters 2–8** (lessons + exams).
8. **Compliance sweep** for language/format violations.
9. **Final navigation README.**

## 5. TESTING AND VALIDATION

- A **format/structure checker** verifying that each lesson has a Definition block per topic, the
  full set of end-of-lesson blocks, and a per-course resource triad.
- A **language-compliance sweep** flagging non-Arabic prose while allowing technical identifiers,
  links, and resource fields to remain untranslated.

### Open items flagged by the plan (resolved during implementation)

1. **10 official terms incl. summers vs. 8 requested semesters** — credits were redistributed into
   8 core semesters plus 4 summer sessions, reconciling to exactly 180 CH.
2. **Some official course titles were not text-extractable from the PDFs** — marked
   `[UNVERIFIED — needs source]` instead of guessing.
3. **Week files cover multiple courses at once** (parallel-course structure) rather than treating
   each week as a single subject.

---

## Provenance note

This file reproduces the plan that was authored in the planning conversation and recovered from its
event log. The original `.agents_tmp/PLAN.md` in this repository had been truncated to its section
headings (117 bytes); the full 18,160-character plan was recovered from the planning conversation's
`event-00034` (`action.new_str`) and restored before execution. Sections 2–5 above are reconstructed
from that plan's own summary, its nine implementation steps, and the assumptions and validation
rules it stated throughout.
