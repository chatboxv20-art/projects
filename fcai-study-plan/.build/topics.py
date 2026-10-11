# -*- coding: utf-8 -*-
"""Week-by-week topic map for every course (part 1: semesters 1-4).
12 teaching weeks each (weeks 1-6 and 9-14; weeks 7, 8, 15, 16 are
review / midterm / final)."""

TOPICS = {}

# ---------------------------------------------------------------------------
# SEMESTER 1
# ---------------------------------------------------------------------------
TOPICS["CS111"] = [
    ("Computing and the Information Age", "الحوسبة وعصر المعلومات"),
    ("Number Systems and Data Representation", "أنظمة الأعداد وتمثيل البيانات"),
    ("Computers and Their Components", "الحاسبات ومكوّناتها"),
    ("The Operating System and Application Software", "نظام التشغيل وبرمجيات التطبيقات"),
    ("Problem Solving and Algorithms", "حل المشكلات والخوارزميات"),
    ("Flowcharts and Pseudocode", "المخططات الانسيابية والكود الوهمي"),
    ("Programming Languages and Compilers", "لغات البرمجة والمترجمات"),
    ("Computer Networks and the Internet", "شبكات الحاسب والإنترنت"),
    ("Databases and Information Systems", "قواعد البيانات ونظم المعلومات"),
    ("Software Engineering and Program Development", "هندسة البرمجيات وتطوير البرامج"),
    ("Security, Privacy and Ethics in Computing", "الأمن والخصوصية وأخلاقيات الحوسبة"),
    ("Frontiers of Computing: AI, IoT and Cloud", "آفاق الحوسبة: الذكاء الاصطناعي والإنترنت والسلحبة"),
]

TOPICS["CS112"] = [
    ("Introduction to Programming and Problem Solving", "مقدمة في البرمجة وحل المشكلات"),
    ("Variables, Data Types and Constants", "المتغيرات وأنواع البيانات والثوابت"),
    ("Operators and Expressions", "المعاملات والتعبيرات"),
    ("Input, Output and Formatting", "الإدخال والإخراج والتنسيق"),
    ("Conditional Statements", "الجمل الشرطية"),
    ("Loops and Iteration", "الحلقات والتكرار"),
    ("Functions and Modular Design", "الدوال والتصميم المعياري"),
    ("Arrays and Strings", "المصفوفات والنصوص"),
    ("Pointers and References", "المؤشرات والمراجع"),
    ("Files and Streams", "الملفات والتدفقات"),
    ("Structures and Records", "الهياكل والسجلات"),
    ("Debugging and Testing Programs", "تنقيح البرامج واختبارها"),
]

TOPICS["MATH101"] = [
    ("Functions, Domains and Graphs", "الدوال والمجالات والمنحنيات"),
    ("Limits and Continuity", "النهايات والاتصال"),
    ("Derivatives and Rates of Change", "المشتقات ومعدلات التغير"),
    ("Rules of Differentiation", "قواعد الاشتقاق"),
    ("Applications of the Derivative", "تطبيقات المشتقة"),
    ("Curve Sketching and Optimization", "رسم المنحنيات والتحسين"),
    ("The Definite and Indefinite Integral", "التكامل المحدود وغير المحدود"),
    ("Techniques of Integration", "أساليب التكامل"),
    ("Applications of Integration", "تطبيقات التكامل"),
    ("Sequences and Series", "المتتابعات والمتسلسلات"),
    ("Functions of Several Variables", "دوال عدة متغيرات"),
    ("Calculus for Computing Problems", "التفاضل والتكامل لمشكلات الحوسبة"),
]

TOPICS["MATH102"] = [
    ("Logic and Propositional Calculus", "المنطق وحساب القضايا"),
    ("Logical Equivalence and Proof Methods", "التكافؤ المنطقي وأساليب البرهان"),
    ("Sets and Set Operations", "المجموعات وعملياتها"),
    ("Relations and Their Properties", "العلاقات وخصائصها"),
    ("Functions and Mappings", "الدوال والتحويلات"),
    ("Counting and the Pigeonhole Principle", "العد ومبدأ الحمام"),
    ("Permutations and Combinations", "التباديل والتوافيق"),
    ("Recurrence Relations", "علاقات الاستدعاء الذاتي"),
    ("Graphs and Graph Terminology", "الرسوم البيانية ومصطلحاتها"),
    ("Trees and Spanning Trees", "الأشجار والأشجار الممتدة"),
    ("Boolean Algebra", "الجبر البولياني"),
    ("Automata and Formal Languages Introduction", "مقدمة في الآلات المجرّدة واللغات الصورية"),
]

TOPICS["PHYS101"] = [
    ("Measurement and Units", "القياس والوحدات"),
    ("Motion in One Dimension", "الحركة في بعد واحد"),
    ("Vectors and Motion in Two Dimensions", "المتجهات والحركة في بعدين"),
    ("Newton's Laws of Motion", "قوانين نيوتن للحركة"),
    ("Applications of Newton's Laws", "تطبيقات قوانين نيوتن"),
    ("Work, Energy and Power", "الشغل والطاقة والقدرة"),
    ("Momentum and Collisions", "الزخم والتصادمات"),
    ("Rotational Motion", "الحركة الدورانية"),
    ("Oscillations and Waves", "الاهتزازات والموجات"),
    ("Electric Charges and Fields", "الشحنات والمجالات الكهربائية"),
    ("Electric Circuits", "الدوائر الكهربائية"),
    ("Physics Foundations for Computing Hardware", "أسس الفيزياء لعتاد الحاسب"),
]

TOPICS["ENG101"] = [
    ("Reading Strategies for Academic Texts", "استراتيجيات قراءة النصوص الأكاديمية"),
    ("Building Technical Vocabulary", "بناء المصطلح الفني"),
    ("Grammar: Tenses and Sentence Structure", "القواعد: الأزمنة وبنية الجملة"),
    ("Grammar: Modals, Conditionals and Passive Voice", "القواعد: الأفعال الناقصة والشرط والمبني للمجهول"),
    ("Listening and Note-Taking", "الاستماع وتدوين الملاحظات"),
    ("Speaking and Presentation Skills", "مهارات التحدث والعرض"),
    ("Writing Paragraphs and Topic Sentences", "كتابة الفقرات والجمل الافتتاحية"),
    ("Summarizing and Paraphrasing", "التلخيص وإعادة الصياغة"),
    ("Describing Data and Processes", "وصف البيانات والعمليات"),
    ("Formal Emails and Professional Correspondence", "الإيميلات الرسمية والمراسلات المهنية"),
    ("Academic Integrity and Referencing", "النزاهة الأكاديمية والتوثيق"),
    ("Review and Integrated Skills Practice", "مراجعة وتدريب متكامل على المهارات"),
]

# ---------------------------------------------------------------------------
# SEMESTER 2
# ---------------------------------------------------------------------------
TOPICS["CS113"] = [
    ("From Procedural to Object-Oriented Thinking", "من البرمجة الإجرائية إلى التفكير الكائني"),
    ("Classes, Objects and Attributes", "الأصناف والكائنات والخصائص"),
    ("Methods, Constructors and Encapsulation", "الدوال والبنّاءات والتغليف"),
    ("Inheritance and Class Hierarchies", "الوراثة وهرمية الأصناف"),
    ("Polymorphism and Dynamic Binding", "تعدّد الأشكال والربط الديناميكي"),
    ("Abstract Classes and Interfaces", "الأصناف المجرّدة والواجهات"),
    ("Exception Handling", "معالجة الاستثناءات"),
    ("Generics and Collections", "الأصناف العامة والمجموعات"),
    ("File Handling and Serialization", "التعامل مع الملفات والتسلسل"),
    ("GUI Programming Basics", "أساسيات واجهات المستخدم الرسومية"),
    ("Design Principles: SOLID", "مبادئ التصميم: SOLID"),
    ("Case Study: Building an OOP Application", "دراسة حالة: بناء تطبيق كائني التوجه"),
]

TOPICS["CS114"] = [
    ("Abstract Data Types and Complexity", "أنواع البيانات المجرّدة والتعقيد"),
    ("Arrays and Dynamic Arrays", "المصفوفات والمصفوفات الديناميكية"),
    ("Linked Lists", "القوائم المترابطة"),
    ("Stacks", "المكدّسات"),
    ("Queues and Priority Queues", "الطوابير وطوابير الأولوية"),
    ("Recursion and Backtracking", "الاستدعاء الذاتي والتراجع"),
    ("Binary Trees and Tree Traversals", "الأشجار الثنائية وطرق المرور عليها"),
    ("Binary Search Trees and Balanced Trees", "أشجار البحث الثنائية والأشجار المتوازنة"),
    ("Heaps and Priority Structures", "الأكوام وهياكل الأولوية"),
    ("Hash Tables and Hashing", "جداول التقطيع والتقطيع"),
    ("Graphs and Graph Representation", "الرسوم البيانية وتمثيلها"),
    ("Sorting and Searching Algorithms", "خوارزميات الترتيب والبحث"),
]

TOPICS["MATH103"] = [
    ("Systems of Linear Equations", "أنظمة المعادلات الخطية"),
    ("Matrices and Matrix Operations", "المصفوفات وعملياتها"),
    ("Determinants and Their Properties", "المحددات وخصائصها"),
    ("Matrix Inverses", "معكوس المصفوفة"),
    ("Vector Spaces and Subspaces", "الفضاءات الاتجاهية والفضاءات الجزئية"),
    ("Linear Independence and Bases", "الاستقلال الخطي والأساسات"),
    ("Linear Transformations", "التحويلات الخطية"),
    ("Eigenvalues and Eigenvectors", "القيم والمتجهات الذاتية"),
    ("Orthogonality and Projections", "التعامد والإسقاطات"),
    ("Diagonalization and Applications", "التقطير وتطبيقاته"),
    ("Singular Value Decomposition Introduction", "مقدمة في تحليل القيم المفردة"),
    ("Linear Algebra for Machine Learning", "الجبر الخطي لتعلّم الآلة"),
]

TOPICS["MATH104"] = [
    ("Descriptive Statistics", "الإحصاء الوصفي"),
    ("Probability Axioms and Rules", "بديهيات الاحتمال وقواعده"),
    ("Conditional Probability and Independence", "الاحتمال الشرطي والاستقلال"),
    ("Random Variables", "المتغيرات العشوائية"),
    ("Discrete Probability Distributions", "التوزيعات الاحتمالية المتقطعة"),
    ("Continuous Probability Distributions", "التوزيعات الاحتمالية المتصلة"),
    ("The Normal Distribution", "التوزيع الطبيعي"),
    ("Sampling and Sampling Distributions", "المعاينة وتوزيعات المعاينة"),
    ("Estimation and Confidence Intervals", "التقدير وفترات الثقة"),
    ("Hypothesis Testing", "اختبار الفروض"),
    ("Correlation and Regression", "الارتباط والانحدار"),
    ("Probability and Statistics for Computing", "الاحتمالات والإحصاء للحوسبة"),
]

TOPICS["PHYS102"] = [
    ("Magnetism and Magnetic Fields", "المغناطيسية والمجالات المغناطيسية"),
    ("Electromagnetic Induction", "الحث الكهرومغناطيسي"),
    ("Alternating Current Circuits", "دوائر التيار المتردد"),
    ("Electromagnetic Waves", "الموجات الكهرومغناطيسية"),
    ("Geometric Optics", "البصريات الهندسية"),
    ("Wave Optics and Interference", "البصريات الموجية والتداخل"),
    ("Special Relativity", "النسبية الخاصة"),
    ("Quantum Physics Foundations", "أسس الفيزياء الكمّية"),
    ("Atomic and Molecular Structure", "التركيب الذري والجزيئي"),
    ("Semiconductors and Electronics", "أشباه الموصلات والإلكترونيات"),
    ("Nuclear Physics and Radiation", "الفيزياء النووية والإشعاع"),
    ("Physics of Modern Computing Devices", "فيزياء أجهزة الحوسبة الحديثة"),
]

TOPICS["ENG102"] = [
    ("Critical Reading and Analysis", "القراءة النقدية والتحليل"),
    ("Advanced Grammar and Style", "القواعد المتقدمة والأسلوب"),
    ("Writing Cohesive Essays", "كتابة مقالات مترابطة"),
    ("Argumentation and Persuasion", "الإقناع والحجاج"),
    ("Technical Reports", "التقارير الفنية"),
    ("Research Skills and Source Evaluation", "مهارات البحث وتقييم المصادر"),
    ("Citation Styles and Referencing", "أنماط التوثيق والاقتباس"),
    ("Presentations and Public Speaking", "العروض والتحدث أمام الجمهور"),
    ("Team Communication and Collaboration", "التواصل والتعاون داخل الفريق"),
    ("Writing About Technology", "الكتابة عن التكنولوجيا"),
    ("Intercultural Communication", "التواصل بين الثقافات"),
    ("Portfolio and Integrated Review", "ملف الأعمال والمراجعة المتكاملة"),
]

# ---------------------------------------------------------------------------
# SEMESTER 3
# ---------------------------------------------------------------------------
TOPICS["CS211"] = [
    ("Algorithm Analysis and Asymptotic Notation", "تحليل الخوارزميات والترميز المقارب"),
    ("Recurrences and the Master Theorem", "علاقات الاستدعاء ونظرية السيد"),
    ("Divide and Conquer", "التقسيم والتغلب"),
    ("Sorting Algorithms and Lower Bounds", "خوارزميات الترتيب والحدود الدنيا"),
    ("Greedy Algorithms", "الخوارزميات الجشعة"),
    ("Dynamic Programming", "البرمجة الديناميكية"),
    ("Graph Traversal: BFS and DFS", "مرور الرسوم: BFS و DFS"),
    ("Shortest Path Algorithms", "خوارزميات أقصر مسار"),
    ("Minimum Spanning Trees", "الحد الأدنى للأشجار الممتدة"),
    ("Network Flow", "تدفق الشبكات"),
    ("NP-Completeness and Reductions", "اكتمال NP والاختزال"),
    ("Approximation and Randomized Algorithms", "الخوارزميات التقريبية والعشوائية"),
]

TOPICS["CS212"] = [
    ("Computer Abstraction and Technology", "تجريد الحاسب والتقنية"),
    ("Instruction Set Architecture", "معمارية مجموعة التعليمات"),
    ("Arithmetic for Computers", "الحساب في الحاسب"),
    ("The Processor: Datapath and Control", "المعالج: مسار البيانات والتحكم"),
    ("Pipelining", "التداخل الزمني"),
    ("Memory Hierarchy and Caches", "هرمية الذاكرة والذاكرات الوسيطة"),
    ("Storage and I/O Systems", "أنظمة التخزين والإدخال والإخراج"),
    ("Assembly Language Fundamentals", "أساسيات لغة التجميع"),
    ("Registers, Addressing Modes and Instructions", "المسجّلات وأنماط العنونة والتعليمات"),
    ("Procedures and the Stack", "الإجراءات والمكدّس"),
    ("Interrupts and System Calls", "المقاطعات ونداءات النظام"),
    ("Performance Measurement and Parallelism", "قياس الأداء والتوازي"),
]

TOPICS["CS213"] = [
    ("Database Systems and Architecture", "نظم قواعد البيانات ومعماريتها"),
    ("The Relational Model", "النموذج العلائقي"),
    ("Relational Algebra", "الجبر العلائقي"),
    ("Entity-Relationship Modelling", "نمذجة الكيان والعلاقة"),
    ("SQL: Data Definition", "SQL: تعريف البيانات"),
    ("SQL: Queries and Joins", "SQL: الاستعلامات والوصلات"),
    ("SQL: Aggregation and Subqueries", "SQL: التجميع والاستعلامات الفرعية"),
    ("Functional Dependencies and Normalization", "الاعتماديات الدالية والتطبيع"),
    ("Transactions and Concurrency Control", "المعاملات والتحكم في التزامن"),
    ("Indexing and Query Optimization", "الفهرسة وتحسين الاستعلامات"),
    ("NoSQL and Distributed Databases", "NoSQL وقواعد البيانات الموزّعة"),
    ("Database Design Case Study", "دراسة حالة تصميم قاعدة بيانات"),
]

TOPICS["MATH201"] = [
    ("Techniques of Integration Revisited", "أساليب التكامل مرة أخرى"),
    ("Improper Integrals", "التكاملات المعتلة"),
    ("Infinite Series and Convergence Tests", "المتسلسلات اللانهائية واختبارات التقارب"),
    ("Power Series and Taylor Series", "متسلسلات القوى ومتسلسلات تايلور"),
    ("Partial Derivatives", "المشتقات الجزئية"),
    ("Multiple Integrals", "التكاملات المتعددة"),
    ("Vector Calculus", "حساب المتجهات"),
    ("Numerical Errors and Stability", "الأخطاء العددية والاستقرار"),
    ("Root Finding Methods", "طرق إيجاد الجذور"),
    ("Interpolation and Curve Fitting", "الاستيفاء وملاءمة المنحنيات"),
    ("Numerical Differentiation and Integration", "الاشتقاق والتكامل العددي"),
    ("Numerical Solutions of Differential Equations", "الحلول العددية للمعادلات التفاضلية"),
]

TOPICS["IS201"] = [
    ("Information Systems in Organizations", "نظم المعلومات في المنظمات"),
    ("Types of Information Systems", "أنواع نظم المعلومات"),
    ("Systems Development Life Cycle", "دورة حياة تطوير النظم"),
    ("Requirements Gathering and Analysis", "جمع المتطلبات وتحليلها"),
    ("Process Modelling", "نمذجة العمليات"),
    ("Data Modelling for Information Systems", "نمذجة البيانات لنظم المعلومات"),
    ("Systems Design", "تصميم النظم"),
    ("Enterprise Systems and ERP", "نظم المؤسسة وتخطيط الموارد"),
    ("Business Intelligence and Analytics", "ذكاء الأعمال والتحليلات"),
    ("E-Commerce and Digital Platforms", "التجارة الإلكترونية والمنصات الرقمية"),
    ("IT Governance and Strategy", "حوكمة تقنية المعلومات واستراتيجيتها"),
    ("Information Systems Case Study", "دراسة حالة في نظم المعلومات"),
]

TOPICS["ENG201"] = [
    ("Audience Analysis and Purpose", "تحليل الجمهور والغرض"),
    ("Structuring Technical Documents", "بناء المستندات الفنية"),
    ("Writing Specifications and Requirements", "كتابة المواصفات والمتطلبات"),
    ("Documenting Code and APIs", "توثيق الكود وواجهات البرمجة"),
    ("User Manuals and Guides", "أدلة المستخدم والإرشادات"),
    ("Data Visualization and Reporting", "تصوير البيانات وإعداد التقارير"),
    ("Proposals and Business Cases", "المقترحات ودراسات الجدوى"),
    ("Presenting Technical Work", "عرض العمل الفني"),
    ("Collaboration and Peer Review", "التعاون والمراجعة المتبادلة"),
    ("Editing and Proofreading", "التحرير والتصحيح اللغوي"),
    ("Professional Portfolios and Profiles", "ملفات الأعمال والملفات المهنية"),
    ("Integrated Technical Communication Project", "مشروع متكامل في التواصل الفني"),
]

# ---------------------------------------------------------------------------
# SEMESTER 4
# ---------------------------------------------------------------------------
TOPICS["CS214"] = [
    ("Operating System Roles and Structure", "أدوار نظام التشغيل وبنيته"),
    ("Processes and Process Management", "العمليات وإدارتها"),
    ("Threads and Multithreading", "الخيوط والتنفيذ متعدد الخيوط"),
    ("CPU Scheduling", "جدولة المعالج"),
    ("Process Synchronization", "تزامن العمليات"),
    ("Deadlocks", "الجمود"),
    ("Memory Management and Paging", "إدارة الذاكرة والتقسيم الصفحي"),
    ("Virtual Memory", "الذاكرة الافتراضية"),
    ("File Systems", "أنظمة الملفات"),
    ("I/O Systems and Device Management", "أنظمة الإدخال والإخراج وإدارة الأجهزة"),
    ("Protection and Security in Operating Systems", "الحماية والأمن في نظم التشغيل"),
    ("Case Study: Linux and Windows Internals", "دراسة حالة: أنظمة لينكس وويندوز"),
]

TOPICS["CS215"] = [
    ("Alphabets, Strings and Languages", "الأبجديات والنصوص واللغات"),
    ("Finite Automata", "الآلات المنتهية"),
    ("Nondeterminism and Equivalence", "اللا تحديد والتكافؤ"),
    ("Regular Expressions", "التعبيرات النمطية"),
    ("Properties of Regular Languages", "خصائص اللغات النمطية"),
    ("Context-Free Grammars", "القواعد الخالية من السياق"),
    ("Pushdown Automata", "الآلات ذات المكدّس"),
    ("Properties of Context-Free Languages", "خصائص اللغات الخالية من السياق"),
    ("Turing Machines", "آلات تورينج"),
    ("Decidability and the Halting Problem", "القابلية للتقرير ومشكلة التوقف"),
    ("Reducibility and Undecidability", "الاختزال وعدم القابلية للتقرير"),
    ("Complexity Classes: P and NP", "أصناف التعقيد: P و NP"),
]

TOPICS["CS216"] = [
    ("Software Engineering and the Software Crisis", "هندسة البرمجيات وأزمة البرمجيات"),
    ("Software Processes and Life Cycle Models", "عمليات البرمجيات ونماذج دورة الحياة"),
    ("Agile Development and Scrum", "التطوير الرشيق وسكرم"),
    ("Requirements Engineering", "هندسة المتطلبات"),
    ("System Modelling and UML", "نمذجة الأنظمة و UML"),
    ("Architectural Design", "التصميم المعماري"),
    ("Detailed Design and Design Patterns", "التصميم التفصيلي وأنماط التصميم"),
    ("Software Construction and Version Control", "بناء البرمجيات والتحكم في الإصدارات"),
    ("Software Testing", "اختبار البرمجيات"),
    ("Software Evolution and Maintenance", "تطوّر البرمجيات وصيانتها"),
    ("Project Planning and Estimation", "تخطيط المشروعات والتقدير"),
    ("Software Quality and Team Project", "جودة البرمجيات ومشروع الفريق"),
]

TOPICS["CS217"] = [
    ("Networks, the Internet and Protocols", "الشبكات والإنترنت والبروتوكولات"),
    ("Network Models: OSI and TCP/IP", "نماذج الشبكات: OSI و TCP/IP"),
    ("Physical Layer and Transmission Media", "الطبقة الفيزيائية ووسائط النقل"),
    ("Data Link Layer and Error Detection", "طبقة ربط البيانات وكشف الأخطاء"),
    ("Medium Access Control", "التحكم في الوصول للوسط"),
    ("The Network Layer and IP Addressing", "طبقة الشبكة وعنونة IP"),
    ("Routing Algorithms", "خوارزميات التوجيه"),
    ("The Transport Layer: TCP and UDP", "طبقة النقل: TCP و UDP"),
    ("Application Layer Protocols", "بروتوكولات طبقة التطبيقات"),
    ("Wireless and Mobile Networks", "الشبكات اللاسلكية والجوالة"),
    ("Network Security Fundamentals", "أساسيات أمن الشبكات"),
    ("Network Design and Administration Case Study", "دراسة حالة تصميم وإدارة الشبكات"),
]

TOPICS["AI201"] = [
    ("What Is Artificial Intelligence", "ما هو الذكاء الاصطناعي"),
    ("Intelligent Agents", "الوكلاء الأذكياء"),
    ("Problem Solving by Search", "حل المشكلات بالبحث"),
    ("Uninformed and Informed Search", "البحث الأعمى والموجّه"),
    ("Adversarial Search and Games", "البحث التنافسي والألعاب"),
    ("Constraint Satisfaction Problems", "مشكلات تحقيق القيود"),
    ("Logical Agents and Propositional Logic", "الوكلاء المنطقيون والمنطق القضوي"),
    ("First-Order Logic and Inference", "المنطق الرتبي الأول والاستدلال"),
    ("Knowledge Representation and Planning", "تمثيل المعرفة والتخطيط"),
    ("Reasoning Under Uncertainty", "الاستدلال تحت عدم اليقين"),
    ("Introduction to Machine Learning in AI", "مقدمة في تعلّم الآلة داخل الذكاء الاصطناعي"),
    ("AI Ethics and Applications", "أخلاقيات الذكاء الاصطناعي وتطبيقاته"),
]

TOPICS["ST201"] = [
    ("Data Types, Levels and Sources", "أنواع البيانات ومستوياتها ومصادرها"),
    ("Organizing and Visualizing Data", "تنظيم البيانات وتصويرها"),
    ("Measures of Center and Spread", "مقاييس النزعة المركزية والتشتت"),
    ("Probability Distributions Review", "مراجعة التوزيعات الاحتمالية"),
    ("Sampling Methods and Bias", "طرق المعاينة والتحيّز"),
    ("Estimation and Confidence Intervals", "التقدير وفترات الثقة"),
    ("Hypothesis Testing for One Sample", "اختبار الفروض لعينة واحدة"),
    ("Comparing Two Samples", "مقارنة عينتين"),
    ("Analysis of Variance", "تحليل التباين"),
    ("Chi-Square and Categorical Data", "مربع كاي والبيانات الفئوية"),
    ("Simple and Multiple Regression", "الانحدار البسيط والمتعدد"),
    ("Data Analysis Case Study", "دراسة حالة في تحليل البيانات"),
]
