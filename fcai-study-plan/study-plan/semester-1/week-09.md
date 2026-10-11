# الأسبوع 9 — الفصل 1

> الدرس ده بيغطّي موضوع واحد في كل مقرر من مقررات الفصل، وكل الشرح مكتوب بالعامية المصرية مع البلوك الإنجليزي الكامل جنبه.

**المقررات اللي في الدرس ده:** CS111 (أساسيات علوم الحاسب)، CS112 (مقدمة في البرمجة)، MATH101 (التفاضل والتكامل 1)، MATH102 (الرياضيات المتقطعة)، PHYS101 (الفيزياء 1)، ENG101 (اللغة الإنجليزية 1)

---

# القسم الأول: أساسيات علوم الحاسب (CS111)

## Programming Languages and Compilers (لغات البرمجة والمترجمات)

Programming Languages and Compilers (لغات البرمجة والمترجمات)
English Definition: Programming Languages and Compilers is a core topic in Computer Science Foundations. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: لغات البرمجة والمترجمات موضوع أساسي في أساسيات علوم الحاسب. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Programming Languages and Compilers** is the focus of this lesson. Computer Science foundations explain how computers represent data, how programs are built, and how the major areas of computing fit together.

**Egyptian Arabic (اللهجة المصرية):**

**لغات البرمجة والمترجمات** هو محور الدرس ده. أساسيات علوم الحاسب بتشرح إزاي الحاسب بيمثّل البيانات، وإزاي البرامج بتتبني، وإزاي مجالات الحوسبة الكبيرة بترتبط ببعض.

### Why It Exists (ليه موجود)

Every advanced course - programming, databases, networks, AI - assumes you know what a computer is and how it processes information. Without a clear grasp of Programming Languages and Compilers, the rest of Computer Science Foundations has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

كل مقرر متقدّم - برمجة، قواعد بيانات، شبكات، ذكاء اصطناعي - بيفترض إنك عارف الحاسب إيه وإزاي بيعالج المعلومات. ومن غير إدراك واضح لموضوع لغات البرمجة والمترجمات، باقي أساسيات علوم الحاسب ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Programming Languages and Compilers is where the theory of Computer Science Foundations meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع لغات البرمجة والمترجمات هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

### Where It Is Used (بنستخدمه فين)

- Writing and reading programs
- Understanding computer hardware and software
- Choosing the right data representation
- Studying networks, databases and AI
- Preparing for all later CS courses

**Egyptian Arabic (اللهجة المصرية):**

- كتابة البرامج وقراءتها
- فهم عتاد الحاسب وبرمجياته
- اختيار تمثيل البيانات المناسب
- دراسة الشبكات وقواعد البيانات والذكاء الاصطناعي
- الاستعداد لكل مقررات الحاسب اللي بعدها

### Real-World Usage and Relevance in the Field (الاستخدام والملاءمة في المجال)

Every app you use - a banking app, a game, a search engine - sits on the same foundations: data representation, algorithms and layers of software.

**Egyptian Arabic (اللهجة المصرية):**

كل تطبيق بتستخدمه - تطبيق بنك، لعبة، محرّك بحث - قاعد على نفس الأساسات: تمثيل البيانات والخوارزميات وطبقات البرمجيات.

### Advantages (المميزات)

- Gives a shared vocabulary for all computing courses
- Explains the 'why' behind hardware and software
- Builds the mental model for problem solving
- Connects theory to everyday technology

**Egyptian Arabic (اللهجة المصرية):**

- بتدي مفردات مشتركة لكل مقررات الحاسب
- بتفسّر 'ليه' ورا العتاد والبرمجيات
- بتبني النموذج الذهني لحل المشكلات
- بتربط النظرية بالتكنولوجيا اليومية

### Limitations (الحدود)

- It is breadth-first, so no single topic goes deep
- Hardware details change quickly
- Needs hands-on practice to stick

**Egyptian Arabic (اللهجة المصرية):**

- بتغطي عرضيًا، فمفيش موضوع بيتعمّق
- تفاصيل العتاد بتتغير بسرعة
- محتاجة تمرين عملي عشان تثبت

### Best Practices (أحسن الممارسات)

- Connect each topic to a real device or app
- Practise representing numbers in binary and hex
- Draw the layers of a computer from hardware to application
- Keep a glossary of new terms

**Egyptian Arabic (اللهجة المصرية):**

- اربط كل موضوع بجهاز أو تطبيق حقيقي
- اتمرّن على تمثيل الأعداد بالثنائي والست عشري
- ارسم طبقات الحاسب من العتاد للتطبيق
- خلي عندك قاموس للمصطلحات الجديدة

### Common Mistakes (الأخطاء الشائعة)

- Memorizing terms without understanding the layers
- Ignoring binary and data representation
- Treating CS as only programming

**Egyptian Arabic (اللهجة المصرية):**

- حفظ المصطلحات من غير فهم الطبقات
- تجاهل الثنائي وتمثيل البيانات
- اعتبار علوم الحاسب مجرد برمجة

### Practical Example (مثال عملي)

A photo is stored as millions of pixels; each pixel's colour is a number, and each number is a pattern of bits - that is data representation in action.

**Egyptian Arabic (اللهجة المصرية):**

الصورة بتتخزن ملايين بكسلات؛ لون كل بكسل رقم، وكل رقم نمط من البتات - ده تمثيل البيانات بيحصل قدامك.

### Hands-On Exercise (تمرين عملي بإيدك)

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Programming Languages and Compilers, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في لغات البرمجة والمترجمات، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Programming Languages and Compilers in one sentence of your own words.
2. Give two situations where Programming Languages and Compilers changes a technical decision.
3. Name one limitation of Programming Languages and Compilers and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف لغات البرمجة والمترجمات في جملة واحدة بكلامك.
2. ادي موقفين لغات البرمجة والمترجمات بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود لغات البرمجة والمترجمات واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Programming Languages and Compilers? (a) a formality with no use (b) a working tool inside Computer Science Foundations (c) an unrelated subject.
Q2. True or false: Programming Languages and Compilers has no limitations.
Q3. In one line, why does Programming Languages and Compilers matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـلغات البرمجة والمترجمات؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه أساسيات علوم الحاسب (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: لغات البرمجة والمترجمات مالوش حدود.
س3. في سطر واحد، ليه لغات البرمجة والمترجمات مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Computer Science Foundations.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه أساسيات علوم الحاسب.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Programming Languages and Compilers to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها لغات البرمجة والمترجمات على برنامج أو نظام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Programming Languages and Compilers until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف لغات البرمجة والمترجمات تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الثاني: مقدمة في البرمجة (CS112)

## Functions and Modular Design (الدوال والتصميم المعياري)

Functions and Modular Design (الدوال والتصميم المعياري)
English Definition: Functions and Modular Design is a core topic in Programming. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: الدوال والتصميم المعياري موضوع أساسي في البرمجة. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Functions and Modular Design** is the focus of this lesson. Programming is the craft of turning a problem into precise instructions a computer can execute, using variables, control flow, functions and data types.

**Egyptian Arabic (اللهجة المصرية):**

**الدوال والتصميم المعياري** هو محور الدرس ده. البرمجة هي مهارة تحويل المشكلة لتعليمات دقيقة الحاسب يقدر ينفّذها، باستخدام المتغيرات والتحكم في السير والدوال وأنواع البيانات.

### Why It Exists (ليه موجود)

Code is how every idea in computing becomes real; without programming, algorithms and designs stay on paper. Without a clear grasp of Functions and Modular Design, the rest of Programming has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

الكود هو الطريقة اللي أي فكرة في الحوسبة بتبقى حقيقية بيها؛ من غير برمجة، الخوارزميات والتصميمات تفضل على الورق. ومن غير إدراك واضح لموضوع الدوال والتصميم المعياري، باقي البرمجة ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Functions and Modular Design is where the theory of Programming meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع الدوال والتصميم المعياري هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

### Where It Is Used (بنستخدمه فين)

- Writing applications and scripts
- Implementing algorithms and data structures
- Automating tasks
- Building web, mobile and AI systems
- Testing and debugging software

**Egyptian Arabic (اللهجة المصرية):**

- كتابة التطبيقات والسكربتات
- تنفيذ الخوارزميات وهياكل البيانات
- أتمتة المهام
- بناء أنظمة الويب والموبايل والذكاء الاصطناعي
- اختبار البرمجيات وتنقيحها

### Real-World Usage and Relevance in the Field (الاستخدام والملاءمة في المجال)

From a calculator app to a self-driving car's perception code, everything is built from the same building blocks: variables, loops, functions and data.

**Egyptian Arabic (اللهجة المصرية):**

من تطبيق الآلة الحاسبة لكود إدراك العربية ذاتية القيادة، كل حاجة مبنية من نفس المكوّنات: المتغيرات والحلقات والدوال والبيانات.

### Advantages (المميزات)

- Turns ideas into working software
- Scales from small scripts to huge systems
- Develops logical and structured thinking
- Skills transfer across languages

**Egyptian Arabic (اللهجة المصرية):**

- بتحوّل الأفكار لبرمجيات شغّالة
- بتتوسّع من سكربتات صغيرة لأنظمة ضخمة
- بتطوّر التفكير المنطقي والمنظّم
- المهارة بتنتقل بين اللغات

### Limitations (الحدود)

- Bad code is hard to maintain and debug
- Performance depends on design choices
- Language syntax must be learned precisely
- Bugs can be subtle and costly

**Egyptian Arabic (اللهجة المصرية):**

- الكود الوحش صعب صيانته وتنقيحه
- الأداء بيعتمد على قرارات التصميم
- لازم تتعلم صياغة اللغة بدقة
- الأخطاء ممكن تبقى خفية ومكلفة

### Best Practices (أحسن الممارسات)

- Break the problem into small functions
- Name variables clearly
- Test each part as you build it
- Use version control from day one
- Read code more than you write it

**Egyptian Arabic (اللهجة المصرية):**

- قسّم المشكلة لدوال صغيرة
- سمّي المتغيرات بوضوح
- اختبر كل جزء وإنت بتبني
- استخدم التحكم في الإصدارات من أول يوم
- اقرا كود أكتر ما بتكتب

### Common Mistakes (الأخطاء الشائعة)

- Ignoring edge cases and invalid input
- Copy-pasting code without understanding it
- Not testing boundary values
- Global variables everywhere

**Egyptian Arabic (اللهجة المصرية):**

- تجاهل الحالات الحدّية والمدخلات الغلط
- نسخ ولصق الكود من غير فهمه
- عدم اختبار القيم الحدّية
- استخدام متغيرات عامة في كل حاجة

### Practical Example (مثال عملي)

To average ten exam marks, you store them in an array, loop to sum them, then divide by ten - a small program that shows variables, loops and functions together.

**Egyptian Arabic (اللهجة المصرية):**

عشان تطلع متوسط عشر درجات، تخزّنهم في مصفوفة، وتلف عليهم تجمع، وبعدين تقسم على عشرة - برنامج صغير بيوضّح المتغيرات والحلقات والدوال مع بعض.

### Hands-On Exercise (تمرين عملي بإيدك)

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Functions and Modular Design, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في الدوال والتصميم المعياري، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Functions and Modular Design in one sentence of your own words.
2. Give two situations where Functions and Modular Design changes a technical decision.
3. Name one limitation of Functions and Modular Design and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف الدوال والتصميم المعياري في جملة واحدة بكلامك.
2. ادي موقفين الدوال والتصميم المعياري بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود الدوال والتصميم المعياري واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Functions and Modular Design? (a) a formality with no use (b) a working tool inside Programming (c) an unrelated subject.
Q2. True or false: Functions and Modular Design has no limitations.
Q3. In one line, why does Functions and Modular Design matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـالدوال والتصميم المعياري؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه البرمجة (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: الدوال والتصميم المعياري مالوش حدود.
س3. في سطر واحد، ليه الدوال والتصميم المعياري مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Programming.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه البرمجة.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Functions and Modular Design to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها الدوال والتصميم المعياري على برنامج أو نظام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Functions and Modular Design until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف الدوال والتصميم المعياري تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الثالث: التفاضل والتكامل 1 (MATH101)

## The Definite and Indefinite Integral (التكامل المحدود وغير المحدود)

The Definite and Indefinite Integral (التكامل المحدود وغير المحدود)
English Definition: The Definite and Indefinite Integral is a core topic in Calculus. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: التكامل المحدود وغير المحدود موضوع أساسي في التفاضل والتكامل. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**The Definite and Indefinite Integral** is the focus of this lesson. Calculus studies change: limits, derivatives, integrals and series, and it provides the mathematics behind optimization and continuous models.

**Egyptian Arabic (اللهجة المصرية):**

**التكامل المحدود وغير المحدود** هو محور الدرس ده. التفاضل والتكامل بيدرس التغيّر: النهايات والمشتقات والتكاملات والمتسلسلات، وبيوفّر الرياضيات ورا التحسين والنماذج المتصلة.

### Why It Exists (ليه موجود)

Machine learning, graphics and numerical methods all rest on derivatives and integrals. Without a clear grasp of The Definite and Indefinite Integral, the rest of Calculus has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

تعلّم الآلة والرسوم بالحاسب والأساليب العددية كلها قايمة على المشتقات والتكاملات. ومن غير إدراك واضح لموضوع التكامل المحدود وغير المحدود، باقي التفاضل والتكامل ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, The Definite and Indefinite Integral is where the theory of Calculus meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع التكامل المحدود وغير المحدود هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

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

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in The Definite and Indefinite Integral, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في التكامل المحدود وغير المحدود، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define The Definite and Indefinite Integral in one sentence of your own words.
2. Give two situations where The Definite and Indefinite Integral changes a technical decision.
3. Name one limitation of The Definite and Indefinite Integral and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف التكامل المحدود وغير المحدود في جملة واحدة بكلامك.
2. ادي موقفين التكامل المحدود وغير المحدود بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود التكامل المحدود وغير المحدود واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes The Definite and Indefinite Integral? (a) a formality with no use (b) a working tool inside Calculus (c) an unrelated subject.
Q2. True or false: The Definite and Indefinite Integral has no limitations.
Q3. In one line, why does The Definite and Indefinite Integral matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـالتكامل المحدود وغير المحدود؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه التفاضل والتكامل (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: التكامل المحدود وغير المحدود مالوش حدود.
س3. في سطر واحد، ليه التكامل المحدود وغير المحدود مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Calculus.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه التفاضل والتكامل.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying The Definite and Indefinite Integral to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها التكامل المحدود وغير المحدود على برنامج أو نظام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of The Definite and Indefinite Integral until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف التكامل المحدود وغير المحدود تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الرابع: الرياضيات المتقطعة (MATH102)

## Permutations and Combinations (التباديل والتوافيق)

Permutations and Combinations (التباديل والتوافيق)
English Definition: Permutations and Combinations is a core topic in Discrete Mathematics. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: التباديل والتوافيق موضوع أساسي في الرياضيات المتقطعة. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Permutations and Combinations** is the focus of this lesson. Discrete mathematics studies countable structures: logic, sets, relations, counting, graphs and Boolean algebra - the mathematics of computer science.

**Egyptian Arabic (اللهجة المصرية):**

**التباديل والتوافيق** هو محور الدرس ده. الرياضيات المتقطعة بتدرس البنى القابلة للعد: المنطق والمجموعات والعلاقات والعد والرسوم والجبر البولياني - رياضيات علوم الحاسب.

### Why It Exists (ليه موجود)

Computers work on discrete states, and correctness proofs, complexity and databases all use discrete mathematics. Without a clear grasp of Permutations and Combinations, the rest of Discrete Mathematics has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

الحاسبات بتشتغل على حالات متقطعة، وبراهين الصحة والتعقيد وقواعد البيانات كلها بتستخدم الرياضيات المتقطعة. ومن غير إدراك واضح لموضوع التباديل والتوافيق، باقي الرياضيات المتقطعة ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Permutations and Combinations is where the theory of Discrete Mathematics meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع التباديل والتوافيق هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

### Where It Is Used (بنستخدمه فين)

- Algorithm correctness and proofs
- Boolean logic and digital circuits
- Graph and network modelling
- Counting and probability
- Automata and formal languages

**Egyptian Arabic (اللهجة المصرية):**

- صحة الخوارزميات والبراهين
- المنطق البولياني والدوائر الرقمية
- نمذجة الرسوم والشبكات
- العد والاحتمالات
- الآلات المجرّدة واللغات الصورية

### Real-World Usage and Relevance in the Field (الاستخدام والملاءمة في المجال)

Every if-statement in code is propositional logic, and every relational database schema is built on set theory and relations.

**Egyptian Arabic (اللهجة المصرية):**

كل جملة if في الكود هي منطق قضايا، وكل مخطط قاعدة بيانات علائقية مبني على نظرية المجموعات والعلاقات.

### Advantages (المميزات)

- Builds rigorous proof skills
- Underpins logic, graphs and databases
- Essential for algorithms and automata
- Trains precise thinking

**Egyptian Arabic (اللهجة المصرية):**

- بتبني مهارات البرهان الصارم
- بتدعم المنطق والرسوم وقواعد البيانات
- أساسية للخوارزميات والآلات المجرّدة
- بتدرّب التفكير الدقيق

### Limitations (الحدود)

- Abstract and proof-heavy for beginners
- Requires comfort with notation
- Some results feel disconnected from code at first

**Egyptian Arabic (اللهجة المصرية):**

- مجردة ومليانة براهين للمبتدئين
- محتاجة راحة مع الترميز الرياضي
- بعض النتائج بتبان منفصلة عن الكود في الأول

### Best Practices (أحسن الممارسات)

- Practise proofs by induction and contradiction
- Translate logic statements into truth tables
- Draw graphs for every relation problem
- Connect counting to probability

**Egyptian Arabic (اللهجة المصرية):**

- اتمرّن على البرهان بالاستقراء والتناقض
- حوّل الجمل المنطقية لجداول الحقيقة
- ارسم رسوم لكل مسألة علاقات
- اربط العد بالاحتمالات

### Common Mistakes (الأخطاء الشائعة)

- Confusing necessary and sufficient conditions
- Mixing up permutations and combinations
- Forgetting the base case in induction
- Treating relations as functions

**Egyptian Arabic (اللهجة المصرية):**

- الخلط بين الشرط اللازم والكافي
- الخلط بين التباديل والتوافيق
- نسيان حالة الأساس في الاستقراء
- التعامل مع العلاقات كدوال

### Practical Example (مثال عملي)

To prove a loop is correct, you show it holds before the loop, keeps holding each iteration, and implies the goal when it ends - induction on code.

**Egyptian Arabic (اللهجة المصرية):**

عشان تثبت إن حلقة صحيحة، بتوضّح إنها صح قبلها، وتفضل صح كل لفة، وتوصّل للهدف لما تخلص - استقراء على الكود.

### Hands-On Exercise (تمرين عملي بإيدك)

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Permutations and Combinations, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في التباديل والتوافيق، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Permutations and Combinations in one sentence of your own words.
2. Give two situations where Permutations and Combinations changes a technical decision.
3. Name one limitation of Permutations and Combinations and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف التباديل والتوافيق في جملة واحدة بكلامك.
2. ادي موقفين التباديل والتوافيق بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود التباديل والتوافيق واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Permutations and Combinations? (a) a formality with no use (b) a working tool inside Discrete Mathematics (c) an unrelated subject.
Q2. True or false: Permutations and Combinations has no limitations.
Q3. In one line, why does Permutations and Combinations matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـالتباديل والتوافيق؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه الرياضيات المتقطعة (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: التباديل والتوافيق مالوش حدود.
س3. في سطر واحد، ليه التباديل والتوافيق مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Discrete Mathematics.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه الرياضيات المتقطعة.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Permutations and Combinations to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها التباديل والتوافيق على برنامج أو نظام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Permutations and Combinations until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف التباديل والتوافيق تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الخامس: الفيزياء 1 (PHYS101)

## Momentum and Collisions (الزخم والتصادمات)

Momentum and Collisions (الزخم والتصادمات)
English Definition: Momentum and Collisions is a core topic in Physics. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: الزخم والتصادمات موضوع أساسي في الفيزياء. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Momentum and Collisions** is the focus of this lesson. Physics describes matter, energy and their interactions, and explains the physical principles that make computing hardware possible.

**Egyptian Arabic (اللهجة المصرية):**

**الزخم والتصادمات** هو محور الدرس ده. الفيزياء بتوصف المادة والطاقة وتفاعلاتهما، وبتفسّر المبادئ الفيزيائية اللي بتخلي عتاد الحاسب ممكنًا.

### Why It Exists (ليه موجود)

Semiconductors, circuits, displays and storage all rest on physical laws you meet in first-year physics. Without a clear grasp of Momentum and Collisions, the rest of Physics has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

أشباه الموصلات والدوائر والشاشات والتخزين كلها قايمة على قوانين فيزيائية بتقابلها في فيزياء السنة الأولى. ومن غير إدراك واضح لموضوع الزخم والتصادمات، باقي الفيزياء ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Momentum and Collisions is where the theory of Physics meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع الزخم والتصادمات هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

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

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Momentum and Collisions, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في الزخم والتصادمات، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Momentum and Collisions in one sentence of your own words.
2. Give two situations where Momentum and Collisions changes a technical decision.
3. Name one limitation of Momentum and Collisions and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف الزخم والتصادمات في جملة واحدة بكلامك.
2. ادي موقفين الزخم والتصادمات بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود الزخم والتصادمات واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Momentum and Collisions? (a) a formality with no use (b) a working tool inside Physics (c) an unrelated subject.
Q2. True or false: Momentum and Collisions has no limitations.
Q3. In one line, why does Momentum and Collisions matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـالزخم والتصادمات؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه الفيزياء (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: الزخم والتصادمات مالوش حدود.
س3. في سطر واحد، ليه الزخم والتصادمات مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Physics.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه الفيزياء.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Momentum and Collisions to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها الزخم والتصادمات على برنامج أو نظام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Momentum and Collisions until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف الزخم والتصادمات تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم السادس: اللغة الإنجليزية 1 (ENG101)

## Writing Paragraphs and Topic Sentences (كتابة الفقرات والجمل الافتتاحية)

Writing Paragraphs and Topic Sentences (كتابة الفقرات والجمل الافتتاحية)
English Definition: Writing Paragraphs and Topic Sentences is a core topic in English and Technical Communication. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: كتابة الفقرات والجمل الافتتاحية موضوع أساسي في الإنجليزية والتواصل الفني. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Writing Paragraphs and Topic Sentences** is the focus of this lesson. English and technical communication cover reading, writing and presenting technical material clearly for academic and professional audiences.

**Egyptian Arabic (اللهجة المصرية):**

**كتابة الفقرات والجمل الافتتاحية** هو محور الدرس ده. الإنجليزية والتواصل الفني بيغطوا القراءة والكتابة وعرض المواد الفنية بوضوح للجمهور الأكاديمي والمهني.

### Why It Exists (ليه موجود)

Computing is global: documentation, research papers, specs and interviews are all in English. Without a clear grasp of Writing Paragraphs and Topic Sentences, the rest of English and Technical Communication has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

الحوسبة عالمية: التوثيق والأوراق البحثية والمواصفات والمقابلات كلها بالإنجليزي. ومن غير إدراك واضح لموضوع كتابة الفقرات والجمل الافتتاحية، باقي الإنجليزية والتواصل الفني ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Writing Paragraphs and Topic Sentences is where the theory of English and Technical Communication meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع كتابة الفقرات والجمل الافتتاحية هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

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

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Writing Paragraphs and Topic Sentences, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في كتابة الفقرات والجمل الافتتاحية، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Writing Paragraphs and Topic Sentences in one sentence of your own words.
2. Give two situations where Writing Paragraphs and Topic Sentences changes a technical decision.
3. Name one limitation of Writing Paragraphs and Topic Sentences and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف كتابة الفقرات والجمل الافتتاحية في جملة واحدة بكلامك.
2. ادي موقفين كتابة الفقرات والجمل الافتتاحية بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود كتابة الفقرات والجمل الافتتاحية واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Writing Paragraphs and Topic Sentences? (a) a formality with no use (b) a working tool inside English and Technical Communication (c) an unrelated subject.
Q2. True or false: Writing Paragraphs and Topic Sentences has no limitations.
Q3. In one line, why does Writing Paragraphs and Topic Sentences matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـكتابة الفقرات والجمل الافتتاحية؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه الإنجليزية والتواصل الفني (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: كتابة الفقرات والجمل الافتتاحية مالوش حدود.
س3. في سطر واحد، ليه كتابة الفقرات والجمل الافتتاحية مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside English and Technical Communication.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه الإنجليزية والتواصل الفني.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Writing Paragraphs and Topic Sentences to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها كتابة الفقرات والجمل الافتتاحية على برنامج أو نظام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Writing Paragraphs and Topic Sentences until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف كتابة الفقرات والجمل الافتتاحية تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

## Learning Resources (المصادر الدراسية)

### CS111 — أساسيات علوم الحاسب

**Primary Resource (المصدر الأساسي)**

- **Resource Name:** Computer Science: An Overview (Brookshear & Brylow)
- **Resource Type:** Textbook
- **Direct Link:** https://www.pearson.com/en-us/subject-catalog/p/computer-science-an-overview/P200000003500
- **Difficulty:** Beginner
- **Estimated Time:** 25 hours

- **Why Recommended:** The standard breadth-first introduction used in many CS programs worldwide.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: المقدمة العرضية المعيارية المستخدمة في برامج حاسب كتير حول العالم.

- **What to Study From It:** Data representation, hardware, software, networks and the limits of computation.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: تمثيل البيانات والعتاد والبرمجيات والشبكات وحدود الحسابات.

**Optional Resource (المصدر الاختياري)**

- **Resource Name:** CS50x: Introduction to Computer Science (Harvard)
- **Resource Type:** Online Course
- **Direct Link:** https://cs50.harvard.edu/x/
- **Difficulty:** Beginner
- **Estimated Time:** 40 hours

- **Why Recommended:** A famous free course that makes the foundations concrete with real programs.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: كورس مجاني مشهور بيخلي الأساسات ملموسة ببرامج حقيقية.

- **What to Study From It:** Abstraction, algorithms, data structures and how computers execute code.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: التجريد والخوارزميات وهياكل البيانات وإزاي الحاسب ينفّذ الكود.

**Practice Platform (منصة التمرين العملي)**

- **Resource Name:** GeeksforGeeks - CS Fundamentals
- **Resource Type:** Practice Platform
- **Direct Link:** https://www.geeksforgeeks.org/computer-science-projects/
- **Difficulty:** Beginner
- **Estimated Time:** 15 hours

- **Why Recommended:** Short articles and quizzes you can use to check each concept quickly.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: مقالات قصيرة واختبارات تقدر تتأكد بيها من كل مفهوم بسرعة.

- **What to Study From It:** Number systems, hardware basics and computing terminology.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: أنظمة الأعداد وأساسيات العتاد ومصطلحات الحوسبة.

### CS112 — مقدمة في البرمجة

**Primary Resource (المصدر الأساسي)**

- **Resource Name:** Python Official Documentation
- **Resource Type:** Official Documentation
- **Direct Link:** https://docs.python.org/3/tutorial/
- **Difficulty:** Beginner
- **Estimated Time:** 20 hours

- **Why Recommended:** The official tutorial is accurate, free and the reference for the language.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: الدرس الرسمي دقيق ومجاني وهو المرجع للغة.

- **What to Study From It:** Data types, control flow, functions, data structures and modules.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: أنواع البيانات والتحكم في السير والدوال وهياكل البيانات والوحدات.

**Optional Resource (المصدر الاختياري)**

- **Resource Name:** CS50P: Introduction to Programming with Python
- **Resource Type:** Online Course
- **Direct Link:** https://cs50.harvard.edu/python/
- **Difficulty:** Beginner
- **Estimated Time:** 35 hours

- **Why Recommended:** A project-based course that teaches clean programming habits early.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: كورس قائم على المشروعات بيعلّم عادات برمجة نظيفة من بدري.

- **What to Study From It:** Functions, conditionals, loops, exceptions, files and object-oriented basics.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: الدوال والشروط والحلقات والاستثناءات والملفات وأساسيات الكائنية.

**Practice Platform (منصة التمرين العملي)**

- **Resource Name:** LeetCode
- **Resource Type:** Practice Platform
- **Direct Link:** https://leetcode.com/
- **Difficulty:** Beginner to Intermediate
- **Estimated Time:** 30 hours

- **Why Recommended:** Hundreds of graded problems with an online judge that checks your solution instantly.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: مئات المسائل المتدرّجة مع حكم إلكتروني بيتأكد من حلك فورًا.

- **What to Study From It:** The 'Easy' problem set on arrays, strings and loops.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: مجموعة المسائل السهلة في المصفوفات والنصوص والحلقات.

### MATH101 — التفاضل والتكامل 1

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

### MATH102 — الرياضيات المتقطعة

**Primary Resource (المصدر الأساسي)**

- **Resource Name:** Discrete Mathematics and Its Applications (Rosen)
- **Resource Type:** Textbook
- **Direct Link:** https://www.mheducation.com/highered/product/discrete-mathematics-and-its-applications-rosen/M9781259676512.html
- **Difficulty:** Intermediate
- **Estimated Time:** 40 hours

- **Why Recommended:** The standard reference for discrete mathematics in CS programs.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: المرجع المعياري للرياضيات المتقطعة في برامج الحاسب.

- **What to Study From It:** Logic, proofs, sets, relations, counting, graphs and Boolean algebra.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: المنطق والبراهين والمجموعات والعلاقات والعد والرسوم والجبر البولياني.

**Optional Resource (المصدر الاختياري)**

- **Resource Name:** MIT 6.042J Mathematics for Computer Science
- **Resource Type:** University Course
- **Direct Link:** https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/
- **Difficulty:** Intermediate
- **Estimated Time:** 35 hours

- **Why Recommended:** A rigorous free course built specifically for computer science students.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: كورس مجاني صارم مصمّم خصيصًا لطلبة علوم الحاسب.

- **What to Study From It:** Proofs, graphs, number theory, counting and probability.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: البراهين والرسوم ونظرية الأعداد والعد والاحتمالات.

**Practice Platform (منصة التمرين العملي)**

- **Resource Name:** Brilliant - Discrete Mathematics
- **Resource Type:** Practice Platform
- **Direct Link:** https://brilliant.org/courses/logic-deduction/
- **Difficulty:** Beginner
- **Estimated Time:** 20 hours

- **Why Recommended:** Interactive puzzles that make logic and proof intuitive.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: ألغاز تفاعلية بتخلي المنطق والبرهان بديهيين.

- **What to Study From It:** Logic, sets, counting and graph puzzles.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: ألغاز المنطق والمجموعات والعد والرسوم.

### PHYS101 — الفيزياء 1

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

### ENG101 — اللغة الإنجليزية 1

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

This week covered the following topics across the semester's courses: CS111: Programming Languages and Compilers; CS112: Functions and Modular Design; MATH101: The Definite and Indefinite Integral; MATH102: Permutations and Combinations; PHYS101: Momentum and Collisions; ENG101: Writing Paragraphs and Topic Sentences. Each topic opened with a bilingual definition, then explained what it is, why it exists, why it matters, where it is used, its advantages and limits, best practices and common mistakes, followed by a practical example and exercises.

**Egyptian Arabic (اللهجة المصرية):**

الأسبوع ده غطّى المواضيع دي في مقررات الفصل: CS111: لغات البرمجة والمترجمات؛ CS112: الدوال والتصميم المعياري؛ MATH101: التكامل المحدود وغير المحدود؛ MATH102: التباديل والتوافيق؛ PHYS101: الزخم والتصادمات؛ ENG101: كتابة الفقرات والجمل الافتتاحية. كل موضوع بدأ بتعريف ثنائي اللغة، وبعدين شرح يعني إيه وليه موجود وليه مهم وبنستخدمه فين، ومميزاته وحدوده وأحسن الممارسات والأخطاء الشائعة، وبعدين مثال عملي وتمارين.

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

Next week continues with: CS111: Computer Networks and the Internet; CS112: Arrays and Strings; MATH101: Techniques of Integration; MATH102: Recurrence Relations; PHYS101: Rotational Motion; ENG101: Summarizing and Paraphrasing.

**Egyptian Arabic (اللهجة المصرية):**

الأسبوع الجاي بيكمل بـ: CS111: شبكات الحاسب والإنترنت؛ CS112: المصفوفات والنصوص؛ MATH101: أساليب التكامل؛ MATH102: علاقات الاستدعاء الذاتي؛ PHYS101: الحركة الدورانية؛ ENG101: التلخيص وإعادة الصياغة.

### Important Terms (مصطلحات مهمة)

#### Bit (بت)
English Definition: The smallest unit of data, either 0 or 1.
Egyptian Arabic Definition: أصغر وحدة بيانات، إما 0 أو 1.

#### Byte (بايت)
English Definition: A group of eight bits, enough to store one character.
Egyptian Arabic Definition: مجموعة من ثمانية بتات، كافية لتخزين حرف واحد.

#### Algorithm (خوارزمية)
English Definition: A finite sequence of steps that solves a problem.
Egyptian Arabic Definition: سلسلة خطوات منتهية بتحل مشكلة.

#### Compiler (مترجم)
English Definition: A program that translates source code into machine code.
Egyptian Arabic Definition: برنامج بيترجم الكود المصدري لكود الآلة.

#### Abstraction (التجريد)
English Definition: Hiding detail behind a simpler interface.
Egyptian Arabic Definition: إخفاء التفاصيل ورا واجهة أبسط.


---

[الدرس السابق: week-08.md](week-08.md) · [رجوع لفصل 1](README.md) · [الدرس الجاي: week-10.md](week-10.md)