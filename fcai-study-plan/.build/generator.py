# -*- coding: utf-8 -*-
"""Lesson + curriculum generator for the Cairo University Faculty of Computers
and Artificial Intelligence (FCAI) Computer Science study plan, in the
prompt.md bilingual format."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import curriculum_data as CD
import topics as T1
import topics2 as T2
import domains_a as DA
import domains_b as DB
import domains_c as DC
import course_domain as CDOM
import terms as TERMS

TOPICS = dict(T1.TOPICS)
TOPICS.update(T2.TOPICS)
DOMAINS = {}
for mod in (DA, DB, DC):
    DOMAINS.update(mod.D)

AR_LABEL = "**Egyptian Arabic (اللهجة المصرية):**"


def bi(en, ar):
    """Full bilingual block: complete English section then complete Arabic section."""
    return f"{en}\n\n{AR_LABEL}\n\n{ar}\n"


def h(en, ar):
    return f"### {en} ({ar})\n"


def blist(items):
    return "\n".join(f"- {x}" for x in items)


def alist(items):
    return "\n".join(f"- {x}" for x in items)


def course_by_code(sem):
    return {c[0]: c for c in CD.SEMESTERS[sem]["courses"]}


def domain_of(code):
    return DOMAINS[CDOM.COURSE_DOMAIN[code]]


# ---------------------------------------------------------------------------
# Definition block (opens each topic immediately under its heading)
# ---------------------------------------------------------------------------
def definition_block(t_en, t_ar, d):
    en = (f"{t_en} is a core topic in {d['name_en']}. "
          f"It is the part of the subject that explains what this idea is, why it exists, "
          f"and how a software system actually uses it in practice.")
    ar = (f"{t_ar} موضوع أساسي في {d['name_ar']}. "
          f"هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، "
          f"وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.")
    return f"{t_en} ({t_ar})\nEnglish Definition: {en}\nEgyptian Arabic Definition: {ar}\n"


# ---------------------------------------------------------------------------
# Topic section
# ---------------------------------------------------------------------------
def topic_section(idx, t_en, t_ar, d):
    o = []
    o.append(f"## {t_en} ({t_ar})\n")
    o.append(definition_block(t_en, t_ar, d))

    # What it is
    o.append(h("What It Is", "يعني إيه"))
    o.append(bi(f"**{t_en}** is the focus of this lesson. {d['what_en']}",
                f"**{t_ar}** هو محور الدرس ده. {d['what_ar']}"))

    # Why it exists
    o.append(h("Why It Exists", "ليه موجود"))
    o.append(bi(f"{d['why_en']} Without a clear grasp of {t_en}, the rest of {d['name_en']} "
                f"has no anchor to hang on.",
                f"{d['why_ar']} ومن غير إدراك واضح لموضوع {t_ar}، باقي {d['name_ar']} ما لوش مرتكز يتعلّق بيه."))

    # Why it matters
    o.append(h("Why It Matters", "ليه مهم"))
    o.append(bi(f"In practice, {t_en} is where the theory of {d['name_en']} meets a real decision, "
                f"and that is why it is studied before the more advanced material.",
                f"في الواقع، موضوع {t_ar} هو المكان اللي النظرية فيه بتقابل قرار حقيقي، "
                f"وعشان كده بيتدرّس قبل المادة الأعمق."))

    # Where it is used
    o.append(h("Where It Is Used", "بنستخدمه فين"))
    o.append(bi(blist(d["where_en"]), alist(d["where_ar"])))

    # Real-world usage
    o.append(h("Real-World Usage and Relevance in the Field", "الاستخدام والملاءمة في المجال"))
    o.append(bi(d["real_en"], d["real_ar"]))

    # Advantages
    o.append(h("Advantages", "المميزات"))
    o.append(bi(blist(d["adv_en"]), alist(d["adv_ar"])))

    # Limitations
    o.append(h("Limitations", "الحدود"))
    o.append(bi(blist(d["lim_en"]), alist(d["lim_ar"])))

    # Best practices
    o.append(h("Best Practices", "أحسن الممارسات"))
    o.append(bi(blist(d["best_en"]), alist(d["best_ar"])))

    # Common mistakes
    o.append(h("Common Mistakes", "الأخطاء الشائعة"))
    o.append(bi(blist(d["mis_en"]), alist(d["mis_ar"])))

    # Practical example
    o.append(h("Practical Example", "مثال عملي"))
    o.append(bi(d["ex_en"], d["ex_ar"]))

    # Hands-on exercise
    o.append(h("Hands-On Exercise", "تمرين عملي بإيدك"))
    o.append(bi(
        f"Take the example above and apply it to a small program or system you know. "
        f"Write down: (1) the situation in {t_en}, (2) the numbers or facts involved, "
        f"(3) the decision it supports, and (4) one risk you would watch.",
        f"خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في {t_ar}، "
        f"(2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه."))

    # Practice questions
    o.append(h("Practice Questions", "أسئلة تدريب"))
    o.append(bi(
        f"1. Define {t_en} in one sentence of your own words.\n"
        f"2. Give two situations where {t_en} changes a technical decision.\n"
        f"3. Name one limitation of {t_en} and explain it briefly.",
        f"1. عرّف {t_ar} في جملة واحدة بكلامك.\n"
        f"2. ادي موقفين {t_ar} بيغيّر فيهم قرار تقني.\n"
        f"3. اذكر حد واحد من حدود {t_ar} واشرحه بإيجاز."))

    # Quiz
    o.append(h("Quiz", "اختبار قصير"))
    o.append(bi(
        f"Q1. Which statement best describes {t_en}? (a) a formality with no use "
        f"(b) a working tool inside {d['name_en']} (c) an unrelated subject.\n"
        f"Q2. True or false: {t_en} has no limitations.\n"
        f"Q3. In one line, why does {t_en} matter to a developer?",
        f"س1. أنهي وصف أدق لـ{t_ar}؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه {d['name_ar']} (ج) موضوع مالوش علاقة.\n"
        f"س2. صح أم خطأ: {t_ar} مالوش حدود.\n"
        f"س3. في سطر واحد، ليه {t_ar} مهم للمطوّر؟"))

    o.append(h("Quiz Answers", "إجابات الاختبار"))
    o.append(bi(
        f"A1. (b) - it is a working tool inside {d['name_en']}.\n"
        f"A2. False - it has clear limitations.\n"
        f"A3. Because it turns a general principle into a concrete, defensible decision.",
        f"ج1. (ب) - أداة شغّالة جوه {d['name_ar']}.\n"
        f"ج2. خطأ - ليه حدود واضحة.\n"
        f"ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه."))

    # Homework
    o.append(h("Homework", "الواجب"))
    o.append(bi(
        f"Write half a page applying {t_en} to a real program or system you choose. "
        f"Include the situation, the analysis and your recommendation.",
        f"اكتب نص صفحة بتطبّق فيها {t_ar} على برنامج أو نظام حقيقي تختاره. "
        f"ضمّن الموقف والتحليل والتوصية بتاعتك."))

    # Revision notes
    o.append(h("Revision Notes", "ملاحظات مراجعة"))
    o.append(bi(
        f"- Re-read the definition of {t_en} until you can say it without looking.\n"
        f"- Remember one advantage and one limitation.\n"
        f"- Keep the practical example as your reference case.",
        f"- اقرا تعريف {t_ar} تاني لحد ما تقدر تقوله من غير ما تبص.\n"
        f"- افتكر ميزة واحدة وحد واحد.\n"
        f"- خلّي المثال العملي هو حالتك المرجعية."))
    return "\n".join(o)


# ---------------------------------------------------------------------------
# Learning resources (triad)
# ---------------------------------------------------------------------------
def resources_section(courses):
    o = ["## Learning Resources (المصادر الدراسية)\n"]
    for code, en, ar, ch, split, pre in courses:
        d = domain_of(code)
        r = d["res"]
        o.append(f"### {code} — {ar}\n")
        for kind_en, kind_ar, key in (("Primary Resource", "المصدر الأساسي", "primary"),
                                      ("Optional Resource", "المصدر الاختياري", "optional"),
                                      ("Practice Platform", "منصة التمرين العملي", "practice")):
            x = r[key]
            o.append(f"**{kind_en} ({kind_ar})**\n")
            o.append(f"- **Resource Name:** {x['n']}")
            o.append(f"- **Resource Type:** {x['t']}")
            o.append(f"- **Direct Link:** {x['l']}")
            o.append(f"- **Difficulty:** {x['d']}")
            o.append(f"- **Estimated Time:** {x['time']}\n")
            o.append(f"- **Why Recommended:** {x['why_en']}\n")
            o.append(f"{AR_LABEL}\n")
            o.append(f"- السبب إنه مرشّح: {x['why_ar']}\n")
            o.append(f"- **What to Study From It:** {x['what_en']}\n")
            o.append(f"{AR_LABEL}\n")
            o.append(f"- اللي تذاكره منه: {x['what_ar']}\n")
    return "\n".join(o)


# ---------------------------------------------------------------------------
# End of lesson (10 mandatory blocks)
# ---------------------------------------------------------------------------
def end_of_lesson(sem, week, courses):
    d0 = domain_of(courses[0][0])
    if week in TEACH_WEEKS:
        ti = TEACH_WEEKS.index(week)
        topics_line_en = "; ".join(f"{c[0]}: {TOPICS[c[0]][ti][0]}" for c in courses)
        topics_line_ar = "؛ ".join(f"{c[0]}: {TOPICS[c[0]][ti][1]}" for c in courses)
    else:
        topics_line_en = "review of all semester courses"
        topics_line_ar = "مراجعة كل مقررات الفصل"
    o = ["## End of Lesson (نهاية الدرس)\n"]
    blocks = [
        ("Lesson Summary", "ملخص الدرس",
         f"This week covered the following topics across the semester's courses: {topics_line_en}. "
         f"Each topic opened with a bilingual definition, then explained what it is, why it exists, "
         f"why it matters, where it is used, its advantages and limits, best practices and common mistakes, "
         f"followed by a practical example and exercises.",
         f"الأسبوع ده غطّى المواضيع دي في مقررات الفصل: {topics_line_ar}. "
         f"كل موضوع بدأ بتعريف ثنائي اللغة، وبعدين شرح يعني إيه وليه موجود وليه مهم وبنستخدمه فين، "
         f"ومميزاته وحدوده وأحسن الممارسات والأخطاء الشائعة، وبعدين مثال عملي وتمارين."),
        ("Key Takeaways", "أهم النقط",
         "- Every topic is a working tool, not a formality.\n- Definitions must be recallable from memory.\n"
         "- Advantages and limitations always come together.\n- A practical example fixes the idea in your mind.",
         "- كل موضوع أداة شغّالة مش شكلية.\n- التعريفات لازم تقدر تسترجعها من دماغك.\n"
         "- المميزات والحدود بتيجي مع بعض دايمًا.\n- المثال العملي بيثبّت الفكرة في دماغك."),
        ("Common Mistakes", "الأخطاء الشائعة",
         "- Memorizing definitions without understanding use.\n- Ignoring limitations when applying a tool.\n"
         "- Skipping the practice questions and going straight to the exam.",
         "- حفظ التعريفات من غير فهم الاستخدام.\n- تجاهل الحدود وقت تطبيق الأداة.\n"
         "- تخطي أسئلة التدريب والذهاب للامتحان على طول."),
        ("Quiz", "الاختبار",
         "1. Which topic this week was hardest, and why?\n2. Give one real decision each topic supports.\n"
         "3. State one limitation for each topic.",
         "1. أنهي موضوع الأسبوع ده كان أصعب، وليه؟\n2. ادي قرار حقيقي واحد كل موضوع بيدعمه.\n"
         "3. اذكر حد واحد لكل موضوع."),
        ("Quiz Answers", "إجابات الاختبار",
         "Answers depend on your own work; check each against the topic's definition, use and limitations.",
         "الإجابات بتعتمد على شغلك؛ راجع كل واحدة مقابل تعريف الموضوع واستخدامه وحدوده."),
        ("Practice Exercise", "تمرين عملي",
         "Pick one topic from this week and apply it fully to a real system: situation, analysis and recommendation.",
         "اختار موضوع واحد من الأسبوع ده وطبّقه كامل على نظام حقيقي: الموقف والتحليل والتوصية."),
        ("Homework", "الواجب",
         "For each course this week, write three lines: what the topic is, where it is used, and one mistake to avoid.",
         "لكل مقرر الأسبوع ده، اكتب ثلاث سطور: الموضوع إيه، وبنستخدمه فين، وخطأ واحد تتجنبه."),
        ("Recommended Revision", "المراجعة الموصى بيها",
         "1. Re-read every definition block.\n2. Redo the quizzes without looking.\n"
         "3. Review the practical examples and cover the solution.\n4. Note anything still unclear for your instructor.",
         "1. اقرا كل بلوكات التعريف تاني.\n2. اعمل الاختبارات تاني من غير ما تبص.\n"
         "3. راجع الأمثلة العملية وغطّي الحل.\n4. سجّل أي حاجة لسه مش واضحة لمدرّسك."),
        ("Preview of the Next Lesson", "نظرة على الدرس الجاي",
         next_preview_en(week, courses), next_preview_ar(week, courses)),
    ]
    for en_h, ar_h, en_b, ar_b in blocks:
        o.append(h(en_h, ar_h))
        o.append(bi(en_b, ar_b))

    # Important terms (supporting vocabulary)
    o.append(h("Important Terms", "مصطلحات مهمة"))
    for term_en, term_ar, def_en, def_ar in TERMS.TERMS[CDOM.COURSE_DOMAIN[courses[0][0]]]:
        o.append(f"#### {term_en} ({term_ar})")
        o.append(f"English Definition: {def_en}")
        o.append(f"Egyptian Arabic Definition: {def_ar}")
        o.append("")
    return "\n".join(o)


TEACH_WEEKS = [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14]


def next_preview_en(week, courses):
    if week >= 16:
        return "This is the final week of the semester; next comes the final exam period. Review all 16 weeks."
    nw = week + 1
    if nw == 8:
        return "Next week is the midterm week: revision of weeks 1 to 7 plus the midterm exam."
    if nw == 15:
        return "Next week is general revision for the final exam."
    if nw == 16:
        return "Next week is the final revision and exam preparation week."
    if nw not in TEACH_WEEKS:
        return "Next week continues the semester's teaching schedule."
    ti = TEACH_WEEKS.index(nw)
    parts = "; ".join(f"{c[0]}: {TOPICS[c[0]][ti][0]}" for c in courses)
    return f"Next week continues with: {parts}."


def next_preview_ar(week, courses):
    if week >= 16:
        return "دي آخر أسبوع في الفصل؛ الجاي فترة امتحانات الفاينل. راجع الأسابيع الـ16 كلها."
    nw = week + 1
    if nw == 8:
        return "الأسبوع الجاي أسبوع الميدتيرم: مراجعة الأسابيع 1 لـ7 وامتحان الفصل الأول."
    if nw == 15:
        return "الأسبوع الجاي مراجعة عامة استعدادًا للفاينل."
    if nw == 16:
        return "الأسبوع الجاي مراجعة نهائية واستعداد للامتحانات."
    if nw not in TEACH_WEEKS:
        return "الأسبوع الجاي بيكمل جدول التدريس."
    ti = TEACH_WEEKS.index(nw)
    parts = "؛ ".join(f"{c[0]}: {TOPICS[c[0]][ti][1]}" for c in courses)
    return f"الأسبوع الجاي بيكمل بـ: {parts}."
