# -*- coding: utf-8 -*-
"""Builds all markdown artefacts for the business study plan."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import curriculum_data as CD
import generator as G

TOPICS = G.TOPICS
DOMAINS = G.DOMAINS
AR_LABEL = G.AR_LABEL
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

ORD_AR = ["الأول", "الثاني", "الثالث", "الرابع", "الخامس", "السادس", "السابع", "الثامن"]

TEACH_WEEKS = [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14]


def courses(sem):
    return CD.SEMESTERS[sem]["courses"]


def w(path, text):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text)


# ---------------------------------------------------------------------------
# WEEK FILES
# ---------------------------------------------------------------------------
def week_header(sem, week):
    cs = courses(sem)
    names = "، ".join(f"{c[0]} ({c[2]})" for c in cs)
    if week in TEACH_WEEKS:
        idx = TEACH_WEEKS.index(week)
        o = [f"# الأسبوع {week} — الفصل {sem}\n"]
        o.append(f"> الدرس ده بيغطّي موضوع واحد في كل مقرر من مقررات الفصل، وكل الشرح مكتوب "
                 f"بالعامية المصرية مع البلوك الإنجليزي الكامل جنبه.\n")
        o.append(f"**المقررات اللي في الدرس ده:** {names}\n")
        o.append("---\n")
        for i, c in enumerate(cs):
            code, en, ar, ch, split, pre = c
            d = G.domain_of(code)
            t_en, t_ar = TOPICS[code][idx]
            o.append(f"# القسم {ORD_AR[i]}: {ar} ({code})\n")
            o.append(G.topic_section(idx, t_en, t_ar, d))
            o.append("\n---\n")
        o.append(G.resources_section(cs))
        o.append("\n---\n")
        o.append(G.end_of_lesson(sem, week, cs))
        o.append("\n---\n")
        prev = week - 1 if week > 1 else None
        nxt = week + 1
        nav = []
        if prev:
            nav.append(f"[الدرس السابق: week-{prev:02d}.md](week-{prev:02d}.md)")
        nav.append(f"[رجوع لفصل {sem}](README.md)")
        nav.append(f"[الدرس الجاي: week-{nxt:02d}.md](week-{nxt:02d}.md)")
        o.append(" · ".join(nav))
        return "\n".join(o)
    return None


def review_week(sem, week, kind):
    cs = courses(sem)
    o = [f"# الأسبوع {week} — الفصل {sem}\n"]
    if kind == "midterm":
        o.append("> أسبوع الميدتيرم. الدرس ده مراجعة شاملة لكل اللي اتشرح من الأسبوع الأول للسابع.\n")
    else:
        o.append("> أسبوع مراجعة. الدرس ده مراجعة شاملة لكل مقررات الفصل.\n")
    o.append("---\n")
    o.append(G.h("What This Week Is For", "الأسبوع ده ليه"))
    if kind == "midterm":
        o.append(G.bi(
            "This is the midterm week. There is no new material; the goal is to consolidate weeks 1 to 7, "
            "practise under exam conditions and close every gap before the midterm paper.",
            "ده أسبوع الميدتيرم. مفيش مادة جديدة؛ الهدف تثبيت الأسابيع 1 لـ7، والتمرين على ظروف الامتحان، "
            "وتقفيل أي فجوة قبل ورقة الميدتيرم."))
    else:
        o.append(G.bi(
            "This is a general revision week. You review the whole semester, rebuild your summary sheet, "
            "and work through full exam papers under time pressure.",
            "ده أسبوع مراجعة عامة. بتراجع الفصل كله، وتبني ورقة ملخصك من جديد، "
            "وتحل نماذج امتحانات كاملة تحت ضغط الوقت."))
    o.append(G.h("Courses and Topics to Review", "المقررات والمواضيع اللي تراجعها"))
    for code, en, ar, ch, split, pre in cs:
        d = G.domain_of(code)
        if kind == "midterm":
            tps = TOPICS[code][:6]
        else:
            tps = TOPICS[code]
        lines_en = "; ".join(t[0] for t in tps)
        lines_ar = "؛ ".join(t[1] for t in tps)
        o.append(f"**{code} — {ar}**")
        o.append(G.bi(f"Review: {lines_en}.", f"راجع: {lines_ar}."))
    o.append(G.end_of_lesson(sem, week, cs))
    o.append("\n---\n")
    if kind == "midterm":
        nav = (f"[الدرس السابق: week-07.md](week-07.md) · [رجوع لفصل {sem}](README.md) · "
               f"[الدرس الجاي: week-09.md](week-09.md)")
    elif week == 15:
        nav = f"[الدرس السابق: week-14.md](week-14.md) · [رجوع لفصل {sem}](README.md) · [الدرس الجاي: week-16.md](week-16.md)"
    else:
        nav = f"[الدرس السابق: week-15.md](week-15.md) · [رجوع لفصل {sem}](README.md)"
    o.append(nav)
    return "\n".join(o)


def build_weeks():
    for sem in range(1, 9):
        for week in TEACH_WEEKS:
            w(f"study-plan/semester-{sem}/week-{week:02d}.md", week_header(sem, week))
        w(f"study-plan/semester-{sem}/week-07.md", review_week(sem, 7, "review"))
        w(f"study-plan/semester-{sem}/week-08-midterm.md", review_week(sem, 8, "midterm"))
        w(f"study-plan/semester-{sem}/week-15.md", review_week(sem, 15, "review"))
        w(f"study-plan/semester-{sem}/week-16.md", review_week(sem, 16, "review"))


# ---------------------------------------------------------------------------
# SEMESTER README
# ---------------------------------------------------------------------------
def semester_readme(sem):
    data = CD.SEMESTERS[sem]
    cs = data["courses"]
    tot = CD.total_ch(sem)
    o = [f"# الفصل الدراسي {sem} — السنة {data['year']} — الفصل {sem}\n"]
    o.append(f"> الفصل ده جزء من خطة 4 سنين / 8 فصول لمشروع بكالوريوس علوم الحاسب — "
             f"كلية الحاسبات والذكاء الاصطناعي، جامعة القاهرة.\n")
    o.append(f"- **المستوى:** {data['level_ar']}")
    o.append(f"- **عدد المقررات:** {len(cs)}")
    o.append(f"- **إجمالي الساعات:** {tot} ساعة معتمدة")
    o.append("- **عدد أسابيع التدريس:** 16 أسبوعًا (الأسبوع 8 ميدتيرم)")
    o.append("- **نهاية الفصل:** فترة امتحانات الفاينل\n")
    o.append("---\n")
    o.append("## المقررات\n")
    o.append("| الكود | اسم المقرر | الساعات | التقسيم | المقرر السابق |")
    o.append("|---|---|---|---|---|")
    for code, en, ar, ch, split, pre in cs:
        pre_s = " + ".join(pre) if pre else "لا يوجد"
        o.append(f"| {code} | {ar} | {ch} | ({split[0]}+{split[1]}+{split[2]}) | {pre_s} |")
    o.append(f"\n**مجموع ساعات الفصل: {tot} ساعة**\n")
    o.append("---\n")
    o.append("## التقويم الأسبوعي\n")
    o.append("| الأسبوع | المقررات والمواضيع |")
    o.append("|---|---|")
    for week in range(1, 17):
        if week == 8:
            o.append("| **8** | **أسبوع الميدتيرم** — امتحان الفصل الأول لكل مقرر. راجع `week-08-midterm.md`. |")
            continue
        if week in (7, 15, 16):
            o.append(f"| {week} | **مراجعة** — مراجعة كل مقررات الفصل وتجميع الملخصات وحل الأسئلة. |")
            continue
        idx = TEACH_WEEKS.index(week)
        parts = " <br> ".join(f"{c[0]}: {TOPICS[c[0]][idx][1]}" for c in cs)
        o.append(f"| {week} | {parts} |")
    o.append("\n> **الأسبوع 8** أسبوع الميدتيرم، ومراجعته بتغطي كل اللي اتشرح في الأسابيع 1 إلى 7.")
    o.append("> **الأسابيع 7 و 15 و 16** مراجعة عامة واستعداد للامتحانات.\n")
    o.append("---\n")
    o.append("## تقييم المقررات\n")
    o.append("| عنصر التقييم | الوزن |")
    o.append("|---|---|")
    o.append("| أعمال الفصل والمتابعة | 10% |")
    o.append("| تمارين وواجبات ومشاريع صغيرة | 20% |")
    o.append("| امتحان الفصل الأول (الميدتيرم) — الأسبوع 8 | 20% |")
    o.append("| امتحان آخر الفصل (الفاينل) | 50% |\n")
    o.append("### جدول الامتحانات\n")
    o.append("| الامتحان | التوقيت | المواضيع |")
    o.append("|---|---|---|")
    o.append("| ميدتيرم كل مقرر | الأسبوع 8 | الأسابيع 1 إلى 7 |")
    o.append("| فاينل كل مقرر | فترة الامتحانات بعد الأسبوع 16 | الأسابيع 1 إلى 16 |\n")
    o.append("تفاصيل أوراق الامتحانات والإجابات النموذجية في فولدر `exams/`.\n")
    o.append("---\n")
    o.append("## قواعد النجاح\n")
    o.append("- النجاح من درجة **50** وفوق.")
    o.append("- المعدل التراكمي بيتحسب من أوزان الرموز بمقياس 4.00 نقطة.")
    o.append("- لازم تحقق شرط كل مقرر قبل ما تسجّله.")
    o.append("- لو رسبت في مقرر هو شرط لمقرر تاني، هتتأخر فصل كامل في السلسلة دي.\n")
    o.append("---\n")
    o.append("## ملفات الفصل\n")
    o.append("| الملف | إيه فيه |")
    o.append("|---|---|")
    o.append("| `week-01.md` … `week-16.md` | دروس كل أسبوع |")
    o.append("| `week-08-midterm.md` | مراجعة أسبوع الميدتيرم |")
    o.append("| `exams/midterm-exam.md` | ورقة امتحان الميدتيرم |")
    o.append("| `exams/midterm-answers.md` | الإجابات النموذجية للميدتيرم |")
    o.append("| `exams/final-exam.md` | ورقة امتحان الفاينل |")
    o.append("| `exams/final-answers.md` | الإجابات النموذجية للفاينل |\n")
    o.append("[رجوع لنقطة البداية](../README.md)")
    return "\n".join(o)


def build_readmes():
    for sem in range(1, 9):
        w(f"study-plan/semester-{sem}/README.md", semester_readme(sem))
