# AGENTS.md

## Repository purpose
This repository holds an academic study-plan deliverable: a 4-year / 8-semester
Business Administration curriculum modeled on the **Faculty of Business (كلية التجارة),
Cairo University** credit-hour system.

## Layout
- `study-plan/README.md` — the full study plan (system, requirements, 8 semesters,
  exam plans, academic calendar, grading, and course catalog).
- `study-plan/course-catalog.csv` — machine-readable catalog of all courses.
- `study-plan/verify_plan.py` — consistency checks for the plan.
- `study-plan/generate_catalog.py` — regenerates the CSV from the README tables.

## Working rules
- The plan must always total **144 credit hours** across **8 semesters**.
- Keep the README and CSV in sync: after editing catalog tables in the README, run
  `python study-plan/generate_catalog.py`.
- After any edit, run `python study-plan/verify_plan.py`; it must print
  "All consistency checks passed." before committing.

## Key facts baked into the plan (verify before changing)
- Faculty: كلية التجارة – جامعة القاهرة; degree: BSc in Commerce (Business Administration).
- Credit-hour system; 4 years = 8 semesters; 144 CH; summer term optional (max 6–9 CH).
- Requirement groups: University 15, Faculty core 36, Major 72, Electives 21.
- Exam weighting: year-work 20% + midterm 20% + final 60% (faculty allows final >= 70%).
- Official 2026-2027 calendar: start 19 Sep 2026; midterms Nov 2026; finals 2-21 Jan 2027;
  Semester 2 from 6 Feb 2027; finals May-Jun 2027.
- Course codes/semester lists are a realistic reconstruction, not the faculty's official
  catalog; confirm current offerings with the faculty academic advising office.
