# -*- coding: utf-8 -*-
"""Week-by-week topic map for every course (part 2: semesters 5-8).
12 teaching weeks each (weeks 1-6 and 9-14)."""

TOPICS = {}

# ---------------------------------------------------------------------------
# SEMESTER 5
# ---------------------------------------------------------------------------
TOPICS["CS311"] = [
    ("Compilers and the Translation Process", "المترجمات وعملية الترجمة"),
    ("Lexical Analysis and Tokens", "التحليل المعجمي والرموز"),
    ("Regular Expressions and Finite Automata in Lexers", "التعبيرات النمطية والآلات المنتهية في المحلّل"),
    ("Syntax Analysis and Context-Free Grammars", "التحليل النحوي والقواعد الخالية من السياق"),
    ("Top-Down Parsing", "التحليل من أعلى لأسفل"),
    ("Bottom-Up Parsing", "التحليل من أسفل لأعلى"),
    ("Semantic Analysis and Symbol Tables", "التحليل الدلالي وجداول الرموز"),
    ("Type Checking", "التحقق من الأنواع"),
    ("Intermediate Code Generation", "توليد الكود الوسيط"),
    ("Code Optimization", "تحسين الكود"),
    ("Code Generation and Register Allocation", "توليد الكود وتوزيع المسجّلات"),
    ("Building a Mini Compiler", "بناء مترجم مصغّر"),
]

TOPICS["CS312"] = [
    ("Introduction to Computer Graphics", "مقدمة في الرسم بالحاسب"),
    ("Graphics Hardware and the Display Pipeline", "عتاد الرسوم وخط عرض البيانات"),
    ("2D Transformations", "التحويلات ثنائية الأبعاد"),
    ("3D Transformations and Homogeneous Coordinates", "التحويلات ثلاثية الأبعاد والإحداثيات المتجانسة"),
    ("Viewing and Projection", "المشاهدة والإسقاط"),
    ("Line and Polygon Rasterization", "تحويل الخطوط والمضلّعات لصورة نقطية"),
    ("Clipping and Fill Algorithms", "خوارزميات القص والتعبئة"),
    ("Hidden Surface Removal", "إزالة الأسطح المخفية"),
    ("Shading and Illumination Models", "التظليل ونماذج الإضاءة"),
    ("Texture Mapping and Colour", "الخرائط النسيجية والألوان"),
    ("Curves, Surfaces and Modelling", "المنحنيات والأسطح والنمذجة"),
    ("Real-Time Rendering and a Graphics Project", "العرض في الزمن الحقيقي ومشروع رسوم"),
]

TOPICS["CS313"] = [
    ("How the Web Works", "إزاي الويب بيشتغل"),
    ("HTML and Semantic Markup", "HTML والترميز الدلالي"),
    ("CSS and Responsive Layout", "CSS والتخطيط المتجاوب"),
    ("JavaScript Fundamentals", "أساسيات JavaScript"),
    ("The Document Object Model", "نموذج كائن المستند"),
    ("Client-Side Interactivity and Events", "التفاعل في جهة العميل والأحداث"),
    ("Asynchronous JavaScript and APIs", "JavaScript اللاتزامني وواجهات البرمجة"),
    ("Front-End Frameworks", "أطر العمل في الواجهة الأمامية"),
    ("Server-Side Programming", "البرمجة في جهة الخادم"),
    ("Databases and the Back End", "قواعد البيانات والواجهة الخلفية"),
    ("REST APIs and Authentication", "واجهات REST والمصادقة"),
    ("Deploying a Full-Stack Web Application", "نشر تطبيق ويب متكامل"),
]

TOPICS["AI301"] = [
    ("What Is Machine Learning", "ما هو تعلّم الآلة"),
    ("The Machine Learning Workflow", "سير عمل تعلّم الآلة"),
    ("Supervised vs Unsupervised Learning", "التعلّم الموجّه مقابل غير الموجّه"),
    ("Linear Regression", "الانحدار الخطي"),
    ("Logistic Regression and Classification", "الانحدار اللوجستي والتصنيف"),
    ("Regularization and the Bias-Variance Trade-off", "التنظيم والمقايضة بين التحيّز والتباين"),
    ("Decision Trees and Ensemble Methods", "أشجار القرار وأساليب التجميع"),
    ("Support Vector Machines", "آلات المتجهات الداعمة"),
    ("k-Nearest Neighbours and Naive Bayes", "أقرب الجيران ونايف بايز"),
    ("Clustering: k-Means and Hierarchical", "العنقدة: k-Means والهرمية"),
    ("Dimensionality Reduction: PCA", "تقليل الأبعاد: PCA"),
    ("Model Evaluation, Cross-Validation and a Project", "تقييم النماذج والتحقق المتقاطع ومشروع"),
]

TOPICS["CS314"] = [
    ("Software Project Management Fundamentals", "أساسيات إدارة مشروعات البرمجيات"),
    ("Project Scope and Requirements Management", "إدارة نطاق المشروع والمتطلبات"),
    ("Work Breakdown Structures", "هياكل تجزئة العمل"),
    ("Effort Estimation Techniques", "أساليب تقدير الجهد"),
    ("Scheduling, Gantt and Critical Path", "الجدولة ومخطط جانت والمسار الحرج"),
    ("Risk Management", "إدارة المخاطر"),
    ("Resource and Team Management", "إدارة الموارد والفريق"),
    ("Agile Planning and Estimation", "التخطيط والتقدير الرشيق"),
    ("Quality Management", "إدارة الجودة"),
    ("Configuration and Change Management", "إدارة الإعدادات والتغيير"),
    ("Monitoring, Control and Metrics", "المتابعة والتحكم والمقاييس"),
    ("Project Closure and Case Study", "إغلاق المشروع ودراسة حالة"),
]

TOPICS["IS301"] = [
    ("Introduction to Human-Computer Interaction", "مقدمة في التفاعل بين الإنسان والحاسب"),
    ("Human Capabilities and Perception", "قدرات الإنسان والإدراك"),
    ("Interaction Design Principles", "مبادئ تصميم التفاعل"),
    ("Usability and User Experience", "قابلية الاستخدام وتجربة المستخدم"),
    ("Designing for the User: Personas and Scenarios", "التصميم للمستخدم: الشخصيات والسيناريوهات"),
    ("Prototyping: Low and High Fidelity", "النماذج الأولية: منخفضة وعالية الدقة"),
    ("Visual Design and Layout", "التصميم البصري والتخطيط"),
    ("Accessibility and Inclusive Design", "إمكانية الوصول والتصميم الشامل"),
    ("Evaluation Methods and Usability Testing", "أساليب التقييم واختبار قابلية الاستخدام"),
    ("Interaction Paradigms and Mobile Design", "أنماط التفاعل وتصميم الموبايل"),
    ("Designing for Emerging Interfaces", "التصميم للواجهات الناشئة"),
    ("HCI Design Project", "مشروع تصميم في التفاعل بين الإنسان والحاسب"),
]

# ---------------------------------------------------------------------------
# SEMESTER 6
# ---------------------------------------------------------------------------
TOPICS["CS321"] = [
    ("Introduction to Distributed Systems", "مقدمة في النظم الموزّعة"),
    ("Distributed System Models and Architectures", "نماذج النظم الموزّعة ومعمارياتها"),
    ("Processes and Threads in Distributed Systems", "العمليات والخيوط في النظم الموزّعة"),
    ("Communication and Remote Invocation", "التواصل والاستدعاء عن بُعد"),
    ("Naming and Name Services", "التسمية وخدمات الأسماء"),
    ("Synchronization and Logical Clocks", "التزامن والساعات المنطقية"),
    ("Consistency and Replication", "الاتساق والنسخ المتماثل"),
    ("Fault Tolerance and Recovery", "تحمّل الأعطال والاستعادة"),
    ("Distributed Transactions", "المعاملات الموزّعة"),
    ("Distributed File Systems", "أنظمة الملفات الموزّعة"),
    ("Consensus and Leader Election", "الإجماع وانتخاب القائد"),
    ("Building a Distributed Application", "بناء تطبيق موزّع"),
]

TOPICS["AI302"] = [
    ("From Machine Learning to Deep Learning", "من تعلّم الآلة إلى التعلّم العميق"),
    ("Neural Networks and Perceptrons", "الشبكات العصبية والبيرسيبترون"),
    ("Activation Functions and Forward Propagation", "دوال التنشيط والانتشار الأمامي"),
    ("Backpropagation and Gradient Descent", "الانتشار العكسي والانحدار التدريجي"),
    ("Training Deep Networks and Regularization", "تدريب الشبكات العميقة والتنظيم"),
    ("Optimization for Deep Learning", "التحسين للتعلّم العميق"),
    ("Convolutional Neural Networks", "الشبكات العصبية الالتفافية"),
    ("Recurrent Networks and Sequence Modelling", "الشبكات التكرارية ونمذجة المتسلسلات"),
    ("Attention and Transformers", "الانتباه والمحوّلات"),
    ("Autoencoders and Representation Learning", "المشفّرات الذاتية وتعلّم التمثيل"),
    ("Generative Models: GANs and Diffusion", "النماذج التوليدية: GANs والانتشار"),
    ("Frameworks and a Deep Learning Project", "أطر العمل ومشروع تعلّم عميق"),
]

TOPICS["CS322"] = [
    ("Security Goals and Threat Models", "أهداف الأمن ونماذج التهديد"),
    ("Classical Cryptography", "التشفير الكلاسيكي"),
    ("Symmetric Encryption and Block Ciphers", "التشفير المتماثل وتشفير الكتل"),
    ("The Data Encryption Standard and AES", "معيار تشفير البيانات و AES"),
    ("Asymmetric Encryption and RSA", "التشفير غير المتماثل و RSA"),
    ("Key Management and Exchange", "إدارة المفاتيح وتبادلها"),
    ("Hash Functions and Message Authentication", "دوال التقطيع ومصادقة الرسائل"),
    ("Digital Signatures and Certificates", "التوقيعات الرقمية والشهادات"),
    ("Authentication Protocols", "بروتوكولات المصادقة"),
    ("Network and Web Security", "أمن الشبكات والويب"),
    ("Malware, Attacks and Intrusion Detection", "البرمجيات الخبيثة والهجمات وكشف التسلل"),
    ("Applied Cryptography and a Security Project", "التشفير التطبيقي ومشروع أمن"),
]

TOPICS["CS323"] = [
    ("Software Architecture Fundamentals", "أساسيات معمارية البرمجيات"),
    ("Architectural Views and Documentation", "وجهات النظر المعمارية وتوثيقها"),
    ("Quality Attributes and Trade-offs", "خصائص الجودة والمقايضات"),
    ("Layered and Client-Server Architectures", "المعماريات الطبقية والعميل والخادم"),
    ("Microservices and Distributed Architecture", "الخدمات المصغّرة والمعمارية الموزّعة"),
    ("Event-Driven Architecture", "المعمارية القائمة على الأحداث"),
    ("Design Principles and SOLID Revisited", "مبادئ التصميم و SOLID مرة أخرى"),
    ("Creational Design Patterns", "أنماط التصميم الإنشائية"),
    ("Structural Design Patterns", "أنماط التصميم البنيوية"),
    ("Behavioural Design Patterns", "أنماط التصميم السلوكية"),
    ("Anti-Patterns and Refactoring", "الأنماط المضادة وإعادة الهيكلة"),
    ("Architecture Evaluation and Case Study", "تقييم المعمارية ودراسة حالة"),
]

TOPICS["CS324"] = [
    ("Cloud Computing Concepts and Models", "مفاهيم الحوسبة السحابية ونماذجها"),
    ("Service Models: IaaS, PaaS, SaaS", "نماذج الخدمة: IaaS و PaaS و SaaS"),
    ("Deployment Models and Providers", "نماذج النشر ومزوّدو الخدمة"),
    ("Virtualization and Containers", "الافتراضية والحاويات"),
    ("Cloud Storage and Databases", "التخزين وقواعد البيانات السحابية"),
    ("Compute Services and Auto-Scaling", "خدمات الحوسبة والتحجيم التلقائي"),
    ("Networking in the Cloud", "الشبكات في السحابة"),
    ("Serverless Computing", "الحوسبة بلا خوادم"),
    ("DevOps and CI/CD in the Cloud", "DevOps والتكامل والنشر المستمر"),
    ("Cloud Security and Identity", "أمن السحابة والهوية"),
    ("Cost Optimization and Monitoring", "تحسين التكلفة والمتابعة"),
    ("Deploying an Application on the Cloud", "نشر تطبيق على السحابة"),
]

TOPICS["ELEC-DS"] = [
    ("Data Science and the Data Lifecycle", "علم البيانات ودورة حياة البيانات"),
    ("Data Collection and Web Scraping", "جمع البيانات وكشط الويب"),
    ("Data Cleaning and Preprocessing", "تنظيف البيانات والمعالجة المسبقة"),
    ("Exploratory Data Analysis", "التحليل الاستكشافي للبيانات"),
    ("Feature Engineering", "هندسة الخصائص"),
    ("Big Data Concepts and the 5 Vs", "مفاهيم البيانات الضخمة ومحدداتها الخمسة"),
    ("Distributed Storage and Hadoop", "التخزين الموزّع و Hadoop"),
    ("MapReduce and Spark", "MapReduce و Spark"),
    ("Streaming Data and Real-Time Analytics", "بيانات التدفق والتحليلات الفورية"),
    ("Data Pipelines and Workflow Tools", "خطوط البيانات وأدوات سير العمل"),
    ("Data Governance and Ethics", "حوكمة البيانات وأخلاقياتها"),
    ("End-to-End Data Science Project", "مشروع علم بيانات متكامل"),
]

# ---------------------------------------------------------------------------
# SEMESTER 7
# ---------------------------------------------------------------------------
TOPICS["AI401"] = [
    ("Introduction to Natural Language Processing", "مقدمة في معالجة اللغات الطبيعية"),
    ("Text Preprocessing and Normalization", "المعالجة المسبقة للنصوص وتوحيدها"),
    ("Regular Expressions and Rule-Based NLP", "التعبيرات النمطية ومعالجة اللغات بالقواعد"),
    ("Language Models: n-grams to Neural", "نماذج اللغة: من n-grams للعصبية"),
    ("Word Embeddings: Word2Vec and GloVe", "تمثيل الكلمات: Word2Vec و GloVe"),
    ("Part-of-Speech Tagging", "وسم أجزاء الكلام"),
    ("Syntactic Parsing", "التحليل النحوي"),
    ("Named Entity Recognition", "التعرّف على الكيانات المسمّاة"),
    ("Sentiment Analysis and Text Classification", "تحليل المشاعر وتصنيف النصوص"),
    ("Sequence Models and Transformers for NLP", "نماذج المتسلسلات والمحوّلات لمعالجة اللغات"),
    ("Machine Translation and Summarization", "الترجمة الآلية والتلخيص"),
    ("Large Language Models and an NLP Project", "النماذج اللغوية الضخمة ومشروع معالجة لغات"),
]

TOPICS["AI402"] = [
    ("Introduction to Computer Vision", "مقدمة في الرؤية بالحاسب"),
    ("Digital Image Formation and Representation", "تكوين الصورة الرقمية وتمثيلها"),
    ("Image Filtering and Convolution", "تصفية الصور والالتفاف"),
    ("Edge Detection and Feature Extraction", "كشف الحواف واستخراج الخصائص"),
    ("Corner and Blob Detection", "كشف الزوايا والبقع"),
    ("Feature Matching and Image Alignment", "مطابقة الخصائص ومحاذاة الصور"),
    ("Camera Models and Geometry", "نماذج الكاميرا والهندسة"),
    ("Convolutional Networks for Vision", "الشبكات الالتفافية للرؤية"),
    ("Object Detection", "كشف الأجسام"),
    ("Image Segmentation", "تقسيم الصور"),
    ("Image Classification and Recognition", "تصنيف الصور والتعرّف عليها"),
    ("Vision Applications and a Project", "تطبيقات الرؤية ومشروع"),
]

TOPICS["CS411"] = [
    ("Advanced Data Models and Systems", "النماذج والأنظمة المتقدمة للبيانات"),
    ("Query Processing and Optimization", "معالجة الاستعلامات وتحسينها"),
    ("Advanced Indexing and Storage", "الفهرسة والتخزين المتقدم"),
    ("Transaction Management and Recovery", "إدارة المعاملات والاستعادة"),
    ("Distributed and Parallel Databases", "قواعد البيانات الموزّعة والمتوازية"),
    ("Data Warehousing and OLAP", "مستودعات البيانات والمعالجة التحليلية"),
    ("ETL and Data Integration", "ETL وتكامل البيانات"),
    ("Column Stores and Analytical Databases", "المخازن العمودية وقواعد البيانات التحليلية"),
    ("NoSQL Databases and CAP", "قواعد بيانات NoSQL ونظرية CAP"),
    ("Big Data Processing Frameworks", "أطر معالجة البيانات الضخمة"),
    ("Graph Databases and Analytics", "قواعد بيانات الرسوم وتحليلاتها"),
    ("Modern Data Architecture Case Study", "دراسة حالة معمارية بيانات حديثة"),
]

TOPICS["CS412"] = [
    ("Software Quality and Testing Fundamentals", "أساسيات جودة البرمجيات والاختبار"),
    ("The Testing Life Cycle and the V-Model", "دورة حياة الاختبار ونموذج V"),
    ("Static Testing and Reviews", "الاختبار الساكن والمراجعات"),
    ("Black-Box Testing Techniques", "أساليب الاختبار الصندوقي الأسود"),
    ("White-Box Testing and Coverage", "الاختبار الصندوقي الأبيض والتغطية"),
    ("Unit Testing and Test-Driven Development", "اختبار الوحدات والتطوير القائم على الاختبار"),
    ("Integration and System Testing", "اختبار التكامل والنظام"),
    ("Performance, Load and Stress Testing", "اختبار الأداء والتحميل والإجهاد"),
    ("Automated Testing and Frameworks", "الاختبار الآلي وأطر العمل"),
    ("Defect Management and Metrics", "إدارة العيوب والمقاييس"),
    ("Quality Assurance and Standards", "ضمان الجودة والمعايير"),
    ("Testing Project and Continuous Quality", "مشروع اختبار والجودة المستمرة"),
]

TOPICS["CS413"] = [
    ("Graduation Project Orientation and Teams", "توجيه مشروع التخرج والفرق"),
    ("Problem Identification and Idea Generation", "تحديد المشكلة وتوليد الأفكار"),
    ("Literature Review and Background Research", "مراجعة الأدبيات والبحث في الخلفية"),
    ("Requirements and Scope Definition", "تحديد المتطلبات والنطاق"),
    ("Feasibility Study and Planning", "دراسة الجدوى والتخطيط"),
    ("System Design and Architecture", "تصميم النظام والمعمارية"),
    ("Technology Selection and Prototyping", "اختيار التقنية والنماذج الأولية"),
    ("First Implementation Sprint", "أول دورة تنفيذ"),
    ("Second Implementation Sprint", "ثاني دورة تنفيذ"),
    ("Testing and Validation", "الاختبار والتحقق"),
    ("Project Documentation and Report", "توثيق المشروع والتقرير"),
    ("First Milestone Presentation and Demo", "عرض وتسليم أول مرحلة"),
]

TOPICS["ELEC-CY"] = [
    ("Cybersecurity Landscape and Threats", "مشهد الأمن السيبراني والتهديدات"),
    ("Security Architecture and Defence in Depth", "معمارية الأمن والدفاع متعدد الطبقات"),
    ("Vulnerability Assessment", "تقييم الثغرات"),
    ("Penetration Testing Methodology", "منهجية اختبار الاختراق"),
    ("Web Application Security", "أمن تطبيقات الويب"),
    ("Network Security and Firewalls", "أمن الشبكات والجدران النارية"),
    ("Malware Analysis Basics", "أساسيات تحليل البرمجيات الخبيثة"),
    ("Incident Response and Forensics", "الاستجابة للحوادث والتحليل الجنائي"),
    ("Identity and Access Management", "إدارة الهوية والوصول"),
    ("Security Operations and SIEM", "عمليات الأمن وأنظمة SIEM"),
    ("Governance, Risk and Compliance", "الحوكمة والمخاطر والالتزام"),
    ("Security Lab and Capture-the-Flag", "معمل أمن ومسابقة التقاط الأعلام"),
]

# ---------------------------------------------------------------------------
# SEMESTER 8
# ---------------------------------------------------------------------------
TOPICS["AI403"] = [
    ("From Supervised to Reinforcement Learning", "من التعلّم الموجّه إلى التعلّم المعزّز"),
    ("Markov Decision Processes", "عمليات قرار ماركوف"),
    ("Return, Value Functions and Bellman Equations", "العائد ودوال القيمة ومعادلات بيلمان"),
    ("Dynamic Programming for RL", "البرمجة الديناميكية للتعلّم المعزّز"),
    ("Monte Carlo Methods", "أساليب مونت كارلو"),
    ("Temporal-Difference Learning", "التعلّم بالفرق الزمني"),
    ("Exploration vs Exploitation and Multi-Armed Bandits", "الاستكشاف مقابل الاستغلال وأذرع البانديت"),
    ("On-Policy and Off-Policy Learning", "التعلّم على السياسة وخارجها"),
    ("Deep Q-Learning", "التعلّم العميق بالقيم"),
    ("Policy Gradient Methods", "أساليب انحدار السياسة"),
    ("Actor-Critic Methods", "أساليب الممثل والناقد"),
    ("RL Applications and a Project", "تطبيقات التعلّم المعزّز ومشروع"),
]

TOPICS["CS421"] = [
    ("Review of Algorithm Design Paradigms", "مراجعة أنماط تصميم الخوارزميات"),
    ("Advanced Complexity Analysis", "تحليل التعقيد المتقدم"),
    ("Amortized Analysis", "التحليل المطفأ"),
    ("Randomized Algorithms", "الخوارزميات العشوائية"),
    ("Approximation Algorithms", "الخوارزميات التقريبية"),
    ("Linear Programming and Duality", "البرمجة الخطية والثنائية"),
    ("Network Flow and Matching", "تدفق الشبكات والمطابقة"),
    ("Online Algorithms and Competitive Analysis", "الخوارزميات الفورية والتحليل التنافسي"),
    ("Parameterized and Fixed-Parameter Algorithms", "الخوارزميات المُعاملية"),
    ("Advanced Graph Algorithms", "خوارزميات الرسوم المتقدمة"),
    ("Parallel and External-Memory Algorithms", "الخوارزميات المتوازية والذاكرة الخارجية"),
    ("Research Frontiers and Algorithm Project", "آفاق البحث ومشروع خوارزميات"),
]

TOPICS["CS422"] = [
    ("Ethics and the Computing Professional", "الأخلاقيات ومهني الحوسبة"),
    ("Professional Codes of Conduct", "مواثيق السلوك المهني"),
    ("Privacy, Data Protection and Surveillance", "الخصوصية وحماية البيانات والمراقبة"),
    ("Security, Safety and Reliability", "الأمن والسلامة والموثوقية"),
    ("Intellectual Property and Licensing", "الملكية الفكرية والترخيص"),
    ("Algorithmic Bias and Fairness", "التحيّز الخوارزمي والعدالة"),
    ("Responsible AI and Autonomy", "الذكاء الاصطناعي المسؤول والاستقلالية"),
    ("Social Media, Misinformation and Society", "التواصل الاجتماعي والمعلومات المضللة والمجتمع"),
    ("Environmental and Sustainability Computing", "حوسبة البيئة والاستدامة"),
    ("Accessibility and Digital Inclusion", "إمكانية الوصول والشمول الرقمي"),
    ("Legal and Regulatory Frameworks", "الأطر القانونية والتنظيمية"),
    ("Case Studies and an Ethics Position Paper", "دراسات حالة وورقة موقف أخلاقية"),
]

TOPICS["CS423"] = [
    ("Graduation Project II Orientation", "توجيه مشروع التخرج 2"),
    ("Refining Requirements and Design", "صقل المتطلبات والتصميم"),
    ("Scaling and Optimization", "التحجيم والتحسين"),
    ("Security and Robustness Hardening", "تقوية الأمن والمتانة"),
    ("User Evaluation and Feedback", "تقييم المستخدم والتغذية الراجعة"),
    ("Final Integration", "التكامل النهائي"),
    ("Deployment and Release", "النشر والإصدار"),
    ("Comprehensive Testing", "الاختبار الشامل"),
    ("Final Documentation and Thesis", "التوثيق النهائي والرسالة"),
    ("Presentation and Demonstration", "العرض والتقديم"),
    ("Evaluation Criteria and Defence", "معايير التقييم والمناقشة"),
    ("Project Closure and Handover", "إغلاق المشروع والتسليم"),
]

TOPICS["ELEC-MOBILE"] = [
    ("Mobile Platforms and Ecosystems", "منصات الموبايل ونظمها البيئية"),
    ("Mobile App Architecture and Lifecycle", "معمارية تطبيق الموبايل ودورة حياته"),
    ("UI and Layout for Mobile", "واجهة المستخدم والتخطيط للموبايل"),
    ("Navigation and State Management", "التنقل وإدارة الحالة"),
    ("Data Storage on Device", "تخزين البيانات على الجهاز"),
    ("Networking and Consuming APIs", "الشبكات واستهلاك واجهات البرمجة"),
    ("Background Tasks and Notifications", "المهام الخلفية والإشعارات"),
    ("Sensors and Device Hardware", "المستشعرات وعتاد الجهاز"),
    ("Mobile Security and Permissions", "أمن الموبايل والصلاحيات"),
    ("Testing and Debugging Mobile Apps", "اختبار وتنقيح تطبيقات الموبايل"),
    ("Publishing to App Stores", "النشر على متاجر التطبيقات"),
    ("Building and Shipping a Mobile App", "بناء وإطلاق تطبيق موبايل"),
]

TOPICS["ELEC-GAME"] = [
    ("Game Development and Genres", "تطوير الألعاب وأنواعها"),
    ("Game Engines and Tooling", "محرّكات الألعاب وأدواتها"),
    ("Game Loops and Time Management", "حلقات اللعبة وإدارة الزمن"),
    ("2D Graphics and Sprite Animation", "رسوم ثنائية الأبعاد وتحريك الكائنات"),
    ("3D Graphics in Games", "الرسوم ثلاثية الأبعاد في الألعاب"),
    ("Game Physics and Collision", "فيزياء اللعبة والتصادم"),
    ("Input Handling and Controls", "معالجة المدخلات وأدوات التحكم"),
    ("Game AI and Behaviour", "ذكاء اللعبة والسلوك"),
    ("Level Design and World Building", "تصميم المراحل وبناء العالم"),
    ("Audio, Effects and Polish", "الصوت والمؤثرات والصقل"),
    ("Performance Optimization for Games", "تحسين الأداء في الألعاب"),
    ("Building and Shipping a Game", "بناء وإطلاق لعبة"),
]
