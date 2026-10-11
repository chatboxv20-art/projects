# الأسبوع 2 — الفصل 5

> الدرس ده بيغطّي موضوع واحد في كل مقرر من مقررات الفصل، وكل الشرح مكتوب بالعامية المصرية مع البلوك الإنجليزي الكامل جنبه.

**المقررات اللي في الدرس ده:** CS311 (تصميم المترجمات)، CS312 (الرسم بالحاسب)، CS313 (تقنيات الويب)، AI301 (تعلّم الآلة)، CS314 (إدارة مشروعات البرمجيات)، IS301 (التفاعل بين الإنسان والحاسب)

---

# القسم الأول: تصميم المترجمات (CS311)

## Lexical Analysis and Tokens (التحليل المعجمي والرموز)

Lexical Analysis and Tokens (التحليل المعجمي والرموز)
English Definition: Lexical Analysis and Tokens is a core topic in Theory of Computation. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: التحليل المعجمي والرموز موضوع أساسي في نظرية الحسابات. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Lexical Analysis and Tokens** is the focus of this lesson. Theory of computation studies what can be computed and at what cost, using automata, grammars and Turing machines.

**Egyptian Arabic (اللهجة المصرية):**

**التحليل المعجمي والرموز** هو محور الدرس ده. نظرية الحسابات بتدرس إيه اللي ممكن يتحسب وبأي تكلفة، باستخدام الآلات المجرّدة والقواعد وآلات تورينج.

### Why It Exists (ليه موجود)

It sets the limits of computing: some problems are unsolvable and some are intractable. Without a clear grasp of Lexical Analysis and Tokens, the rest of Theory of Computation has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

بتحدّد حدود الحوسبة: في مشكلات مستحيلة الحل و في مشكلات مستعصية. ومن غير إدراك واضح لموضوع التحليل المعجمي والرموز، باقي نظرية الحسابات ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Lexical Analysis and Tokens is where the theory of Theory of Computation meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع التحليل المعجمي والرموز هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

### Where It Is Used (بنستخدمه فين)

- Compiler and language design
- Pattern matching and regex
- Complexity analysis
- Verification and formal methods
- Decidability questions

**Egyptian Arabic (اللهجة المصرية):**

- تصميم المترجمات واللغات
- مطابقة الأنماط والتعبيرات النمطية
- تحليل التعقيد
- التحقق والأساليب الصورية
- أسئلة القابلية للتقرير

### Real-World Usage and Relevance in the Field (الاستخدام والملاءمة في المجال)

Regular expressions in a search box work because regular languages are exactly what finite automata recognize.

**Egyptian Arabic (اللهجة المصرية):**

التعبيرات النمطية في صندوق البحث بتشتغل لأن اللغات النمطية هي بالظبط اللي الآلات المنتهية بتتعرف عليها.

### Advantages (المميزات)

- Defines what is computable
- Gives rigorous models for languages
- Underpins compilers and complexity
- Sharpens formal reasoning

**Egyptian Arabic (اللهجة المصرية):**

- بتحدّد إيه اللي قابل للحساب
- بتدي نماذج صارمة للغات
- بتدعم المترجمات والتعقيد
- بتصقل التفكير الصوري

### Limitations (الحدود)

- Very abstract for beginners
- Proofs require care
- Models idealize real machines

**Egyptian Arabic (اللهجة المصرية):**

- مجردة جدًا للمبتدئين
- البراهين محتاجة دقة
- النماذج بتمثّل الآلات الحقيقية بشكل مثالي

### Best Practices (أحسن الممارسات)

- Build automata for simple languages first
- Practise conversion between models
- Draw state diagrams for every proof
- Connect each model to a real tool

**Egyptian Arabic (اللهجة المصرية):**

- ابني آلات للغات بسيطة الأول
- اتمرّن على التحويل بين النماذج
- ارسم مخططات الحالات لكل برهان
- اربط كل نموذج بأداة حقيقية

### Common Mistakes (الأخطاء الشائعة)

- Confusing DFA and NFA
- Forgetting to prove non-regularity
- Mixing undecidable with intractable
- Errors in grammar derivations

**Egyptian Arabic (اللهجة المصرية):**

- الخلط بين DFA و NFA
- نسيان إثبات عدم النمطية
- الخلط بين غير القابل للتقرير والمستعصي
- أخطاء في اشتقاق القواعد

### Practical Example (مثال عملي)

A program that checks whether a string has balanced brackets is a pushdown automaton, which is why a stack is the natural implementation.

**Egyptian Arabic (اللهجة المصرية):**

برنامج بيتأكد إن الأقواس متوازنة في نص هو آلة ذات مكدّس، وعشان كده المكدّس هو التنفيذ الطبيعي.

### Hands-On Exercise (تمرين عملي بإيدك)

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Lexical Analysis and Tokens, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نطام صغير تعرفه. اكتب: (1) الموقف في التحليل المعجمي والرموز، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Lexical Analysis and Tokens in one sentence of your own words.
2. Give two situations where Lexical Analysis and Tokens changes a technical decision.
3. Name one limitation of Lexical Analysis and Tokens and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف التحليل المعجمي والرموز في جملة واحدة بكلامك.
2. ادي موقفين التحليل المعجمي والرموز بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود التحليل المعجمي والرموز واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Lexical Analysis and Tokens? (a) a formality with no use (b) a working tool inside Theory of Computation (c) an unrelated subject.
Q2. True or false: Lexical Analysis and Tokens has no limitations.
Q3. In one line, why does Lexical Analysis and Tokens matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـالتحليل المعجمي والرموز؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه نظرية الحسابات (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: التحليل المعجمي والرموز مالوش حدود.
س3. في سطر واحد، ليه التحليل المعجمي والرموز مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Theory of Computation.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه نظرية الحسابات.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Lexical Analysis and Tokens to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها التحليل المعجمي والرموز على برنامج أو نطام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Lexical Analysis and Tokens until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف التحليل المعجمي والرموز تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الثاني: الرسم بالحاسب (CS312)

## Graphics Hardware and the Display Pipeline (عتاد الرسوم وخط عرض البيانات)

Graphics Hardware and the Display Pipeline (عتاد الرسوم وخط عرض البيانات)
English Definition: Graphics Hardware and the Display Pipeline is a core topic in Computer Graphics. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: عتاد الرسوم وخط عرض البيانات موضوع أساسي في الرسم بالحاسب. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Graphics Hardware and the Display Pipeline** is the focus of this lesson. Computer graphics generates and manipulates images using geometry, transformations, rasterization and shading on graphics hardware.

**Egyptian Arabic (اللهجة المصرية):**

**عتاد الرسوم وخط عرض البيانات** هو محور الدرس ده. الرسم بالحاسب بيولّد ويتعامل مع الصور باستخدام الهندسة والتحويلات والتحويل النقطي والتظليل على عتاد الرسوم.

### Why It Exists (ليه موجود)

Games, films, CAD, visualization and AR/VR all depend on graphics pipelines. Without a clear grasp of Graphics Hardware and the Display Pipeline, the rest of Computer Graphics has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

الألعاب والأفلام والتصميم بالحاسب والتصوير المرئي والواقع المعزّز كلهم بيعتمدوا على خطوط عرض الرسوم. ومن غير إدراك واضح لموضوع عتاد الرسوم وخط عرض البيانات، باقي الرسم بالحاسب ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Graphics Hardware and the Display Pipeline is where the theory of Computer Graphics meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع عتاد الرسوم وخط عرض البيانات هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

### Where It Is Used (بنستخدمه فين)

- Video games and animation
- CAD and engineering design
- Data and scientific visualization
- AR and VR
- Image processing

**Egyptian Arabic (اللهجة المصرية):**

- ألعاب الفيديو والتحريك
- التصميم الهندسي بالحاسب
- تصوير البيانات والعلوم
- الواقع المعزّز والافتراضي
- معالجة الصور

### Real-World Usage and Relevance in the Field (الاستخدام والملاءمة في المجال)

Every frame in a game transforms thousands of 3D vertices into a 2D image in milliseconds - that is the graphics pipeline.

**Egyptian Arabic (اللهجة المصرية):**

كل إطار في لعبة بيحوّل آلاف الرؤوس ثلاثية الأبعاد لصورة ثنائية الأبعاد في أجزاء من الثانية - ده خط عرض الرسوم.

### Advantages (المميزات)

- Creates realistic and interactive visuals
- Leverages fast GPU hardware
- Foundation for games and AR/VR
- Combines math and art

**Egyptian Arabic (اللهجة المصرية):**

- بيولّد صور واقعية وتفاعلية
- بيستفيد من عتاد GPU السريع
- أساس للألعاب والواقع المعزّز
- بيدمج الرياضيات والفن

### Limitations (الحدود)

- Complex math and matrix work
- Performance is critical
- Hardware differences matter
- Realism is expensive

**Egyptian Arabic (اللهجة المصرية):**

- رياضيات ومصفوفات معقّدة
- الأداء حرج
- اختلافات العتاد بتفرق
- الواقعية مكلفة

### Best Practices (أحسن الممارسات)

- Master transformations and coordinate spaces
- Understand the rendering pipeline stages
- Profile GPU performance
- Start with simple scenes

**Egyptian Arabic (اللهجة المصرية):**

- اتقن التحويلات وفضاءات الإحداثيات
- افهم مراحل خط العرض
- حلّل أداء GPU
- ابدأ بمشاهد بسيطة

### Common Mistakes (الأخطاء الشائعة)

- Confusing model, world and view spaces
- Wrong matrix multiplication order
- Ignoring normalization of vectors
- Not culling off-screen geometry

**Egyptian Arabic (اللهجة المصرية):**

- الخلط بين فضاءات النموذج والعالم والعرض
- ترتيب ضرب المصفوفات الغلط
- تجاهل تطبيع المتجهات
- عدم إسقاط الهندسة خارج الشاشة

### Practical Example (مثال عملي)

Rotating a character model means multiplying every vertex by a rotation matrix, then projecting the result onto the screen.

**Egyptian Arabic (اللهجة المصرية):**

تدوير مجسم شخصية معناه ضرب كل رأس في مصفوفة دوران، وبعدين إسقاط الناتج على الشاشة.

### Hands-On Exercise (تمرين عملي بإيدك)

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Graphics Hardware and the Display Pipeline, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نطام صغير تعرفه. اكتب: (1) الموقف في عتاد الرسوم وخط عرض البيانات، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Graphics Hardware and the Display Pipeline in one sentence of your own words.
2. Give two situations where Graphics Hardware and the Display Pipeline changes a technical decision.
3. Name one limitation of Graphics Hardware and the Display Pipeline and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف عتاد الرسوم وخط عرض البيانات في جملة واحدة بكلامك.
2. ادي موقفين عتاد الرسوم وخط عرض البيانات بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود عتاد الرسوم وخط عرض البيانات واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Graphics Hardware and the Display Pipeline? (a) a formality with no use (b) a working tool inside Computer Graphics (c) an unrelated subject.
Q2. True or false: Graphics Hardware and the Display Pipeline has no limitations.
Q3. In one line, why does Graphics Hardware and the Display Pipeline matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـعتاد الرسوم وخط عرض البيانات؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه الرسم بالحاسب (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: عتاد الرسوم وخط عرض البيانات مالوش حدود.
س3. في سطر واحد، ليه عتاد الرسوم وخط عرض البيانات مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Computer Graphics.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه الرسم بالحاسب.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Graphics Hardware and the Display Pipeline to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها عتاد الرسوم وخط عرض البيانات على برنامج أو نطام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Graphics Hardware and the Display Pipeline until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف عتاد الرسوم وخط عرض البيانات تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الثالث: تقنيات الويب (CS313)

## HTML and Semantic Markup (HTML والترميز الدلالي)

HTML and Semantic Markup (HTML والترميز الدلالي)
English Definition: HTML and Semantic Markup is a core topic in Web Technologies. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: HTML والترميز الدلالي موضوع أساسي في تقنيات الويب. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**HTML and Semantic Markup** is the focus of this lesson. Web technologies cover how browsers, servers and databases work together to deliver interactive applications over HTTP.

**Egyptian Arabic (اللهجة المصرية):**

**HTML والترميز الدلالي** هو محور الدرس ده. تقنيات الويب بتغطي إزاي المتصفحات والسيرفرات وقواعد البيانات بتشتغل مع بعض لتقديم تطبيقات تفاعلية عبر HTTP.

### Why It Exists (ليه موجود)

The web is the default platform for software delivery, so every developer needs front-end and back-end skills. Without a clear grasp of HTML and Semantic Markup, the rest of Web Technologies has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

الويب هو المنصة الافتراضية لتسليم البرمجيات، وعشان كده كل مطوّر محتاج مهارات الواجهة الأمامية والخلفية. ومن غير إدراك واضح لموضوع HTML والترميز الدلالي، باقي تقنيات الويب ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, HTML and Semantic Markup is where the theory of Web Technologies meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع HTML والترميز الدلالي هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

### Where It Is Used (بنستخدمه فين)

- Websites and web apps
- E-commerce platforms
- Dashboards and admin panels
- APIs and integrations
- Progressive web apps

**Egyptian Arabic (اللهجة المصرية):**

- المواقع وتطبيقات الويب
- منصات التجارة الإلكترونية
- لوحات المعلومات ولوحات التحكم
- واجهات البرمجة والتكاملات
- تطبيقات الويب التقدمية

### Real-World Usage and Relevance in the Field (الاستخدام والملاءمة في المجال)

When you order food online, the front end collects your order, an API validates it, and a database stores it - the full web stack in seconds.

**Egyptian Arabic (اللهجة المصرية):**

لما تطلب أكل أونلاين، الواجهة الأمامية بتجمع طلبك، وواجهة برمجة بتتحقق منه، وقاعدة بيانات بتخزّنه - كامل حزمة الويب في ثواني.

### Advantages (المميزات)

- Runs everywhere with no installation
- Fast iteration and deployment
- Huge ecosystem of tools
- Easy to reach users globally

**Egyptian Arabic (اللهجة المصرية):**

- بيشتغل في أي مكان من غير تثبيت
- تطوير ونشر سريع
- نظام بيئي ضخم من الأدوات
- سهل الوصول للمستخدمين عالميًا

### Limitations (الحدود)

- Security risks like XSS and CSRF
- Browser and device differences
- Performance depends on networks
- Fragmented tooling

**Egyptian Arabic (اللهجة المصرية):**

- مخاطر أمنية زي XSS و CSRF
- اختلافات المتصفحات والأجهزة
- الأداء بيعتمد على الشبكات
- أدوات متفرّقة

### Best Practices (أحسن الممارسات)

- Separate concerns between front and back end
- Validate input on both sides
- Use HTTPS and secure authentication
- Optimize assets and caching

**Egyptian Arabic (اللهجة المصرية):**

- افصل الاهتمامات بين الواجهة الأمامية والخلفية
- تحقق من المدخلات على الجانبين
- استخدم HTTPS ومصادقة آمنة
- حسّن الأصول والتخزين المؤقت

### Common Mistakes (الأخطاء الشائعة)

- Trusting client-side validation only
- Storing secrets in front-end code
- Ignoring accessibility
- N+1 queries in the back end

**Egyptian Arabic (اللهجة المصرية):**

- الاعتماد على تحقق جهة العميل بس
- تخزين الأسرار في كود الواجهة الأمامية
- تجاهل إمكانية الوصول
- استعلامات N+1 في الخلفية

### Practical Example (مثال عملي)

A to-do app stores tasks via a REST API, and the browser re-renders the list without a full page reload.

**Egyptian Arabic (اللهجة المصرية):**

تطبيق مهام بيخزّن المهام عبر واجهة REST، والمتصفح بيعيد رسم القائمة من غير إعادة تحميل كاملة.

### Hands-On Exercise (تمرين عملي بإيدك)

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in HTML and Semantic Markup, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نطام صغير تعرفه. اكتب: (1) الموقف في HTML والترميز الدلالي، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define HTML and Semantic Markup in one sentence of your own words.
2. Give two situations where HTML and Semantic Markup changes a technical decision.
3. Name one limitation of HTML and Semantic Markup and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف HTML والترميز الدلالي في جملة واحدة بكلامك.
2. ادي موقفين HTML والترميز الدلالي بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود HTML والترميز الدلالي واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes HTML and Semantic Markup? (a) a formality with no use (b) a working tool inside Web Technologies (c) an unrelated subject.
Q2. True or false: HTML and Semantic Markup has no limitations.
Q3. In one line, why does HTML and Semantic Markup matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـHTML والترميز الدلالي؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه تقنيات الويب (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: HTML والترميز الدلالي مالوش حدود.
س3. في سطر واحد، ليه HTML والترميز الدلالي مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Web Technologies.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه تقنيات الويب.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying HTML and Semantic Markup to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها HTML والترميز الدلالي على برنامج أو نطام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of HTML and Semantic Markup until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف HTML والترميز الدلالي تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الرابع: تعلّم الآلة (AI301)

## The Machine Learning Workflow (سير عمل تعلّم الآلة)

The Machine Learning Workflow (سير عمل تعلّم الآلة)
English Definition: The Machine Learning Workflow is a core topic in Machine Learning. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: سير عمل تعلّم الآلة موضوع أساسي في تعلّم الآلة. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**The Machine Learning Workflow** is the focus of this lesson. Machine learning builds models that learn patterns from data to make predictions or decisions without being explicitly programmed.

**Egyptian Arabic (اللهجة المصرية):**

**سير عمل تعلّم الآلة** هو محور الدرس ده. تعلّم الآلة بيبني نماذج بتتعلم الأنماط من البيانات عشان تتنبأ أو تقرر من غير برمجة صريحة.

### Why It Exists (ليه موجود)

It powers recommendations, detection, forecasting and automation across industries. Without a clear grasp of The Machine Learning Workflow, the rest of Machine Learning has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

بيشغّل التوصيات والكشف والتنبؤ والأتمتة في كل الصناعات. ومن غير إدراك واضح لموضوع سير عمل تعلّم الآلة، باقي تعلّم الآلة ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, The Machine Learning Workflow is where the theory of Machine Learning meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع سير عمل تعلّم الآلة هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

### Where It Is Used (بنستخدمه فين)

- Recommendation systems
- Fraud and anomaly detection
- Forecasting and prediction
- Image and text classification
- Personalization

**Egyptian Arabic (اللهجة المصرية):**

- أنظمة التوصيات
- كشف الاحتيال والشذوذ
- التنبؤ والتوقّع
- تصنيف الصور والنصوص
- التخصيص

### Real-World Usage and Relevance in the Field (الاستخدام والملاءمة في المجال)

Your email filter learns from millions of labelled messages which patterns indicate spam, then flags new ones.

**Egyptian Arabic (اللهجة المصرية):**

فلتر الإيميل بيتعلم من ملايين الرسائل الموسومة إيه الأنماط اللي بتدل على السبام، وبعدين يعلّم الجديدة.

### Advantages (المميزات)

- Learns complex patterns automatically
- Improves with more data
- Handles many data types
- Automates prediction at scale

**Egyptian Arabic (اللهجة المصرية):**

- بيتعلم أنماط معقدة تلقائيًا
- بيتحسّن بزيادة البيانات
- بيتعامل مع أنواع بيانات كتير
- بيأتمت التنبؤ على نطاق واسع

### Limitations (الحدود)

- Needs quality labelled data
- Can overfit or be biased
- Hard to interpret some models
- Performance drifts over time

**Egyptian Arabic (اللهجة المصرية):**

- محتاج بيانات موسومة بجودة
- ممكن يفرط في التوفيق أو يتحيّز
- بعض النماذج صعب تفسيرها
- الأداء بينحرف بمرور الوقت

### Best Practices (أحسن الممارسات)

- Split data into train, validation and test
- Engineer and scale features carefully
- Cross-validate before trusting results
- Monitor for drift after deployment

**Egyptian Arabic (اللهجة المصرية):**

- قسّم البيانات لتدريب وتحقق واختبار
- هندس الخصائص وقيسها بعناية
- استخدم التحقق المتقاطع قبل الثقة بالنتائج
- راقب الانحراف بعد النشر

### Common Mistakes (الأخطاء الشائعة)

- Evaluating on training data
- Data leakage between splits
- Ignoring class imbalance
- Tuning on the test set

**Egyptian Arabic (اللهجة المصرية):**

- التقييم على بيانات التدريب
- تسريب البيانات بين التقسيمات
- تجاهل اختلال الفئات
- الضبط على مجموعة الاختبار

### Practical Example (مثال عملي)

A model predicts house prices from area and location; a linear regression fits the data, and cross-validation estimates how well it generalizes.

**Egyptian Arabic (اللهجة المصرية):**

نموذج بيتنبأ بأسعار البيوت من المساحة والموقع؛ الانحدار الخطي بيلاءم البيانات، والتحقق المتقاطع بيقدّر مدى تعميمه.

### Hands-On Exercise (تمرين عملي بإيدك)

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in The Machine Learning Workflow, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نطام صغير تعرفه. اكتب: (1) الموقف في سير عمل تعلّم الآلة، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define The Machine Learning Workflow in one sentence of your own words.
2. Give two situations where The Machine Learning Workflow changes a technical decision.
3. Name one limitation of The Machine Learning Workflow and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف سير عمل تعلّم الآلة في جملة واحدة بكلامك.
2. ادي موقفين سير عمل تعلّم الآلة بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود سير عمل تعلّم الآلة واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes The Machine Learning Workflow? (a) a formality with no use (b) a working tool inside Machine Learning (c) an unrelated subject.
Q2. True or false: The Machine Learning Workflow has no limitations.
Q3. In one line, why does The Machine Learning Workflow matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـسير عمل تعلّم الآلة؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه تعلّم الآلة (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: سير عمل تعلّم الآلة مالوش حدود.
س3. في سطر واحد، ليه سير عمل تعلّم الآلة مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Machine Learning.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه تعلّم الآلة.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying The Machine Learning Workflow to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها سير عمل تعلّم الآلة على برنامج أو نطام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of The Machine Learning Workflow until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف سير عمل تعلّم الآلة تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الخامس: إدارة مشروعات البرمجيات (CS314)

## Project Scope and Requirements Management (إدارة نطاق المشروع والمتطلبات)

Project Scope and Requirements Management (إدارة نطاق المشروع والمتطلبات)
English Definition: Project Scope and Requirements Management is a core topic in Software Engineering. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: إدارة نطاق المشروع والمتطلبات موضوع أساسي في هندسة البرمجيات. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Project Scope and Requirements Management** is the focus of this lesson. Software engineering applies engineering discipline to building software: requirements, design, construction, testing and maintenance at scale.

**Egyptian Arabic (اللهجة المصرية):**

**إدارة نطاق المشروع والمتطلبات** هو محور الدرس ده. هندسة البرمجيات بتطبّق الانضباط الهندسي على بناء البرمجيات: المتطلبات والتصميم والبناء والاختبار والصيانة على نطاق واسع.

### Why It Exists (ليه موجود)

Large software fails without process: unclear requirements and untested code cost the most. Without a clear grasp of Project Scope and Requirements Management, the rest of Software Engineering has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

البرمجيات الكبيرة بتفشل من غير عملية: المتطلبات الغامضة والكود غير المختبر هما الأغلى. ومن غير إدراك واضح لموضوع إدارة نطاق المشروع والمتطلبات، باقي هندسة البرمجيات ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Project Scope and Requirements Management is where the theory of Software Engineering meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع إدارة نطاق المشروع والمتطلبات هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

### Where It Is Used (بنستخدمه فين)

- Product and enterprise development
- Agile teams and sprints
- Quality assurance and testing
- Architecture and design
- Maintenance and evolution

**Egyptian Arabic (اللهجة المصرية):**

- تطوير المنتجات والمؤسسات
- الفرق الرشيقة والدورات
- ضمان الجودة والاختبار
- المعمارية والتصميم
- الصيانة والتطوّر

### Real-World Usage and Relevance in the Field (الاستخدام والملاءمة في المجال)

Most software cost is maintenance, not initial coding, which is why good design and tests matter so much.

**Egyptian Arabic (اللهجة المصرية):**

معظم تكلفة البرمجيات صيانة مش كتابة أولية، وعشان كده التصميم الكويس والاختبارات بيفرقوا جدًا.

### Advantages (المميزات)

- Manages complexity at scale
- Reduces costly failures
- Improves team collaboration
- Makes systems maintainable

**Egyptian Arabic (اللهجة المصرية):**

- بتدير التعقيد على نطاق واسع
- بتقلل الأعطال المكلفة
- بتحسّن تعاون الفريق
- بتخلي الأنظمة قابلة للصيانة

### Limitations (الحدود)

- Process can become bureaucracy
- Estimates are uncertain
- Not all problems fit one methodology
- Documentation can go stale

**Egyptian Arabic (اللهجة المصرية):**

- العملية ممكن تتحول لروتين
- التقديرات غير مؤكدة
- مش كل المشكلات تناسب منهجية واحدة
- التوثيق ممكن يقدم

### Best Practices (أحسن الممارسات)

- Elicit and validate requirements early
- Design before coding
- Automate tests and builds
- Review code with peers
- Keep design simple

**Egyptian Arabic (اللهجة المصرية):**

- اجمع المتطلبات وتحقق منها بدري
- صمّم قبل ما تكتب كود
- أتمت الاختبارات والبناء
- راجع الكود مع الزملاء
- خلي التصميم بسيط

### Common Mistakes (الأخطاء الشائعة)

- Skipping requirements and jumping to code
- Testing only at the end
- Ignoring non-functional requirements
- Over-engineering for imagined needs

**Egyptian Arabic (اللهجة المصرية):**

- تخطي المتطلبات والقفز للكود
- الاختبار في الآخر بس
- تجاهل المتطلبات غير الوظيفية
- الهندسة الزائدة لاحتياجات متخيّلة

### Practical Example (مثال عملي)

A team building a banking app writes user stories, designs the data model, and writes automated tests before each feature is merged.

**Egyptian Arabic (اللهجة المصرية):**

فريق بيبني تطبيق بنك بيكتب قصص المستخدم، ويصمّم نموذج البيانات، ويكتب اختبارات آلية قبل دمج كل ميزة.

### Hands-On Exercise (تمرين عملي بإيدك)

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Project Scope and Requirements Management, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نطام صغير تعرفه. اكتب: (1) الموقف في إدارة نطاق المشروع والمتطلبات، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Project Scope and Requirements Management in one sentence of your own words.
2. Give two situations where Project Scope and Requirements Management changes a technical decision.
3. Name one limitation of Project Scope and Requirements Management and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف إدارة نطاق المشروع والمتطلبات في جملة واحدة بكلامك.
2. ادي موقفين إدارة نطاق المشروع والمتطلبات بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود إدارة نطاق المشروع والمتطلبات واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Project Scope and Requirements Management? (a) a formality with no use (b) a working tool inside Software Engineering (c) an unrelated subject.
Q2. True or false: Project Scope and Requirements Management has no limitations.
Q3. In one line, why does Project Scope and Requirements Management matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـإدارة نطاق المشروع والمتطلبات؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه هندسة البرمجيات (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: إدارة نطاق المشروع والمتطلبات مالوش حدود.
س3. في سطر واحد، ليه إدارة نطاق المشروع والمتطلبات مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Software Engineering.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه هندسة البرمجيات.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Project Scope and Requirements Management to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها إدارة نطاق المشروع والمتطلبات على برنامج أو نطام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Project Scope and Requirements Management until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف إدارة نطاق المشروع والمتطلبات تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم السادس: التفاعل بين الإنسان والحاسب (IS301)

## Human Capabilities and Perception (قدرات الإنسان والإدراك)

Human Capabilities and Perception (قدرات الإنسان والإدراك)
English Definition: Human Capabilities and Perception is a core topic in Information Systems. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: قدرات الإنسان والإدراك موضوع أساسي في نظم المعلومات. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Human Capabilities and Perception** is the focus of this lesson. Information systems combine people, processes and technology to collect, process and deliver information that supports decisions.

**Egyptian Arabic (اللهجة المصرية):**

**قدرات الإنسان والإدراك** هو محور الدرس ده. نظم المعلومات بتجمع الناس والعمليات والتكنولوجيا عشان تجمع وتعالج وتوصّل المعلومات اللي بتدعم القرارات.

### Why It Exists (ليه موجود)

Technology only creates value when it fits the organization's processes and goals. Without a clear grasp of Human Capabilities and Perception, the rest of Information Systems has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

التكنولوجيا مش بتخلق قيمة إلا لما تناسب عمليات المنظمة وأهدافها. ومن غير إدراك واضح لموضوع قدرات الإنسان والإدراك، باقي نظم المعلومات ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Human Capabilities and Perception is where the theory of Information Systems meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع قدرات الإنسان والإدراك هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

### Where It Is Used (بنستخدمه فين)

- Enterprise and ERP systems
- Business intelligence and analytics
- E-commerce platforms
- IT strategy and governance
- Digital transformation

**Egyptian Arabic (اللهجة المصرية):**

- أنظمة المؤسسات و ERP
- ذكاء الأعمال والتحليلات
- منصات التجارة الإلكترونية
- استراتيجية وحوكمة تقنية المعلومات
- التحول الرقمي

### Real-World Usage and Relevance in the Field (الاستخدام والملاءمة في المجال)

An online bank combines a mobile app, a database and a call centre - an information system whose value is in the whole, not the parts.

**Egyptian Arabic (اللهجة المصرية):**

بنك أونلاين بيجمع تطبيق موبايل وقاعدة بيانات ومركز اتصال - نظام معلومات قيمته في الكل مش الأجزاء.

### Advantages (المميزات)

- Aligns technology with business goals
- Improves decision quality
- Integrates data across departments
- Enables digital transformation

**Egyptian Arabic (اللهجة المصرية):**

- بيفوّق التكنولوجيا مع أهداف العمل
- بيحسّن جودة القرار
- بيدمج البيانات بين الأقسام
- بيمكّن التحول الرقمي

### Limitations (الحدود)

- Organizational change is hard
- Integration is complex and costly
- Poor data quality undermines value
- Systems can outlive their usefulness

**Egyptian Arabic (اللهجة المصرية):**

- التغيير التنظيمي صعب
- التكامل معقّد ومكلف
- جودة البيانات الرديئة بتضرب القيمة
- الأنظمة ممكن تعيش أطول من فايدتها

### Best Practices (أحسن الممارسات)

- Start from business requirements
- Model processes before systems
- Ensure data quality and governance
- Plan for change management

**Egyptian Arabic (اللهجة المصرية):**

- ابدأ من متطلبات العمل
- انمذج العمليات قبل الأنظمة
- اضمن جودة البيانات وحوكمتها
- خطط لإدارة التغيير

### Common Mistakes (الأخطاء الشائعة)

- Buying technology without process change
- Ignoring user adoption
- Duplicating data across silos
- Skipping requirements analysis

**Egyptian Arabic (اللهجة المصرية):**

- شراء التكنولوجيا من غير تغيير العمليات
- تجاهل تبنّي المستخدمين
- تكرار البيانات بين الجزر المنفصلة
- تخطي تحليل المتطلبات

### Practical Example (مثال عملي)

A hospital information system links appointments, lab results and billing so a doctor sees a full patient record in one screen.

**Egyptian Arabic (اللهجة المصرية):**

نظام معلومات مستشفى بيربط المواعيد ونتائج التحاليل والفوترة عشان الدكتور يشوف سجل المريض كامل في شاشة واحدة.

### Hands-On Exercise (تمرين عملي بإيدك)

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Human Capabilities and Perception, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نطام صغير تعرفه. اكتب: (1) الموقف في قدرات الإنسان والإدراك، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Human Capabilities and Perception in one sentence of your own words.
2. Give two situations where Human Capabilities and Perception changes a technical decision.
3. Name one limitation of Human Capabilities and Perception and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف قدرات الإنسان والإدراك في جملة واحدة بكلامك.
2. ادي موقفين قدرات الإنسان والإدراك بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود قدرات الإنسان والإدراك واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Human Capabilities and Perception? (a) a formality with no use (b) a working tool inside Information Systems (c) an unrelated subject.
Q2. True or false: Human Capabilities and Perception has no limitations.
Q3. In one line, why does Human Capabilities and Perception matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـقدرات الإنسان والإدراك؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه نظم المعلومات (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: قدرات الإنسان والإدراك مالوش حدود.
س3. في سطر واحد، ليه قدرات الإنسان والإدراك مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Information Systems.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه نظم المعلومات.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Human Capabilities and Perception to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها قدرات الإنسان والإدراك على برنامج أو نطام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Human Capabilities and Perception until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف قدرات الإنسان والإدراك تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

## Learning Resources (المصادر الدراسية)

### CS311 — تصميم المترجمات

**Primary Resource (المصدر الأساسي)**

- **Resource Name:** Introduction to the Theory of Computation (Sipser)
- **Resource Type:** Textbook
- **Direct Link:** https://www.cengage.com/c/introduction-to-the-theory-of-computation-3e-sipser/9781133187790/
- **Difficulty:** Advanced
- **Estimated Time:** 35 hours

- **Why Recommended:** The clearest and most respected theory of computation textbook.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: أوضح وأشهر كتاب في نظرية الحسابات.

- **What to Study From It:** Automata, grammars, Turing machines, decidability and complexity.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: الآلات المجرّدة والقواعد وآلات تورينج والقابلية للتقرير والتعقيد.

**Optional Resource (المصدر الاختياري)**

- **Resource Name:** MIT 18.404J Theory of Computation
- **Resource Type:** University Course
- **Direct Link:** https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/
- **Difficulty:** Advanced
- **Estimated Time:** 30 hours

- **Why Recommended:** Free rigorous lectures by Michael Sipser himself.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: محاضرات مجانية صارمة من مايكل سيبسر نفسه.

- **What to Study From It:** Automata, computability, reductions and complexity.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: الآلات المجرّدة والقابلية للحساب والاختزال والتعقيد.

**Practice Platform (منصة التمرين العملي)**

- **Resource Name:** JFLAP
- **Resource Type:** Practice Tool
- **Direct Link:** https://www.jflap.org/
- **Difficulty:** Intermediate
- **Estimated Time:** 15 hours

- **Why Recommended:** Build and simulate automata, grammars and Turing machines visually.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: ابني وحاكي الآلات المجرّدة والقواعد وآلات تورينج بصريًا.

- **What to Study From It:** DFA, NFA, regular expressions, grammars and Turing machine exercises.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: تمارين DFA و NFA والتعبيرات النمطية والقواعد وآلات تورينج.

### CS312 — الرسم بالحاسب

**Primary Resource (المصدر الأساسي)**

- **Resource Name:** Fundamentals of Computer Graphics (Marschner & Shirley)
- **Resource Type:** Textbook
- **Direct Link:** https://www.taylorfrancis.com/books/mono/10.1201/9780429184270/fundamentals-computer-graphics-steve-marschner-peter-shirley
- **Difficulty:** Advanced
- **Estimated Time:** 40 hours

- **Why Recommended:** The standard graphics textbook covering the full pipeline.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: كتاب الرسوم المعياري اللي بيغطي خط العرض كامل.

- **What to Study From It:** Transformations, rasterization, shading, curves and ray tracing.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: التحويلات والتحويل النقطي والتظليل والمنحنيات وتتبّع الأشعة.

**Optional Resource (المصدر الاختياري)**

- **Resource Name:** LearnOpenGL
- **Resource Type:** Online Course
- **Direct Link:** https://learnopengl.com/
- **Difficulty:** Intermediate
- **Estimated Time:** 35 hours

- **Why Recommended:** A hands-on tutorial series that builds a renderer from scratch.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: سلسلة دروس عملية بتبني مُصيّر من الصفر.

- **What to Study From It:** Shaders, textures, lighting, camera and model loading.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: المظللات والخامات والإضاءة والكاميرا وتحميل المجسمات.

**Practice Platform (منصة التمرين العملي)**

- **Resource Name:** Shadertoy
- **Resource Type:** Practice Platform
- **Direct Link:** https://www.shadertoy.com/
- **Difficulty:** Advanced
- **Estimated Time:** 20 hours

- **Why Recommended:** Write and run fragment shaders in the browser to practise shading.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: اكتب وشغّل مظللات القطع في المتصفح للتمرين على التظليل.

- **What to Study From It:** Procedural shading, lighting and ray marching.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: التظليل الإجرائي والإضاءة ومسير الأشعة.

### CS313 — تقنيات الويب

**Primary Resource (المصدر الأساسي)**

- **Resource Name:** MDN Web Docs
- **Resource Type:** Official Documentation
- **Direct Link:** https://developer.mozilla.org/
- **Difficulty:** Beginner
- **Estimated Time:** 30 hours

- **Why Recommended:** The most reliable reference for HTML, CSS and JavaScript.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: أوثق مرجع لـ HTML و CSS و JavaScript.

- **What to Study From It:** HTML structure, CSS layout, JavaScript and web APIs.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: بنية HTML وتخطيط CSS و JavaScript وواجهات الويب.

**Optional Resource (المصدر الاختياري)**

- **Resource Name:** The Odin Project
- **Resource Type:** Online Course
- **Direct Link:** https://www.theodinproject.com/
- **Difficulty:** Beginner
- **Estimated Time:** 40 hours

- **Why Recommended:** A free full-stack curriculum that builds real projects.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: منهج متكامل مجاني بيبني مشروعات حقيقية.

- **What to Study From It:** Front-end, back-end, databases and deployment.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: الواجهة الأمامية والخلفية وقواعد البيانات والنشر.

**Practice Platform (منصة التمرين العملي)**

- **Resource Name:** Frontend Mentor
- **Resource Type:** Practice Platform
- **Direct Link:** https://www.frontendmentor.io/
- **Difficulty:** Beginner to Intermediate
- **Estimated Time:** 20 hours

- **Why Recommended:** Real design challenges you implement with HTML, CSS and JS.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: تحديات تصميم حقيقية بتنفّذها بـ HTML و CSS و JS.

- **What to Study From It:** Responsive layouts, components and interactive challenges.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: تخطيطات متجاوبة ومكوّنات وتحديات تفاعلية.

### AI301 — تعلّم الآلة

**Primary Resource (المصدر الأساسي)**

- **Resource Name:** Hands-On Machine Learning (Geron)
- **Resource Type:** Textbook
- **Direct Link:** https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/
- **Difficulty:** Intermediate
- **Estimated Time:** 40 hours

- **Why Recommended:** A practical guide that teaches ML through code and projects.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: دليل عملي بيعلم تعلّم الآلة بالكود والمشروعات.

- **What to Study From It:** Regression, classification, trees, ensembles and neural networks.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: الانحدار والتصنيف والأشجار والتجميع والشبكات العصبية.

**Optional Resource (المصدر الاختياري)**

- **Resource Name:** Andrew Ng - Machine Learning Specialization
- **Resource Type:** Online Course
- **Direct Link:** https://www.coursera.org/specializations/machine-learning-introduction
- **Difficulty:** Beginner
- **Estimated Time:** 40 hours

- **Why Recommended:** The classic introduction that explains ML intuition clearly.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: المقدمة الكلاسيكية اللي بتشرح حدس تعلّم الآلة بوضوح.

- **What to Study From It:** Supervised learning, regularization, neural nets and advice.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: التعلّم الموجّه والتنظيم والشبكات العصبية والنصائح.

**Practice Platform (منصة التمرين العملي)**

- **Resource Name:** Kaggle Competitions
- **Resource Type:** Practice Platform
- **Direct Link:** https://www.kaggle.com/competitions
- **Difficulty:** Intermediate
- **Estimated Time:** 30 hours

- **Why Recommended:** Real datasets and leaderboards to practise end-to-end ML.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: مجموعات بيانات حقيقية ولوحات نتائج للتمرين على تعلّم الآلة من الأول للآخر.

- **What to Study From It:** Feature engineering, model selection and evaluation.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: هندسة الخصائص واختيار النموذج والتقييم.

### CS314 — إدارة مشروعات البرمجيات

**Primary Resource (المصدر الأساسي)**

- **Resource Name:** Software Engineering (Sommerville)
- **Resource Type:** Textbook
- **Direct Link:** https://www.pearson.com/en-us/subject-catalog/p/software-engineering/P200000003295
- **Difficulty:** Intermediate
- **Estimated Time:** 40 hours

- **Why Recommended:** A comprehensive, widely used software engineering textbook.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: كتاب هندسة برمجيات شامل ومستخدم على نطاق واسع.

- **What to Study From It:** Processes, requirements, design, testing and project management.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: العمليات والمتطلبات والتصميم والاختبار وإدارة المشروعات.

**Optional Resource (المصدر الاختياري)**

- **Resource Name:** The Scrum Guide
- **Resource Type:** Official Guide
- **Direct Link:** https://scrumguides.org/
- **Difficulty:** Beginner
- **Estimated Time:** 6 hours

- **Why Recommended:** The short official definition of Scrum used by agile teams everywhere.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: التعريف الرسمي المختصر لسكرم المستخدم في الفرق الرشيقة في كل مكان.

- **What to Study From It:** Scrum roles, events, artifacts and agile values.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: أدوار سكرم وأحداثه ومخرجاته وقيم الرشاقة.

**Practice Platform (منصة التمرين العملي)**

- **Resource Name:** GitHub - Collaborate on Code
- **Resource Type:** Practice Platform
- **Direct Link:** https://docs.github.com/en/get-started
- **Difficulty:** Beginner
- **Estimated Time:** 12 hours

- **Why Recommended:** Practise version control, branching and code review on real repositories.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: اتمرّن على التحكم في الإصدارات والتفرّع ومراجعة الكود على مستودعات حقيقية.

- **What to Study From It:** Branches, pull requests, issues and code review.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: الفروع وطلبات الدمج والمشكلات ومراجعة الكود.

### IS301 — التفاعل بين الإنسان والحاسب

**Primary Resource (المصدر الأساسي)**

- **Resource Name:** Management Information Systems (Laudon & Laudon)
- **Resource Type:** Textbook
- **Direct Link:** https://www.pearson.com/en-us/subject-catalog/p/management-information-systems-managing-the-digital-firm/P200000005947
- **Difficulty:** Beginner
- **Estimated Time:** 30 hours

- **Why Recommended:** The standard text on how IS supports business and management.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: المرجع المعياري لإزاي نظم المعلومات بتدعم الأعمال والإدارة.

- **What to Study From It:** IS in organizations, e-commerce, BI, governance and strategy.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: نظم المعلومات في المنظمات والتجارة الإلكترونية وذكاء الأعمال والحوكمة والاستراتيجية.

**Optional Resource (المصدر الاختياري)**

- **Resource Name:** TOGAF Enterprise Architecture Overview
- **Resource Type:** Framework Guide
- **Direct Link:** https://www.opengroup.org/togaf
- **Difficulty:** Intermediate
- **Estimated Time:** 12 hours

- **Why Recommended:** A widely used framework for designing enterprise systems.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: إطار مستخدم على نطاق واسع لتصميم أنظمة المؤسسات.

- **What to Study From It:** Architecture domains, governance and transformation planning.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: مجالات المعمارية والحوكمة وتخطيط التحول.

**Practice Platform (منصة التمرين العملي)**

- **Resource Name:** BPMN Modelling Practice
- **Resource Type:** Practice Tool
- **Direct Link:** https://www.bpmn.org/
- **Difficulty:** Intermediate
- **Estimated Time:** 12 hours

- **Why Recommended:** Model business processes that information systems will support.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: انمذج عمليات العمل اللي نظم المعلومات هتدعمها.

- **What to Study From It:** Process diagrams, events, gateways and tasks.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: مخططات العمليات والأحداث والبوابات والمهام.


---

## End of Lesson (نهاية الدرس)

### Lesson Summary (ملخص الدرس)

This week covered the following topics across the semester's courses: CS311: Lexical Analysis and Tokens; CS312: Graphics Hardware and the Display Pipeline; CS313: HTML and Semantic Markup; AI301: The Machine Learning Workflow; CS314: Project Scope and Requirements Management; IS301: Human Capabilities and Perception. Each topic opened with a bilingual definition, then explained what it is, why it exists, why it matters, where it is used, its advantages and limits, best practices and common mistakes, followed by a practical example and exercises.

**Egyptian Arabic (اللهجة المصرية):**

الأسبوع ده غطّى المواضيع دي في مقررات الفصل: CS311: التحليل المعجمي والرموز؛ CS312: عتاد الرسوم وخط عرض البيانات؛ CS313: HTML والترميز الدلالي؛ AI301: سير عمل تعلّم الآلة؛ CS314: إدارة نطاق المشروع والمتطلبات؛ IS301: قدرات الإنسان والإدراك. كل موضوع بدأ بتعريف ثنائي اللغة، وبعدين شرح يعني إيه وليه موجود وليه مهم وبنستخدمه فين، ومميزاته وحدوده وأحسن الممارسات والأخطاء الشائعة، وبعدين مثال عملي وتمارين.

### Key Takeaways (أهم النقط)

- Every topic is a working tool, not a formality.
- Definitions must be recallable from memory.
- Advantages and limitations always come together.
- A practical example fixes the idea in your mind.

**Egyptian Arabic (اللهجة المصرية):**

- كل موضوع أداة شغّالة مش شكلية.
- التعريفات لازم تقدر تسترجعها من دماغك.
- المميزات والحدود بتيجي مع بعض دايمًا.
- المثال العملي بيثبّت الفكرة في دماغك.

### Common Mistakes (الأخطاء الشائعة)

- Memorizing definitions without understanding use.
- Ignoring limitations when applying a tool.
- Skipping the practice questions and going straight to the exam.

**Egyptian Arabic (اللهجة المصرية):**

- حفظ التعريفات من غير فهم الاستخدام.
- تجاهل الحدود وقت تطبيق الأداة.
- تخطي أسئلة التدريب والذهاب للامتحان على طول.

### Quiz (الاختبار)

1. Which topic this week was hardest, and why?
2. Give one real decision each topic supports.
3. State one limitation for each topic.

**Egyptian Arabic (اللهجة المصرية):**

1. أنهي موضوع الأسبوع ده كان أصعب، وليه؟
2. ادي قرار حقيقي واحد كل موضوع بيدعمه.
3. اذكر حد واحد لكل موضوع.

### Quiz Answers (إجابات الاختبار)

Answers depend on your own work; check each against the topic's definition, use and limitations.

**Egyptian Arabic (اللهجة المصرية):**

الإجابات بتعتمد على شغلك؛ راجع كل واحدة مقابل تعريف الموضوع واستخدامه وحدوده.

### Practice Exercise (تمرين عملي)

Pick one topic from this week and apply it fully to a real system: situation, analysis and recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اختار موضوع واحد من الأسبوع ده وطبّقه كامل على نطام حقيقي: الموقف والتحليل والتوصية.

### Homework (الواجب)

For each course this week, write three lines: what the topic is, where it is used, and one mistake to avoid.

**Egyptian Arabic (اللهجة المصرية):**

لكل مقرر الأسبوع ده، اكتب ثلاث سطور: الموضوع إيه، وبنستخدمه فين، وخطأ واحد تتجنبه.

### Recommended Revision (المراجعة الموصى بيها)

1. Re-read every definition block.
2. Redo the quizzes without looking.
3. Review the practical examples and cover the solution.
4. Note anything still unclear for your instructor.

**Egyptian Arabic (اللهجة المصرية):**

1. اقرا كل بلوكات التعريف تاني.
2. اعمل الاختبارات تاني من غير ما تبص.
3. راجع الأمثلة العملية وغطّي الحل.
4. سجّل أي حاجة لسه مش واضحة لمدرّسك.

### Preview of the Next Lesson (نظرة على الدرس الجاي)

Next week continues with: CS311: Regular Expressions and Finite Automata in Lexers; CS312: 2D Transformations; CS313: CSS and Responsive Layout; AI301: Supervised vs Unsupervised Learning; CS314: Work Breakdown Structures; IS301: Interaction Design Principles.

**Egyptian Arabic (اللهجة المصرية):**

الأسبوع الجاي بيكمل بـ: CS311: التعبيرات النمطية والآلات المنتهية في المحلّل؛ CS312: التحويلات ثنائية الأبعاد؛ CS313: CSS والتخطيط المتجاوب؛ AI301: التعلّم الموجّه مقابل غير الموجّه؛ CS314: هياكل تجزئة العمل؛ IS301: مبادئ تصميم التفاعل.

### Important Terms (مصطلحات مهمة)

#### Automaton (آلة مجرّدة)
English Definition: An abstract machine that recognizes a language.
Egyptian Arabic Definition: آلة مجرّدة بتتعرف على لغة.

#### Grammar (قواعد)
English Definition: Rules that generate the strings of a language.
Egyptian Arabic Definition: قواعد بتولّد نصوص اللغة.

#### Regular Language (لغة نمطية)
English Definition: A language recognized by a finite automaton.
Egyptian Arabic Definition: لغة بتتعرف عليها آلة منتهية.

#### Turing Machine (آلة تورينج)
English Definition: A model of general computation.
Egyptian Arabic Definition: نموذج للحساب العام.

#### Decidable (قابل للتقرير)
English Definition: A problem a machine can always answer.
Egyptian Arabic Definition: مشكلة الآلة تقدر تجاوب عليها دايمًا.


---

[الدرس السابق: week-01.md](week-01.md) · [رجوع لفصل 5](README.md) · [الدرس الجاي: week-03.md](week-03.md)