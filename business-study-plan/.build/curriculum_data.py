# -*- coding: utf-8 -*-
"""Single source of truth for the Cairo University Faculty of Business
(Business Administration track) 4-year / 8-semester study plan.

Each course: (code, english_title, arabic_title, credit_hours, split, prereq)
split = (lecture, tutorial, practical)
prereq = list of prerequisite course codes (or free text)
"""

FACULTY_AR = "كلية التجارة والأعمال — جامعة القاهرة"
FACULTY_EN = "Faculty of Business (Faculty of Commerce & Business Administration), Cairo University"
TRACK_AR = "مسار إدارة الأعمال (Business Administration)"
TRACK_EN = "Business Administration track"

# ---------------------------------------------------------------------------
# ELECTIVES (labels only; the actual elective courses are listed per semester)
# ---------------------------------------------------------------------------
ELECTIVES = {
    "ELEC-MKT": "التسويق الرقمي وإدارة العلامة التجارية",
    "ELEC-ENT": "ريادة الأعمال والابتكار",
    "ELEC-DAT": "تحليل البيانات للأعمال",
    "ELEC-ACC": "المحاسبة الضريبية",
    "ELEC-FIN": "أسواق المال والاستثمار",
    "ELEC-HR": "إدارة المواهب والقيادة",
    "ELEC-INT": "إدارة الأعمال الدولية",
    "ELEC-PRO": "إدارة المشروعات الاحترافية (PMP)",
}

C1 = (2, 1, 0)  # standard 3-CH split: 2 lecture + 1 tutorial

SEMESTERS = {
    1: {
        "year": 1, "level_ar": "المستوى الأول — Freshman", "total": 16,
        "courses": [
            ("ACC101", "Principles of Financial Accounting", "مبادئ المحاسبة المالية", 3, C1, []),
            ("MGT101", "Principles of Management", "مبادئ الإدارة", 3, C1, []),
            ("ECO101", "Principles of Microeconomics", "مبادئ الاقتصاد الجزئي", 3, C1, []),
            ("MTH101", "Mathematics for Business", "الرياضة للأعمال", 3, C1, []),
            ("BUS101", "Introduction to Business", "مقدمة في إدارة الأعمال", 2, (1, 1, 0), []),
            ("CIS101", "Introduction to Information Technology", "مقدمة في تكنولوجيا المعلومات", 2, (1, 0, 2), []),
        ],
    },
    2: {
        "year": 1, "level_ar": "المستوى الأول — Freshman", "total": 16,
        "courses": [
            ("ACC102", "Intermediate Accounting", "المحاسبة المتوسطة", 3, C1, ["ACC101"]),
            ("MGT102", "Organizational Behavior", "السلوك التنظيمي", 3, C1, ["MGT101"]),
            ("ECO102", "Principles of Macroeconomics", "مبادئ الاقتصاد الكلي", 3, C1, ["ECO101"]),
            ("STA101", "Statistics for Business", "الإحصاء للأعمال", 3, C1, ["MTH101"]),
            ("BUS102", "Business Communication", "الاتصال والكتابة في الأعمال", 2, (1, 1, 0), []),
            ("LAW101", "Business Law", "قانون الأعمال", 2, (1, 1, 0), []),
        ],
    },
    3: {
        "year": 2, "level_ar": "المستوى الثاني — Sophomore", "total": 16,
        "courses": [
            ("MKT201", "Principles of Marketing", "مبادئ التسويق", 3, C1, ["MGT101"]),
            ("FIN201", "Financial Management", "الإدارة المالية", 3, C1, ["ACC101"]),
            ("ACC201", "Cost Accounting", "محاسبة التكاليف", 3, C1, ["ACC102"]),
            ("ECO201", "Business Economics", "اقتصاديات الأعمال", 3, C1, ["ECO102"]),
            ("MTH201", "Business Mathematics and Calculus", "الرياضة المالية والتفاضل", 2, (1, 1, 0), ["MTH101"]),
            ("ELEC-ENT", "Elective: Entrepreneurship and Innovation", "اختياري: ريادة الأعمال والابتكار", 2, (1, 1, 0), []),
        ],
    },
    4: {
        "year": 2, "level_ar": "المستوى الثاني — Sophomore", "total": 16,
        "courses": [
            ("MGT201", "Human Resource Management", "إدارة الموارد البشرية", 3, C1, ["MGT102"]),
            ("MGT202", "Production and Operations Management", "إدارة الإنتاج والعمليات", 3, C1, ["MGT101"]),
            ("FIN202", "Corporate Finance", "التمويل المؤسسي", 3, C1, ["FIN201"]),
            ("MKT202", "Consumer Behavior", "سلوك المستهلك", 3, C1, ["MKT201"]),
            ("CIS201", "Management Information Systems", "نظم المعلومات الإدارية", 2, (1, 1, 0), ["CIS101"]),
            ("ELEC-DAT", "Elective: Data Analysis for Business", "اختياري: تحليل البيانات للأعمال", 2, (1, 0, 2), ["STA101"]),
        ],
    },
    5: {
        "year": 3, "level_ar": "المستوى الثالث — Junior", "total": 16,
        "courses": [
            ("ACC301", "Managerial Accounting", "المحاسبة الإدارية", 3, C1, ["ACC201"]),
            ("MKT301", "Marketing Management", "إدارة التسويق", 3, C1, ["MKT202"]),
            ("FIN301", "Investment and Portfolio Management", "الاستثمار وإدارة المحافظ", 3, C1, ["FIN202"]),
            ("MGT301", "Operations and Supply Chain Management", "إدارة العمليات وسلاسل التوريد", 3, C1, ["MGT202"]),
            ("MTH301", "Quantitative Methods for Business", "الأساليب الكمية للأعمال", 2, (1, 1, 0), ["STA101"]),
            ("ELEC-MKT", "Elective: Digital Marketing", "اختياري: التسويق الرقمي", 2, (1, 1, 0), ["MKT201"]),
        ],
    },
    6: {
        "year": 3, "level_ar": "المستوى الثالث — Junior", "total": 16,
        "courses": [
            ("MGT302", "Strategic Management", "الإدارة الاستراتيجية", 3, C1, ["MGT201", "MKT201"]),
            ("FIN302", "Financial Markets and Institutions", "الأسواق والمؤسسات المالية", 3, C1, ["FIN202"]),
            ("BUS301", "Business Research Methods", "مناهج البحث في الأعمال", 3, C1, ["STA101"]),
            ("MGT303", "International Business", "إدارة الأعمال الدولية", 3, C1, ["MGT201"]),
            ("BUS302", "Entrepreneurship and Small Business", "ريادة الأعمال والمشروعات الصغيرة", 2, (1, 1, 0), ["ELEC-ENT"]),
            ("ELEC-HR", "Elective: Talent Management and Leadership", "اختياري: إدارة المواهب والقيادة", 2, (1, 1, 0), ["MGT201"]),
        ],
    },
    7: {
        "year": 4, "level_ar": "المستوى الرابع — Senior", "total": 16,
        "courses": [
            ("MGT401", "Advanced Strategic Management", "الإدارة الاستراتيجية المتقدمة", 3, C1, ["MGT302"]),
            ("FIN401", "Risk Management", "إدارة المخاطر", 3, C1, ["FIN302"]),
            ("MGT402", "Project Management", "إدارة المشروعات", 3, C1, ["MGT301"]),
            ("BUS401", "Business Ethics and Corporate Governance", "أخلاقيات الأعمال وحوكمة الشركات", 2, (1, 1, 0), []),
            ("BUS402", "Graduation Project 1", "مشروع التخرج 1", 2, (1, 0, 2), []),
            ("ELEC-PRO", "Elective: Professional Project Management (PMP)", "اختياري: إدارة المشروعات الاحترافية", 3, (2, 1, 0), []),
        ],
    },
    8: {
        "year": 4, "level_ar": "المستوى الرابع — Senior", "total": 16,
        "courses": [
            ("MGT403", "Change and Innovation Management", "إدارة التغيير والابتكار", 3, C1, ["MGT302"]),
            ("FIN402", "International Finance", "التمويل الدولي", 3, C1, ["FIN302"]),
            ("MKT401", "Strategic Marketing", "التسويق الاستراتيجي", 3, C1, ["MKT301"]),
            ("BUS403", "Business Policy and Strategy", "سياسات واستراتيجيات الأعمال", 3, C1, ["MGT401"]),
            ("BUS404", "Graduation Project 2", "مشروع التخرج 2", 2, (1, 0, 2), ["BUS402"]),
            ("ELEC-FIN", "Elective: Financial Markets and Investment", "اختياري: أسواق المال والاستثمار", 2, (1, 1, 0), ["FIN301"]),
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
