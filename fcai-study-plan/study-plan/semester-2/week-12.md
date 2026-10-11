# الأسبوع 12 — الفصل 2

> الدرس ده بيغطّي موضوع واحد في كل مقرر من مقررات الفصل، وكل الشرح مكتوب بالعامية المصرية مع البلوك الإنجليزي الكامل جنبه.

**المقررات اللي في الدرس ده:** CS113 (البرمجة كائنية التوجه)، CS114 (هياكل البيانات)، MATH103 (الجبر الخطي)، MATH104 (الاحتمالات والإحصاء)، PHYS102 (الفيزياء 2)، ENG102 (اللغة الإنجليزية 2)

---

# القسم الأول: البرمجة كائنية التوجه (CS113)

## GUI Programming Basics (أساسيات واجهات المستخدم الرسومية)

GUI Programming Basics (أساسيات واجهات المستخدم الرسومية)
English Definition: GUI Programming Basics is a core topic in Object-Oriented Programming. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: أساسيات واجهات المستخدم الرسومية موضوع أساسي في البرمجة كائنية التوجه. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**GUI Programming Basics** is the focus of this lesson. Object-oriented programming organizes software into objects that combine data and behaviour, using classes, inheritance and polymorphism.

**Egyptian Arabic (اللهجة المصرية):**

**أساسيات واجهات المستخدم الرسومية** هو محور الدرس ده. البرمجة كائنية التوجه بتنظّم البرمجيات في كائنات بتجمع البيانات والسلوك، باستخدام الأصناف والوراثة وتعدّد الأشكال.

### Why It Exists (ليه موجود)

Large systems stay manageable when code is modelled as reusable, loosely coupled objects. Without a clear grasp of GUI Programming Basics, the rest of Object-Oriented Programming has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

الأنظمة الكبيرة تفضل قابلة للإدارة لما الكود يترسم ككائنات قابلة لإعادة الاستخدام ومترابطة بشكل مرن. ومن غير إدراك واضح لموضوع أساسيات واجهات المستخدم الرسومية، باقي البرمجة كائنية التوجه ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, GUI Programming Basics is where the theory of Object-Oriented Programming meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع أساسيات واجهات المستخدم الرسومية هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

### Where It Is Used (بنستخدمه فين)

- Application and enterprise software
- Game engines and simulations
- Frameworks and libraries
- GUI development
- Modelling real-world entities

**Egyptian Arabic (اللهجة المصرية):**

- تطبيقات وبرمجيات المؤسسات
- محرّكات الألعاب والمحاكاة
- أطر العمل والمكتبات
- تطوير واجهات المستخدم
- نمذجة كيانات العالم الحقيقي

### Real-World Usage and Relevance in the Field (الاستخدام والملاءمة في المجال)

A banking app models an Account object with a balance and methods to deposit and withdraw; inheritance lets a SavingsAccount reuse it.

**Egyptian Arabic (اللهجة المصرية):**

تطبيق بنك بيرسم كائن الحساب له رصيد ودوال إيداع وسحب؛ الوراثة بتخلي حساب التوفير يعيد استخدامه.

### Advantages (المميزات)

- Reuse through inheritance and composition
- Encapsulation hides complexity
- Polymorphism simplifies extension
- Maps well to real-world models

**Egyptian Arabic (اللهجة المصرية):**

- إعادة الاستخدام بالوراثة والتركيب
- التغليف بيخفي التعقيد
- تعدّد الأشكال بيبسّط التوسعة
- بيطابق نماذج العالم الحقيقي

### Limitations (الحدود)

- Overuse of inheritance causes fragile code
- Deep hierarchies are hard to change
- Can be slower than procedural code
- Requires careful design upfront

**Egyptian Arabic (اللهجة المصرية):**

- الإفراط في الوراثة بيعمل كود هش
- الهرميات العميقة صعب تغييرها
- ممكن تبقى أبطأ من الكود الإجرائي
- محتاجة تصميم دقيق من البداية

### Best Practices (أحسن الممارسات)

- Favour composition over inheritance
- Keep classes small and focused
- Program to interfaces, not implementations
- Apply SOLID principles

**Egyptian Arabic (اللهجة المصرية):**

- فضّل التركيب على الوراثة
- خلي الأصناف صغيرة ومركّزة
- برمج على الواجهات مش التنفيذات
- طبّق مبادئ SOLID

### Common Mistakes (الأخطاء الشائعة)

- God classes that do everything
- Breaking encapsulation with public fields
- Confusing inheritance with composition
- Ignoring the Liskov substitution principle

**Egyptian Arabic (اللهجة المصرية):**

- أصناف ضخمة بتعمل كل حاجة
- كسر التغليف بحقول عامة
- الخلط بين الوراثة والتركيب
- تجاهل مبدأ استبدال ليسكوف

### Practical Example (مثال عملي)

A shape hierarchy defines a Shape interface with an area method; circles and rectangles implement it, and code that sums areas never needs to change.

**Egyptian Arabic (اللهجة المصرية):**

هرمية الأشكال بتعرّف واجهة الشكل بدالة المساحة؛ الدواير والمستطيلات بتنفّذها، والكود اللي بيجمع المساحات ما بيحتاجش يتغير.

### Hands-On Exercise (تمرين عملي بإيدك)

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in GUI Programming Basics, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نطام صغير تعرفه. اكتب: (1) الموقف في أساسيات واجهات المستخدم الرسومية، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define GUI Programming Basics in one sentence of your own words.
2. Give two situations where GUI Programming Basics changes a technical decision.
3. Name one limitation of GUI Programming Basics and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف أساسيات واجهات المستخدم الرسومية في جملة واحدة بكلامك.
2. ادي موقفين أساسيات واجهات المستخدم الرسومية بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود أساسيات واجهات المستخدم الرسومية واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes GUI Programming Basics? (a) a formality with no use (b) a working tool inside Object-Oriented Programming (c) an unrelated subject.
Q2. True or false: GUI Programming Basics has no limitations.
Q3. In one line, why does GUI Programming Basics matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـأساسيات واجهات المستخدم الرسومية؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه البرمجة كائنية التوجه (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: أساسيات واجهات المستخدم الرسومية مالوش حدود.
س3. في سطر واحد، ليه أساسيات واجهات المستخدم الرسومية مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Object-Oriented Programming.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه البرمجة كائنية التوجه.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying GUI Programming Basics to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها أساسيات واجهات المستخدم الرسومية على برنامج أو نطام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of GUI Programming Basics until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف أساسيات واجهات المستخدم الرسومية تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الثاني: هياكل البيانات (CS114)

## Hash Tables and Hashing (جداول التقطيع والتقطيع)

Hash Tables and Hashing (جداول التقطيع والتقطيع)
English Definition: Hash Tables and Hashing is a core topic in Data Structures. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: جداول التقطيع والتقطيع موضوع أساسي في هياكل البيانات. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Hash Tables and Hashing** is the focus of this lesson. Data structures are ways of organizing data in memory - arrays, lists, stacks, queues, trees, hash tables and graphs - so that operations are fast and correct.

**Egyptian Arabic (اللهجة المصرية):**

**جداول التقطيع والتقطيع** هو محور الدرس ده. هياكل البيانات هي طرق تنظيم البيانات في الذاكرة - مصفوفات، قوائم، مكدّسات، طوابير، أشجار، جداول تقطيع ورسوم - عشان العمليات تبقى سريعة وصحيحة.

### Why It Exists (ليه موجود)

The right structure can turn a slow program into a fast one; almost every algorithm depends on choosing one. Without a clear grasp of Hash Tables and Hashing, the rest of Data Structures has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

الهيكل الصح ممكن يحوّل برنامج بطيء لسريع؛ تقريبًا كل خوارزمية بتعتمد على اختيار هيكل مناسب. ومن غير إدراك واضح لموضوع جداول التقطيع والتقطيع، باقي هياكل البيانات ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Hash Tables and Hashing is where the theory of Data Structures meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع جداول التقطيع والتقطيع هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

### Where It Is Used (بنستخدمه فين)

- Implementing algorithms efficiently
- Databases and indexing
- Compilers and interpreters
- Operating systems and schedulers
- Search engines and networks

**Egyptian Arabic (اللهجة المصرية):**

- تنفيذ الخوارزميات بكفاءة
- قواعد البيانات والفهرسة
- المترجمات والمفسّرات
- نظم التشغيل والجدولة
- محرّكات البحث والشبكات

### Real-World Usage and Relevance in the Field (الاستخدام والملاءمة في المجال)

When you search a contact on your phone, a hash table or a balanced tree is doing the work behind the scenes.

**Egyptian Arabic (اللهجة المصرية):**

لما تبحث عن رقم في جهات اتصالك، جدول تقطيع أو شجرة متوازنة هو اللي شغّال ورا الكواليس.

### Advantages (المميزات)

- Makes operations faster and predictable
- Clarifies the cost of each operation
- Reused across every area of computing
- Builds the base for algorithms and databases

**Egyptian Arabic (اللهجة المصرية):**

- بتخلي العمليات أسرع وأكثر قابلية للتوقّع
- بتوضّح تكلفة كل عملية
- بتُستخدم في كل مجالات الحوسبة
- بتبني الأساس للخوارزميات وقواعد البيانات

### Limitations (الحدود)

- Choice depends on the access pattern
- Memory overhead differs between structures
- Poor choice can cause huge slowdowns
- Implementation bugs are common

**Egyptian Arabic (اللهجة المصرية):**

- الاختيار بيعتمد على نمط الوصول
- استهلاك الذاكرة بيختلف بين الهياكل
- الاختيار الغلط ممكن يسبب بطء ضخم
- أخطاء التنفيذ شائعة

### Best Practices (أحسن الممارسات)

- Analyse the operations you need before choosing
- Know the time complexity of each operation
- Prefer the simplest structure that works
- Test with large inputs, not just small ones

**Egyptian Arabic (اللهجة المصرية):**

- حلّل العمليات المطلوبة قبل ما تختار
- اعرف تعقيد الزمن لكل عملية
- فضّل أبسط هيكل يحقق الغرض
- اختبر بمدخلات كبيرة مش صغيرة بس

### Common Mistakes (الأخطاء الشائعة)

- Using a list where a hash table is needed
- Ignoring worst-case complexity
- Forgetting that arrays are fixed size
- Mixing up stack and queue order

**Egyptian Arabic (اللهجة المصرية):**

- استخدام قائمة مكان ما جدول تقطيع مطلوب
- تجاهل تعقيد أسوأ حالة
- نسيان إن المصفوفة حجمها ثابت
- الخلط بين ترتيب المكدّس والطابور

### Practical Example (مثال عملي)

A web browser's back button is a stack: each page you visit is pushed, and going back pops the last one.

**Egyptian Arabic (اللهجة المصرية):**

زر الرجوع في المتصفح مكدّس: كل صفحة تزورها بتتحط فوق، والرجوع بيشيل آخر واحدة.

### Hands-On Exercise (تمرين عملي بإيدك)

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Hash Tables and Hashing, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نطام صغير تعرفه. اكتب: (1) الموقف في جداول التقطيع والتقطيع، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Hash Tables and Hashing in one sentence of your own words.
2. Give two situations where Hash Tables and Hashing changes a technical decision.
3. Name one limitation of Hash Tables and Hashing and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف جداول التقطيع والتقطيع في جملة واحدة بكلامك.
2. ادي موقفين جداول التقطيع والتقطيع بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود جداول التقطيع والتقطيع واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Hash Tables and Hashing? (a) a formality with no use (b) a working tool inside Data Structures (c) an unrelated subject.
Q2. True or false: Hash Tables and Hashing has no limitations.
Q3. In one line, why does Hash Tables and Hashing matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـجداول التقطيع والتقطيع؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه هياكل البيانات (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: جداول التقطيع والتقطيع مالوش حدود.
س3. في سطر واحد، ليه جداول التقطيع والتقطيع مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Data Structures.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه هياكل البيانات.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Hash Tables and Hashing to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها جداول التقطيع والتقطيع على برنامج أو نطام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Hash Tables and Hashing until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف جداول التقطيع والتقطيع تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الثالث: الجبر الخطي (MATH103)

## Diagonalization and Applications (التقطير وتطبيقاته)

Diagonalization and Applications (التقطير وتطبيقاته)
English Definition: Diagonalization and Applications is a core topic in Linear Algebra. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: التقطير وتطبيقاته موضوع أساسي في الجبر الخطي. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Diagonalization and Applications** is the focus of this lesson. Linear algebra studies vectors, matrices and linear transformations, and gives the tools to solve systems of equations and work with high-dimensional data.

**Egyptian Arabic (اللهجة المصرية):**

**التقطير وتطبيقاته** هو محور الدرس ده. الجبر الخطي بيدرس المتجهات والمصفوفات والتحويلات الخطية، وبيوفّر أدوات حل أنظمة المعادلات والتعامل مع بيانات عالية الأبعاد.

### Why It Exists (ليه موجود)

Machine learning, graphics and data analysis represent data as vectors and matrices and transform them with linear algebra. Without a clear grasp of Diagonalization and Applications, the rest of Linear Algebra has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

تعلّم الآلة والرسوم وتحليل البيانات بتمثّل البيانات كمتجهات ومصفوفات وتحوّلها بالجبر الخطي. ومن غير إدراك واضح لموضوع التقطير وتطبيقاته، باقي الجبر الخطي ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Diagonalization and Applications is where the theory of Linear Algebra meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع التقطير وتطبيقاته هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

### Where It Is Used (بنستخدمه فين)

- Machine learning and data analysis
- Computer graphics transformations
- Solving systems of equations
- Signal and image processing
- Optimization

**Egyptian Arabic (اللهجة المصرية):**

- تعلّم الآلة وتحليل البيانات
- تحويلات الرسوم بالحاسب
- حل أنظمة المعادلات
- معالجة الإشارات والصور
- التحسين

### Real-World Usage and Relevance in the Field (الاستخدام والملاءمة في المجال)

A recommendation system stores each user and item as a vector; the dot product of those vectors predicts what you might like.

**Egyptian Arabic (اللهجة المصرية):**

نظام التوصيات بيخزّن كل مستخدم وعنصر كمتجه؛ حاصل الضرب القياسي بين المتجهات دي بيتنبأ بإيه اللي ممكن يعجبك.

### Advantages (المميزات)

- Compact representation of large data
- Enables fast numerical computation
- Foundation for ML and graphics
- Solves large systems systematically

**Egyptian Arabic (اللهجة المصرية):**

- تمثيل مختصر لبيانات كبيرة
- بتمكّن حساب عددي سريع
- أساس لتعلّم الآلة والرسوم
- بتحل الأنظمة الكبيرة بشكل منظّم

### Limitations (الحدود)

- Not all matrices are invertible
- Numerical instability can occur
- Assumes linear relationships
- Large matrices are costly without optimization

**Egyptian Arabic (اللهجة المصرية):**

- مش كل المصفوفات ليها معكوس
- ممكن يحصل عدم استقرار عددي
- بتفترض علاقات خطية
- المصفوفات الكبيرة مكلفة من غير تحسين

### Best Practices (أحسن الممارسات)

- Visualize vectors and transformations geometrically
- Check invertibility before solving
- Use factorization for large systems
- Link eigenvalues to real problems

**Egyptian Arabic (اللهجة المصرية):**

- تصوّر المتجهات والتحويلات هندسيًا
- اتأكد من وجود المعكوس قبل الحل
- استخدم التحليل للمصفوفات الكبيرة
- اربط القيم الذاتية بمشكلات حقيقية

### Common Mistakes (الأخطاء الشائعة)

- Multiplying matrices in the wrong order
- Assuming every matrix has an inverse
- Confusing rank with dimension
- Ignoring numerical error

**Egyptian Arabic (اللهجة المصرية):**

- ضرب المصفوفات بترتيب غلط
- افتراض إن كل مصفوفة ليها معكوس
- الخلط بين الرتبة والأبعاد
- تجاهل الخطأ العددي

### Practical Example (مثال عملي)

Rotating a 3D object on screen is a matrix multiplication applied to every vertex of the model.

**Egyptian Arabic (اللهجة المصرية):**

تدوير جسم ثلاثي الأبعاد على الشاشة هو ضرب مصفوفة في كل رأس من رؤوس المجسم.

### Hands-On Exercise (تمرين عملي بإيدك)

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Diagonalization and Applications, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نطام صغير تعرفه. اكتب: (1) الموقف في التقطير وتطبيقاته، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Diagonalization and Applications in one sentence of your own words.
2. Give two situations where Diagonalization and Applications changes a technical decision.
3. Name one limitation of Diagonalization and Applications and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف التقطير وتطبيقاته في جملة واحدة بكلامك.
2. ادي موقفين التقطير وتطبيقاته بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود التقطير وتطبيقاته واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Diagonalization and Applications? (a) a formality with no use (b) a working tool inside Linear Algebra (c) an unrelated subject.
Q2. True or false: Diagonalization and Applications has no limitations.
Q3. In one line, why does Diagonalization and Applications matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـالتقطير وتطبيقاته؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه الجبر الخطي (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: التقطير وتطبيقاته مالوش حدود.
س3. في سطر واحد، ليه التقطير وتطبيقاته مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Linear Algebra.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه الجبر الخطي.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Diagonalization and Applications to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها التقطير وتطبيقاته على برنامج أو نطام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Diagonalization and Applications until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف التقطير وتطبيقاته تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الرابع: الاحتمالات والإحصاء (MATH104)

## Hypothesis Testing (اختبار الفروض)

Hypothesis Testing (اختبار الفروض)
English Definition: Hypothesis Testing is a core topic in Probability and Statistics. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: اختبار الفروض موضوع أساسي في الاحتمالات والإحصاء. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Hypothesis Testing** is the focus of this lesson. Probability and statistics quantify uncertainty, summarize data, and let you draw conclusions from samples using distributions and inference.

**Egyptian Arabic (اللهجة المصرية):**

**اختبار الفروض** هو محور الدرس ده. الاحتمالات والإحصاء بيقيسوا عدم اليقين، ويلخّصوا البيانات، ويخلّوك تستنتج من العينات باستخدام التوزيعات والاستدلال.

### Why It Exists (ليه موجود)

Machine learning, security and data analysis are all built on probabilistic reasoning. Without a clear grasp of Hypothesis Testing, the rest of Probability and Statistics has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

تعلّم الآلة والأمن وتحليل البيانات كلهم مبنيين على الاستدلال الاحتمالي. ومن غير إدراك واضح لموضوع اختبار الفروض، باقي الاحتمالات والإحصاء ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Hypothesis Testing is where the theory of Probability and Statistics meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع اختبار الفروض هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

### Where It Is Used (بنستخدمه فين)

- Machine learning and AI
- A/B testing and experiments
- Risk and reliability analysis
- Data analysis and reporting
- Cryptography and security

**Egyptian Arabic (اللهجة المصرية):**

- تعلّم الآلة والذكاء الاصطناعي
- اختبار A/B والتجارب
- تحليل المخاطر والموثوقية
- تحليل البيانات وإعداد التقارير
- التشفير والأمن

### Real-World Usage and Relevance in the Field (الاستخدام والملاءمة في المجال)

When a model says an email is 95% spam, it is reporting a conditional probability learned from data.

**Egyptian Arabic (اللهجة المصرية):**

لما نموذج يقول إن الإيميل سبام بنسبة 95%، هو بيقول احتمال شرطي اتعلمه من البيانات.

### Advantages (المميزات)

- Handles uncertainty rigorously
- Enables inference from samples
- Foundation for ML and testing
- Guides decisions under risk

**Egyptian Arabic (اللهجة المصرية):**

- بيتعامل مع عدم اليقين بصرامة
- بيمكّن الاستدلال من العينات
- أساس لتعلّم الآلة والاختبار
- بيوجّه القرارات تحت المخاطر

### Limitations (الحدود)

- Assumptions can be violated in practice
- Correlation is not causation
- Small samples mislead
- Misuse can produce false confidence

**Egyptian Arabic (اللهجة المصرية):**

- الفروض ممكن تتكسر عمليًا
- الارتباط مش سببية
- العينات الصغيرة بتضلّل
- سوء الاستخدام ممكن يطلع ثقة زائفة

### Best Practices (أحسن الممارسات)

- Check the assumptions of each test
- Distinguish correlation from causation
- Report uncertainty, not just point estimates
- Use enough data before concluding

**Egyptian Arabic (اللهجة المصرية):**

- اتأكد من فروض كل اختبار
- افرق بين الارتباط والسببية
- اذكر عدم اليقين مش التقدير النقطي بس
- استخدم بيانات كفاية قبل ما تستنتج

### Common Mistakes (الأخطاء الشائعة)

- Confusing p-values with effect size
- Ignoring sampling bias
- Treating dependent events as independent
- Overfitting conclusions to noise

**Egyptian Arabic (اللهجة المصرية):**

- الخلط بين قيم p وحجم الأثر
- تجاهل تحيّز المعاينة
- التعامل مع الأحداث التابعة كإنها مستقلة
- توفيق الاستنتاجات على الضوضاء

### Practical Example (مثال عملي)

A website tests two button colours; if the difference in click-through is larger than random variation, statistics says the change is real.

**Egyptian Arabic (اللهجة المصرية):**

موقع بيختبر لونين لزرار؛ لو الفرق في نسبة الضغط أكبر من التغيّر العشوائي، الإحصاء بيقول إن التغيير حقيقي.

### Hands-On Exercise (تمرين عملي بإيدك)

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Hypothesis Testing, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نطام صغير تعرفه. اكتب: (1) الموقف في اختبار الفروض، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Hypothesis Testing in one sentence of your own words.
2. Give two situations where Hypothesis Testing changes a technical decision.
3. Name one limitation of Hypothesis Testing and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف اختبار الفروض في جملة واحدة بكلامك.
2. ادي موقفين اختبار الفروض بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود اختبار الفروض واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Hypothesis Testing? (a) a formality with no use (b) a working tool inside Probability and Statistics (c) an unrelated subject.
Q2. True or false: Hypothesis Testing has no limitations.
Q3. In one line, why does Hypothesis Testing matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـاختبار الفروض؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه الاحتمالات والإحصاء (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: اختبار الفروض مالوش حدود.
س3. في سطر واحد، ليه اختبار الفروض مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Probability and Statistics.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه الاحتمالات والإحصاء.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Hypothesis Testing to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها اختبار الفروض على برنامج أو نطام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Hypothesis Testing until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف اختبار الفروض تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الخامس: الفيزياء 2 (PHYS102)

## Semiconductors and Electronics (أشباه الموصلات والإلكترونيات)

Semiconductors and Electronics (أشباه الموصلات والإلكترونيات)
English Definition: Semiconductors and Electronics is a core topic in Physics. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: أشباه الموصلات والإلكترونيات موضوع أساسي في الفيزياء. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Semiconductors and Electronics** is the focus of this lesson. Physics describes matter, energy and their interactions, and explains the physical principles that make computing hardware possible.

**Egyptian Arabic (اللهجة المصرية):**

**أشباه الموصلات والإلكترونيات** هو محور الدرس ده. الفيزياء بتوصف المادة والطاقة وتفاعلاتهما، وبتفسّر المبادئ الفيزيائية اللي بتخلي عتاد الحاسب ممكنًا.

### Why It Exists (ليه موجود)

Semiconductors, circuits, displays and storage all rest on physical laws you meet in first-year physics. Without a clear grasp of Semiconductors and Electronics, the rest of Physics has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

أشباه الموصلات والدوائر والشاشات والتخزين كلها قايمة على قوانين فيزيائية بتقابلها في فيزياء السنة الأولى. ومن غير إدراك واضح لموضوع أشباه الموصلات والإلكترونيات، باقي الفيزياء ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Semiconductors and Electronics is where the theory of Physics meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع أشباه الموصلات والإلكترونيات هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

### Where It Is Used (بنستخدمه فين)

- Semiconductor devices and transistors
- Electronic circuits and power
- Displays and sensors
- Magnetic and optical storage
- Signals and communication

**Egyptian Arabic (اللهجة المصرية):**

- أجهزة أشباه الموصلات والترانزستورات
- الدوائر الإلكترونية والطاقة
- الشاشات والمستشعرات
- التخزين المغناطيسي والبصري
- الإشارات والاتصال

### Real-World Usage and Relevance in the Field (الاستخدام والملاءمة في المجال)

A transistor is a tiny switch controlled by electric fields; billions of them on a chip perform every computation your computer does.

**Egyptian Arabic (اللهجة المصرية):**

الترانزستور مفتاح صغير بيتحكم فيه مجال كهربائي؛ مليارات منه على شريحة بتعمل كل عملية حاسبك بيعملها.

### Advantages (المميزات)

- Explains how hardware really works
- Builds modelling and measurement skills
- Foundation for electronics and signals
- Trains quantitative reasoning

**Egyptian Arabic (اللهجة المصرية):**

- بتفسّر إزاي العتاد بيشتغل فعلًا
- بتبني مهارات النمذجة والقياس
- أساس للإلكترونيات والإشارات
- بتدرّب التفكير الكمي

### Limitations (الحدود)

- Real systems are more complex than ideal models
- Requires solid calculus
- Measurement error is always present

**Egyptian Arabic (اللهجة المصرية):**

- الأنظمة الحقيقية أعقد من النماذج المثالية
- محتاجة تفاضل وتكامل قوي
- خطأ القياس موجود دايمًا

### Best Practices (أحسن الممارسات)

- Draw the system before solving
- Track units through every step
- Use conservation laws to simplify
- Verify with limiting cases

**Egyptian Arabic (اللهجة المصرية):**

- ارسم النظام قبل ما تحل
- تابع الوحدات في كل خطوة
- استخدم قوانين الحفظ للتبسيط
- اتأكد بالحالات الحدّية

### Common Mistakes (الأخطاء الشائعة)

- Dropping units
- Mixing scalar and vector quantities
- Ignoring sign conventions
- Applying formulas outside their range

**Egyptian Arabic (اللهجة المصرية):**

- إسقاط الوحدات
- الخلط بين الكميات القياسية والمتجهية
- تجاهل اصطلاحات الإشارة
- تطبيق القوانين برّه نطاقها

### Practical Example (مثال عملي)

An electric current is the flow of charge; controlling that flow with a transistor is how a chip encodes a 0 or a 1.

**Egyptian Arabic (اللهجة المصرية):**

التيار الكهربائي هو تدفق الشحنة؛ التحكم في التدفق ده بترانزستور هو الطريقة اللي الشريحة بترمّز بيها صفر أو واحد.

### Hands-On Exercise (تمرين عملي بإيدك)

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Semiconductors and Electronics, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نطام صغير تعرفه. اكتب: (1) الموقف في أشباه الموصلات والإلكترونيات، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Semiconductors and Electronics in one sentence of your own words.
2. Give two situations where Semiconductors and Electronics changes a technical decision.
3. Name one limitation of Semiconductors and Electronics and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف أشباه الموصلات والإلكترونيات في جملة واحدة بكلامك.
2. ادي موقفين أشباه الموصلات والإلكترونيات بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود أشباه الموصلات والإلكترونيات واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Semiconductors and Electronics? (a) a formality with no use (b) a working tool inside Physics (c) an unrelated subject.
Q2. True or false: Semiconductors and Electronics has no limitations.
Q3. In one line, why does Semiconductors and Electronics matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـأشباه الموصلات والإلكترونيات؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه الفيزياء (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: أشباه الموصلات والإلكترونيات مالوش حدود.
س3. في سطر واحد، ليه أشباه الموصلات والإلكترونيات مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Physics.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه الفيزياء.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Semiconductors and Electronics to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها أشباه الموصلات والإلكترونيات على برنامج أو نطام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Semiconductors and Electronics until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف أشباه الموصلات والإلكترونيات تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم السادس: اللغة الإنجليزية 2 (ENG102)

## Writing About Technology (الكتابة عن التكنولوجيا)

Writing About Technology (الكتابة عن التكنولوجيا)
English Definition: Writing About Technology is a core topic in English and Technical Communication. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: الكتابة عن التكنولوجيا موضوع أساسي في الإنجليزية والتواصل الفني. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Writing About Technology** is the focus of this lesson. English and technical communication cover reading, writing and presenting technical material clearly for academic and professional audiences.

**Egyptian Arabic (اللهجة المصرية):**

**الكتابة عن التكنولوجيا** هو محور الدرس ده. الإنجليزية والتواصل الفني بيغطوا القراءة والكتابة وعرض المواد الفنية بوضوح للجمهور الأكاديمي والمهني.

### Why It Exists (ليه موجود)

Computing is global: documentation, research papers, specs and interviews are all in English. Without a clear grasp of Writing About Technology, the rest of English and Technical Communication has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

الحوسبة عالمية: التوثيق والأوراق البحثية والمواصفات والمقابلات كلها بالإنجليزي. ومن غير إدراك واضح لموضوع الكتابة عن التكنولوجيا، باقي الإنجليزية والتواصل الفني ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Writing About Technology is where the theory of English and Technical Communication meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع الكتابة عن التكنولوجيا هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

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

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Writing About Technology, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نطام صغير تعرفه. اكتب: (1) الموقف في الكتابة عن التكنولوجيا، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Writing About Technology in one sentence of your own words.
2. Give two situations where Writing About Technology changes a technical decision.
3. Name one limitation of Writing About Technology and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف الكتابة عن التكنولوجيا في جملة واحدة بكلامك.
2. ادي موقفين الكتابة عن التكنولوجيا بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود الكتابة عن التكنولوجيا واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Writing About Technology? (a) a formality with no use (b) a working tool inside English and Technical Communication (c) an unrelated subject.
Q2. True or false: Writing About Technology has no limitations.
Q3. In one line, why does Writing About Technology matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـالكتابة عن التكنولوجيا؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه الإنجليزية والتواصل الفني (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: الكتابة عن التكنولوجيا مالوش حدود.
س3. في سطر واحد، ليه الكتابة عن التكنولوجيا مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside English and Technical Communication.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه الإنجليزية والتواصل الفني.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Writing About Technology to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها الكتابة عن التكنولوجيا على برنامج أو نطام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Writing About Technology until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف الكتابة عن التكنولوجيا تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

## Learning Resources (المصادر الدراسية)

### CS113 — البرمجة كائنية التوجه

**Primary Resource (المصدر الأساسي)**

- **Resource Name:** Java SE Documentation
- **Resource Type:** Official Documentation
- **Direct Link:** https://docs.oracle.com/en/java/javase/
- **Difficulty:** Intermediate
- **Estimated Time:** 25 hours

- **Why Recommended:** The official reference for the language most OOP courses use.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: المرجع الرسمي للغة اللي معظم مقررات الكائنية بتستخدمها.

- **What to Study From It:** Classes, inheritance, interfaces, generics and collections.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: الأصناف والوراثة والواجهات والأصناف العامة والمجموعات.

**Optional Resource (المصدر الاختياري)**

- **Resource Name:** Refactoring.Guru - Design Patterns
- **Resource Type:** Online Resource
- **Direct Link:** https://refactoring.guru/design-patterns
- **Difficulty:** Intermediate
- **Estimated Time:** 15 hours

- **Why Recommended:** Clear explanations of OOP design patterns with code examples.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: شرح واضح لأنماط تصميم الكائنية بأمثلة كود.

- **What to Study From It:** Creational, structural and behavioural design patterns.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: أنماط التصميم الإنشائية والبنيوية والسلوكية.

**Practice Platform (منصة التمرين العملي)**

- **Resource Name:** Exercism - Object-Oriented Tracks
- **Resource Type:** Practice Platform
- **Direct Link:** https://exercism.org/
- **Difficulty:** Beginner to Intermediate
- **Estimated Time:** 20 hours

- **Why Recommended:** Real exercises with mentor feedback in many OOP languages.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: تمارين حقيقية بتغذية راجعة من مرشدين في لغات كائنية كتير.

- **What to Study From It:** Class design, inheritance and polymorphism exercises.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: تمارين تصميم الأصناف والوراثة وتعدّد الأشكال.

### CS114 — هياكل البيانات

**Primary Resource (المصدر الأساسي)**

- **Resource Name:** Introduction to Algorithms (CLRS)
- **Resource Type:** Textbook
- **Direct Link:** https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/
- **Difficulty:** Intermediate
- **Estimated Time:** 40 hours

- **Why Recommended:** The definitive reference for data structures and algorithms used in universities worldwide.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: المرجع الأشهر لهياكل البيانات والخوارزميات المستخدم في جامعات العالم.

- **What to Study From It:** Arrays, linked lists, trees, hash tables, graphs and their complexity.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: المصفوفات والقوائم المترابطة والأشجار وجداول التقطيع والرسوم وتعقيدها.

**Optional Resource (المصدر الاختياري)**

- **Resource Name:** Visualgo - Data Structure Visualizations
- **Resource Type:** Interactive Tool
- **Direct Link:** https://visualgo.net/en
- **Difficulty:** Beginner
- **Estimated Time:** 15 hours

- **Why Recommended:** Animates each structure so you can see insertions, deletions and searches step by step.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: بتحرّك كل هيكل عشان تشوف الإضافة والحذف والبحث خطوة بخطوة.

- **What to Study From It:** Visualize lists, trees, heaps, hash tables and graph traversals.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: تصوّر القوائم والأشجار والأكوام وجداول التقطيع ومرور الرسوم.

**Practice Platform (منصة التمرين العملي)**

- **Resource Name:** HackerRank - Data Structures Track
- **Resource Type:** Practice Platform
- **Direct Link:** https://www.hackerrank.com/domains/data-structures
- **Difficulty:** Beginner to Intermediate
- **Estimated Time:** 25 hours

- **Why Recommended:** Guided problems grouped by structure, with instant feedback.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: مسائل موجّهة مجمّعة حسب الهيكل، مع تقييم فوري.

- **What to Study From It:** Arrays, linked lists, trees, stacks, queues and hash tables.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: المصفوفات والقوائم المترابطة والأشجار والمكدّسات والطوابير وجداول التقطيع.

### MATH103 — الجبر الخطي

**Primary Resource (المصدر الأساسي)**

- **Resource Name:** Linear Algebra and Its Applications (Lay)
- **Resource Type:** Textbook
- **Direct Link:** https://www.pearson.com/en-us/subject-catalog/p/linear-algebra-and-its-applications/P200000006235
- **Difficulty:** Intermediate
- **Estimated Time:** 35 hours

- **Why Recommended:** A clear, application-driven linear algebra textbook.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: كتاب جبر خطي واضح ومبني على التطبيقات.

- **What to Study From It:** Systems, matrices, vector spaces, eigenvalues and orthogonal projection.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: الأنظمة والمصفوفات والفضاءات الاتجاهية والقيم الذاتية والإسقاط المتعامد.

**Optional Resource (المصدر الاختياري)**

- **Resource Name:** MIT 18.06 Linear Algebra (Gilbert Strang)
- **Resource Type:** University Course
- **Direct Link:** https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/
- **Difficulty:** Intermediate
- **Estimated Time:** 35 hours

- **Why Recommended:** Legendary lectures that make linear algebra geometric and intuitive.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: محاضرات أسطورية بتخلي الجبر الخطي هندسي وبديهي.

- **What to Study From It:** Elimination, vector spaces, eigenvalues and applications.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: الحذف والفضاءات الاتجاهية والقيم الذاتية والتطبيقات.

**Practice Platform (منصة التمرين العملي)**

- **Resource Name:** 3Blue1Brown - Essence of Linear Algebra
- **Resource Type:** Video Series
- **Direct Link:** https://www.3blue1brown.com/topics/linear-algebra
- **Difficulty:** Beginner
- **Estimated Time:** 12 hours

- **Why Recommended:** Animated explanations that build strong geometric intuition.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: شرح متحرك بيبني حدسًا هندسيًا قويًا.

- **What to Study From It:** Vectors, transformations, determinants and eigenvectors visually.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: المتجهات والتحويلات والمحددات والمتجهات الذاتية بصريًا.

### MATH104 — الاحتمالات والإحصاء

**Primary Resource (المصدر الأساسي)**

- **Resource Name:** Introduction to Probability (Bertsekas & Tsitsiklis)
- **Resource Type:** Textbook
- **Direct Link:** https://athenasc.com/probbook.html
- **Difficulty:** Intermediate
- **Estimated Time:** 35 hours

- **Why Recommended:** A rigorous yet readable introduction to probability used at MIT.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: مقدمة صارمة وسهلة القراءة في الاحتمالات مستخدمة في MIT.

- **What to Study From It:** Probability, random variables, distributions and inference.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: الاحتمالات والمتغيرات العشوائية والتوزيعات والاستدلال.

**Optional Resource (المصدر الاختياري)**

- **Resource Name:** StatQuest with Josh Starmer
- **Resource Type:** Video Series
- **Direct Link:** https://www.youtube.com/@statquest
- **Difficulty:** Beginner
- **Estimated Time:** 20 hours

- **Why Recommended:** Friendly, clear videos that explain statistics and ML concepts simply.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: فيديوهات ودّية وواضحة بتشرح الإحصاء ومفاهيم تعلّم الآلة ببساطة.

- **What to Study From It:** Distributions, hypothesis testing, regression and ML statistics.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: التوزيعات واختبار الفروض والانحدار وإحصاء تعلّم الآلة.

**Practice Platform (منصة التمرين العملي)**

- **Resource Name:** Khan Academy - Statistics and Probability
- **Resource Type:** Practice Platform
- **Direct Link:** https://www.khanacademy.org/math/statistics-probability
- **Difficulty:** Beginner
- **Estimated Time:** 20 hours

- **Why Recommended:** Graded exercises with instant feedback on every statistical concept.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: تمارين متدرّجة بتقييم فوري على كل مفهوم إحصائي.

- **What to Study From It:** Probability, distributions, sampling and inference practice.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: تدريب على الاحتمالات والتوزيعات والمعاينة والاستدلال.

### PHYS102 — الفيزياء 2

**Primary Resource (المصدر الأساسي)**

- **Resource Name:** University Physics (Young & Freedman)
- **Resource Type:** Textbook
- **Direct Link:** https://www.pearson.com/en-us/subject-catalog/p/university-physics/P200000006239
- **Difficulty:** Intermediate
- **Estimated Time:** 40 hours

- **Why Recommended:** A comprehensive university physics text with strong problem sets.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: كتاب فيزياء جامعي شامل بمجموعات مسائل قوية.

- **What to Study From It:** Mechanics, waves, electricity, magnetism and modern physics.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: الميكانيكا والموجات والكهرباء والمغناطيسية والفيزياء الحديثة.

**Optional Resource (المصدر الاختياري)**

- **Resource Name:** MIT 8.01 Classical Mechanics
- **Resource Type:** University Course
- **Direct Link:** https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/
- **Difficulty:** Intermediate
- **Estimated Time:** 30 hours

- **Why Recommended:** Free MIT lectures that build physics intuition from the ground up.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: محاضرات MIT المجانية بتبني حدس الفيزياء من الصفر.

- **What to Study From It:** Kinematics, Newton's laws, energy, momentum and rotation.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: الحركة وقوانين نيوتن والطاقة والزخم والدوران.

**Practice Platform (منصة التمرين العملي)**

- **Resource Name:** The Physics Classroom
- **Resource Type:** Practice Platform
- **Direct Link:** https://www.physicsclassroom.com/
- **Difficulty:** Beginner
- **Estimated Time:** 15 hours

- **Why Recommended:** Clear tutorials with interactive practice on core topics.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: دروس واضحة مع تدريب تفاعلي على المواضيع الأساسية.

- **What to Study From It:** Mechanics, waves and electricity practice problems.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: مسائل تدريبية في الميكانيكا والموجات والكهرباء.

### ENG102 — اللغة الإنجليزية 2

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

This week covered the following topics across the semester's courses: CS113: GUI Programming Basics; CS114: Hash Tables and Hashing; MATH103: Diagonalization and Applications; MATH104: Hypothesis Testing; PHYS102: Semiconductors and Electronics; ENG102: Writing About Technology. Each topic opened with a bilingual definition, then explained what it is, why it exists, why it matters, where it is used, its advantages and limits, best practices and common mistakes, followed by a practical example and exercises.

**Egyptian Arabic (اللهجة المصرية):**

الأسبوع ده غطّى المواضيع دي في مقررات الفصل: CS113: أساسيات واجهات المستخدم الرسومية؛ CS114: جداول التقطيع والتقطيع؛ MATH103: التقطير وتطبيقاته؛ MATH104: اختبار الفروض؛ PHYS102: أشباه الموصلات والإلكترونيات؛ ENG102: الكتابة عن التكنولوجيا. كل موضوع بدأ بتعريف ثنائي اللغة، وبعدين شرح يعني إيه وليه موجود وليه مهم وبنستخدمه فين، ومميزاته وحدوده وأحسن الممارسات والأخطاء الشائعة، وبعدين مثال عملي وتمارين.

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

Next week continues with: CS113: Design Principles: SOLID; CS114: Graphs and Graph Representation; MATH103: Singular Value Decomposition Introduction; MATH104: Correlation and Regression; PHYS102: Nuclear Physics and Radiation; ENG102: Intercultural Communication.

**Egyptian Arabic (اللهجة المصرية):**

الأسبوع الجاي بيكمل بـ: CS113: مبادئ التصميم: SOLID؛ CS114: الرسوم البيانية وتمثيلها؛ MATH103: مقدمة في تحليل القيم المفردة؛ MATH104: الارتباط والانحدار؛ PHYS102: الفيزياء النووية والإشعاع؛ ENG102: التواصل بين الثقافات.

### Important Terms (مصطلحات مهمة)

#### Class (صنف)
English Definition: A blueprint that defines attributes and behaviour.
Egyptian Arabic Definition: مخطط بيحدّد الخصائص والسلوك.

#### Object (كائن)
English Definition: An instance of a class.
Egyptian Arabic Definition: نسخة من الصنف.

#### Inheritance (الوراثة)
English Definition: Deriving a class from another to reuse behaviour.
Egyptian Arabic Definition: اشتقاق صنف من تاني لإعادة استخدام السلوك.

#### Encapsulation (التغليف)
English Definition: Bundling data with methods and hiding internals.
Egyptian Arabic Definition: ضم البيانات مع الدوال وإخفاء الداخل.

#### Polymorphism (تعدّد الأشكال)
English Definition: Using one interface for many types.
Egyptian Arabic Definition: استخدام واجهة واحدة لأنواع كتير.


---

[الدرس السابق: week-11.md](week-11.md) · [رجوع لفصل 2](README.md) · [الدرس الجاي: week-13.md](week-13.md)