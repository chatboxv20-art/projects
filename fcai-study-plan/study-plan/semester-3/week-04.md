# الأسبوع 4 — الفصل 3

> الدرس ده بيغطّي موضوع واحد في كل مقرر من مقررات الفصل، وكل الشرح مكتوب بالعامية المصرية مع البلوك الإنجليزي الكامل جنبه.

**المقررات اللي في الدرس ده:** CS211 (تصميم وتحليل الخوارزميات)، CS212 (تنظيم الحاسب ولغة التجميع)، CS213 (نظم قواعد البيانات)، MATH201 (التفاضل والتكامل 2 والأساليب العددية)، IS201 (مقدمة في نظم المعلومات)، ENG201 (الكتابة الفنية والتواصل)

---

# القسم الأول: تصميم وتحليل الخوارزميات (CS211)

## Sorting Algorithms and Lower Bounds (خوارزميات الترتيب والحدود الدنيا)

Sorting Algorithms and Lower Bounds (خوارزميات الترتيب والحدود الدنيا)
English Definition: Sorting Algorithms and Lower Bounds is a core topic in Algorithms. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: خوارزميات الترتيب والحدود الدنيا موضوع أساسي في الخوارزميات. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Sorting Algorithms and Lower Bounds** is the focus of this lesson. Algorithms are precise, finite procedures for solving problems - sorting, searching, shortest paths, optimization - analysed for correctness and efficiency.

**Egyptian Arabic (اللهجة المصرية):**

**خوارزميات الترتيب والحدود الدنيا** هو محور الدرس ده. الخوارزميات هي إجراءات دقيقة ومنتهية لحل المشكلات - ترتيب، بحث، أقصر مسار، تحسين - وبتتحلّل من حيث الصحة والكفاءة.

### Why It Exists (ليه موجود)

Efficiency decides whether a solution works on real data or times out; algorithms give the language to reason about that. Without a clear grasp of Sorting Algorithms and Lower Bounds, the rest of Algorithms has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

الكفاءة بتحدد هل الحل هيشتغل على بيانات حقيقية ولا هيتوقف؛ الخوارزميات بتدي اللغة اللي تستنتج بيها. ومن غير إدراك واضح لموضوع خوارزميات الترتيب والحدود الدنيا، باقي الخوارزميات ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Sorting Algorithms and Lower Bounds is where the theory of Algorithms meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع خوارزميات الترتيب والحدود الدنيا هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

### Where It Is Used (بنستخدمه فين)

- Sorting and searching data
- Route planning and maps
- Compilers and schedulers
- Machine learning and optimization
- Cryptography and networks

**Egyptian Arabic (اللهجة المصرية):**

- ترتيب البيانات والبحث فيها
- تخطيط المسارات والخرائط
- المترجمات والجدولة
- تعلّم الآلة والتحسين
- التشفير والشبكات

### Real-World Usage and Relevance in the Field (الاستخدام والملاءمة في المجال)

Every time a maps app finds the fastest route, a shortest-path algorithm is running over a graph of roads.

**Egyptian Arabic (اللهجة المصرية):**

كل مرة تطبيق خرائط يلاقي أسرع طريق، خوارزمية أقصر مسار شغّالة على رسم بياني للطرق.

### Advantages (المميزات)

- Gives provable correctness and complexity
- Turns intractable problems into solvable ones
- Design paradigms transfer across problems
- Essential for interviews and research

**Egyptian Arabic (اللهجة المصرية):**

- بتدي صحة وتعقيد قابلين للبرهان
- بتحوّل المشكلات المستعصية لقابلة للحل
- أنماط التصميم بتنتقل بين المشكلات
- أساسية للمقابلات والبحث العلمي

### Limitations (الحدود)

- Some problems have no efficient algorithm
- Real data may break worst-case assumptions
- Correctness proofs can be hard
- Constant factors still matter in practice

**Egyptian Arabic (اللهجة المصرية):**

- في مشكلات مفيش لها خوارزمية فعّالة
- البيانات الحقيقية ممكن تكسر فروض أسوأ حالة
- براهين الصحة ممكن تبقى صعبة
- العوامل الثابتة لسه بتفرق عمليًا

### Best Practices (أحسن الممارسات)

- State the problem precisely first
- Prove correctness before optimizing
- Analyse time and space complexity
- Test on edge cases and large inputs

**Egyptian Arabic (اللهجة المصرية):**

- حدّد المشكلة بدقة الأول
- أثبت الصحة قبل التحسين
- حلّل تعقيد الزمن والمساحة
- اختبر على الحالات الحدّية والمدخلات الكبيرة

### Common Mistakes (الأخطاء الشائعة)

- Choosing an algorithm by habit, not analysis
- Ignoring the input size when comparing
- Assuming the fastest is always the best
- Skipping correctness checks

**Egyptian Arabic (اللهجة المصرية):**

- اختيار الخوارزمية بالعادة مش بالتحليل
- تجاهل حجم المدخل وقت المقارنة
- افتراض إن الأسرع هو الأفضل دايمًا
- تخطي فحوص الصحة

### Practical Example (مثال عملي)

Sorting a million records by insertion sort is too slow, but merge sort handles it in about twenty passes - complexity changes everything.

**Egyptian Arabic (اللهجة المصرية):**

ترتيب مليون سجل بترتيب الإدخال بطيء جدًا، لكن الدمج بيرتبهم في حوالي عشرين مرور - التعقيد بيغيّر كل حاجة.

### Hands-On Exercise (تمرين عملي بإيدك)

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Sorting Algorithms and Lower Bounds, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في خوارزميات الترتيب والحدود الدنيا، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Sorting Algorithms and Lower Bounds in one sentence of your own words.
2. Give two situations where Sorting Algorithms and Lower Bounds changes a technical decision.
3. Name one limitation of Sorting Algorithms and Lower Bounds and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف خوارزميات الترتيب والحدود الدنيا في جملة واحدة بكلامك.
2. ادي موقفين خوارزميات الترتيب والحدود الدنيا بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود خوارزميات الترتيب والحدود الدنيا واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Sorting Algorithms and Lower Bounds? (a) a formality with no use (b) a working tool inside Algorithms (c) an unrelated subject.
Q2. True or false: Sorting Algorithms and Lower Bounds has no limitations.
Q3. In one line, why does Sorting Algorithms and Lower Bounds matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـخوارزميات الترتيب والحدود الدنيا؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه الخوارزميات (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: خوارزميات الترتيب والحدود الدنيا مالوش حدود.
س3. في سطر واحد، ليه خوارزميات الترتيب والحدود الدنيا مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Algorithms.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه الخوارزميات.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Sorting Algorithms and Lower Bounds to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها خوارزميات الترتيب والحدود الدنيا على برنامج أو نظام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Sorting Algorithms and Lower Bounds until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف خوارزميات الترتيب والحدود الدنيا تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الثاني: تنظيم الحاسب ولغة التجميع (CS212)

## The Processor: Datapath and Control (المعالج: مسار البيانات والتحكم)

The Processor: Datapath and Control (المعالج: مسار البيانات والتحكم)
English Definition: The Processor: Datapath and Control is a core topic in Computer Organization and Architecture. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: المعالج: مسار البيانات والتحكم موضوع أساسي في تنظيم الحاسب ومعماريته. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**The Processor: Datapath and Control** is the focus of this lesson. Computer organization explains how processors, memory, buses and I/O devices work together to execute instructions and assembly programs.

**Egyptian Arabic (اللهجة المصرية):**

**المعالج: مسار البيانات والتحكم** هو محور الدرس ده. تنظيم الحاسب بيفسّر إزاي المعالجات والذاكرة والنواقل وأجهزة الإدخال والإخراج بتشتغل مع بعض لتنفيذ التعليمات وبرامج التجميع.

### Why It Exists (ليه موجود)

Performance, security and low-level bugs only make sense once you know how the machine actually executes code. Without a clear grasp of The Processor: Datapath and Control, the rest of Computer Organization and Architecture has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

الأداء والأمن والأخطاء منخفضة المستوى مش بتوضح إلا لما تعرف الجهاز بينفّذ الكود إزاي فعلًا. ومن غير إدراك واضح لموضوع المعالج: مسار البيانات والتحكم، باقي تنظيم الحاسب ومعماريته ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, The Processor: Datapath and Control is where the theory of Computer Organization and Architecture meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع المعالج: مسار البيانات والتحكم هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

### Where It Is Used (بنستخدمه فين)

- Performance tuning and profiling
- Embedded and systems programming
- Compilers and operating systems
- Hardware design
- Security and exploit analysis

**Egyptian Arabic (اللهجة المصرية):**

- ضبط الأداء والتحليل
- البرمجة المدمجة والنظم
- المترجمات ونظم التشغيل
- تصميم العتاد
- الأمن وتحليل الثغرات

### Real-World Usage and Relevance in the Field (الاستخدام والملاءمة في المجال)

A cache miss can make a loop ten times slower; understanding the memory hierarchy is how engineers write fast code.

**Egyptian Arabic (اللهجة المصرية):**

غياب البيانات في الذاكرة الوسيطة ممكن يبطّئ حلقة عشر مرات؛ فهم هرمية الذاكرة هو اللي بيخلي المهندسين يكتبوا كود سريع.

### Advantages (المميزات)

- Explains real performance behaviour
- Links software to hardware
- Foundation for systems courses
- Enables low-level optimization

**Egyptian Arabic (اللهجة المصرية):**

- بتفسّر سلوك الأداء الحقيقي
- بتربط البرمجيات بالعتاد
- أساس لمقررات النظم
- بتمكّن التحسين منخفض المستوى

### Limitations (الحدود)

- Hardware details vary between machines
- Assembly is verbose and error-prone
- Architectures change over time

**Egyptian Arabic (اللهجة المصرية):**

- تفاصيل العتاد بتختلف بين الأجهزة
- لغة التجميع طويلة ومعرّضة للأخطاء
- المعماريات بتتغير بمرور الوقت

### Best Practices (أحسن الممارسات)

- Trace instructions through the datapath
- Learn the memory hierarchy first
- Profile before optimizing
- Read assembly to understand compilers

**Egyptian Arabic (اللهجة المصرية):**

- تتبّع التعليمات خلال مسار البيانات
- اتعلم هرمية الذاكرة الأول
- اعمل تحليل أداء قبل التحسين
- اقرا التجميع عشان تفهم المترجمات

### Common Mistakes (الأخطاء الشائعة)

- Assuming all memory accesses cost the same
- Ignoring cache behaviour
- Confusing registers with memory
- Hand-optimizing before profiling

**Egyptian Arabic (اللهجة المصرية):**

- افتراض إن كل وصول للذاكرة بنفس التكلفة
- تجاهل سلوك الذاكرة الوسيطة
- الخلط بين المسجّلات والذاكرة
- التحسين اليدوي قبل التحليل

### Practical Example (مثال عملي)

Multiplying two large matrices in the right loop order keeps data in cache and can run several times faster - same math, different memory access.

**Egyptian Arabic (اللهجة المصرية):**

ضرب مصفوفتين كبيرتين بترتيب الحلقات الصح بيخلي البيانات في الذاكرة الوسيطة وممكن يشتغل أسرع عدة مرات - نفس الرياضيات ووصول ذاكرة مختلف.

### Hands-On Exercise (تمرين عملي بإيدك)

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in The Processor: Datapath and Control, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في المعالج: مسار البيانات والتحكم، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define The Processor: Datapath and Control in one sentence of your own words.
2. Give two situations where The Processor: Datapath and Control changes a technical decision.
3. Name one limitation of The Processor: Datapath and Control and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف المعالج: مسار البيانات والتحكم في جملة واحدة بكلامك.
2. ادي موقفين المعالج: مسار البيانات والتحكم بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود المعالج: مسار البيانات والتحكم واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes The Processor: Datapath and Control? (a) a formality with no use (b) a working tool inside Computer Organization and Architecture (c) an unrelated subject.
Q2. True or false: The Processor: Datapath and Control has no limitations.
Q3. In one line, why does The Processor: Datapath and Control matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـالمعالج: مسار البيانات والتحكم؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه تنظيم الحاسب ومعماريته (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: المعالج: مسار البيانات والتحكم مالوش حدود.
س3. في سطر واحد، ليه المعالج: مسار البيانات والتحكم مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Computer Organization and Architecture.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه تنظيم الحاسب ومعماريته.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying The Processor: Datapath and Control to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها المعالج: مسار البيانات والتحكم على برنامج أو نظام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of The Processor: Datapath and Control until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف المعالج: مسار البيانات والتحكم تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الثالث: نظم قواعد البيانات (CS213)

## Entity-Relationship Modelling (نمذجة الكيان والعلاقة)

Entity-Relationship Modelling (نمذجة الكيان والعلاقة)
English Definition: Entity-Relationship Modelling is a core topic in Database Systems. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: نمذجة الكيان والعلاقة موضوع أساسي في نظم قواعد البيانات. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Entity-Relationship Modelling** is the focus of this lesson. Database systems store, organize and query large amounts of structured data using the relational model, SQL, transactions and indexing.

**Egyptian Arabic (اللهجة المصرية):**

**نمذجة الكيان والعلاقة** هو محور الدرس ده. نظم قواعد البيانات بتخزّن وتنظّم وتستعلم عن كميات كبيرة من البيانات المنظّمة باستخدام النموذج العلائقي و SQL والمعاملات والفهرسة.

### Why It Exists (ليه موجود)

Almost every application needs durable, consistent, concurrent access to data. Without a clear grasp of Entity-Relationship Modelling, the rest of Database Systems has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

تقريبًا كل تطبيق محتاج وصول دائم ومتسق ومتزامن للبيانات. ومن غير إدراك واضح لموضوع نمذجة الكيان والعلاقة، باقي نظم قواعد البيانات ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Entity-Relationship Modelling is where the theory of Database Systems meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع نمذجة الكيان والعلاقة هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

### Where It Is Used (بنستخدمه فين)

- Web and mobile back ends
- Enterprise and ERP systems
- Analytics and reporting
- Banking and transactions
- Content and inventory management

**Egyptian Arabic (اللهجة المصرية):**

- الواجهات الخلفية للويب والموبايل
- أنظمة المؤسسات و ERP
- التحليلات والتقارير
- البنوك والمعاملات
- إدارة المحتوى والمخزون

### Real-World Usage and Relevance in the Field (الاستخدام والملاءمة في المجال)

When you book a flight, a database transaction guarantees that the seat is reserved exactly once, even with thousands of users booking at once.

**Egyptian Arabic (اللهجة المصرية):**

لما تحجز رحلة، معاملة قاعدة بيانات بتضمن إن المقعد اتحجز مرة واحدة بالظبط، حتى مع آلاف المستخدمين في نفس الوقت.

### Advantages (المميزات)

- Enforces consistency and integrity
- Powerful declarative querying with SQL
- Handles concurrency and recovery
- Scales to huge datasets

**Egyptian Arabic (اللهجة المصرية):**

- بتفرض الاتساق والنزاهة
- استعلام وصفي قوي بـ SQL
- بتتعامل مع التزامن والاستعادة
- بتتوسّع لبيانات ضخمة

### Limitations (الحدود)

- Schema changes are costly
- Poor design hurts performance
- Scaling writes is hard
- NoSQL trades consistency for flexibility

**Egyptian Arabic (اللهجة المصرية):**

- تغيير المخطط مكلف
- التصميم الوحش بيضر الأداء
- توسيع الكتابة صعب
- NoSQL بتقايض الاتساق بالمرونة

### Best Practices (أحسن الممارسات)

- Normalize first, denormalize for performance
- Index the columns you filter on
- Use transactions for related writes
- Design the schema from requirements

**Egyptian Arabic (اللهجة المصرية):**

- طبّع الأول، وخفّف التطبيع للأداء
- اعمل فهرس على الأعمدة اللي بتفلتر بيها
- استخدم المعاملات للكتابات المترابطة
- صمّم المخطط من المتطلبات

### Common Mistakes (الأخطاء الشائعة)

- Storing everything in one huge table
- Missing indexes on join columns
- Ignoring transaction isolation
- Writing queries that fetch unneeded rows

**Egyptian Arabic (اللهجة المصرية):**

- تخزين كل حاجة في جدول ضخم واحد
- غياب الفهارس على أعمدة الوصل
- تجاهل عزل المعاملات
- كتابة استعلامات بتجيب صفوف مش محتاجة

### Practical Example (مثال عملي)

An online store keeps customers, orders and products in separate related tables; a join reconstructs a full order without duplicating data.

**Egyptian Arabic (اللهجة المصرية):**

متجر إلكتروني بيخزّن العملاء والطلبات والمنتجات في جداول مترابطة منفصلة؛ الوصلة بتعيد بناء الطلب كامل من غير تكرار البيانات.

### Hands-On Exercise (تمرين عملي بإيدك)

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Entity-Relationship Modelling, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في نمذجة الكيان والعلاقة، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Entity-Relationship Modelling in one sentence of your own words.
2. Give two situations where Entity-Relationship Modelling changes a technical decision.
3. Name one limitation of Entity-Relationship Modelling and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف نمذجة الكيان والعلاقة في جملة واحدة بكلامك.
2. ادي موقفين نمذجة الكيان والعلاقة بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود نمذجة الكيان والعلاقة واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Entity-Relationship Modelling? (a) a formality with no use (b) a working tool inside Database Systems (c) an unrelated subject.
Q2. True or false: Entity-Relationship Modelling has no limitations.
Q3. In one line, why does Entity-Relationship Modelling matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـنمذجة الكيان والعلاقة؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه نظم قواعد البيانات (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: نمذجة الكيان والعلاقة مالوش حدود.
س3. في سطر واحد، ليه نمذجة الكيان والعلاقة مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Database Systems.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه نظم قواعد البيانات.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Entity-Relationship Modelling to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها نمذجة الكيان والعلاقة على برنامج أو نظام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Entity-Relationship Modelling until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف نمذجة الكيان والعلاقة تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الرابع: التفاضل والتكامل 2 والأساليب العددية (MATH201)

## Power Series and Taylor Series (متسلسلات القوى ومتسلسلات تايلور)

Power Series and Taylor Series (متسلسلات القوى ومتسلسلات تايلور)
English Definition: Power Series and Taylor Series is a core topic in Calculus. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: متسلسلات القوى ومتسلسلات تايلور موضوع أساسي في التفاضل والتكامل. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Power Series and Taylor Series** is the focus of this lesson. Calculus studies change: limits, derivatives, integrals and series, and it provides the mathematics behind optimization and continuous models.

**Egyptian Arabic (اللهجة المصرية):**

**متسلسلات القوى ومتسلسلات تايلور** هو محور الدرس ده. التفاضل والتكامل بيدرس التغيّر: النهايات والمشتقات والتكاملات والمتسلسلات، وبيوفّر الرياضيات ورا التحسين والنماذج المتصلة.

### Why It Exists (ليه موجود)

Machine learning, graphics and numerical methods all rest on derivatives and integrals. Without a clear grasp of Power Series and Taylor Series, the rest of Calculus has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

تعلّم الآلة والرسوم بالحاسب والأساليب العددية كلها قايمة على المشتقات والتكاملات. ومن غير إدراك واضح لموضوع متسلسلات القوى ومتسلسلات تايلور، باقي التفاضل والتكامل ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Power Series and Taylor Series is where the theory of Calculus meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع متسلسلات القوى ومتسلسلات تايلور هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

### Where It Is Used (بنستخدمه فين)

- Optimization and gradient descent
- Physics and engineering models
- Computer graphics and curves
- Numerical methods
- Probability and statistics

**Egyptian Arabic (اللهجة المصرية):**

- التحسين والانحدار التدريجي
- النماذج الفيزيائية والهندسية
- الرسوم بالحاسب والمنحنيات
- الأساليب العددية
- الاحتمالات والإحصاء

### Real-World Usage and Relevance in the Field (الاستخدام والملاءمة في المجال)

Training a neural network means repeatedly using derivatives to adjust weights - that is calculus running millions of times per second.

**Egyptian Arabic (اللهجة المصرية):**

تدريب شبكة عصبية معناه استخدام المشتقات بشكل متكرر لتعديل الأوزان - ده تفاضل شغّال ملايين المرات في الثانية.

### Advantages (المميزات)

- Foundation for all continuous modelling
- Enables optimization and learning
- Explains rates and accumulation
- Connects to geometry and physics

**Egyptian Arabic (اللهجة المصرية):**

- أساس لكل النمذجة المتصلة
- بتمكّن التحسين والتعلّم
- بتفسّر المعدلات والتراكم
- بتربط بالهندسة والفيزياء

### Limitations (الحدود)

- Symbolic results can be hard or impossible
- Assumes continuity and smoothness
- Real data is often noisy
- Numerical errors can accumulate

**Egyptian Arabic (اللهجة المصرية):**

- النتائج الرمزية ممكن تبقى صعبة أو مستحيلة
- بتفترض الاتصال والنعومة
- البيانات الحقيقية غالبًا مشوّشة
- الأخطاء العددية ممكن تتراكم

### Best Practices (أحسن الممارسات)

- Master the derivative rules first
- Sketch functions to build intuition
- Check symbolic answers numerically
- Link each rule to an application

**Egyptian Arabic (اللهجة المصرية):**

- اتقن قواعد الاشتقاق الأول
- ارسم الدوال عشان تبني الحدس
- اتأكد من الحلول الرمزية عدديًا
- اربط كل قاعدة بتطبيق

### Common Mistakes (الأخطاء الشائعة)

- Forgetting the chain rule
- Ignoring domains and discontinuities
- Sign errors in integration
- Applying results outside their assumptions

**Egyptian Arabic (اللهجة المصرية):**

- نسيان قاعدة السلسلة
- تجاهل المجالات ونقاط عدم الاتصال
- أخطاء الإشارة في التكامل
- تطبيق النتائج برّه فروضها

### Practical Example (مثال عملي)

To find the maximum profit of a business, you write profit as a function, take its derivative and solve for where the slope is zero.

**Egyptian Arabic (اللهجة المصرية):**

عشان تلاقي أقصى ربح لمشروع، تكتب الربح كدالة، تاخد مشتقتها، وتحل عند النقطة اللي الميل فيها صفر.

### Hands-On Exercise (تمرين عملي بإيدك)

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Power Series and Taylor Series, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في متسلسلات القوى ومتسلسلات تايلور، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Power Series and Taylor Series in one sentence of your own words.
2. Give two situations where Power Series and Taylor Series changes a technical decision.
3. Name one limitation of Power Series and Taylor Series and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف متسلسلات القوى ومتسلسلات تايلور في جملة واحدة بكلامك.
2. ادي موقفين متسلسلات القوى ومتسلسلات تايلور بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود متسلسلات القوى ومتسلسلات تايلور واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Power Series and Taylor Series? (a) a formality with no use (b) a working tool inside Calculus (c) an unrelated subject.
Q2. True or false: Power Series and Taylor Series has no limitations.
Q3. In one line, why does Power Series and Taylor Series matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـمتسلسلات القوى ومتسلسلات تايلور؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه التفاضل والتكامل (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: متسلسلات القوى ومتسلسلات تايلور مالوش حدود.
س3. في سطر واحد، ليه متسلسلات القوى ومتسلسلات تايلور مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Calculus.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه التفاضل والتكامل.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Power Series and Taylor Series to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها متسلسلات القوى ومتسلسلات تايلور على برنامج أو نظام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Power Series and Taylor Series until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف متسلسلات القوى ومتسلسلات تايلور تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الخامس: مقدمة في نظم المعلومات (IS201)

## Requirements Gathering and Analysis (جمع المتطلبات وتحليلها)

Requirements Gathering and Analysis (جمع المتطلبات وتحليلها)
English Definition: Requirements Gathering and Analysis is a core topic in Information Systems. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: جمع المتطلبات وتحليلها موضوع أساسي في نظم المعلومات. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Requirements Gathering and Analysis** is the focus of this lesson. Information systems combine people, processes and technology to collect, process and deliver information that supports decisions.

**Egyptian Arabic (اللهجة المصرية):**

**جمع المتطلبات وتحليلها** هو محور الدرس ده. نظم المعلومات بتجمع الناس والعمليات والتكنولوجيا عشان تجمع وتعالج وتوصّل المعلومات اللي بتدعم القرارات.

### Why It Exists (ليه موجود)

Technology only creates value when it fits the organization's processes and goals. Without a clear grasp of Requirements Gathering and Analysis, the rest of Information Systems has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

التكنولوجيا مش بتخلق قيمة إلا لما تناسب عمليات المنظمة وأهدافها. ومن غير إدراك واضح لموضوع جمع المتطلبات وتحليلها، باقي نظم المعلومات ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Requirements Gathering and Analysis is where the theory of Information Systems meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع جمع المتطلبات وتحليلها هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

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

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Requirements Gathering and Analysis, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في جمع المتطلبات وتحليلها، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Requirements Gathering and Analysis in one sentence of your own words.
2. Give two situations where Requirements Gathering and Analysis changes a technical decision.
3. Name one limitation of Requirements Gathering and Analysis and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف جمع المتطلبات وتحليلها في جملة واحدة بكلامك.
2. ادي موقفين جمع المتطلبات وتحليلها بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود جمع المتطلبات وتحليلها واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Requirements Gathering and Analysis? (a) a formality with no use (b) a working tool inside Information Systems (c) an unrelated subject.
Q2. True or false: Requirements Gathering and Analysis has no limitations.
Q3. In one line, why does Requirements Gathering and Analysis matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـجمع المتطلبات وتحليلها؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه نظم المعلومات (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: جمع المتطلبات وتحليلها مالوش حدود.
س3. في سطر واحد، ليه جمع المتطلبات وتحليلها مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Information Systems.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه نظم المعلومات.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Requirements Gathering and Analysis to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها جمع المتطلبات وتحليلها على برنامج أو نظام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Requirements Gathering and Analysis until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف جمع المتطلبات وتحليلها تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم السادس: الكتابة الفنية والتواصل (ENG201)

## Documenting Code and APIs (توثيق الكود وواجهات البرمجة)

Documenting Code and APIs (توثيق الكود وواجهات البرمجة)
English Definition: Documenting Code and APIs is a core topic in English and Technical Communication. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: توثيق الكود وواجهات البرمجة موضوع أساسي في الإنجليزية والتواصل الفني. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Documenting Code and APIs** is the focus of this lesson. English and technical communication cover reading, writing and presenting technical material clearly for academic and professional audiences.

**Egyptian Arabic (اللهجة المصرية):**

**توثيق الكود وواجهات البرمجة** هو محور الدرس ده. الإنجليزية والتواصل الفني بيغطوا القراءة والكتابة وعرض المواد الفنية بوضوح للجمهور الأكاديمي والمهني.

### Why It Exists (ليه موجود)

Computing is global: documentation, research papers, specs and interviews are all in English. Without a clear grasp of Documenting Code and APIs, the rest of English and Technical Communication has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

الحوسبة عالمية: التوثيق والأوراق البحثية والمواصفات والمقابلات كلها بالإنجليزي. ومن غير إدراك واضح لموضوع توثيق الكود وواجهات البرمجة، باقي الإنجليزية والتواصل الفني ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Documenting Code and APIs is where the theory of English and Technical Communication meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع توثيق الكود وواجهات البرمجة هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

### Where It Is Used (بنستخدمه فين)

- Writing technical reports and documentation
- Reading research papers
- Presenting and defending work
- Writing professional emails
- Collaborating in global teams

**Egyptian Arabic (اللهجة المصرية):**

- كتابة التقارير الفنية والتوثيق
- قراءة الأوراق البحثية
- العرض والدفاع عن الشغل
- كتابة الإيميلات المهنية
- التعاون في فرق عالمية

### Real-World Usage and Relevance in the Field (الاستخدام والملاءمة في المجال)

A software engineer writes more prose than code: commit messages, README files, design docs and bug reports.

**Egyptian Arabic (اللهجة المصرية):**

مهندس البرمجيات بيكتب نصوص أكتر من كود: رسائل الـcommit وملفات README ووثائق التصميم وتقارير الأخطاء.

### Advantages (المميزات)

- Opens access to global knowledge
- Improves documentation and collaboration
- Sharpens critical reading
- Essential for research and interviews

**Egyptian Arabic (اللهجة المصرية):**

- بيفتح الوصول للمعرفة العالمية
- بيحسّن التوثيق والتعاون
- بيصقل القراءة النقدية
- أساسي للبحث والمقابلات

### Limitations (الحدود)

- Progress needs consistent practice
- Technical writing has its own conventions
- Translation can hide meaning if careless

**Egyptian Arabic (اللهجة المصرية):**

- التقدّم محتاج تمرين مستمر
- الكتابة الفنية ليها اصطلاحاتها
- الترجمة ممكن تخفي المعنى لو كانت مهملة

### Best Practices (أحسن الممارسات)

- Read widely and take notes in English
- Learn the structure of technical documents
- Revise for clarity and concision
- Practise speaking aloud regularly

**Egyptian Arabic (اللهجة المصرية):**

- اقرا كتير وخد ملاحظات بالإنجليزي
- اتعلم بنية المستندات الفنية
- راجع عشان الوضوح والإيجاز
- اتمرّن على التحدث بصوت عالي بانتظام

### Common Mistakes (الأخطاء الشائعة)

- Translating idioms literally
- Overusing passive voice
- Ignoring the audience
- Copying sources without citation

**Egyptian Arabic (اللهجة المصرية):**

- ترجمة التعبيرات الاصطلاحية حرفيًا
- الإفراط في المبني للمجهول
- تجاهل الجمهور
- نسخ المصادر من غير توثيق

### Practical Example (مثال عملي)

A clear bug report states what happened, what was expected, and the steps to reproduce - three sentences that save hours.

**Egyptian Arabic (اللهجة المصرية):**

تقرير خطأ واضح بيقول إيه اللي حصل، وإيه اللي كان متوقّع، وخطوات إعادة المشكلة - ثلاث جمل بتوفّر ساعات.

### Hands-On Exercise (تمرين عملي بإيدك)

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Documenting Code and APIs, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في توثيق الكود وواجهات البرمجة، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Documenting Code and APIs in one sentence of your own words.
2. Give two situations where Documenting Code and APIs changes a technical decision.
3. Name one limitation of Documenting Code and APIs and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف توثيق الكود وواجهات البرمجة في جملة واحدة بكلامك.
2. ادي موقفين توثيق الكود وواجهات البرمجة بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود توثيق الكود وواجهات البرمجة واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Documenting Code and APIs? (a) a formality with no use (b) a working tool inside English and Technical Communication (c) an unrelated subject.
Q2. True or false: Documenting Code and APIs has no limitations.
Q3. In one line, why does Documenting Code and APIs matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـتوثيق الكود وواجهات البرمجة؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه الإنجليزية والتواصل الفني (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: توثيق الكود وواجهات البرمجة مالوش حدود.
س3. في سطر واحد، ليه توثيق الكود وواجهات البرمجة مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside English and Technical Communication.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه الإنجليزية والتواصل الفني.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Documenting Code and APIs to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها توثيق الكود وواجهات البرمجة على برنامج أو نظام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Documenting Code and APIs until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف توثيق الكود وواجهات البرمجة تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

## Learning Resources (المصادر الدراسية)

### CS211 — تصميم وتحليل الخوارزميات

**Primary Resource (المصدر الأساسي)**

- **Resource Name:** Introduction to Algorithms (CLRS)
- **Resource Type:** Textbook
- **Direct Link:** https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/
- **Difficulty:** Advanced
- **Estimated Time:** 45 hours

- **Why Recommended:** The most complete treatment of algorithm design and analysis.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: أشمل مرجع لتصميم الخوارزميات وتحليلها.

- **What to Study From It:** Divide and conquer, greedy, dynamic programming, graphs and NP-completeness.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: التقسيم والتغلب والجشع والبرمجة الديناميكية والرسوم واكتمال NP.

**Optional Resource (المصدر الاختياري)**

- **Resource Name:** MIT 6.006 Introduction to Algorithms
- **Resource Type:** University Course
- **Direct Link:** https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/
- **Difficulty:** Intermediate
- **Estimated Time:** 35 hours

- **Why Recommended:** Free MIT lectures that build intuition for complexity and design.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: محاضرات MIT المجانية بتبني الحدس للتعقيد والتصميم.

- **What to Study From It:** Sorting, hashing, graphs, dynamic programming and shortest paths.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: الترتيب والتقطيع والرسوم والبرمجة الديناميكية وأقصر مسار.

**Practice Platform (منصة التمرين العملي)**

- **Resource Name:** Codeforces
- **Resource Type:** Practice Platform
- **Direct Link:** https://codeforces.com/
- **Difficulty:** Intermediate to Advanced
- **Estimated Time:** 40 hours

- **Why Recommended:** Competitive programming contests that sharpen algorithmic thinking.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: مسابقات برمجة تنافسية بتصقل التفكير الخوارزمي.

- **What to Study From It:** Greedy, dynamic programming, graphs and number theory problems.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: مسائل الجشع والبرمجة الديناميكية والرسوم ونظرية الأعداد.

### CS212 — تنظيم الحاسب ولغة التجميع

**Primary Resource (المصدر الأساسي)**

- **Resource Name:** Computer Organization and Design (Patterson & Hennessy)
- **Resource Type:** Textbook
- **Direct Link:** https://www.elsevier.com/books/computer-organization-and-design-mips-edition/patterson/978-0-12-820109-1
- **Difficulty:** Intermediate
- **Estimated Time:** 40 hours

- **Why Recommended:** The standard text linking assembly, datapath, pipeline and memory.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: المرجع المعياري اللي بيربط التجميع ومسار البيانات والتداخل والذاكرة.

- **What to Study From It:** ISA, arithmetic, pipelining, caches and I/O.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: مجموعة التعليمات والحساب والتداخل والذاكرات الوسيطة والإدخال والإخراج.

**Optional Resource (المصدر الاختياري)**

- **Resource Name:** Nand2Tetris - Build a Computer
- **Resource Type:** Online Course
- **Direct Link:** https://www.nand2tetris.org/
- **Difficulty:** Intermediate
- **Estimated Time:** 40 hours

- **Why Recommended:** You build a computer from logic gates up, which makes everything concrete.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: بتبني حاسب من البوابات المنطقية لفوق، وده بيخلي كل حاجة ملموسة.

- **What to Study From It:** Logic gates, ALU, memory, assembly and the hardware-software interface.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: البوابات المنطقية ووحدة الحساب والذاكرة والتجميع وواجهة العتاد والبرمجيات.

**Practice Platform (منصة التمرين العملي)**

- **Resource Name:** MARS MIPS Simulator
- **Resource Type:** Practice Tool
- **Direct Link:** http://courses.missouristate.edu/KenVollmar/MARS/
- **Difficulty:** Intermediate
- **Estimated Time:** 15 hours

- **Why Recommended:** Run and step through MIPS assembly to see registers and memory change.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: شغّل وتتبّع لغة تجميع MIPS عشان تشوف المسجّلات والذاكرة بتتغير.

- **What to Study From It:** Assembly exercises on arithmetic, procedures and the stack.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: تمارين تجميع على الحساب والإجراءات والمكدّس.

### CS213 — نظم قواعد البيانات

**Primary Resource (المصدر الأساسي)**

- **Resource Name:** Database System Concepts (Silberschatz, Korth & Sudarshan)
- **Resource Type:** Textbook
- **Direct Link:** https://www.db-book.com/
- **Difficulty:** Intermediate
- **Estimated Time:** 40 hours

- **Why Recommended:** The classic database textbook covering theory and practice.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: الكتاب الكلاسيكي لقواعد البيانات بيغطي النظرية والتطبيق.

- **What to Study From It:** Relational model, SQL, normalization, transactions and indexing.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: النموذج العلائقي و SQL والتطبيع والمعاملات والفهرسة.

**Optional Resource (المصدر الاختياري)**

- **Resource Name:** SQLBolt
- **Resource Type:** Interactive Tutorial
- **Direct Link:** https://sqlbolt.com/
- **Difficulty:** Beginner
- **Estimated Time:** 10 hours

- **Why Recommended:** Learn SQL interactively in the browser with immediate feedback.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: اتعلم SQL تفاعليًا في المتصفح بتغذية راجعة فورية.

- **What to Study From It:** SELECT, joins, aggregation and modifying data.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: الاستعلام والوصلات والتجميع وتعديل البيانات.

**Practice Platform (منصة التمرين العملي)**

- **Resource Name:** LeetCode - Database Problems
- **Resource Type:** Practice Platform
- **Direct Link:** https://leetcode.com/problemset/database/
- **Difficulty:** Intermediate
- **Estimated Time:** 20 hours

- **Why Recommended:** Realistic SQL problems that build query skills fast.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: مسائل SQL واقعية بتبني مهارات الاستعلام بسرعة.

- **What to Study From It:** Joins, subqueries, window functions and aggregation.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: الوصلات والاستعلامات الفرعية ودوال النوافذ والتجميع.

### MATH201 — التفاضل والتكامل 2 والأساليب العددية

**Primary Resource (المصدر الأساسي)**

- **Resource Name:** Calculus (Stewart)
- **Resource Type:** Textbook
- **Direct Link:** https://www.stewartcalculus.com/
- **Difficulty:** Beginner to Intermediate
- **Estimated Time:** 40 hours

- **Why Recommended:** The most widely used calculus textbook, with clear examples and exercises.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: أشهر كتاب تفاضل وتكامل، بأمثلة وتمارين واضحة.

- **What to Study From It:** Limits, derivatives, integrals, series and multivariable calculus.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: النهايات والمشتقات والتكاملات والمتسلسلات وحساب المتغيرات المتعددة.

**Optional Resource (المصدر الاختياري)**

- **Resource Name:** Khan Academy - Calculus
- **Resource Type:** Online Course
- **Direct Link:** https://www.khanacademy.org/math/calculus-1
- **Difficulty:** Beginner
- **Estimated Time:** 30 hours

- **Why Recommended:** Short videos and graded practice that make each idea click.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: فيديوهات قصيرة وتدريبات متدرّجة بتوضّح كل فكرة.

- **What to Study From It:** Limits, differentiation, integration and applications.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: النهايات والاشتقاق والتكامل والتطبيقات.

**Practice Platform (منصة التمرين العملي)**

- **Resource Name:** Paul's Online Math Notes
- **Resource Type:** Practice Platform
- **Direct Link:** https://tutorial.math.lamar.edu/
- **Difficulty:** Intermediate
- **Estimated Time:** 20 hours

- **Why Recommended:** Concise notes with hundreds of fully worked practice problems.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: ملاحظات مختصرة فيها مئات المسائل المحلولة بالكامل.

- **What to Study From It:** Worked examples on derivatives, integrals and series.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: أمثلة محلولة على المشتقات والتكاملات والمتسلسلات.

### IS201 — مقدمة في نظم المعلومات

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

### ENG201 — الكتابة الفنية والتواصل

**Primary Resource (المصدر الأساسي)**

- **Resource Name:** Technical Communication Today (Johnson-Sheehan)
- **Resource Type:** Textbook
- **Direct Link:** https://www.pearson.com/en-us/subject-catalog/p/technical-communication-today/P200000005948
- **Difficulty:** Beginner
- **Estimated Time:** 25 hours

- **Why Recommended:** A practical guide to writing documents engineers actually use.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: دليل عملي لكتابة المستندات اللي المهندسين بيستخدموها فعلًا.

- **What to Study From It:** Reports, proposals, documentation and presentation structure.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: التقارير والمقترحات والتوثيق وبنية العرض.

**Optional Resource (المصدر الاختياري)**

- **Resource Name:** Purdue OWL - Technical Writing
- **Resource Type:** Online Resource
- **Direct Link:** https://owl.purdue.edu/owl/subject_specific_writing/professional_technical_writing/index.html
- **Difficulty:** Beginner
- **Estimated Time:** 12 hours

- **Why Recommended:** Free, reliable guidance on style, citation and document types.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: إرشاد مجاني وموثوق في الأسلوب والتوثيق وأنواع المستندات.

- **What to Study From It:** Grammar, style, citation and technical document conventions.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: القواعد والأسلوب والتوثيق واصطلاحات المستندات الفنية.

**Practice Platform (منصة التمرين العملي)**

- **Resource Name:** Grammarly Handbook
- **Resource Type:** Practice Platform
- **Direct Link:** https://www.grammarly.com/blog/
- **Difficulty:** Beginner
- **Estimated Time:** 10 hours

- **Why Recommended:** Short, searchable explanations of grammar and writing issues.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: شروح قصيرة قابلة للبحث لمشكلات القواعد والكتابة.

- **What to Study From It:** Grammar, punctuation and clarity exercises.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: تمارين القواعد وعلامات الترقيم والوضوح.


---

## End of Lesson (نهاية الدرس)

### Lesson Summary (ملخص الدرس)

This week covered the following topics across the semester's courses: CS211: Sorting Algorithms and Lower Bounds; CS212: The Processor: Datapath and Control; CS213: Entity-Relationship Modelling; MATH201: Power Series and Taylor Series; IS201: Requirements Gathering and Analysis; ENG201: Documenting Code and APIs. Each topic opened with a bilingual definition, then explained what it is, why it exists, why it matters, where it is used, its advantages and limits, best practices and common mistakes, followed by a practical example and exercises.

**Egyptian Arabic (اللهجة المصرية):**

الأسبوع ده غطّى المواضيع دي في مقررات الفصل: CS211: خوارزميات الترتيب والحدود الدنيا؛ CS212: المعالج: مسار البيانات والتحكم؛ CS213: نمذجة الكيان والعلاقة؛ MATH201: متسلسلات القوى ومتسلسلات تايلور؛ IS201: جمع المتطلبات وتحليلها؛ ENG201: توثيق الكود وواجهات البرمجة. كل موضوع بدأ بتعريف ثنائي اللغة، وبعدين شرح يعني إيه وليه موجود وليه مهم وبنستخدمه فين، ومميزاته وحدوده وأحسن الممارسات والأخطاء الشائعة، وبعدين مثال عملي وتمارين.

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

اختار موضوع واحد من الأسبوع ده وطبّقه كامل على نظام حقيقي: الموقف والتحليل والتوصية.

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

Next week continues with: CS211: Greedy Algorithms; CS212: Pipelining; CS213: SQL: Data Definition; MATH201: Partial Derivatives; IS201: Process Modelling; ENG201: User Manuals and Guides.

**Egyptian Arabic (اللهجة المصرية):**

الأسبوع الجاي بيكمل بـ: CS211: الخوارزميات الجشعة؛ CS212: التداخل الزمني؛ CS213: SQL: تعريف البيانات؛ MATH201: المشتقات الجزئية؛ IS201: نمذجة العمليات؛ ENG201: أدلة المستخدم والإرشادات.

### Important Terms (مصطلحات مهمة)

#### Time Complexity (تعقيد الزمن)
English Definition: How running time grows with input size.
Egyptian Arabic Definition: إزاي وقت التشغيل بيكبر مع حجم المدخل.

#### Big-O Notation (ترميز O الكبير)
English Definition: An upper bound on an algorithm's growth rate.
Egyptian Arabic Definition: حد أعلى لمعدل نمو الخوارزمية.

#### Recursion (الاستدعاء الذاتي)
English Definition: Solving a problem by solving smaller instances of itself.
Egyptian Arabic Definition: حل المشكلة بحل نسخ أصغر منها.

#### Greedy (جشع)
English Definition: Making the locally best choice at each step.
Egyptian Arabic Definition: اتخاذ أفضل اختيار محلي في كل خطوة.

#### Dynamic Programming (البرمجة الديناميكية)
English Definition: Solving overlapping subproblems once and reusing results.
Egyptian Arabic Definition: حل المشكلات الفرعية المتداخلة مرة وإعادة استخدام النتائج.


---

[الدرس السابق: week-03.md](week-03.md) · [رجوع لفصل 3](README.md) · [الدرس الجاي: week-05.md](week-05.md)