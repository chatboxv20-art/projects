# الأسبوع 5 — الفصل 4

> الدرس ده بيغطّي موضوع واحد في كل مقرر من مقررات الفصل، وكل الشرح مكتوب بالعامية المصرية مع البلوك الإنجليزي الكامل جنبه.

**المقررات اللي في الدرس ده:** CS214 (نظم التشغيل)، CS215 (نظرية الحسابات)، CS216 (هندسة البرمجيات)، CS217 (شبكات الحاسب)، AI201 (مقدمة في الذكاء الاصطناعي)، ST201 (الأساليب الإحصائية وتحليل البيانات)

---

# القسم الأول: نظم التشغيل (CS214)

## Process Synchronization (تزامن العمليات)

Process Synchronization (تزامن العمليات)
English Definition: Process Synchronization is a core topic in Operating Systems. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: تزامن العمليات موضوع أساسي في نظم التشغيل. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Process Synchronization** is the focus of this lesson. Operating systems manage hardware resources - CPU, memory, files and devices - and provide the abstractions that programs run on.

**Egyptian Arabic (اللهجة المصرية):**

**تزامن العمليات** هو محور الدرس ده. نظم التشغيل بتدير موارد العتاد - المعالج والذاكرة والملفات والأجهزة - وبتوفّر التجريدات اللي البرامج بتشتغل فوقها.

### Why It Exists (ليه موجود)

Every program runs on an OS; scheduling, memory and concurrency problems are solved there. Without a clear grasp of Process Synchronization, the rest of Operating Systems has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

كل برنامج بيشتغل على نظام تشغيل؛ مشكلات الجدولة والذاكرة والتزامن بتتحل هناك. ومن غير إدراك واضح لموضوع تزامن العمليات، باقي نظم التشغيل ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Process Synchronization is where the theory of Operating Systems meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع تزامن العمليات هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

### Where It Is Used (بنستخدمه فين)

- System and embedded programming
- Servers and cloud platforms
- Performance and concurrency tuning
- Security and isolation
- Device drivers

**Egyptian Arabic (اللهجة المصرية):**

- برمجة النظم والمدمجة
- السيرفرات ومنصات السحابة
- ضبط الأداء والتزامن
- الأمن والعزل
- مشغّلات الأجهزة

### Real-World Usage and Relevance in the Field (الاستخدام والملاءمة في المجال)

Running hundreds of apps at once works because the OS schedules the CPU and gives each process the illusion of its own memory.

**Egyptian Arabic (اللهجة المصرية):**

تشغيل مئات التطبيقات مع بعض بيشتغل لأن نظام التشغيل بجدول المعالج وبيدي كل عملية إحساس إن ليها ذاكرتها الخاصة.

### Advantages (المميزات)

- Abstracts away hardware complexity
- Enables safe multitasking
- Efficient resource sharing
- Foundation for distributed and cloud systems

**Egyptian Arabic (اللهجة المصرية):**

- بتجرّد تعقيد العتاد
- بتمكّن تعدد المهام الآمن
- مشاركة موارد فعّالة
- أساس للنظم الموزّعة والسحابية

### Limitations (الحدود)

- Concurrency bugs are subtle
- Context switching has overhead
- Kernel bugs crash the whole system
- Trade-offs between speed and safety

**Egyptian Arabic (اللهجة المصرية):**

- أخطاء التزامن خفية
- تبديل السياق فيه تكلفة
- أخطاء النواة بتسقّط النظام كله
- مقايضات بين السرعة والأمان

### Best Practices (أحسن الممارسات)

- Protect shared data with locks or atomics
- Understand scheduling and blocking
- Use the right synchronization primitive
- Test concurrency under load

**Egyptian Arabic (اللهجة المصرية):**

- احمي البيانات المشتركة بالأقفال أو العمليات الذرية
- افهم الجدولة والحجب
- استخدم أداة التزامن المناسبة
- اختبر التزامن تحت الحمل

### Common Mistakes (الأخطاء الشائعة)

- Race conditions on shared variables
- Forgetting to release locks
- Confusing concurrency with parallelism
- Assuming threads share nothing

**Egyptian Arabic (اللهجة المصرية):**

- ظروف التسابق على المتغيرات المشتركة
- نسيان تحرير الأقفال
- الخلط بين التزامن والتوازي
- افتراض إن الخيوط مابتتشاركش حاجة

### Practical Example (مثال عملي)

A web server handles thousands of requests by running many threads, but a shared counter without a lock can lose updates.

**Egyptian Arabic (اللهجة المصرية):**

سيرفر ويب بيتعامل مع آلاف الطلبات بتشغيل خيوط كتير، لكن عدّاد مشترك من غير قفل ممكن يضيّع تحديثات.

### Hands-On Exercise (تمرين عملي بإيدك)

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Process Synchronization, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نطام صغير تعرفه. اكتب: (1) الموقف في تزامن العمليات، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Process Synchronization in one sentence of your own words.
2. Give two situations where Process Synchronization changes a technical decision.
3. Name one limitation of Process Synchronization and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف تزامن العمليات في جملة واحدة بكلامك.
2. ادي موقفين تزامن العمليات بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود تزامن العمليات واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Process Synchronization? (a) a formality with no use (b) a working tool inside Operating Systems (c) an unrelated subject.
Q2. True or false: Process Synchronization has no limitations.
Q3. In one line, why does Process Synchronization matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـتزامن العمليات؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه نظم التشغيل (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: تزامن العمليات مالوش حدود.
س3. في سطر واحد، ليه تزامن العمليات مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Operating Systems.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه نظم التشغيل.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Process Synchronization to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها تزامن العمليات على برنامج أو نطام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Process Synchronization until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف تزامن العمليات تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الثاني: نظرية الحسابات (CS215)

## Properties of Regular Languages (خصائص اللغات النمطية)

Properties of Regular Languages (خصائص اللغات النمطية)
English Definition: Properties of Regular Languages is a core topic in Theory of Computation. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: خصائص اللغات النمطية موضوع أساسي في نظرية الحسابات. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Properties of Regular Languages** is the focus of this lesson. Theory of computation studies what can be computed and at what cost, using automata, grammars and Turing machines.

**Egyptian Arabic (اللهجة المصرية):**

**خصائص اللغات النمطية** هو محور الدرس ده. نظرية الحسابات بتدرس إيه اللي ممكن يتحسب وبأي تكلفة، باستخدام الآلات المجرّدة والقواعد وآلات تورينج.

### Why It Exists (ليه موجود)

It sets the limits of computing: some problems are unsolvable and some are intractable. Without a clear grasp of Properties of Regular Languages, the rest of Theory of Computation has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

بتحدّد حدود الحوسبة: في مشكلات مستحيلة الحل و في مشكلات مستعصية. ومن غير إدراك واضح لموضوع خصائص اللغات النمطية، باقي نظرية الحسابات ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Properties of Regular Languages is where the theory of Theory of Computation meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع خصائص اللغات النمطية هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

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

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Properties of Regular Languages, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نطام صغير تعرفه. اكتب: (1) الموقف في خصائص اللغات النمطية، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Properties of Regular Languages in one sentence of your own words.
2. Give two situations where Properties of Regular Languages changes a technical decision.
3. Name one limitation of Properties of Regular Languages and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف خصائص اللغات النمطية في جملة واحدة بكلامك.
2. ادي موقفين خصائص اللغات النمطية بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود خصائص اللغات النمطية واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Properties of Regular Languages? (a) a formality with no use (b) a working tool inside Theory of Computation (c) an unrelated subject.
Q2. True or false: Properties of Regular Languages has no limitations.
Q3. In one line, why does Properties of Regular Languages matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـخصائص اللغات النمطية؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه نظرية الحسابات (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: خصائص اللغات النمطية مالوش حدود.
س3. في سطر واحد، ليه خصائص اللغات النمطية مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Theory of Computation.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه نظرية الحسابات.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Properties of Regular Languages to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها خصائص اللغات النمطية على برنامج أو نطام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Properties of Regular Languages until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف خصائص اللغات النمطية تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الثالث: هندسة البرمجيات (CS216)

## System Modelling and UML (نمذجة الأنظمة و UML)

System Modelling and UML (نمذجة الأنظمة و UML)
English Definition: System Modelling and UML is a core topic in Software Engineering. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: نمذجة الأنظمة و UML موضوع أساسي في هندسة البرمجيات. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**System Modelling and UML** is the focus of this lesson. Software engineering applies engineering discipline to building software: requirements, design, construction, testing and maintenance at scale.

**Egyptian Arabic (اللهجة المصرية):**

**نمذجة الأنظمة و UML** هو محور الدرس ده. هندسة البرمجيات بتطبّق الانضباط الهندسي على بناء البرمجيات: المتطلبات والتصميم والبناء والاختبار والصيانة على نطاق واسع.

### Why It Exists (ليه موجود)

Large software fails without process: unclear requirements and untested code cost the most. Without a clear grasp of System Modelling and UML, the rest of Software Engineering has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

البرمجيات الكبيرة بتفشل من غير عملية: المتطلبات الغامضة والكود غير المختبر هما الأغلى. ومن غير إدراك واضح لموضوع نمذجة الأنظمة و UML، باقي هندسة البرمجيات ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, System Modelling and UML is where the theory of Software Engineering meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع نمذجة الأنظمة و UML هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

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

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in System Modelling and UML, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نطام صغير تعرفه. اكتب: (1) الموقف في نمذجة الأنظمة و UML، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define System Modelling and UML in one sentence of your own words.
2. Give two situations where System Modelling and UML changes a technical decision.
3. Name one limitation of System Modelling and UML and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف نمذجة الأنظمة و UML في جملة واحدة بكلامك.
2. ادي موقفين نمذجة الأنظمة و UML بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود نمذجة الأنظمة و UML واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes System Modelling and UML? (a) a formality with no use (b) a working tool inside Software Engineering (c) an unrelated subject.
Q2. True or false: System Modelling and UML has no limitations.
Q3. In one line, why does System Modelling and UML matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـنمذجة الأنظمة و UML؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه هندسة البرمجيات (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: نمذجة الأنظمة و UML مالوش حدود.
س3. في سطر واحد، ليه نمذجة الأنظمة و UML مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Software Engineering.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه هندسة البرمجيات.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying System Modelling and UML to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها نمذجة الأنظمة و UML على برنامج أو نطام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of System Modelling and UML until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف نمذجة الأنظمة و UML تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الرابع: شبكات الحاسب (CS217)

## Medium Access Control (التحكم في الوصول للوسط)

Medium Access Control (التحكم في الوصول للوسط)
English Definition: Medium Access Control is a core topic in Computer Networks. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: التحكم في الوصول للوسط موضوع أساسي في شبكات الحاسب. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Medium Access Control** is the focus of this lesson. Computer networks connect devices so they can exchange data, using layered protocols from the physical link up to applications.

**Egyptian Arabic (اللهجة المصرية):**

**التحكم في الوصول للوسط** هو محور الدرس ده. شبكات الحاسب بتربط الأجهزة عشان تتبادل البيانات، باستخدام بروتوكولات طبقية من الرابط الفيزيائي لفوق للتطبيقات.

### Why It Exists (ليه موجود)

The internet, cloud and every distributed system are networks; you cannot build them without understanding the layers. Without a clear grasp of Medium Access Control, the rest of Computer Networks has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

الإنترنت والسحابة وكل نظام موزّع شبكات؛ مش هتقدر تبنيها من غير فهم الطبقات. ومن غير إدراك واضح لموضوع التحكم في الوصول للوسط، باقي شبكات الحاسب ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Medium Access Control is where the theory of Computer Networks meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع التحكم في الوصول للوسط هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

### Where It Is Used (بنستخدمه فين)

- Internet and web communication
- Cloud and data centres
- Mobile and wireless systems
- Security and firewalls
- IoT and embedded devices

**Egyptian Arabic (اللهجة المصرية):**

- اتصال الإنترنت والويب
- السحابة ومراكز البيانات
- الأنظمة الجوالة واللاسلكية
- الأمن والجدران النارية
- إنترنت الأشياء والأجهزة المدمجة

### Real-World Usage and Relevance in the Field (الاستخدام والملاءمة في المجال)

When you load a web page, packets travel through many routers, and TCP reassembles them in order even if they arrive mixed up.

**Egyptian Arabic (اللهجة المصرية):**

لما تفتح صفحة ويب، الحزم بتعدي على راوترات كتير، و TCP بيعيد تجميعها بالترتيب حتى لو وصلت مبعترة.

### Advantages (المميزات)

- Enables global communication
- Layered design isolates problems
- Standards allow interoperability
- Foundation for cloud and distributed systems

**Egyptian Arabic (اللهجة المصرية):**

- بتمكّن التواصل العالمي
- التصميم الطبقي بيعزل المشكلات
- المعايير بتتيح التشغيل المتداخل
- أساس للسحابة والنظم الموزّعة

### Limitations (الحدود)

- Congestion and latency are hard to eliminate
- Security is an ongoing challenge
- Wireless links are unreliable
- Debugging spans many layers

**Egyptian Arabic (اللهجة المصرية):**

- الازدحام والزمن المستغرق صعب إلغاؤهم
- الأمن تحدٍّ مستمر
- الوصلات اللاسلكية غير موثوقة
- التنقيح بيمتد على طبقات كتير

### Best Practices (أحسن الممارسات)

- Learn the layers and their responsibilities
- Use tools like Wireshark to see real traffic
- Understand TCP vs UDP trade-offs
- Subnet and address carefully

**Egyptian Arabic (اللهجة المصرية):**

- اتعلم الطبقات ومسؤولياتها
- استخدم أدوات زي Wireshark عشان تشوف الترافيك الحقيقي
- افهم المقايضة بين TCP و UDP
- اعمل تقسيم وعنونة بعناية

### Common Mistakes (الأخطاء الشائعة)

- Confusing IP addresses with MAC addresses
- Assuming the network is always reliable
- Ignoring latency when designing protocols
- Misconfiguring subnets and routing

**Egyptian Arabic (اللهجة المصرية):**

- الخلط بين عناوين IP وعناوين MAC
- افتراض إن الشبكة موثوقة دايمًا
- تجاهل الزمن المستغرق وقت تصميم البروتوكولات
- أخطاء إعداد الشبكات الفرعية والتوجيه

### Practical Example (مثال عملي)

A video call uses UDP to keep latency low and accepts some packet loss, while a file download uses TCP to guarantee every byte arrives.

**Egyptian Arabic (اللهجة المصرية):**

مكالمة الفيديو بتستخدم UDP عشان تقلل الزمن المستغرق وتتحمّل فقدان بعض الحزم، بينما تحميل ملف بيستخدم TCP لضمان وصول كل بايت.

### Hands-On Exercise (تمرين عملي بإيدك)

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Medium Access Control, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نطام صغير تعرفه. اكتب: (1) الموقف في التحكم في الوصول للوسط، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Medium Access Control in one sentence of your own words.
2. Give two situations where Medium Access Control changes a technical decision.
3. Name one limitation of Medium Access Control and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف التحكم في الوصول للوسط في جملة واحدة بكلامك.
2. ادي موقفين التحكم في الوصول للوسط بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود التحكم في الوصول للوسط واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Medium Access Control? (a) a formality with no use (b) a working tool inside Computer Networks (c) an unrelated subject.
Q2. True or false: Medium Access Control has no limitations.
Q3. In one line, why does Medium Access Control matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـالتحكم في الوصول للوسط؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه شبكات الحاسب (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: التحكم في الوصول للوسط مالوش حدود.
س3. في سطر واحد، ليه التحكم في الوصول للوسط مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Computer Networks.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه شبكات الحاسب.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Medium Access Control to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها التحكم في الوصول للوسط على برنامج أو نطام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Medium Access Control until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف التحكم في الوصول للوسط تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الخامس: مقدمة في الذكاء الاصطناعي (AI201)

## Adversarial Search and Games (البحث التنافسي والألعاب)

Adversarial Search and Games (البحث التنافسي والألعاب)
English Definition: Adversarial Search and Games is a core topic in Artificial Intelligence. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: البحث التنافسي والألعاب موضوع أساسي في الذكاء الاصطناعي. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Adversarial Search and Games** is the focus of this lesson. Artificial intelligence builds agents that perceive, reason and act - using search, logic, learning and planning to solve problems.

**Egyptian Arabic (اللهجة المصرية):**

**البحث التنافسي والألعاب** هو محور الدرس ده. الذكاء الاصطناعي بيبني وكلاء بيحسّوا ويفكّروا ويتصرفوا - باستخدام البحث والمنطق والتعلّم والتخطيط لحل المشكلات.

### Why It Exists (ليه موجود)

AI now powers search, recommendations, assistants and automation across every industry. Without a clear grasp of Adversarial Search and Games, the rest of Artificial Intelligence has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

الذكاء الاصطناعي بقى بيشغّل البحث والتوصيات والمساعدين والأتمتة في كل صناعة. ومن غير إدراك واضح لموضوع البحث التنافسي والألعاب، باقي الذكاء الاصطناعي ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Adversarial Search and Games is where the theory of Artificial Intelligence meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع البحث التنافسي والألعاب هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

### Where It Is Used (بنستخدمه فين)

- Search and recommendation engines
- Games and planning systems
- Robotics and autonomous systems
- Assistants and chatbots
- Decision support

**Egyptian Arabic (اللهجة المصرية):**

- محرّكات البحث والتوصيات
- الألعاب وأنظمة التخطيط
- الروبوتات والأنظمة المستقلة
- المساعدين وروبوتات المحادثة
- دعم القرار

### Real-World Usage and Relevance in the Field (الاستخدام والملاءمة في المجال)

A chess engine searches possible moves and evaluates positions; a recommendation engine learns from behaviour - both are AI agents.

**Egyptian Arabic (اللهجة المصرية):**

محرّك الشطرنج بيبحث في الحركات الممكنة ويقيّم المواقف؛ ومحرّك التوصيات بيتعلم من السلوك - الاتنين وكلاء ذكاء اصطناعي.

### Advantages (المميزات)

- Solves problems too complex to code by hand
- Adapts from data and feedback
- Handles uncertainty and scale
- Powers automation and assistance

**Egyptian Arabic (اللهجة المصرية):**

- بيحل مشكلات معقدة جدًا لكتابتها يدويًا
- بيتكيّف من البيانات والتغذية الراجعة
- بيتعامل مع عدم اليقين والنطاق الواسع
- بيشغّل الأتمتة والمساعدة

### Limitations (الحدود)

- Needs data and compute
- Can be biased or brittle
- Hard to explain decisions
- Search space explodes quickly

**Egyptian Arabic (اللهجة المصرية):**

- محتاج بيانات وقدرة حوسبة
- ممكن يبقى متحيّز أو هش
- صعب تفسير قراراته
- فضاء البحث بيتفجّر بسرعة

### Best Practices (أحسن الممارسات)

- Define the problem and state space clearly
- Choose the right search or learning method
- Evaluate rigorously
- Consider ethics and bias

**Egyptian Arabic (اللهجة المصرية):**

- حدّد المشكلة وفضاء الحالات بوضوح
- اختار طريقة البحث أو التعلّم المناسبة
- قيّم بصرامة
- خد الأخلاقيات والتحيّز في الحساب

### Common Mistakes (الأخطاء الشائعة)

- Confusing AI with machine learning only
- Ignoring the search space size
- Overfitting to training data
- Skipping evaluation

**Egyptian Arabic (اللهجة المصرية):**

- الخلط بين الذكاء الاصطناعي وتعلّم الآلة فقط
- تجاهل حجم فضاء البحث
- الإفراط في التوفيق على بيانات التدريب
- تخطي التقييم

### Practical Example (مثال عملي)

A route planner treats cities as states and roads as actions, then runs A* search to find the shortest path - AI as intelligent search.

**Egyptian Arabic (اللهجة المصرية):**

مخطّط المسارات بيعتبر المدن حالات والطرق أفعال، وبعدين يشغّل بحث A* لإيجاد أقصر مسار - ذكاء اصطناعي كبحث ذكي.

### Hands-On Exercise (تمرين عملي بإيدك)

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Adversarial Search and Games, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نطام صغير تعرفه. اكتب: (1) الموقف في البحث التنافسي والألعاب، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Adversarial Search and Games in one sentence of your own words.
2. Give two situations where Adversarial Search and Games changes a technical decision.
3. Name one limitation of Adversarial Search and Games and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف البحث التنافسي والألعاب في جملة واحدة بكلامك.
2. ادي موقفين البحث التنافسي والألعاب بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود البحث التنافسي والألعاب واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Adversarial Search and Games? (a) a formality with no use (b) a working tool inside Artificial Intelligence (c) an unrelated subject.
Q2. True or false: Adversarial Search and Games has no limitations.
Q3. In one line, why does Adversarial Search and Games matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـالبحث التنافسي والألعاب؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه الذكاء الاصطناعي (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: البحث التنافسي والألعاب مالوش حدود.
س3. في سطر واحد، ليه البحث التنافسي والألعاب مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Artificial Intelligence.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه الذكاء الاصطناعي.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Adversarial Search and Games to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها البحث التنافسي والألعاب على برنامج أو نطام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Adversarial Search and Games until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف البحث التنافسي والألعاب تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم السادس: الأساليب الإحصائية وتحليل البيانات (ST201)

## Sampling Methods and Bias (طرق المعاينة والتحيّز)

Sampling Methods and Bias (طرق المعاينة والتحيّز)
English Definition: Sampling Methods and Bias is a core topic in Statistics and Data Analysis. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: طرق المعاينة والتحيّز موضوع أساسي في الإحصاء وتحليل البيانات. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Sampling Methods and Bias** is the focus of this lesson. Statistics and data analysis turn raw data into evidence: summarizing, testing hypotheses, and modelling relationships.

**Egyptian Arabic (اللهجة المصرية):**

**طرق المعاينة والتحيّز** هو محور الدرس ده. الإحصاء وتحليل البيانات بيحوّلوا البيانات الخام لأدلة: تلخيص واختبار فروض ونمذجة علاقات.

### Why It Exists (ليه موجود)

Data-driven decisions need more than averages; they need correct inference. Without a clear grasp of Sampling Methods and Bias, the rest of Statistics and Data Analysis has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

القرارات المبنية على البيانات محتاجة أكتر من المتوسطات؛ محتاجة استدلال صحيح. ومن غير إدراك واضح لموضوع طرق المعاينة والتحيّز، باقي الإحصاء وتحليل البيانات ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Sampling Methods and Bias is where the theory of Statistics and Data Analysis meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع طرق المعاينة والتحيّز هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

### Where It Is Used (بنستخدمه فين)

- Business and product analytics
- A/B testing and experiments
- Machine learning pipelines
- Research and surveys
- Quality control

**Egyptian Arabic (اللهجة المصرية):**

- تحليلات الأعمال والمنتجات
- اختبار A/B والتجارب
- خطوط تعلّم الآلة
- البحث والاستبيانات
- ضبط الجودة

### Real-World Usage and Relevance in the Field (الاستخدام والملاءمة في المجال)

A product team runs an experiment and uses a t-test to decide whether a new feature really improved retention or it was chance.

**Egyptian Arabic (اللهجة المصرية):**

فريق منتج بيعمل تجربة وبيستخدم اختبار t عشان يقرر هل ميزة جديدة حسّنت فعلاً البقاء ولا كانت صدفة.

### Advantages (المميزات)

- Turns data into decisions
- Quantifies uncertainty
- Detects real effects
- Foundation for machine learning

**Egyptian Arabic (اللهجة المصرية):**

- بيحوّل البيانات لقرارات
- بيقيس عدم اليقين
- بيكتشف التأثيرات الحقيقية
- أساس لتعلّم الآلة

### Limitations (الحدود)

- Wrong assumptions give wrong answers
- Correlation is not causation
- Bias in sampling propagates
- Overfitting to small samples

**Egyptian Arabic (اللهجة المصرية):**

- الفروض الغلط بتدي إجابات غلط
- الارتباط مش سببية
- التحيّز في المعاينة بينتقل
- الإفراط في التوفيق على العينات الصغيرة

### Best Practices (أحسن الممارسات)

- Clean and inspect data first
- Choose the test that matches the design
- Report effect sizes and intervals
- Validate on held-out data

**Egyptian Arabic (اللهجة المصرية):**

- نظّف البيانات وافحصها الأول
- اختار الاختبار المناسب للتصميم
- اذكر حجم الأثر والفترات
- تحقّق على بيانات محتجزة

### Common Mistakes (الأخطاء الشائعة)

- P-hacking and multiple comparisons
- Confusing statistical and practical significance
- Ignoring missing data
- Assuming normal distributions blindly

**Egyptian Arabic (اللهجة المصرية):**

- التلاعب بقيم p والمقارنات المتعددة
- الخلط بين الدلالة الإحصائية والعملية
- تجاهل البيانات الناقصة
- افتراض التوزيع الطبيعي أعمى

### Practical Example (مثال عملي)

Before concluding a new checkout design increased sales, the team checks the confidence interval and whether the sample was random.

**Egyptian Arabic (اللهجة المصرية):**

قبل ما يستنتجوا إن تصميم دفع جديد زوّد المبيعات، الفريق بيتأكد من فترة الثقة وهل العينة كانت عشوائية.

### Hands-On Exercise (تمرين عملي بإيدك)

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Sampling Methods and Bias, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نطام صغير تعرفه. اكتب: (1) الموقف في طرق المعاينة والتحيّز، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Sampling Methods and Bias in one sentence of your own words.
2. Give two situations where Sampling Methods and Bias changes a technical decision.
3. Name one limitation of Sampling Methods and Bias and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف طرق المعاينة والتحيّز في جملة واحدة بكلامك.
2. ادي موقفين طرق المعاينة والتحيّز بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود طرق المعاينة والتحيّز واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Sampling Methods and Bias? (a) a formality with no use (b) a working tool inside Statistics and Data Analysis (c) an unrelated subject.
Q2. True or false: Sampling Methods and Bias has no limitations.
Q3. In one line, why does Sampling Methods and Bias matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـطرق المعاينة والتحيّز؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه الإحصاء وتحليل البيانات (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: طرق المعاينة والتحيّز مالوش حدود.
س3. في سطر واحد، ليه طرق المعاينة والتحيّز مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Statistics and Data Analysis.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه الإحصاء وتحليل البيانات.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Sampling Methods and Bias to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها طرق المعاينة والتحيّز على برنامج أو نطام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Sampling Methods and Bias until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف طرق المعاينة والتحيّز تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

## Learning Resources (المصادر الدراسية)

### CS214 — نظم التشغيل

**Primary Resource (المصدر الأساسي)**

- **Resource Name:** Operating System Concepts (Silberschatz, Galvin & Gagne)
- **Resource Type:** Textbook
- **Direct Link:** https://os-book.com/
- **Difficulty:** Intermediate
- **Estimated Time:** 40 hours

- **Why Recommended:** The standard OS textbook, known as the dinosaur book.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: الكتاب المعياري لنظم التشغيل، المعروف بكتاب الديناصور.

- **What to Study From It:** Processes, scheduling, synchronization, memory and file systems.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: العمليات والجدولة والتزامن والذاكرة وأنظمة الملفات.

**Optional Resource (المصدر الاختياري)**

- **Resource Name:** OSTEP - Operating Systems: Three Easy Pieces
- **Resource Type:** Open Textbook
- **Direct Link:** https://pages.cs.wisc.edu/~remzi/OSTEP/
- **Difficulty:** Intermediate
- **Estimated Time:** 35 hours

- **Why Recommended:** A free, friendly OS book with excellent explanations.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: كتاب نظم تشغيل مجاني وودود بشرح ممتاز.

- **What to Study From It:** Virtualization, concurrency and persistence with real code.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: الافتراضية والتزامن والدوام مع كود حقيقي.

**Practice Platform (منصة التمرين العملي)**

- **Resource Name:** xv6 Teaching Operating System
- **Resource Type:** Practice Platform
- **Direct Link:** https://pdos.csail.mit.edu/6.828/2023/xv6.html
- **Difficulty:** Advanced
- **Estimated Time:** 30 hours

- **Why Recommended:** A small real OS you can read, modify and run.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: نظام تشغيل صغير حقيقي تقدر تقراه وتعدّله وتشغّله.

- **What to Study From It:** System calls, scheduling, memory and file system labs.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: معامل نداءات النظام والجدولة والذاكرة ونظام الملفات.

### CS215 — نظرية الحسابات

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

### CS216 — هندسة البرمجيات

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

### CS217 — شبكات الحاسب

**Primary Resource (المصدر الأساسي)**

- **Resource Name:** Computer Networking: A Top-Down Approach (Kurose & Ross)
- **Resource Type:** Textbook
- **Direct Link:** https://gaia.cs.umass.edu/kurose_ross/index.php
- **Difficulty:** Intermediate
- **Estimated Time:** 40 hours

- **Why Recommended:** A top-down textbook that starts from real applications and works down.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: كتاب من فوق لتحت بيبدأ من التطبيقات الحقيقية وينزل للأسفل.

- **What to Study From It:** Application, transport, network and link layers with real protocols.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: طبقات التطبيقات والنقل والشبكة والرابط ببروتوكولات حقيقية.

**Optional Resource (المصدر الاختياري)**

- **Resource Name:** Cisco Networking Basics
- **Resource Type:** Online Course
- **Direct Link:** https://www.netacad.com/courses/networking-basics
- **Difficulty:** Beginner
- **Estimated Time:** 25 hours

- **Why Recommended:** Hands-on networking course with practical labs.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: كورس شبكات عملي بمعامل تطبيقية.

- **What to Study From It:** IP addressing, routing, switching and network configuration.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: عنونة IP والتوجيه والتحويل وإعداد الشبكات.

**Practice Platform (منصة التمرين العملي)**

- **Resource Name:** Wireshark Labs
- **Resource Type:** Practice Platform
- **Direct Link:** https://gaia.cs.umass.edu/kurose_ross/wireshark.php
- **Difficulty:** Intermediate
- **Estimated Time:** 15 hours

- **Why Recommended:** Capture and analyse real packets to see protocols in action.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: التقط وحلّل حزم حقيقية عشان تشوف البروتوكولات شغّالة.

- **What to Study From It:** HTTP, TCP, DNS, IP and Ethernet traffic analysis.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: تحليل ترافيك HTTP و TCP و DNS و IP و Ethernet.

### AI201 — مقدمة في الذكاء الاصطناعي

**Primary Resource (المصدر الأساسي)**

- **Resource Name:** Artificial Intelligence: A Modern Approach (Russell & Norvig)
- **Resource Type:** Textbook
- **Direct Link:** https://aima.cs.berkeley.edu/
- **Difficulty:** Intermediate
- **Estimated Time:** 45 hours

- **Why Recommended:** The definitive AI textbook, used by universities worldwide.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: الكتاب المرجعي في الذكاء الاصطناعي، مستخدم في جامعات العالم.

- **What to Study From It:** Search, logic, planning, uncertainty, learning and perception.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: البحث والمنطق والتخطيط وعدم اليقين والتعلّم والإدراك.

**Optional Resource (المصدر الاختياري)**

- **Resource Name:** CS188 Intro to AI (UC Berkeley)
- **Resource Type:** University Course
- **Direct Link:** https://inst.eecs.berkeley.edu/~cs188/
- **Difficulty:** Intermediate
- **Estimated Time:** 35 hours

- **Why Recommended:** A famous AI course with projects that make search and learning hands-on.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: كورس ذكاء اصطناعي شهير بمشروعات بتخلي البحث والتعلّم عمليين.

- **What to Study From It:** Search, games, MDPs, reinforcement learning and Bayes nets.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: البحث والألعاب وعمليات ماركوف والتعلّم المعزّز وشبكات بايز.

**Practice Platform (منصة التمرين العملي)**

- **Resource Name:** Kaggle Learn
- **Resource Type:** Practice Platform
- **Direct Link:** https://www.kaggle.com/learn
- **Difficulty:** Beginner
- **Estimated Time:** 20 hours

- **Why Recommended:** Short hands-on courses on AI and data skills with real datasets.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: كورسات عملية قصيرة في مهارات الذكاء الاصطناعي والبيانات بمجموعات بيانات حقيقية.

- **What to Study From It:** Intro to AI, Python, and applied machine learning.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: مقدمة الذكاء الاصطناعي وبايثون وتعلّم الآلة التطبيقي.

### ST201 — الأساليب الإحصائية وتحليل البيانات

**Primary Resource (المصدر الأساسي)**

- **Resource Name:** Statistics for Data Science (Bruce & Bruce)
- **Resource Type:** Textbook
- **Direct Link:** https://www.oreilly.com/library/view/practical-statistics-for/9781491952955/
- **Difficulty:** Beginner
- **Estimated Time:** 25 hours

- **Why Recommended:** A practical, code-based introduction to statistics for data work.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: مقدمة عملية قائمة على الكود للإحصاء لشغل البيانات.

- **What to Study From It:** Exploratory analysis, sampling, hypothesis testing and regression.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: التحليل الاستكشافي والمعاينة واختبار الفروض والانحدار.

**Optional Resource (المصدر الاختياري)**

- **Resource Name:** StatQuest - Statistics Fundamentals
- **Resource Type:** Video Series
- **Direct Link:** https://www.youtube.com/@statquest
- **Difficulty:** Beginner
- **Estimated Time:** 15 hours

- **Why Recommended:** Clear videos that explain each statistical test step by step.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: فيديوهات واضحة بتشرح كل اختبار إحصائي خطوة بخطوة.

- **What to Study From It:** Distributions, t-tests, ANOVA, regression and p-values.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: التوزيعات واختبارات t وتحليل التباين والانحدار وقيم p.

**Practice Platform (منصة التمرين العملي)**

- **Resource Name:** Kaggle Learn - Data Analysis
- **Resource Type:** Practice Platform
- **Direct Link:** https://www.kaggle.com/learn/pandas
- **Difficulty:** Beginner
- **Estimated Time:** 15 hours

- **Why Recommended:** Hands-on data analysis with real datasets in the browser.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: تحليل بيانات عملي بمجموعات بيانات حقيقية في المتصفح.

- **What to Study From It:** Pandas, data cleaning, summarization and visualization.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: بانداس وتنظيف البيانات والتلخيص والتصوير.


---

## End of Lesson (نهاية الدرس)

### Lesson Summary (ملخص الدرس)

This week covered the following topics across the semester's courses: CS214: Process Synchronization; CS215: Properties of Regular Languages; CS216: System Modelling and UML; CS217: Medium Access Control; AI201: Adversarial Search and Games; ST201: Sampling Methods and Bias. Each topic opened with a bilingual definition, then explained what it is, why it exists, why it matters, where it is used, its advantages and limits, best practices and common mistakes, followed by a practical example and exercises.

**Egyptian Arabic (اللهجة المصرية):**

الأسبوع ده غطّى المواضيع دي في مقررات الفصل: CS214: تزامن العمليات؛ CS215: خصائص اللغات النمطية؛ CS216: نمذجة الأنظمة و UML؛ CS217: التحكم في الوصول للوسط؛ AI201: البحث التنافسي والألعاب؛ ST201: طرق المعاينة والتحيّز. كل موضوع بدأ بتعريف ثنائي اللغة، وبعدين شرح يعني إيه وليه موجود وليه مهم وبنستخدمه فين، ومميزاته وحدوده وأحسن الممارسات والأخطاء الشائعة، وبعدين مثال عملي وتمارين.

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

Next week continues with: CS214: Deadlocks; CS215: Context-Free Grammars; CS216: Architectural Design; CS217: The Network Layer and IP Addressing; AI201: Constraint Satisfaction Problems; ST201: Estimation and Confidence Intervals.

**Egyptian Arabic (اللهجة المصرية):**

الأسبوع الجاي بيكمل بـ: CS214: الجمود؛ CS215: القواعد الخالية من السياق؛ CS216: التصميم المعماري؛ CS217: طبقة الشبكة وعنونة IP؛ AI201: مشكلات تحقيق القيود؛ ST201: التقدير وفترات الثقة.

### Important Terms (مصطلحات مهمة)

#### Process (عملية)
English Definition: A running program with its own memory.
Egyptian Arabic Definition: برنامج شغّال بذاكرته الخاصة.

#### Thread (خيط)
English Definition: A lightweight unit of execution within a process.
Egyptian Arabic Definition: وحدة تنفيذ خفيفة داخل العملية.

#### Scheduling (الجدولة)
English Definition: Deciding which process runs next on the CPU.
Egyptian Arabic Definition: تحديد أي عملية تشتغل بعدين على المعالج.

#### Deadlock (الجمود)
English Definition: A state where processes wait on each other forever.
Egyptian Arabic Definition: حالة عمليات بتستنى بعض للأبد.

#### Virtual Memory (الذاكرة الافتراضية)
English Definition: Giving programs more memory than physically available.
Egyptian Arabic Definition: إعطاء البرامج ذاكرة أكبر من المتاح فعليًا.


---

[الدرس السابق: week-04.md](week-04.md) · [رجوع لفصل 4](README.md) · [الدرس الجاي: week-06.md](week-06.md)