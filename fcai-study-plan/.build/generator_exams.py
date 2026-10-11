# -*- coding: utf-8 -*-
"""Exam papers and model answers for each semester."""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import curriculum_data as CD
import generator as G
from generator_build import w, courses, ORD_AR, TOPICS, AR_LABEL, TEACH_WEEKS

OPT_LABELS = ["أ", "ب", "ج", "د"]


def _mcq(code, q_index, d, t_ar):
    """Deterministic MCQ: shuffle options so the correct answer varies by question."""
    correct = f"أداة شغّالة جوه {d['name_ar']} بتدعم قرارات حقيقية"
    opts = [
        correct,
        "تعريف شكلي بدون تطبيق عملي",
        "مفهوم نظري مالوش استخدام مباشر",
        "موضوع من مجال دراسي آخر تمامًا",
    ]
    rnd = random.Random(f"{code}:{q_index}")
    rnd.shuffle(opts)
    return opts, opts.index(correct)


def _mcq_question(n, code, ar, t_ar, d, q_index):
    opts, _ = _mcq(code, q_index, d, t_ar)
    o = [f"**{n}.** إيه أنسب وصف لدور **{t_ar}** في مقرر **{ar}**؟ _(مقرر {code})_\n"]
    for i, text in enumerate(opts):
        o.append(f"   - {OPT_LABELS[i]}) {text}")
    o.append("")
    return "\n".join(o)


def _mcq_answer(n, code, t_ar, d, q_index):
    opts, ci = _mcq(code, q_index, d, t_ar)
    correct = opts[ci]
    o = [f"**{n}.** الإجابة **{OPT_LABELS[ci]}** _(مقرر {code})_\n"]
    o.append(f"دور {t_ar} مرتبط مباشرة بأنه {correct}، لأن {d['name_ar']} "
             f"بتستخدمه فعلًا وقت القرار مش كتعريف شكلي. "
             f"الاختيارات التانية بتوصّفه كإنه نظري بلا استخدام أو من مجال تاني، "
             f"وده يخالف بلوك التعريف وبلوك الاستخدام في الدرس.\n")
    return "\n".join(o)


def midterm_exam(sem):
    cs = courses(sem)
    codes = "، ".join(c[0] for c in cs)
    o = [f"# امتحان الفصل الأول (الميدتيرم) — الفصل {sem}\n"]
    o.append(f"- **المقررات الممتحَنة:** {codes}")
    o.append("- **المدة:** ساعتان لكل مقرر")
    o.append("- **المجموع:** 84 درجة للورقة (الوزن 20% من نتيجة كل مقرر)")
    o.append("- **النطاق:** الأسابيع 1 إلى 7")
    o.append("- **الكتاب:** مغلق (يُسمح بآلة حاسبة علمية غير قابلة للبرمجة)")
    o.append("- **التعليمات:** اقرا السؤال كاملًا قبل البدء، واكتب الخطوات، ولا تترك سؤالًا "
             "بدون إجابة — درجات الخطوات محسوبة.\n")
    o.append("---\n")
    o.append("## القسم الأول: أسئلة الاختيار من متعدد\n")
    o.append("**اختر الإجابة الصحيحة الواحدة. كل سؤال بدرجتين.**\n")
    n = 0
    for c in cs:
        code, en, ar, ch, split, pre = c
        d = G.domain_of(code)
        for j, (t_en, t_ar) in enumerate(TOPICS[code][:2]):
            n += 1
            o.append(_mcq_question(n, code, ar, t_ar, d, j))
    o.append("**مجموع القسم: 24 درجة**\n")
    o.append("---\n")
    o.append("## القسم الثاني: أسئلة قصيرة\n")
    o.append("**أجب بإيجاز ودقة.**\n")
    n = 0
    for c in cs:
        code, en, ar, ch, split, pre = c
        t_en, t_ar = TOPICS[code][2]
        n += 1
        o.append(f"**{n}.** اشرح الفكرة الأساسية لـ**{t_ar}**، واذكر ميزة واحدة وحدًّا واحدًا له. "
                 f"_(مقرر {code})_  **(4 درجات)**\n")
    o.append("**مجموع القسم: 24 درجة**\n")
    o.append("---\n")
    o.append("## القسم الثالث: مسائل وتطبيقات\n")
    o.append("**حلّ بالخطوات كاملة، وبرّر كل خطوة.**\n")
    n = 0
    for c in cs:
        code, en, ar, ch, split, pre = c
        t_en, t_ar = TOPICS[code][3]
        n += 1
        o.append(f"**{n}.** طبّق **{t_ar}** على حالة عمل حقيقية: اكتب الموقف، والتحليل، "
                 f"والتوصية، وأي خطر تراقبه. _(مقرر {code})_  **(6 درجات)**\n")
    o.append("**مجموع القسم: 36 درجة**\n")
    o.append("---\n")
    o.append("## توزيع الدرجات\n")
    o.append("| القسم | الدرجة |")
    o.append("|---|---|")
    o.append("| أسئلة الاختيار من متعدد | 24 |")
    o.append("| الأسئلة القصيرة | 24 |")
    o.append("| المسائل والتطبيقات | 36 |")
    o.append("| **المجموع** | **84** |\n")
    o.append("فترة الامتحان: راجع الجدول في `../README.md`. الإجابات النموذجية في الملف المرافق بنفس الاسم مع كلمة answers.")
    return "\n".join(o)


def midterm_answers(sem):
    cs = courses(sem)
    o = [f"# الإجابات النموذجية — الميدتيرم الفصل {sem}\n"]
    o.append("> الإجابات دي بتوضّح الخطوات اللي بيتم على أساسها توزيع الدرجات، مش النتيجة النهائية بس.\n")
    o.append("---\n")
    o.append("## القسم الأول: إجابات الاختيار من متعدد\n")
    n = 0
    for c in cs:
        code, en, ar, ch, split, pre = c
        d = G.domain_of(code)
        for j, (t_en, t_ar) in enumerate(TOPICS[code][:2]):
            n += 1
            o.append(_mcq_answer(n, code, t_ar, d, j))
    o.append("---\n")
    o.append("## القسم الثاني: إجابات الأسئلة القصيرة\n")
    n = 0
    for c in cs:
        code, en, ar, ch, split, pre = c
        d = G.domain_of(code)
        t_en, t_ar = TOPICS[code][2]
        n += 1
        o.append(f"**{n}.** الفكرة الأساسية لـ{t_ar} إنه {d['what_ar']} "
                 f"وأهم ميزة إنه {d['adv_ar'][0]}، وأهم حد إنه {d['lim_ar'][0]}. "
                 f"والإجابة الكاملة لازم تشمل الفكرة والميزة والحد، كل واحدة بسببه.\n")
    o.append("---\n")
    o.append("## القسم الثالث: الحل النموذجي للمسائل\n")
    n = 0
    for c in cs:
        code, en, ar, ch, split, pre = c
        d = G.domain_of(code)
        t_en, t_ar = TOPICS[code][3]
        n += 1
        o.append(f"**{n}.** الحل لازم يغطي أربع خطوات مترابطة: أولًا وصف الموقف في {t_ar} بدقة، "
                 f"ثانيًا تحليل الوضع بأرقام أو حقائق من {d['name_ar']}، "
                 f"ثالثًا توصية مبنية على التحليل، ورابعًا خطر واحد على الأقل مع خطة لمراقبته.\n")
    o.append("---\n")
    o.append("## قواعد التصحيح\n")
    o.append("- **الاختيار من متعدد:** الدرجة كاملة للإجابة الصحيحة فقط، مافيش درجة جزئية.")
    o.append("- **الأسئلة القصيرة:** الدرجة بتتوزّع على عناصر الإجابة المطلوبة.")
    o.append("- **المسائل:** درجات الخطوات محسوبة، والنتيجة بدون خطوات تفقد معظم الدرجة.")
    o.append("- **الوحدات والأرقام:** نقص الوحدة أو الخطأ فيها بيخصم.")
    return "\n".join(o)


def final_exam(sem):
    cs = courses(sem)
    codes = "، ".join(c[0] for c in cs)
    o = [f"# امتحان آخر الفصل (الفاينل) — الفصل {sem}\n"]
    o.append(f"- **المقررات الممتحَنة:** {codes}")
    o.append("- **المدة:** ثلاث ساعات لكل مقرر")
    o.append("- **المجموع:** 96 درجة للورقة (الوزن 50% من نتيجة كل مقرر)")
    o.append("- **النطاق:** الأسابيع 1 إلى 16، مع تركيز أكبر على الأسابيع 9 إلى 16")
    o.append("- **الكتاب:** مغلق (يُسمح بآلة حاسبة علمية غير قابلة للبرمجة)")
    o.append("- **التعليمات:** اقرا السؤال كاملًا، واكتب الخطوات، وبرّر كل إجابة.\n")
    o.append("---\n")
    o.append("## القسم الأول: أسئلة الاختيار من متعدد\n")
    o.append("**اختر الإجابة الصحيحة الواحدة. كل سؤال بدرجتين.**\n")
    n = 0
    for c in cs:
        code, en, ar, ch, split, pre = c
        d = G.domain_of(code)
        for j, wi in enumerate((9, 11)):
            t_en, t_ar = TOPICS[code][TEACH_WEEKS.index(wi)]
            n += 1
            o.append(_mcq_question(n, code, ar, t_ar, d, 100 + j))
    o.append("**مجموع القسم: 24 درجة**\n")
    o.append("---\n")
    o.append("## القسم الثاني: أسئلة قصيرة\n")
    o.append("**أجب بإيجاز ودقة.**\n")
    n = 0
    for c in cs:
        code, en, ar, ch, split, pre = c
        t_en, t_ar = TOPICS[code][8]
        n += 1
        o.append(f"**{n}.** اشرح **{t_ar}** واذكر تطبيقًا واقعيًا واحدًا له. _(مقرر {code})_  **(4 درجات)**\n")
    o.append("**مجموع القسم: 24 درجة**\n")
    o.append("---\n")
    o.append("## القسم الثالث: مسائل وتطبيقات\n")
    o.append("**حلّ بالخطوات كاملة، وبرّر كل خطوة.**\n")
    n = 0
    for c in cs:
        code, en, ar, ch, split, pre = c
        t_en, t_ar = TOPICS[code][11]
        n += 1
        o.append(f"**{n}.** حلّل حالة عمل باستخدام **{t_ar}**: الموقف، والتحليل بالأرقام، "
                 f"والقرار، وبديل واحد كنت هتفكر فيه. _(مقرر {code})_  **(8 درجات)**\n")
    o.append("**مجموع القسم: 48 درجة**\n")
    o.append("---\n")
    o.append("## توزيع الدرجات\n")
    o.append("| القسم | الدرجة |")
    o.append("|---|---|")
    o.append("| أسئلة الاختيار من متعدد | 24 |")
    o.append("| الأسئلة القصيرة | 24 |")
    o.append("| المسائل والتطبيقات | 48 |")
    o.append("| **المجموع** | **96** |\n")
    o.append("فترة الامتحان: راجع الجدول في `../README.md`. الإجابات النموذجية في الملف المرافق.")
    return "\n".join(o)


def final_answers(sem):
    cs = courses(sem)
    o = [f"# الإجابات النموذجية — الفاينل الفصل {sem}\n"]
    o.append("> الإجابات دي بتوضّح الخطوات اللي بيتم على أساسها توزيع الدرجات.\n")
    o.append("---\n")
    o.append("## القسم الأول: إجابات الاختيار من متعدد\n")
    n = 0
    for c in cs:
        code, en, ar, ch, split, pre = c
        d = G.domain_of(code)
        for j, wi in enumerate((9, 11)):
            t_en, t_ar = TOPICS[code][TEACH_WEEKS.index(wi)]
            n += 1
            o.append(_mcq_answer(n, code, t_ar, d, 100 + j))
    o.append("---\n")
    o.append("## القسم الثاني: إجابات الأسئلة القصيرة\n")
    n = 0
    for c in cs:
        code, en, ar, ch, split, pre = c
        d = G.domain_of(code)
        t_en, t_ar = TOPICS[code][8]
        n += 1
        o.append(f"**{n}.** {t_ar} {d['what_ar']} وتطبيقه الواقعي إن {d['real_ar']} "
                 f"والإجابة الكاملة لازم تشمل التعريف والتطبيق مع مثال.\n")
    o.append("---\n")
    o.append("## القسم الثالث: الحل النموذجي للمسائل\n")
    n = 0
    for c in cs:
        code, en, ar, ch, split, pre = c
        d = G.domain_of(code)
        t_en, t_ar = TOPICS[code][11]
        n += 1
        o.append(f"**{n}.** الحل لازم يشمل: وصف الموقف في {t_ar}، والتحليل بالأرقام من "
                 f"{d['name_ar']}، والقرار الموصى بيه، وبديل واحد على الأقل مع سبب استبعاده. "
                 f"درجات كل خطوة محسوبة منفصلة.\n")
    o.append("---\n")
    o.append("## قواعد التصحيح\n")
    o.append("- **الاختيار من متعدد:** الدرجة كاملة للإجابة الصحيحة فقط، مافيش درجة جزئية.")
    o.append("- **الأسئلة القصيرة:** الدرجة بتتوزّع على عناصر الإجابة المطلوبة.")
    o.append("- **المسائل:** درجات الخطوات محسوبة، والنتيجة بدون خطوات تفقد معظم الدرجة.")
    return "\n".join(o)


def build_exams():
    for sem in range(1, 9):
        w(f"study-plan/semester-{sem}/exams/midterm-exam.md", midterm_exam(sem))
        w(f"study-plan/semester-{sem}/exams/midterm-answers.md", midterm_answers(sem))
        w(f"study-plan/semester-{sem}/exams/final-exam.md", final_exam(sem))
        w(f"study-plan/semester-{sem}/exams/final-answers.md", final_answers(sem))
