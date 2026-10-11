# الأسبوع 9 — الفصل 8

> الدرس ده بيغطّي موضوع واحد في كل مقرر من مقررات الفصل، وكل الشرح مكتوب بالعامية المصرية مع البلوك الإنجليزي الكامل جنبه.

**المقررات اللي في الدرس ده:** AI403 (التعلّم المعزّز)، CS421 (الخوارزميات المتقدمة والتعقيد)، CS422 (أخلاقيات الحوسبة والممارسة المهنية)، CS423 (مشروع التخرج 2)، ELEC-MOBILE (اختياري: تطوير تطبيقات الموبايل)، ELEC-GAME (اختياري: تطوير الألعاب)

---

# القسم الأول: التعلّم المعزّز (AI403)

## Exploration vs Exploitation and Multi-Armed Bandits (الاستكشاف مقابل الاستغلال وأذرع البانديت)

Exploration vs Exploitation and Multi-Armed Bandits (الاستكشاف مقابل الاستغلال وأذرع البانديت)
English Definition: Exploration vs Exploitation and Multi-Armed Bandits is a core topic in Reinforcement Learning. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: الاستكشاف مقابل الاستغلال وأذرع البانديت موضوع أساسي في التعلّم المعزّز. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Exploration vs Exploitation and Multi-Armed Bandits** is the focus of this lesson. Reinforcement learning trains an agent to make decisions by interacting with an environment and maximizing long-term reward.

**Egyptian Arabic (اللهجة المصرية):**

**الاستكشاف مقابل الاستغلال وأذرع البانديت** هو محور الدرس ده. التعلّم المعزّز بيدرّب وكيل يتخذ قرارات بالتفاعل مع بيئة وتعظيم المكافأة على المدى الطويل.

### Why It Exists (ليه موجود)

Many real problems - games, robotics, control - are sequential decisions, not one-shot predictions. Without a clear grasp of Exploration vs Exploitation and Multi-Armed Bandits, the rest of Reinforcement Learning has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

مشكلات حقيقية كتير - ألعاب وروبوتات وتحكم - قرارات متسلسلة مش تنبؤات لمرة واحدة. ومن غير إدراك واضح لموضوع الاستكشاف مقابل الاستغلال وأذرع البانديت، باقي التعلّم المعزّز ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Exploration vs Exploitation and Multi-Armed Bandits is where the theory of Reinforcement Learning meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع الاستكشاف مقابل الاستغلال وأذرع البانديت هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

### Where It Is Used (بنستخدمه فين)

- Game playing agents
- Robotics and control
- Resource scheduling
- Recommendation and ads
- Autonomous systems

**Egyptian Arabic (اللهجة المصرية):**

- وكلاء لعب الألعاب
- الروبوتات والتحكم
- جدولة الموارد
- التوصيات والإعلانات
- الأنظمة المستقلة

### Real-World Usage and Relevance in the Field (الاستخدام والملاءمة في المجال)

A robot learns to walk by trying actions and getting rewards for moving forward and penalties for falling.

**Egyptian Arabic (اللهجة المصرية):**

روبوت بيتعلم يمشي بتجربة أفعال وبياخد مكافأة لما يتقدم وعقاب لما يقع.

### Advantages (المميزات)

- Learns from interaction, not labels
- Optimizes long-term goals
- Handles sequential decisions
- Works in simulation then transfers

**Egyptian Arabic (اللهجة المصرية):**

- بيتعلم من التفاعل مش الوسوم
- بيحسّن أهداف طويلة الأجل
- بيتعامل مع القرارات المتسلسلة
- بيشتغل في المحاكاة وبعدين ينتقل

### Limitations (الحدود)

- Sample inefficient
- Reward design is tricky
- Unstable training
- Simulation gap

**Egyptian Arabic (اللهجة المصرية):**

- غير كفء في استخدام العينات
- تصميم المكافأة صعب
- تدريب غير مستقر
- فجوة بين المحاكاة والواقع

### Best Practices (أحسن الممارسات)

- Design rewards carefully
- Use simulation and safe exploration
- Monitor stability and tune
- Evaluate on held-out episodes

**Egyptian Arabic (اللهجة المصرية):**

- صمّم المكافآت بعناية
- استخدم المحاكاة والاستكشاف الآمن
- راقب الاستقرار واضبط
- قيّم على حلقات محتجزة

### Common Mistakes (الأخطاء الشائعة)

- Sparse rewards with no shaping
- Ignoring exploration
- Comparing agents on too few episodes
- Reward hacking

**Egyptian Arabic (اللهجة المصرية):**

- مكافآت متباعدة بلا تشكيل
- تجاهل الاستكشاف
- مقارنة الوكلاء على حلقات قليلة جدًا
- اختراق المكافأة

### Practical Example (مثال عملي)

A game agent learns to play by receiving a point for each goal and losing points for mistakes, improving policy over millions of episodes.

**Egyptian Arabic (اللهجة المصرية):**

وكيل لعبة بيتعلم يلعب بإنه ياخد نقطة لكل هدف ويخسر نقاط للأخطاء، وبيحسّن سياسته على ملايين الحلقات.

### Hands-On Exercise (تمرين عملي بإيدك)

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Exploration vs Exploitation and Multi-Armed Bandits, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نطام صغير تعرفه. اكتب: (1) الموقف في الاستكشاف مقابل الاستغلال وأذرع البانديت، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Exploration vs Exploitation and Multi-Armed Bandits in one sentence of your own words.
2. Give two situations where Exploration vs Exploitation and Multi-Armed Bandits changes a technical decision.
3. Name one limitation of Exploration vs Exploitation and Multi-Armed Bandits and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف الاستكشاف مقابل الاستغلال وأذرع البانديت في جملة واحدة بكلامك.
2. ادي موقفين الاستكشاف مقابل الاستغلال وأذرع البانديت بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود الاستكشاف مقابل الاستغلال وأذرع البانديت واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Exploration vs Exploitation and Multi-Armed Bandits? (a) a formality with no use (b) a working tool inside Reinforcement Learning (c) an unrelated subject.
Q2. True or false: Exploration vs Exploitation and Multi-Armed Bandits has no limitations.
Q3. In one line, why does Exploration vs Exploitation and Multi-Armed Bandits matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـالاستكشاف مقابل الاستغلال وأذرع البانديت؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه التعلّم المعزّز (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: الاستكشاف مقابل الاستغلال وأذرع البانديت مالوش حدود.
س3. في سطر واحد، ليه الاستكشاف مقابل الاستغلال وأذرع البانديت مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Reinforcement Learning.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه التعلّم المعزّز.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Exploration vs Exploitation and Multi-Armed Bandits to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها الاستكشاف مقابل الاستغلال وأذرع البانديت على برنامج أو نطام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Exploration vs Exploitation and Multi-Armed Bandits until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف الاستكشاف مقابل الاستغلال وأذرع البانديت تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الثاني: الخوارزميات المتقدمة والتعقيد (CS421)

## Network Flow and Matching (تدفق الشبكات والمطابقة)

Network Flow and Matching (تدفق الشبكات والمطابقة)
English Definition: Network Flow and Matching is a core topic in Advanced Algorithms and Complexity. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: تدفق الشبكات والمطابقة موضوع أساسي في الخوارزميات المتقدمة والتعقيد. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Network Flow and Matching** is the focus of this lesson. Advanced algorithms study deeper design techniques and complexity theory: randomization, approximation, linear programming and hardness.

**Egyptian Arabic (اللهجة المصرية):**

**تدفق الشبكات والمطابقة** هو محور الدرس ده. الخوارزميات المتقدمة بتدرس تقنيات تصميم أعمق ونظرية التعقيد: العشوائية والتقريب والبرمجة الخطية والصلابة.

### Why It Exists (ليه موجود)

Some problems have no fast exact solution, so you must reason about hardness and approximation. Without a clear grasp of Network Flow and Matching, the rest of Advanced Algorithms and Complexity has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

بعض المشكلات ملهاش حل دقيق سريع، فلازم تستنتج عن الصلابة والتقريب. ومن غير إدراك واضح لموضوع تدفق الشبكات والمطابقة، باقي الخوارزميات المتقدمة والتعقيد ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Network Flow and Matching is where the theory of Advanced Algorithms and Complexity meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع تدفق الشبكات والمطابقة هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

### Where It Is Used (بنستخدمه فين)

- Optimization and scheduling
- Network design
- Machine learning theory
- Cryptography
- Competitive programming

**Egyptian Arabic (اللهجة المصرية):**

- التحسين والجدولة
- تصميم الشبكات
- نظرية تعلّم الآلة
- التشفير
- البرمجة التنافسية

### Real-World Usage and Relevance in the Field (الاستخدام والملاءمة في المجال)

Delivery routing is NP-hard, so companies use approximation algorithms that are guaranteed to be within a few percent of optimal.

**Egyptian Arabic (اللهجة المصرية):**

توجيه التوصيل صلب من نوع NP، فشركات بتستخدم خوارزميات تقريبية مضمون إنها في حدود نسبة قليلة من الأمثل.

### Advantages (المميزات)

- Tackles hard problems systematically
- Quantifies solution quality
- Deepens proof skills
- Key for research

**Egyptian Arabic (اللهجة المصرية):**

- بتتعامل مع المشكلات الصعبة بشكل منهجي
- بتقيس جودة الحل
- بتعمّق مهارات البرهان
- أساسية للبحث

### Limitations (الحدود)

- Highly mathematical
- Approximations may not suffice
- Randomized results are probabilistic
- Hard to implement efficiently

**Egyptian Arabic (اللهجة المصرية):**

- رياضية جدًا
- التقريبات ممكن ما تكفيش
- النتائج العشوائية احتمالية
- صعب تنفيذها بكفاءة

### Best Practices (أحسن الممارسات)

- Identify the hardness first
- Choose the right paradigm
- Prove guarantees carefully
- Implement with attention to constants

**Egyptian Arabic (اللهجة المصرية):**

- حدّد الصلابة الأول
- اختار النمط المناسب
- أثبت الضمانات بعناية
- نفّذ مع الاهتمام بالعوامل الثابتة

### Common Mistakes (الأخطاء الشائعة)

- Assuming P equals NP
- Ignoring approximation ratios
- Misusing randomized analysis
- Underestimating implementation cost

**Egyptian Arabic (اللهجة المصرية):**

- افتراض إن P تساوي NP
- تجاهل نسب التقريب
- سوء استخدام التحليل العشوائي
- التقليل من تكلفة التنفيذ

### Practical Example (مثال عملي)

Vertex cover is NP-hard; a simple 2-approximation picks both endpoints of any uncovered edge and guarantees at most twice the optimum.

**Egyptian Arabic (اللهجة المصرية):**

تغطية الرؤوس صلبة؛ تقريب ثنائي بسيط بياخد طرفي أي ضلع غير مغطى وبيضمن على الأكثر ضعف الأمثل.

### Hands-On Exercise (تمرين عملي بإيدك)

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Network Flow and Matching, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نطام صغير تعرفه. اكتب: (1) الموقف في تدفق الشبكات والمطابقة، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Network Flow and Matching in one sentence of your own words.
2. Give two situations where Network Flow and Matching changes a technical decision.
3. Name one limitation of Network Flow and Matching and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف تدفق الشبكات والمطابقة في جملة واحدة بكلامك.
2. ادي موقفين تدفق الشبكات والمطابقة بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود تدفق الشبكات والمطابقة واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Network Flow and Matching? (a) a formality with no use (b) a working tool inside Advanced Algorithms and Complexity (c) an unrelated subject.
Q2. True or false: Network Flow and Matching has no limitations.
Q3. In one line, why does Network Flow and Matching matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـتدفق الشبكات والمطابقة؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه الخوارزميات المتقدمة والتعقيد (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: تدفق الشبكات والمطابقة مالوش حدود.
س3. في سطر واحد، ليه تدفق الشبكات والمطابقة مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Advanced Algorithms and Complexity.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه الخوارزميات المتقدمة والتعقيد.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Network Flow and Matching to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها تدفق الشبكات والمطابقة على برنامج أو نطام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Network Flow and Matching until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف تدفق الشبكات والمطابقة تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الثالث: أخلاقيات الحوسبة والممارسة المهنية (CS422)

## Responsible AI and Autonomy (الذكاء الاصطناعي المسؤول والاستقلالية)

Responsible AI and Autonomy (الذكاء الاصطناعي المسؤول والاستقلالية)
English Definition: Responsible AI and Autonomy is a core topic in Computing Ethics and Professional Practice. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: الذكاء الاصطناعي المسؤول والاستقلالية موضوع أساسي في أخلاقيات الحوسبة والممارسة المهنية. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Responsible AI and Autonomy** is the focus of this lesson. Computing ethics examines the social, legal and professional responsibilities of those who build and deploy technology.

**Egyptian Arabic (اللهجة المصرية):**

**الذكاء الاصطناعي المسؤول والاستقلالية** هو محور الدرس ده. أخلاقيات الحوسبة بتفحص المسؤوليات الاجتماعية والقانونية والمهنية لمن يبنون وينشرون التكنولوجيا.

### Why It Exists (ليه موجود)

Technology shapes society, and engineers must reason about privacy, fairness, safety and misuse. Without a clear grasp of Responsible AI and Autonomy, the rest of Computing Ethics and Professional Practice has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

التكنولوجيا بتشكّل المجتمع، والمهندسين لازم يستنتجوا عن الخصوصية والعدالة والسلامة وإساءة الاستخدام. ومن غير إدراك واضح لموضوع الذكاء الاصطناعي المسؤول والاستقلالية، باقي أخلاقيات الحوسبة والممارسة المهنية ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Responsible AI and Autonomy is where the theory of Computing Ethics and Professional Practice meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع الذكاء الاصطناعي المسؤول والاستقلالية هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

### Where It Is Used (بنستخدمه فين)

- Privacy and data protection
- AI fairness and accountability
- Security disclosure
- Professional conduct
- Policy and regulation

**Egyptian Arabic (اللهجة المصرية):**

- الخصوصية وحماية البيانات
- عدالة الذكاء الاصطناعي والمساءلة
- الإفصاح عن الثغرات
- السلوك المهني
- السياسات والتنظيم

### Real-World Usage and Relevance in the Field (الاستخدام والملاءمة في المجال)

A company deciding to deploy a facial-recognition system must weigh accuracy against privacy, bias and legal limits.

**Egyptian Arabic (اللهجة المصرية):**

شركة بتقرر تنشر نظام تعرّف على الوجوه لازم توازن بين الدقة والخصوصية والتحيّز والحدود القانونية.

### Advantages (المميزات)

- Guides responsible decisions
- Protects users and society
- Builds professional trust
- Aligns with legal duties

**Egyptian Arabic (اللهجة المصرية):**

- بتوجّه القرارات المسؤولة
- بتحمي المستخدمين والمجتمع
- بتبني الثقة المهنية
- بتتوافق مع الواجبات القانونية

### Limitations (الحدود)

- Ethical dilemmas rarely have clean answers
- Laws lag behind technology
- Cultural differences matter
- Pressure to ship can override caution

**Egyptian Arabic (اللهجة المصرية):**

- المعضلات الأخلاقية نادرًا ليها إجابات نظيفة
- القوانين متأخرة عن التكنولوجيا
- الاختلافات الثقافية بتفرق
- ضغط الإطلاق ممكن يتغلّب على الحذر

### Best Practices (أحسن الممارسات)

- Follow professional codes
- Assess impact before deployment
- Be transparent about limitations
- Protect user data by default

**Egyptian Arabic (اللهجة المصرية):**

- اتبع المواثيق المهنية
- قيّم الأثر قبل النشر
- كن شفافًا بخصوص القيود
- احمي بيانات المستخدم افتراضيًا

### Common Mistakes (الأخطاء الشائعة)

- Treating ethics as optional
- Ignoring bias in models
- Collecting more data than needed
- Hiding known harms

**Egyptian Arabic (اللهجة المصرية):**

- التعامل مع الأخلاقيات كإنها اختيارية
- تجاهل التحيّز في النماذج
- جمع بيانات أكتر من اللازم
- إخفاء الأضرار المعروفة

### Practical Example (مثال عملي)

Before launching a hiring algorithm, a team audits it for gender bias and documents how candidates can appeal decisions.

**Egyptian Arabic (اللهجة المصرية):**

قبل إطلاق خوارزمية توظيف، الفريق بيراجعها للتحيّز الجندري وبيوثّق إزاي المرشحين يقدروا يعترضوا على القرارات.

### Hands-On Exercise (تمرين عملي بإيدك)

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Responsible AI and Autonomy, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نطام صغير تعرفه. اكتب: (1) الموقف في الذكاء الاصطناعي المسؤول والاستقلالية، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Responsible AI and Autonomy in one sentence of your own words.
2. Give two situations where Responsible AI and Autonomy changes a technical decision.
3. Name one limitation of Responsible AI and Autonomy and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف الذكاء الاصطناعي المسؤول والاستقلالية في جملة واحدة بكلامك.
2. ادي موقفين الذكاء الاصطناعي المسؤول والاستقلالية بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود الذكاء الاصطناعي المسؤول والاستقلالية واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Responsible AI and Autonomy? (a) a formality with no use (b) a working tool inside Computing Ethics and Professional Practice (c) an unrelated subject.
Q2. True or false: Responsible AI and Autonomy has no limitations.
Q3. In one line, why does Responsible AI and Autonomy matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـالذكاء الاصطناعي المسؤول والاستقلالية؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه أخلاقيات الحوسبة والممارسة المهنية (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: الذكاء الاصطناعي المسؤول والاستقلالية مالوش حدود.
س3. في سطر واحد، ليه الذكاء الاصطناعي المسؤول والاستقلالية مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Computing Ethics and Professional Practice.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه أخلاقيات الحوسبة والممارسة المهنية.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Responsible AI and Autonomy to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها الذكاء الاصطناعي المسؤول والاستقلالية على برنامج أو نطام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Responsible AI and Autonomy until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف الذكاء الاصطناعي المسؤول والاستقلالية تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الرابع: مشروع التخرج 2 (CS423)

## Deployment and Release (النشر والإصدار)

Deployment and Release (النشر والإصدار)
English Definition: Deployment and Release is a core topic in Graduation Project. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: النشر والإصدار موضوع أساسي في مشروع التخرج. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Deployment and Release** is the focus of this lesson. The graduation project is a year-long capstone where you take a real problem from idea to a working, tested and documented system.

**Egyptian Arabic (اللهجة المصرية):**

**النشر والإصدار** هو محور الدرس ده. مشروع التخرج هو مشروع السنة الأخيرة اللي بتاخد فيه مشكلة حقيقية من الفكرة لنظام شغّال ومختبر وموثّق.

### Why It Exists (ليه موجود)

It integrates everything you learned and produces a portfolio piece employers and graduate schools value. Without a clear grasp of Deployment and Release, the rest of Graduation Project has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

بيدمج كل اللي اتعلمته وبيطلع قطعة في ملف أعمالك بتقيّمها جهات العمل والدراسات العليا. ومن غير إدراك واضح لموضوع النشر والإصدار، باقي مشروع التخرج ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Deployment and Release is where the theory of Graduation Project meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع النشر والإصدار هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

### Where It Is Used (بنستخدمه فين)

- Software and AI products
- Research prototypes
- Startups and MVPs
- Industry-sponsored projects
- Open-source contributions

**Egyptian Arabic (اللهجة المصرية):**

- منتجات البرمجيات والذكاء الاصطناعي
- النماذج البحثية
- الشركات الناشئة والنماذج الأولية
- المشروعات المدعومة من الصناعة
- المساهمات مفتوحة المصدر

### Real-World Usage and Relevance in the Field (الاستخدام والملاءمة في المجال)

A capstone team builds a real-time sign-language translator: they research, design, implement, test and present it over two semesters.

**Egyptian Arabic (اللهجة المصرية):**

فريق مشروع تخرج بيبني مترجم لغة إشارة لحظي: ببحثوا ويصمّموا وينفّذوا ويختبروا ويعرضوا على فصلين.

### Advantages (المميزات)

- Integrates the whole curriculum
- Builds teamwork and leadership
- Creates a portfolio artifact
- Connects study to real problems

**Egyptian Arabic (اللهجة المصرية):**

- بيدمج المنهج كله
- بيبني العمل الجماعي والقيادة
- بيعمل قطعة لملف الأعمال
- بيربط الدراسة بمشكلات حقيقية

### Limitations (الحدود)

- Scope creep threatens delivery
- Team coordination is hard
- Time is limited
- Some projects depend on external data

**Egyptian Arabic (اللهجة المصرية):**

- تضخّم النطاق بيهدد التسليم
- تنسيق الفريق صعب
- الوقت محدود
- بعض المشروعات بتعتمد على بيانات خارجية

### Best Practices (أحسن الممارسات)

- Define a clear, achievable scope
- Plan sprints and milestones
- Test and document continuously
- Prepare demos and the report early

**Egyptian Arabic (اللهجة المصرية):**

- حدّد نطاق واضح وقابل للتحقيق
- خطط دورات ومراحل
- اختبر ووثّق باستمرار
- جهّز العروض والتقرير بدري

### Common Mistakes (الأخطاء الشائعة)

- Choosing a scope too big to finish
- Leaving documentation to the end
- No version control or tests
- Ignoring the supervisor's feedback

**Egyptian Arabic (اللهجة المصرية):**

- اختيار نطاق أكبر من إن يخلص
- تأجيل التوثيق للآخر
- غياب التحكم في الإصدارات والاختبارات
- تجاهل ملاحظات المشرف

### Practical Example (مثال عملي)

A project team defines requirements in semester one, builds a prototype, then hardens, tests and defends it in semester two.

**Egyptian Arabic (اللهجة المصرية):**

فريق مشروع بيحدّد المتطلبات في الفصل الأول، ويبني نموذجًا أوليًا، وبعدين يقوّيه ويختبره ويدافع عنه في الفصل التاني.

### Hands-On Exercise (تمرين عملي بإيدك)

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Deployment and Release, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نطام صغير تعرفه. اكتب: (1) الموقف في النشر والإصدار، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Deployment and Release in one sentence of your own words.
2. Give two situations where Deployment and Release changes a technical decision.
3. Name one limitation of Deployment and Release and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف النشر والإصدار في جملة واحدة بكلامك.
2. ادي موقفين النشر والإصدار بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود النشر والإصدار واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Deployment and Release? (a) a formality with no use (b) a working tool inside Graduation Project (c) an unrelated subject.
Q2. True or false: Deployment and Release has no limitations.
Q3. In one line, why does Deployment and Release matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـالنشر والإصدار؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه مشروع التخرج (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: النشر والإصدار مالوش حدود.
س3. في سطر واحد، ليه النشر والإصدار مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Graduation Project.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه مشروع التخرج.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Deployment and Release to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها النشر والإصدار على برنامج أو نطام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Deployment and Release until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف النشر والإصدار تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الخامس: اختياري: تطوير تطبيقات الموبايل (ELEC-MOBILE)

## Background Tasks and Notifications (المهام الخلفية والإشعارات)

Background Tasks and Notifications (المهام الخلفية والإشعارات)
English Definition: Background Tasks and Notifications is a core topic in Web Technologies. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: المهام الخلفية والإشعارات موضوع أساسي في تقنيات الويب. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Background Tasks and Notifications** is the focus of this lesson. Web technologies cover how browsers, servers and databases work together to deliver interactive applications over HTTP.

**Egyptian Arabic (اللهجة المصرية):**

**المهام الخلفية والإشعارات** هو محور الدرس ده. تقنيات الويب بتغطي إزاي المتصفحات والسيرفرات وقواعد البيانات بتشتغل مع بعض لتقديم تطبيقات تفاعلية عبر HTTP.

### Why It Exists (ليه موجود)

The web is the default platform for software delivery, so every developer needs front-end and back-end skills. Without a clear grasp of Background Tasks and Notifications, the rest of Web Technologies has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

الويب هو المنصة الافتراضية لتسليم البرمجيات، وعشان كده كل مطوّر محتاج مهارات الواجهة الأمامية والخلفية. ومن غير إدراك واضح لموضوع المهام الخلفية والإشعارات، باقي تقنيات الويب ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Background Tasks and Notifications is where the theory of Web Technologies meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع المهام الخلفية والإشعارات هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

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

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Background Tasks and Notifications, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نطام صغير تعرفه. اكتب: (1) الموقف في المهام الخلفية والإشعارات، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Background Tasks and Notifications in one sentence of your own words.
2. Give two situations where Background Tasks and Notifications changes a technical decision.
3. Name one limitation of Background Tasks and Notifications and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف المهام الخلفية والإشعارات في جملة واحدة بكلامك.
2. ادي موقفين المهام الخلفية والإشعارات بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود المهام الخلفية والإشعارات واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Background Tasks and Notifications? (a) a formality with no use (b) a working tool inside Web Technologies (c) an unrelated subject.
Q2. True or false: Background Tasks and Notifications has no limitations.
Q3. In one line, why does Background Tasks and Notifications matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـالمهام الخلفية والإشعارات؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه تقنيات الويب (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: المهام الخلفية والإشعارات مالوش حدود.
س3. في سطر واحد، ليه المهام الخلفية والإشعارات مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Web Technologies.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه تقنيات الويب.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Background Tasks and Notifications to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها المهام الخلفية والإشعارات على برنامج أو نطام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Background Tasks and Notifications until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف المهام الخلفية والإشعارات تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم السادس: اختياري: تطوير الألعاب (ELEC-GAME)

## Input Handling and Controls (معالجة المدخلات وأدوات التحكم)

Input Handling and Controls (معالجة المدخلات وأدوات التحكم)
English Definition: Input Handling and Controls is a core topic in Computer Graphics. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: معالجة المدخلات وأدوات التحكم موضوع أساسي في الرسم بالحاسب. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Input Handling and Controls** is the focus of this lesson. Computer graphics generates and manipulates images using geometry, transformations, rasterization and shading on graphics hardware.

**Egyptian Arabic (اللهجة المصرية):**

**معالجة المدخلات وأدوات التحكم** هو محور الدرس ده. الرسم بالحاسب بيولّد ويتعامل مع الصور باستخدام الهندسة والتحويلات والتحويل النقطي والتظليل على عتاد الرسوم.

### Why It Exists (ليه موجود)

Games, films, CAD, visualization and AR/VR all depend on graphics pipelines. Without a clear grasp of Input Handling and Controls, the rest of Computer Graphics has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

الألعاب والأفلام والتصميم بالحاسب والتصوير المرئي والواقع المعزّز كلهم بيعتمدوا على خطوط عرض الرسوم. ومن غير إدراك واضح لموضوع معالجة المدخلات وأدوات التحكم، باقي الرسم بالحاسب ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Input Handling and Controls is where the theory of Computer Graphics meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع معالجة المدخلات وأدوات التحكم هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

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

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Input Handling and Controls, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نطام صغير تعرفه. اكتب: (1) الموقف في معالجة المدخلات وأدوات التحكم، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Input Handling and Controls in one sentence of your own words.
2. Give two situations where Input Handling and Controls changes a technical decision.
3. Name one limitation of Input Handling and Controls and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف معالجة المدخلات وأدوات التحكم في جملة واحدة بكلامك.
2. ادي موقفين معالجة المدخلات وأدوات التحكم بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود معالجة المدخلات وأدوات التحكم واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Input Handling and Controls? (a) a formality with no use (b) a working tool inside Computer Graphics (c) an unrelated subject.
Q2. True or false: Input Handling and Controls has no limitations.
Q3. In one line, why does Input Handling and Controls matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـمعالجة المدخلات وأدوات التحكم؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه الرسم بالحاسب (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: معالجة المدخلات وأدوات التحكم مالوش حدود.
س3. في سطر واحد، ليه معالجة المدخلات وأدوات التحكم مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Computer Graphics.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه الرسم بالحاسب.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Input Handling and Controls to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها معالجة المدخلات وأدوات التحكم على برنامج أو نطام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Input Handling and Controls until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف معالجة المدخلات وأدوات التحكم تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

## Learning Resources (المصادر الدراسية)

### AI403 — التعلّم المعزّز

**Primary Resource (المصدر الأساسي)**

- **Resource Name:** Reinforcement Learning: An Introduction (Sutton & Barto)
- **Resource Type:** Open Textbook
- **Direct Link:** http://incompleteideas.net/book/the-book-2nd.html
- **Difficulty:** Advanced
- **Estimated Time:** 40 hours

- **Why Recommended:** The definitive, free textbook on reinforcement learning.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: الكتاب المرجعي المجاني في التعلّم المعزّز.

- **What to Study From It:** MDPs, dynamic programming, TD learning, policy gradients and deep RL.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: عمليات ماركوف والبرمجة الديناميكية والتعلّم بالفرق الزمني وانحدار السياسة والتعلّم العميق.

**Optional Resource (المصدر الاختياري)**

- **Resource Name:** Spinning Up in Deep RL (OpenAI)
- **Resource Type:** Online Course
- **Direct Link:** https://spinningup.openai.com/
- **Difficulty:** Advanced
- **Estimated Time:** 30 hours

- **Why Recommended:** A hands-on introduction to deep RL with runnable code.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: مقدمة عملية في التعلّم المعزّز العميق بكود قابل للتشغيل.

- **What to Study From It:** Policy gradients, actor-critic, DDPG and TRPO.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: انحدار السياسة والممثل والناقد و DDPG و TRPO.

**Practice Platform (منصة التمرين العملي)**

- **Resource Name:** Gymnasium Environments
- **Resource Type:** Practice Platform
- **Direct Link:** https://gymnasium.farama.org/
- **Difficulty:** Intermediate
- **Estimated Time:** 25 hours

- **Why Recommended:** Standard environments to implement and test RL agents.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: بيئات معيارية لتنفيذ واختبار وكلاء التعلّم المعزّز.

- **What to Study From It:** CartPole, Atari and continuous-control tasks.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: مهام CartPole و Atari والتحكم المستمر.

### CS421 — الخوارزميات المتقدمة والتعقيد

**Primary Resource (المصدر الأساسي)**

- **Resource Name:** Approximation Algorithms (Vazirani)
- **Resource Type:** Textbook
- **Direct Link:** https://link.springer.com/book/10.1007/978-3-662-04565-7
- **Difficulty:** Advanced
- **Estimated Time:** 35 hours

- **Why Recommended:** A clear treatment of approximation algorithms and hardness.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: معالجة واضحة للخوارزميات التقريبية والصلابة.

- **What to Study From It:** Approximation, LP rounding, primal-dual and hardness.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: التقريب وتدوير البرمجة الخطية والثنائية الأصلية والصلابة.

**Optional Resource (المصدر الاختياري)**

- **Resource Name:** MIT 6.046J Design and Analysis of Algorithms
- **Resource Type:** University Course
- **Direct Link:** https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/
- **Difficulty:** Advanced
- **Estimated Time:** 35 hours

- **Why Recommended:** Advanced algorithm lectures on randomization, approximation and flows.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: محاضرات خوارزميات متقدمة في العشوائية والتقريب والتدفقات.

- **What to Study From It:** Randomized algorithms, approximation, linear programming and flows.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: الخوارزميات العشوائية والتقريب والبرمجة الخطية والتدفقات.

**Practice Platform (منصة التمرين العملي)**

- **Resource Name:** Codeforces Div. 1 Problems
- **Resource Type:** Practice Platform
- **Direct Link:** https://codeforces.com/problemset
- **Difficulty:** Advanced
- **Estimated Time:** 40 hours

- **Why Recommended:** Hard problems that require advanced techniques.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: مسائل صعبة بتطلب تقنيات متقدمة.

- **What to Study From It:** Advanced graph, flow, DP and randomized problems.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: مسائل رسوم وتدفق وبرمجة ديناميكية وعشوائية متقدمة.

### CS422 — أخلاقيات الحوسبة والممارسة المهنية

**Primary Resource (المصدر الأساسي)**

- **Resource Name:** ACM Code of Ethics and Professional Conduct
- **Resource Type:** Official Code
- **Direct Link:** https://www.acm.org/code-of-ethics
- **Difficulty:** Beginner
- **Estimated Time:** 6 hours

- **Why Recommended:** The professional code that defines computing responsibilities.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: الميثاق المهني اللي بيحدّد مسؤوليات الحوسبة.

- **What to Study From It:** Professional duties, honesty, privacy and social responsibility.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: الواجبات المهنية والأمانة والخصوصية والمسؤولية الاجتماعية.

**Optional Resource (المصدر الاختياري)**

- **Resource Name:** Ethics in Computing (NC State)
- **Resource Type:** Online Resource
- **Direct Link:** https://ethics.csc.ncsu.edu/
- **Difficulty:** Beginner
- **Estimated Time:** 10 hours

- **Why Recommended:** Case-based resource covering computing ethics topics.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: مصدر قائم على الحالات بيغطي مواضيع أخلاقيات الحوسبة.

- **What to Study From It:** Privacy, intellectual property, risk and professional issues.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: الخصوصية والملكية الفكرية والمخاطر والقضايا المهنية.

**Practice Platform (منصة التمرين العملي)**

- **Resource Name:** Harvard Business Review - Ethics Cases
- **Resource Type:** Case Library
- **Direct Link:** https://hbr.org/topic/ethics
- **Difficulty:** Intermediate
- **Estimated Time:** 10 hours

- **Why Recommended:** Real decision cases that sharpen ethical judgement.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: حالات قرار حقيقية بتصقل الحكم الأخلاقي.

- **What to Study From It:** Cases on technology, privacy and corporate responsibility.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: حالات في التكنولوجيا والخصوصية والمسؤولية المؤسسية.

### CS423 — مشروع التخرج 2

**Primary Resource (المصدر الأساسي)**

- **Resource Name:** Thesis and Project Writing Guides (MIT/Stanford)
- **Resource Type:** Official Guide
- **Direct Link:** https://writing.wisc.edu/handbook/
- **Difficulty:** Intermediate
- **Estimated Time:** 15 hours

- **Why Recommended:** Reliable guidance on structuring and writing a technical thesis.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: إرشاد موثوق في بناء وكتابة رسالة فنية.

- **What to Study From It:** Proposal writing, structure, methodology and referencing.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: كتابة المقترح والبنية والمنهجية والتوثيق.

**Optional Resource (المصدر الاختياري)**

- **Resource Name:** GitHub Projects and Repositories
- **Resource Type:** Practice Platform
- **Direct Link:** https://docs.github.com/en/issues/planning-and-tracking-with-projects
- **Difficulty:** Beginner
- **Estimated Time:** 10 hours

- **Why Recommended:** Plan, track and showcase the project in a real repository.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: خطط وتابع واعرض المشروع في مستودع حقيقي.

- **What to Study From It:** Boards, issues, milestones and releases.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: اللوحات والمشكلات والمراحل والإصدارات.

**Practice Platform (منصة التمرين العملي)**

- **Resource Name:** Overleaf - LaTeX for Reports
- **Resource Type:** Practice Tool
- **Direct Link:** https://www.overleaf.com/learn
- **Difficulty:** Beginner
- **Estimated Time:** 12 hours

- **Why Recommended:** Write a professional report with LaTeX collaboration.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: اكتب تقريرًا احترافيًا بتعاون LaTeX.

- **What to Study From It:** Document structure, figures, tables and bibliography.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: بنية المستند والأشكال والجداول والمراجع.

### ELEC-MOBILE — اختياري: تطوير تطبيقات الموبايل

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

### ELEC-GAME — اختياري: تطوير الألعاب

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


---

## End of Lesson (نهاية الدرس)

### Lesson Summary (ملخص الدرس)

This week covered the following topics across the semester's courses: AI403: Exploration vs Exploitation and Multi-Armed Bandits; CS421: Network Flow and Matching; CS422: Responsible AI and Autonomy; CS423: Deployment and Release; ELEC-MOBILE: Background Tasks and Notifications; ELEC-GAME: Input Handling and Controls. Each topic opened with a bilingual definition, then explained what it is, why it exists, why it matters, where it is used, its advantages and limits, best practices and common mistakes, followed by a practical example and exercises.

**Egyptian Arabic (اللهجة المصرية):**

الأسبوع ده غطّى المواضيع دي في مقررات الفصل: AI403: الاستكشاف مقابل الاستغلال وأذرع البانديت؛ CS421: تدفق الشبكات والمطابقة؛ CS422: الذكاء الاصطناعي المسؤول والاستقلالية؛ CS423: النشر والإصدار؛ ELEC-MOBILE: المهام الخلفية والإشعارات؛ ELEC-GAME: معالجة المدخلات وأدوات التحكم. كل موضوع بدأ بتعريف ثنائي اللغة، وبعدين شرح يعني إيه وليه موجود وليه مهم وبنستخدمه فين، ومميزاته وحدوده وأحسن الممارسات والأخطاء الشائعة، وبعدين مثال عملي وتمارين.

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

Next week continues with: AI403: On-Policy and Off-Policy Learning; CS421: Online Algorithms and Competitive Analysis; CS422: Social Media, Misinformation and Society; CS423: Comprehensive Testing; ELEC-MOBILE: Sensors and Device Hardware; ELEC-GAME: Game AI and Behaviour.

**Egyptian Arabic (اللهجة المصرية):**

الأسبوع الجاي بيكمل بـ: AI403: التعلّم على السياسة وخارجها؛ CS421: الخوارزميات الفورية والتحليل التنافسي؛ CS422: التواصل الاجتماعي والمعلومات المضللة والمجتمع؛ CS423: الاختبار الشامل؛ ELEC-MOBILE: المستشعرات وعتاد الجهاز؛ ELEC-GAME: ذكاء اللعبة والسلوك.

### Important Terms (مصطلحات مهمة)

#### Agent (وكيل)
English Definition: The learner that takes actions.
Egyptian Arabic Definition: المتعلّم اللي بيتخذ أفعال.

#### Reward (مكافأة)
English Definition: Feedback signal from the environment.
Egyptian Arabic Definition: إشارة تغذية راجعة من البيئة.

#### Policy (سياسة)
English Definition: A mapping from states to actions.
Egyptian Arabic Definition: ربط بين الحالات والأفعال.

#### Episode (حلقة)
English Definition: One full interaction until termination.
Egyptian Arabic Definition: تفاعل كامل لحد النهاية.

#### Exploration (الاستكشاف)
English Definition: Trying new actions to learn.
Egyptian Arabic Definition: تجربة أفعال جديدة عشان تتعلم.


---

[الدرس السابق: week-08.md](week-08.md) · [رجوع لفصل 8](README.md) · [الدرس الجاي: week-10.md](week-10.md)