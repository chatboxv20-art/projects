# -*- coding: utf-8 -*-
"""Week-by-week topic map for every course: 12 teaching weeks each
(weeks 1-6 and 9-14; weeks 7, 8, 15, 16 are review / midterm / final)."""

TOPICS = {}

TOPICS["ACC101"] = [
    ("Accounting and the Business Environment", "المحاسبة وبيئة الأعمال"),
    ("Recording Transactions and the Accounting Equation", "تسجيل العمليات ومعادلة المحاسبة"),
    ("The Journal, the Ledger and the Trial Balance", "دفتر اليومية ودفتر الأستاذ وميزان المراجعة"),
    ("Adjusting Entries and Completing the Accounting Cycle", "القيود التسوية وإتمام الدورة المحاسبية"),
    ("Merchandising Operations and Inventory", "عمليات البيع وتقييم المخزون"),
    ("Internal Control and Cash", "الرقابة الداخلية وإدارة النقدية"),
    ("Receivables and Bad Debts", "المدينون والديون المعدومة"),
    ("Plant Assets and Depreciation", "الأصول الثابتة والإهلاك"),
    ("Current Liabilities and Payroll", "الالتزامات المتداولة والرواتب"),
    ("Partnerships and Corporations", "الشركات التضامنية والمساهمة"),
    ("Long-Term Liabilities and Bonds", "الالتزامات طويلة الأجل والسندات"),
    ("The Statement of Cash Flows and Financial Statement Analysis", "قائمة التدفقات النقدية وتحليل القوائم المالية"),
]

TOPICS["MGT101"] = [
    ("Management and the Manager's Role", "الإدارة ودور المدير"),
    ("The Evolution of Management Thought", "تطور الفكر الإداري"),
    ("Planning and Strategic Thinking", "التخطيط والتفكير الاستراتيجي"),
    ("Decision Making", "اتخاذ القرار"),
    ("Organizing and Organizational Structure", "التنظيم والهيكل التنظيمي"),
    ("Staffing and Human Resources", "التوظيف وإدارة الموارد البشرية"),
    ("Leading and Motivation", "القيادة والتحفيز"),
    ("Communication and Group Dynamics", "الاتصال وديناميكية الجماعات"),
    ("Controlling and Performance Measurement", "الرقابة وقياس الأداء"),
    ("Operations and Quality Management", "العمليات وإدارة الجودة"),
    ("Managing Change and Innovation", "إدارة التغيير والابتكار"),
    ("Business Ethics and Social Responsibility", "أخلاقيات الأعمال والمسؤولية الاجتماعية"),
]

TOPICS["ECO101"] = [
    ("The Economic Problem and Scarcity", "المشكلة الاقتصادية والندرة"),
    ("Demand, Supply and Market Equilibrium", "الطلب والعرض وتوازن السوق"),
    ("Elasticity and Its Applications", "المرونة وتطبيقاتها"),
    ("Consumer Behavior and Utility", "سلوك المستهلك والمنفعة"),
    ("Production and Cost", "الإنتاج والتكاليف"),
    ("Market Structures: Perfect Competition", "هياكل السوق: المنافسة الكاملة"),
    ("Monopoly and Imperfect Competition", "الاحتكار والمنافسة غير الكاملة"),
    ("Factor Markets and Income Distribution", "أسواق عناصر الإنتاج وتوزيع الدخل"),
    ("Market Failure and Government Intervention", "فشل السوق وتدخل الحكومة"),
    ("Public Goods and Externalities", "السلع العامة والآثار الخارجية"),
    ("International Trade and Comparative Advantage", "التجارة الدولية والميزة النسبية"),
    ("Applied Microeconomics for Business", "الاقتصاد الجزئي التطبيقي للأعمال"),
]

TOPICS["MTH101"] = [
    ("Numbers, Equations and Business Applications", "الأعداد والمعادلات وتطبيقاتها"),
    ("Functions and Their Graphs", "الدوال ومنحنياتها"),
    ("Linear Functions and Break-Even Analysis", "الدوال الخطية وتحليل نقطة التعادل"),
    ("Systems of Equations", "أنظمة المعادلات"),
    ("Quadratic and Polynomial Functions", "الدوال التربيعية وكثيرات الحدود"),
    ("Exponential and Logarithmic Functions", "الدوال الأسية واللوغاريتمية"),
    ("Mathematics of Finance: Interest", "رياضة التمويل: الفائدة"),
    ("Annuities and Present Value", "الأقساط والقيمة الحالية"),
    ("Limits and Continuity", "النهايات والاتصال"),
    ("Differentiation and Marginal Analysis", "التفاضل والتحليل الحدي"),
    ("Optimization and Applications", "تعظيم وتقليل الدوال وتطبيقاتها"),
    ("Matrices and Linear Programming", "المصفوفات والبرمجة الخطية"),
]

TOPICS["BUS101"] = [
    ("The Business Environment", "بيئة الأعمال"),
    ("Forms of Business Ownership", "أشكال ملكية المشروعات"),
    ("The Functions of Business", "وظائف الأعمال"),
    ("Business and the Economy", "الأعمال والاقتصاد"),
    ("Marketing in the Modern Firm", "التسويق في المنشأة الحديثة"),
    ("Managing Financial Resources", "إدارة الموارد المالية"),
    ("Operations and Production Basics", "أساسيات العمليات والإنتاج"),
    ("Human Capital in Business", "رأس المال البشري في الأعمال"),
    ("Information Technology in Business", "تكنولوجيا المعلومات في الأعمال"),
    ("Entrepreneurship and Startups", "ريادة الأعمال والشركات الناشئة"),
    ("Business Ethics and Sustainability", "أخلاقيات الأعمال والاستدامة"),
    ("Global Business Today", "الأعمال العالمية اليوم"),
]

TOPICS["CIS101"] = [
    ("Computer Systems and Hardware", "أنظمة الحاسوب والعتاد"),
    ("Software and Operating Systems", "البرمجيات وأنظمة التشغيل"),
    ("The Internet and the Web", "الإنترنت والشبكة العنكبوتية"),
    ("Digital Communication Tools", "أدوات الاتصال الرقمية"),
    ("Introduction to Data and Databases", "مقدمة في البيانات وقواعد البيانات"),
    ("Spreadsheets for Business", "الجداول الإلكترونية للأعمال"),
    ("Word Processing and Presentations", "معالجة النصوص والعروض التقديمية"),
    ("Information Security and Privacy", "أمن المعلومات والخصوصية"),
    ("E-Commerce and Digital Business", "التجارة الإلكترونية والأعمال الرقمية"),
    ("Cloud Computing and Collaboration", "الحوسبة السحابية والعمل التعاوني"),
    ("Introduction to Business Analytics", "مقدمة في تحليلات الأعمال"),
    ("Emerging Technologies in Business", "التقنيات الناشئة في الأعمال"),
]

TOPICS["ACC102"] = [
    ("The Conceptual Framework of Accounting", "الإطار المفاهيمي للمحاسبة"),
    ("Accounting for Partnerships", "المحاسبة في الشركات التضامنية"),
    ("Accounting for Corporations: Share Capital", "محاسبة الشركات المساهمة: رأس المال"),
    ("Dividends and Retained Earnings", "التوزيعات والأرباح المحتجزة"),
    ("Long-Term Investments", "الاستثمارات طويلة الأجل"),
    ("Revenue Recognition", "الاعتراف بالإيراد"),
    ("Accounting for Leases", "محاسبة عقود الإيجار"),
    ("Accounting for Income Taxes", "محاسبة ضريبة الدخل"),
    ("Pensions and Post-Retirement Benefits", "المعاشات ومزايا ما بعد التقاعد"),
    ("Accounting Changes and Error Correction", "التغيرات المحاسبية وتصحيح الأخطاء"),
    ("Financial Reporting and Disclosure", "التقرير المالي والإفصاح"),
    ("International Financial Reporting Standards (IFRS)", "المعايير الدولية للتقرير المالي"),
]

TOPICS["MGT102"] = [
    ("Introduction to Organizational Behavior", "مقدمة في السلوك التنظيمي"),
    ("Personality and Individual Differences", "الشخصية والفروق الفردية"),
    ("Perception and Attribution", "الإدراك والإسناد"),
    ("Attitudes and Job Satisfaction", "الاتجاهات والرضا الوظيفي"),
    ("Motivation Theories", "نظريات التحفيز"),
    ("Group Behavior and Teamwork", "سلوك الجماعات والعمل الجماعي"),
    ("Leadership in Organizations", "القيادة في المنظمات"),
    ("Power, Politics and Conflict", "القوة والسياسة والصراع"),
    ("Organizational Culture", "الثقافة التنظيمية"),
    ("Organizational Change and Development", "التغيير والتطوير التنظيمي"),
    ("Stress and Well-Being at Work", "الضغوط والصحة النفسية في العمل"),
    ("Decision Making in Organizations", "اتخاذ القرار في المنظمات"),
]

TOPICS["ECO102"] = [
    ("Measuring National Output and Income", "قياس الناتج والدخل القومي"),
    ("Economic Growth and Productivity", "النمو الاقتصادي والإنتاجية"),
    ("Unemployment and the Labor Market", "البطالة وسوق العمل"),
    ("Inflation and Price Indices", "التضخم وأرقام الأسعار القياسية"),
    ("Aggregate Demand and Aggregate Supply", "الطلب الكلي والعرض الكلي"),
    ("Consumption, Saving and Investment", "الاستهلاك والادخار والاستثمار"),
    ("Money, Banking and the Central Bank", "النقود والبنوك والبنك المركزي"),
    ("Monetary Policy", "السياسة النقدية"),
    ("Fiscal Policy and the Government Budget", "السياسة المالية والموازنة العامة"),
    ("The Balance of Payments and Exchange Rates", "ميزان المدفوعات وأسعار الصرف"),
    ("Business Cycles and Stabilization", "الدورات الاقتصادية والاستقرار"),
    ("Macroeconomic Policy in Egypt", "السياسة الاقتصادية الكلية في مصر"),
]

TOPICS["STA101"] = [
    ("Data, Variables and Levels of Measurement", "البيانات والمتغيرات ومستويات القياس"),
    ("Organizing and Presenting Data", "تنظيم البيانات وعرضها"),
    ("Measures of Central Tendency", "مقاييس النزعة المركزية"),
    ("Measures of Dispersion", "مقاييس التشتت"),
    ("Probability Fundamentals", "أساسيات الاحتمالات"),
    ("Discrete Probability Distributions", "التوزيعات الاحتمالية المنفصلة"),
    ("The Normal Distribution", "التوزيع الطبيعي"),
    ("Sampling and Sampling Distributions", "المعاينة وتوزيعات المعاينة"),
    ("Estimation and Confidence Intervals", "التقدير وفترات الثقة"),
    ("Hypothesis Testing", "اختبار الفروض"),
    ("Correlation and Simple Regression", "الارتباط والانحدار البسيط"),
    ("Applying Statistics in Business", "تطبيق الإحصاء في الأعمال"),
]

TOPICS["BUS102"] = [
    ("Foundations of Business Communication", "أساسيات الاتصال في الأعمال"),
    ("Audience Analysis and Purpose", "تحليل الجمهور والهدف"),
    ("Writing Clear Business Messages", "كتابة الرسائل الإدارية الواضحة"),
    ("Business Letters and Memos", "الخطابات الإدارية والمذكرات"),
    ("Reports and Proposals", "التقارير والمقترحات"),
    ("Digital and Email Communication", "الاتصال الرقمي والبريد الإلكتروني"),
    ("Interpersonal and Team Communication", "الاتصال الشخصي والجماعي"),
    ("Meetings, Minutes and Agendas", "الاجتماعات ومحاضرها وجداول أعمالها"),
    ("Presentations and Public Speaking", "العروض التقديمية والخطابة"),
    ("Cross-Cultural Communication", "الاتصال عبر الثقافات"),
    ("Persuasion and Negotiation", "الإقناع والتفاوض"),
    ("Employment Communication: CV and Interview", "اتصال التوظيف: السيرة الذاتية والمقابلة"),
]

TOPICS["LAW101"] = [
    ("Introduction to Law and the Legal System", "مقدمة في القانون والنظام القانوني"),
    ("Sources of Law and the Courts", "مصادر القانون والمحاكم"),
    ("Contracts: Formation and Elements", "العقود: التكوين والعناصر"),
    ("Contract Performance and Breach", "تنفيذ العقد والإخلال به"),
    ("Commercial Law and Commercial Papers", "القانون التجاري والأوراق التجارية"),
    ("Agency and Distribution Agreements", "الوكالة وعقود التوزيع"),
    ("Company Law and Corporate Forms", "قانون الشركات وأشكالها"),
    ("Intellectual Property and Trademarks", "الملكية الفكرية والعلامات التجارية"),
    ("Labor and Employment Law", "قانون العمل والتوظيف"),
    ("Taxation Law Basics", "أساسيات قانون الضرائب"),
    ("Consumer Protection and Competition Law", "حماية المستهلك وقانون المنافسة"),
    ("Dispute Resolution and Arbitration", "تسوية المنازعات والتحكيم"),
]

TOPICS["MKT201"] = [
    ("Marketing and the Marketing Process", "التسويق وعملية التسويق"),
    ("The Marketing Environment", "البيئة التسويقية"),
    ("Marketing Strategy and the Marketing Plan", "الاستراتيجية التسويقية وخطة التسويق"),
    ("Marketing Information and Research", "المعلومات التسويقية والبحوث"),
    ("Consumer and Business Buyer Behavior", "سلوك المشتري الاستهلاكي والصناعي"),
    ("Segmentation, Targeting and Positioning", "التجزئة والاستهداف والتموضع"),
    ("Product and Brand Strategy", "استراتيجية المنتج والعلامة التجارية"),
    ("New Product Development and the Product Life Cycle", "تطوير المنتجات ودورة حياة المنتج"),
    ("Pricing Strategies", "استراتيجيات التسعير"),
    ("Distribution Channels and Retailing", "قنوات التوزيع والتجزئة"),
    ("Integrated Marketing Communication and Promotion", "الاتصال التسويقي المتكامل والترويج"),
    ("Digital and Global Marketing", "التسويق الرقمي والعالمي"),
]

TOPICS["FIN201"] = [
    ("The Role and Goal of Financial Management", "دور الإدارة المالية وهدفها"),
    ("The Financial Environment and Markets", "البيئة المالية والأسواق"),
    ("Financial Statements and Cash Flow", "القوائم المالية والتدفق النقدي"),
    ("Financial Statement Analysis and Ratios", "تحليل القوائم المالية والنسب"),
    ("Time Value of Money", "القيمة الزمنية للنقود"),
    ("Bond Valuation", "تقييم السندات"),
    ("Stock Valuation", "تقييم الأسهم"),
    ("Capital Budgeting: NPV and IRR", "الموازنة الرأسمالية: صافي القيمة الحالية ومعدل العائد الداخلي"),
    ("Risk and Return", "المخاطر والعائد"),
    ("Cost of Capital", "تكلفة رأس المال"),
    ("Capital Structure and Leverage", "هيكل رأس المال والرفع المالي"),
    ("Working Capital Management", "إدارة رأس المال العامل"),
]

TOPICS["ACC201"] = [
    ("Cost Concepts and Classification", "مفاهيم التكاليف وتصنيفها"),
    ("Job Order Costing", "تكاليف الأوامر الإنتاجية"),
    ("Process Costing", "تكاليف المراحل الإنتاجية"),
    ("Activity-Based Costing", "التكاليف على أساس الأنشطة"),
    ("Cost-Volume-Profit Analysis", "تحليل التكلفة والحجم والربح"),
    ("Variable and Absorption Costing", "التكاليف المتغيرة والتكاليف المستوعبة"),
    ("Budgeting and Profit Planning", "الموازنات والتخطيط للربح"),
    ("Standard Costs and Variance Analysis", "التكاليف المعيارية وتحليل الانحرافات"),
    ("Flexible Budgets and Overhead Analysis", "الموازنات المرنة وتحليل التكاليف غير المباشرة"),
    ("Relevant Costs for Decision Making", "التكاليف الملائمة لاتخاذ القرار"),
    ("Pricing Decisions and Target Costing", "قرارات التسعير والتكلفة المستهدفة"),
    ("Performance Measurement and the Balanced Scorecard", "قياس الأداء وبطاقة الأداء المتوازن"),
]

TOPICS["ECO201"] = [
    ("Business Economics and Managerial Decision Making", "اقتصاديات الأعمال والقرار الإداري"),
    ("Demand Estimation and Forecasting", "تقدير الطلب والتنبؤ"),
    ("Production and Cost Analysis for Managers", "تحليل الإنتاج والتكاليف للمديرين"),
    ("Market Structure and Firm Strategy", "هياكل السوق واستراتيجية المنشأة"),
    ("Pricing Practices and Strategies", "ممارسات واستراتيجيات التسعير"),
    ("Risk, Uncertainty and Decision Making", "المخاطر وعدم التأكد واتخاذ القرار"),
    ("Capital Budgeting from an Economic View", "الموازنة الرأسمالية من منظور اقتصادي"),
    ("Government Regulation and Business", "التنظيم الحكومي والأعمال"),
    ("Long-Run Investment Decisions", "قرارات الاستثمار طويلة الأجل"),
    ("The Economics of Information and Technology", "اقتصاديات المعلومات والتكنولوجيا"),
    ("Global Business Economics", "اقتصاديات الأعمال العالمية"),
    ("Applied Business Economics Cases", "حالات تطبيقية في اقتصاديات الأعمال"),
]

TOPICS["MTH201"] = [
    ("Review of Business Functions and Models", "مراجعة دوال ونماذج الأعمال"),
    ("Simple and Compound Interest", "الفائدة البسيطة والمركبة"),
    ("Discounting and Present Value", "الخصم والقيمة الحالية"),
    ("Annuities and Sinking Funds", "الأقساط وصناديق الإطفاء"),
    ("Loan Amortization and Bonds", "جدولة القروض والسندات"),
    ("Limits and Rates of Change", "النهايات ومعدلات التغير"),
    ("Rules of Differentiation", "قواعد التفاضل"),
    ("Marginal Analysis in Business", "التحليل الحدي في الأعمال"),
    ("Optimization: Maxima and Minima", "التعظيم: القيم العظمى والصغرى"),
    ("Constrained Optimization and Lagrange", "التعظيم المقيّد ومضاعف لاجرانج"),
    ("Integration and Areas", "التكامل والمساحات"),
    ("Applications of Calculus in Business", "تطبيقات التفاضل والتكامل في الأعمال"),
]

TOPICS["ELEC-ENT"] = [
    ("The Entrepreneurial Mindset", "العقلية الريادية"),
    ("Recognizing Opportunities", "التعرف على الفرص"),
    ("Feasibility Analysis", "دراسة الجدوى"),
    ("Business Models and Business Model Canvas", "نماذج الأعمال ونموذج الأعمال التجاري"),
    ("Writing a Business Plan", "كتابة خطة العمل"),
    ("Financing the New Venture", "تمويل المشروع الجديد"),
    ("Marketing for Startups", "التسويق للشركات الناشئة"),
    ("Building and Managing a Team", "بناء وإدارة الفريق"),
    ("Legal and Ethical Issues for Startups", "القضايا القانونية والأخلاقية للشركات الناشئة"),
    ("Growth Strategies and Scaling", "استراتيجيات النمو والتوسع"),
    ("Managing Risk and Failure", "إدارة المخاطر والفشل"),
    ("The Entrepreneurial Ecosystem in Egypt", "منظومة ريادة الأعمال في مصر"),
]

TOPICS["MGT201"] = [
    ("Introduction to Human Resource Management", "مقدمة في إدارة الموارد البشرية"),
    ("HR Strategy and the Business Environment", "استراتيجية الموارد البشرية وبيئة الأعمال"),
    ("Job Analysis and Job Design", "تحليل وتصميم الوظائف"),
    ("Human Resource Planning", "تخطيط الموارد البشرية"),
    ("Recruitment and Selection", "الاستقطاب والاختيار"),
    ("Training and Development", "التدريب والتطوير"),
    ("Performance Management and Appraisal", "إدارة الأداء وتقييمه"),
    ("Compensation and Benefits", "الأجور والمزايا"),
    ("Employee Relations and Labor Law", "علاقات العاملين وقانون العمل"),
    ("Occupational Health and Safety", "الصحة والسلامة المهنية"),
    ("International Human Resource Management", "إدارة الموارد البشرية الدولية"),
    ("Contemporary Issues in HRM", "قضايا معاصرة في إدارة الموارد البشرية"),
]

TOPICS["MGT202"] = [
    ("Operations Management and Productivity", "إدارة العمليات والإنتاجية"),
    ("Operations Strategy", "استراتيجية العمليات"),
    ("Product and Service Design", "تصميم المنتج والخدمة"),
    ("Process Design and Analysis", "تصميم العمليات وتحليلها"),
    ("Capacity Planning", "تخطيط الطاقة الإنتاجية"),
    ("Location and Layout Strategies", "استراتيجيات الموقع والتخطيط الداخلي"),
    ("Forecasting Demand", "التنبؤ بالطلب"),
    ("Inventory Management", "إدارة المخزون"),
    ("Aggregate Planning and Scheduling", "التخطيط الإجمالي والجدولة"),
    ("Material Requirements Planning", "تخطيط الاحتياجات من المواد"),
    ("Quality Management and Lean Systems", "إدارة الجودة وأنظمة الرشاقة"),
    ("Project Management Basics", "أساسيات إدارة المشروعات"),
]

TOPICS["FIN202"] = [
    ("Corporate Governance and the Financial Manager", "حوكمة الشركات والمدير المالي"),
    ("Financial Planning and Forecasting", "التخطيط المالي والتنبؤ"),
    ("The Time Value of Money in Corporate Decisions", "القيمة الزمنية للنقود في القرارات المؤسسية"),
    ("Bond and Stock Valuation Revisited", "إعادة تقييم السندات والأسهم"),
    ("Risk and Return: CAPM", "المخاطر والعائد: نموذج تسعير الأصول الرأسمالية"),
    ("Cost of Capital and WACC", "تكلفة رأس المال والمتوسط المرجح"),
    ("Capital Budgeting and Investment Appraisal", "الموازنة الرأسمالية وتقييم الاستثمار"),
    ("Dividend Policy", "سياسة توزيع الأرباح"),
    ("Capital Structure Decisions", "قرارات هيكل رأس المال"),
    ("Working Capital and Cash Management", "رأس المال العامل وإدارة النقدية"),
    ("Mergers, Acquisitions and Corporate Restructuring", "الاندماج والاستحواذ وإعادة الهيكلة"),
    ("Corporate Financial Strategy", "الاستراتيجية المالية للشركة"),
]

TOPICS["MKT202"] = [
    ("Introduction to Consumer Behavior", "مقدمة في سلوك المستهلك"),
    ("Motivation, Needs and Goals", "الدوافع والحاجات والأهداف"),
    ("Personality and Self-Concept", "الشخصية ومفهوم الذات"),
    ("Perception and Learning", "الإدراك والتعلم"),
    ("Attitudes and Persuasion", "الاتجاهات والإقناع"),
    ("Reference Groups and Social Influences", "الجماعات المرجعية والمؤثرات الاجتماعية"),
    ("Family and Household Decision Making", "الأسرة وقرارات الشراء"),
    ("Culture and Subculture", "الثقافة والثقافات الفرعية"),
    ("The Consumer Decision Process", "عملية قرار المستهلك"),
    ("Post-Purchase Behavior and Loyalty", "سلوك ما بعد الشراء والولاء"),
    ("Digital Consumer Behavior", "سلوك المستهلك الرقمي"),
    ("Applying Consumer Insights to Marketing", "تطبيق رؤى المستهلك في التسويق"),
]

TOPICS["CIS201"] = [
    ("Information Systems in Business Today", "نظم المعلومات في الأعمال اليوم"),
    ("Global E-Business and Collaboration", "الأعمال الإلكترونية والتعاون العالمي"),
    ("Information Systems, Organizations and Strategy", "نظم المعلومات والمنظمات والاستراتيجية"),
    ("Ethical and Social Issues in Information Systems", "القضايا الأخلاقية والاجتماعية في نظم المعلومات"),
    ("IT Infrastructure and Platforms", "البنية التحتية لتكنولوجيا المعلومات"),
    ("Foundations of Business Intelligence", "أساسيات ذكاء الأعمال"),
    ("Databases and Information Management", "قواعد البيانات وإدارة المعلومات"),
    ("Telecommunications, the Internet and Wireless", "الاتصالات والإنترنت واللاسلكي"),
    ("Securing Information Systems", "تأمين نظم المعلومات"),
    ("Enterprise Applications and ERP", "تطبيقات المؤسسة وتخطيط مواردها"),
    ("Building Information Systems", "بناء نظم المعلومات"),
    ("Managing Projects and Change in IS", "إدارة المشروعات والتغيير في نظم المعلومات"),
]

TOPICS["ELEC-DAT"] = [
    ("Data Analytics in Business", "تحليلات البيانات في الأعمال"),
    ("Data Collection and Cleaning", "جمع البيانات وتنظيفها"),
    ("Descriptive Analytics and Dashboards", "التحليلات الوصفية ولوحات المعلومات"),
    ("Data Visualization Principles", "مبادئ تصوير البيانات"),
    ("Excel and Spreadsheet Analytics", "التحليلات بالجداول الإلكترونية"),
    ("Introduction to SQL and Databases", "مقدمة في SQL وقواعد البيانات"),
    ("Predictive Analytics Basics", "أساسيات التحليلات التنبؤية"),
    ("Regression and Forecasting", "الانحدار والتنبؤ"),
    ("Segmentation and Clustering", "التجزئة والعنقدة"),
    ("A/B Testing and Experimentation", "الاختبار المقارن والتجارب"),
    ("Prescriptive Analytics and Optimization", "التحليلات التوجيهية والتحسين"),
    ("Communicating Data Insights", "توصيل رؤى البيانات"),
]
