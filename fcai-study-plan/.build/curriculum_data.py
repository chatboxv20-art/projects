# -*- coding: utf-8 -*-
"""Single source of truth for the Cairo University Faculty of Computers and
Artificial Intelligence (FCAI) 4-year / 8-semester Computer Science study plan.

Each course: (code, english_title, arabic_title, credit_hours, split, prereq)
split = (lecture, tutorial, practical)
prereq = list of prerequisite course codes (or free text)
"""

FACULTY_AR = "كلية الحاسبات والذكاء الاصطناعي — جامعة القاهرة"
FACULTY_EN = ("Faculty of Computers and Artificial Intelligence (FCAI), "
              "Cairo University")
TRACK_AR = "مسار علوم الحاسب (Computer Science)"
TRACK_EN = "Computer Science track"

# ---------------------------------------------------------------------------
# ELECTIVES (labels only; the actual elective courses are listed per semester)
# ---------------------------------------------------------------------------
ELECTIVES = {
    "ELEC-DS": "علم البيانات وتحليل البيانات الضخمة",
    "ELEC-CY": "الأمن السيبراني",
    "ELEC-MOBILE": "تطوير تطبيقات الموبايل",
    "ELEC-GAME": "تطوير الألعاب",
    "ELEC-IOT": "إنترنت الأشياء",
    "ELEC-BC": "البلوكشين والتقنية المالية",
    "ELEC-ROBO": "الروبوتات",
    "ELEC-HPC": "الحوسبة عالية الأداء",
}

C1 = (2, 1, 0)   # standard 3-CH split: 2 lecture + 1 tutorial
C2 = (2, 0, 1)   # 3-CH split with a lab hour
C3 = (2, 1, 2)   # 3-CH split with two practical hours
C4 = (1, 1, 0)   # 2-CH split: 1 lecture + 1 tutorial
C5 = (2, 0, 0)   # 2-CH lecture-only split

SEMESTERS = {
    1: {
        "year": 1, "level_ar": "المستوى الأول — Freshman", "total": 17,
        "courses": [
            ("CS111", "Fundamentals of Computer Science", "أساسيات علوم الحاسب", 3, C1, []),
            ("CS112", "Introduction to Programming", "مقدمة في البرمجة", 3, C3, []),
            ("MATH101", "Calculus I", "التفاضل والتكامل 1", 3, C1, []),
            ("MATH102", "Discrete Mathematics", "الرياضيات المتقطعة", 3, C1, []),
            ("PHYS101", "Physics I", "الفيزياء 1", 3, C2, []),
            ("ENG101", "English Language I", "اللغة الإنجليزية 1", 2, C4, []),
        ],
    },
    2: {
        "year": 1, "level_ar": "المستوى الأول — Freshman", "total": 17,
        "courses": [
            ("CS113", "Object-Oriented Programming", "البرمجة كائنية التوجه", 3, C3, ["CS112"]),
            ("CS114", "Data Structures", "هياكل البيانات", 3, C1, ["CS112"]),
            ("MATH103", "Linear Algebra", "الجبر الخطي", 3, C1, ["MATH101"]),
            ("MATH104", "Probability and Statistics", "الاحتمالات والإحصاء", 3, C1, ["MATH101"]),
            ("PHYS102", "Physics II", "الفيزياء 2", 3, C2, ["PHYS101"]),
            ("ENG102", "English Language II", "اللغة الإنجليزية 2", 2, C4, ["ENG101"]),
        ],
    },
    3: {
        "year": 2, "level_ar": "المستوى الثاني — Sophomore", "total": 17,
        "courses": [
            ("CS211", "Design and Analysis of Algorithms", "تصميم وتحليل الخوارزميات", 3, C1, ["CS114", "MATH102"]),
            ("CS212", "Computer Organization and Assembly Language", "تنظيم الحاسب ولغة التجميع", 3, C2, ["CS111"]),
            ("CS213", "Database Systems", "نظم قواعد البيانات", 3, C1, ["CS114"]),
            ("MATH201", "Calculus II and Numerical Methods", "التفاضل والتكامل 2 والأساليب العددية", 3, C1, ["MATH101"]),
            ("IS201", "Introduction to Information Systems", "مقدمة في نظم المعلومات", 3, C1, ["CS111"]),
            ("ENG201", "Technical Writing and Communication", "الكتابة الفنية والتواصل", 2, C4, ["ENG102"]),
        ],
    },
    4: {
        "year": 2, "level_ar": "المستوى الثاني — Sophomore", "total": 17,
        "courses": [
            ("CS214", "Operating Systems", "نظم التشغيل", 3, C1, ["CS212"]),
            ("CS215", "Theory of Computation", "نظرية الحسابات", 3, C1, ["MATH102"]),
            ("CS216", "Software Engineering", "هندسة البرمجيات", 3, C1, ["CS113"]),
            ("CS217", "Computer Networks", "شبكات الحاسب", 3, C1, ["CS212"]),
            ("AI201", "Introduction to Artificial Intelligence", "مقدمة في الذكاء الاصطناعي", 3, C1, ["CS114", "MATH104"]),
            ("ST201", "Statistical Methods and Data Analysis", "الأساليب الإحصائية وتحليل البيانات", 2, C4, ["MATH104"]),
        ],
    },
    5: {
        "year": 3, "level_ar": "المستوى الثالث — Junior", "total": 17,
        "courses": [
            ("CS311", "Compiler Design", "تصميم المترجمات", 3, C1, ["CS215", "CS114"]),
            ("CS312", "Computer Graphics", "الرسم بالحاسب", 3, C2, ["MATH103", "CS113"]),
            ("CS313", "Web Technologies", "تقنيات الويب", 3, C3, ["CS213"]),
            ("AI301", "Machine Learning", "تعلّم الآلة", 3, C1, ["AI201", "MATH104"]),
            ("CS314", "Software Project Management", "إدارة مشروعات البرمجيات", 3, C1, ["CS216"]),
            ("IS301", "Human-Computer Interaction", "التفاعل بين الإنسان والحاسب", 2, C4, []),
        ],
    },
    6: {
        "year": 3, "level_ar": "المستوى الثالث — Junior", "total": 17,
        "courses": [
            ("CS321", "Distributed Systems", "النظم الموزّعة", 3, C1, ["CS214", "CS217"]),
            ("AI302", "Deep Learning", "التعلّم العميق", 3, C1, ["AI301"]),
            ("CS322", "Information Security and Cryptography", "أمن المعلومات والتشفير", 3, C1, ["CS217", "MATH102"]),
            ("CS323", "Software Architecture and Design Patterns", "معمارية البرمجيات وأنماط التصميم", 3, C1, ["CS216"]),
            ("CS324", "Cloud Computing", "الحوسبة السحابية", 3, C1, ["CS217"]),
            ("ELEC-DS", "Elective: Data Science and Big Data", "اختياري: علم البيانات والبيانات الضخمة", 2, C4, ["ST201"]),
        ],
    },
    7: {
        "year": 4, "level_ar": "المستوى الرابع — Senior", "total": 17,
        "courses": [
            ("AI401", "Natural Language Processing", "معالجة اللغات الطبيعية", 3, C1, ["AI301"]),
            ("AI402", "Computer Vision", "الرؤية بالحاسب", 3, C1, ["AI301"]),
            ("CS411", "Advanced Databases and Big Data", "قواعد البيانات المتقدمة والبيانات الضخمة", 3, C1, ["CS213"]),
            ("CS412", "Software Testing and Quality Assurance", "اختبار البرمجيات وضمان الجودة", 3, C1, ["CS216"]),
            ("CS413", "Graduation Project I", "مشروع التخرج 1", 3, C3, ["CS216"]),
            ("ELEC-CY", "Elective: Cybersecurity", "اختياري: الأمن السيبراني", 2, C4, ["CS217"]),
        ],
    },
    8: {
        "year": 4, "level_ar": "المستوى الرابع — Senior", "total": 17,
        "courses": [
            ("AI403", "Reinforcement Learning", "التعلّم المعزّز", 3, C1, ["AI301"]),
            ("CS421", "Advanced Algorithms and Complexity", "الخوارزميات المتقدمة والتعقيد", 3, C1, ["CS211"]),
            ("CS422", "Computing Ethics and Professional Practice", "أخلاقيات الحوسبة والممارسة المهنية", 3, C1, []),
            ("CS423", "Graduation Project II", "مشروع التخرج 2", 3, C3, ["CS413"]),
            ("ELEC-MOBILE", "Elective: Mobile Application Development", "اختياري: تطوير تطبيقات الموبايل", 2, C4, ["CS113"]),
            ("ELEC-GAME", "Elective: Game Development", "اختياري: تطوير الألعاب", 3, C3, ["CS312"]),
        ],
    },
}


def total_ch(sem):
    return sum(c[3] for c in SEMESTERS[sem]["courses"])


if __name__ == "__main__":
    grand = 0
    for s in range(1, 9):
        t = total_ch(s)
        grand += t
        print(f"Semester {s}: {len(SEMESTERS[s]['courses'])} courses, {t} CH")
    print("GRAND TOTAL:", grand)
