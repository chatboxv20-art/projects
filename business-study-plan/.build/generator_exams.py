# -*- coding: utf-8 -*-
"""Exam papers and model answers for each semester."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import curriculum_data as CD
import generator as G
from generator_build import w, courses, ORD_AR, TOPICS, AR_LABEL, TEACH_WEEKS


def midterm_exam(sem):
    cs = courses(sem)
    codes = "، ".join(c[0] for c in cs)
    o = [f"# امتحان الفصل الأول (الميدتيرم) — الفصل {sem}\n"]
    o.append(f"- **المقررات الممتحَنة:** {codes}")
    o.append("- **المدة:** ساعتان لكل مقرر")
    o.append("- **المجموع:** 40 درجة لكل مقرر (الوزن 20% من نتيجة المقرر)")
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
        for t_en, t_ar in TOPICS[code][:2]:
            n += 1
            o.append(f"**{n}.** إيه أنسب وصف لدور **{t_ar}** في مقرر **{ar}**؟ _(مقرر {code})_\n")
            o.append(f"   - أ) أداة شغّالة جوه {d['name_ar']} بتدعم قرارات حقيقية")
            o.append("   - ب) تعريف شكلي بدون تطبيق عملي")
            o.append("   - ج) مفهوم نظري مالوش استخدام مباشر")
            o.append("   - د) موضوع من مجال دراسي آخر تمامًا\n")
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
        for t_en, t_ar in TOPICS[code][:2]:
            n += 1
            o.append(f"**{n}.** الإجابة **أ** _(مقرر {code})_\n")
            o.append(f"دور {t_ar} مرتبط مباشرة بأنه أداة شغّالة جوه {d['name_ar']} بتدعم قرارات حقيقية. "
                     f"الاختيار الصحيح بيوصّف الوظيفة الحقيقية للموضوع، أما باقي الاختيارات فبتوصّفه "
                     f"كإنه شكلي أو نظري بلا استخدام أو من مجال آخر، وده يخالف بلوك التعريف وبلوك الاستخدام في الدرس.\n")
    o.append("---\n")
    o.append("## القسم الثاني: إجابات الأسئلة القصيرة\n")
    n = 0
    for c in cs:
        code, en, ar, ch, split, pre = c
        d = G.domain_of(code)
        t_en, t_ar = TOPICS[code][2]
        n += 1
        o.append(f"**{n}.** الفكرة الأساسية لـ{t_ar} إنه {d['what_ar']} "
                 f"والميزة إنه {d['adv_ar'][0]}، والحد إنه {d['lim_ar'][0]}. "
                 f"والإجابة الكاملة لازم تشمل الفكرة والميزة والحد مع سبب كل واحدة.\n")
    o.append("---\n")
    o.append("## القسم الثالث: الحل النموذجي للمسائل\n")
    n = 0
    for c in cs:
        code, en, ar, ch, split, pre = c
        d = G.domain_of(code)
        t_en, t_ar = TOPICS[code][3]
        n += 1
        o.append(f"**{n}.** الحل لازم يغطي أربع خطوات: أولًا وصف الموقف بدقة، ثانيًا تحليل الوضع "
                 f"بأرقام أو حقائق، ثالثًا توصية مبنية على التحليل، ورابعًا خطر واحد على الأقل مع خطة لمراقبته.\n")
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
    o.append("- **المجموع:** 100 درجة لكل مقرر (الوزن 50% من نتيجة المقرر)")
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
        for wi in (9, 11):
            t_en, t_ar = TOPICS[code][TEACH_WEEKS.index(wi)]
            n += 1
            o.append(f"**{n}.** إيه أنسب وصف لدور **{t_ar}** في مقرر **{ar}**؟ _(مقرر {code})_\n")
            o.append(f"   - أ) أداة شغّالة جوه {d['name_ar']} بتدعم قرارات حقيقية")
            o.append("   - ب) تعريف شكلي بدون تطبيق عملي")
            o.append("   - ج) مفهوم نظري مالوش استخدام مباشر")
            o.append("   - د) موضوع من مجال دراسي آخر تمامًا\n")
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
        for wi in (9, 11):
            t_en, t_ar = TOPICS[code][TEACH_WEEKS.index(wi)]
            n += 1
            o.append(f"**{n}.** الإجابة **أ** _(مقرر {code})_\n")
            o.append(f"دور {t_ar} مرتبط مباشرة بأنه أداة شغّالة جوه {d['name_ar']}. "
                     f"الاختيار الصحيح بيوصّف الوظيفة الحقيقية للموضوع، أما باقي الاختيارات فبتوصّفه "
                     f"كإنه شكلي أو نظري بلا استخدام أو من مجال آخر.\n")
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
        o.append(f"**{n}.** الحل لازم يشمل: وصف الموقف، والتحليل بالأرقام، والقرار الموصى بيه، "
                 f"وبديل واحد على الأقل مع سبب استبعاده. درجات كل خطوة محسوبة منفصلة.\n")
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
