# الأسبوع 6 — الفصل 6

> الدرس ده بيغطّي موضوع واحد في كل مقرر من مقررات الفصل، وكل الشرح مكتوب بالعامية المصرية مع البلوك الإنجليزي الكامل جنبه.

**المقررات اللي في الدرس ده:** CS321 (النظم الموزّعة)، AI302 (التعلّم العميق)، CS322 (أمن المعلومات والتشفير)، CS323 (معمارية البرمجيات وأنماط التصميم)، CS324 (الحوسبة السحابية)، ELEC-DS (اختياري: علم البيانات والبيانات الضخمة)

---

# القسم الأول: النظم الموزّعة (CS321)

## Synchronization and Logical Clocks (التزامن والساعات المنطقية)

Synchronization and Logical Clocks (التزامن والساعات المنطقية)
English Definition: Synchronization and Logical Clocks is a core topic in Distributed Systems. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: التزامن والساعات المنطقية موضوع أساسي في النظم الموزّعة. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Synchronization and Logical Clocks** is the focus of this lesson. Distributed systems run across many machines that coordinate over a network to appear as one coherent system.

**Egyptian Arabic (اللهجة المصرية):**

**التزامن والساعات المنطقية** هو محور الدرس ده. النظم الموزّعة بتشتغل على أجهزة كتير بتتنسّق عبر شبكة عشان تبان كنظام واحد متماسك.

### Why It Exists (ليه موجود)

Scale, fault tolerance and global reach require spreading work across many machines. Without a clear grasp of Synchronization and Logical Clocks, the rest of Distributed Systems has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

النطاق الواسع وتحمّل الأعطال والانتشار العالمي بيحتاجوا توزيع الشغل على أجهزة كتير. ومن غير إدراك واضح لموضوع التزامن والساعات المنطقية، باقي النظم الموزّعة ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Synchronization and Logical Clocks is where the theory of Distributed Systems meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع التزامن والساعات المنطقية هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

### Where It Is Used (بنستخدمه فين)

- Cloud platforms and microservices
- Databases and storage
- Blockchain and ledgers
- Search and messaging systems
- Content delivery

**Egyptian Arabic (اللهجة المصرية):**

- منصات السحابة والخدمات المصغّرة
- قواعد البيانات والتخزين
- البلوكشين والدفاتر
- أنظمة البحث والرسائل
- توصيل المحتوى

### Real-World Usage and Relevance in the Field (الاستخدام والملاءمة في المجال)

A global chat app keeps messages consistent and available even when servers in one region fail - that is distributed systems.

**Egyptian Arabic (اللهجة المصرية):**

تطبيق محادثة عالمي بيخلي الرسائل متسقة ومتاحة حتى لما سيرفرات منطقة تفشل - ده النظم الموزّعة.

### Advantages (المميزات)

- Scales horizontally
- Tolerates failures
- Low latency worldwide
- High availability

**Egyptian Arabic (اللهجة المصرية):**

- بتتوسّع أفقيًا
- بتتحمّل الأعطال
- زمن استجابة منخفض عالميًا
- توافر عالٍ

### Limitations (الحدود)

- Consistency is hard to guarantee
- Partial failures are complex
- Debugging is difficult
- Clock and ordering issues

**Egyptian Arabic (اللهجة المصرية):**

- الاتساق صعب ضمانه
- الأعطال الجزئية معقّدة
- التنقيح صعب
- مشكلات الساعة والترتيب

### Best Practices (أحسن الممارسات)

- Choose consistency model per use case
- Design for failure from the start
- Use idempotent operations
- Add observability and tracing

**Egyptian Arabic (اللهجة المصرية):**

- اختار نموذج الاتساق حسب الاستخدام
- صمّم لتحمّل الفشل من البداية
- استخدم عمليات قابلة للتكرار بأمان
- أضف المراقبة والتتبّع

### Common Mistakes (الأخطاء الشائعة)

- Assuming the network is reliable
- Ignoring partial failure
- Confusing concurrency with distribution
- Underestimating clock skew

**Egyptian Arabic (اللهجة المصرية):**

- افتراض إن الشبكة موثوقة
- تجاهل الفشل الجزئي
- الخلط بين التزامن والتوزيع
- التقليل من انحراف الساعات

### Practical Example (مثال عملي)

A key-value store replicates data to three servers; if one fails, the others keep serving reads and writes.

**Egyptian Arabic (اللهجة المصرية):**

مخزن مفتاح-قيمة بينسخ البيانات على ثلاث سيرفرات؛ لو واحد فشل، الباقي بيفضل يخدم القراءة والكتابة.

### Hands-On Exercise (تمرين عملي بإيدك)

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Synchronization and Logical Clocks, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في التزامن والساعات المنطقية، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Synchronization and Logical Clocks in one sentence of your own words.
2. Give two situations where Synchronization and Logical Clocks changes a technical decision.
3. Name one limitation of Synchronization and Logical Clocks and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف التزامن والساعات المنطقية في جملة واحدة بكلامك.
2. ادي موقفين التزامن والساعات المنطقية بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود التزامن والساعات المنطقية واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Synchronization and Logical Clocks? (a) a formality with no use (b) a working tool inside Distributed Systems (c) an unrelated subject.
Q2. True or false: Synchronization and Logical Clocks has no limitations.
Q3. In one line, why does Synchronization and Logical Clocks matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـالتزامن والساعات المنطقية؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه النظم الموزّعة (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: التزامن والساعات المنطقية مالوش حدود.
س3. في سطر واحد، ليه التزامن والساعات المنطقية مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Distributed Systems.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه النظم الموزّعة.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Synchronization and Logical Clocks to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها التزامن والساعات المنطقية على برنامج أو نظام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Synchronization and Logical Clocks until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف التزامن والساعات المنطقية تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الثاني: التعلّم العميق (AI302)

## Optimization for Deep Learning (التحسين للتعلّم العميق)

Optimization for Deep Learning (التحسين للتعلّم العميق)
English Definition: Optimization for Deep Learning is a core topic in Deep Learning. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: التحسين للتعلّم العميق موضوع أساسي في التعلّم العميق. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Optimization for Deep Learning** is the focus of this lesson. Deep learning uses multi-layer neural networks to learn representations from raw data like images, text and audio.

**Egyptian Arabic (اللهجة المصرية):**

**التحسين للتعلّم العميق** هو محور الدرس ده. التعلّم العميق بيستخدم شبكات عصبية متعددة الطبقات عشان تتعلم تمثيلات من البيانات الخام زي الصور والنصوص والصوت.

### Why It Exists (ليه موجود)

Deep learning broke records in vision, speech and language and drives modern AI products. Without a clear grasp of Optimization for Deep Learning, the rest of Deep Learning has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

التعلّم العميق كسر أرقام قياسية في الرؤية والكلام واللغة وبيشغّل منتجات الذكاء الاصطناعي الحديثة. ومن غير إدراك واضح لموضوع التحسين للتعلّم العميق، باقي التعلّم العميق ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Optimization for Deep Learning is where the theory of Deep Learning meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع التحسين للتعلّم العميق هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

### Where It Is Used (بنستخدمه فين)

- Image and video recognition
- Speech and language systems
- Recommendation and ranking
- Generative models
- Autonomous systems

**Egyptian Arabic (اللهجة المصرية):**

- التعرّف على الصور والفيديو
- أنظمة الكلام واللغة
- التوصيات والترتيب
- النماذج التوليدية
- الأنظمة المستقلة

### Real-World Usage and Relevance in the Field (الاستخدام والملاءمة في المجال)

A convolutional network recognizes objects in photos; a transformer translates languages - both learn features from raw data.

**Egyptian Arabic (اللهجة المصرية):**

شبكة التفافية بتتعرّف على الأجسام في الصور؛ ومحوّل بيترجم اللغات - الاتنين بيتعلموا الخصائص من البيانات الخام.

### Advantages (المميزات)

- Learns features automatically
- State of the art on perception tasks
- Scales with data and compute
- Transfer learning reuses models

**Egyptian Arabic (اللهجة المصرية):**

- بيتعلم الخصائص تلقائيًا
- الأحدث في مهام الإدراك
- بيتوسّع مع البيانات والحوسبة
- التعلّم بالنقل بيعيد استخدام النماذج

### Limitations (الحدود)

- Data and compute hungry
- Opaque and hard to debug
- Sensitive to hyperparameters
- Can encode bias

**Egyptian Arabic (اللهجة المصرية):**

- شرِه للبيانات والحوسبة
- غامض وصعب تنقيحه
- حسّاس للمعاملات الفائقة
- ممكن يرمّز التحيّز

### Best Practices (أحسن الممارسات)

- Start from a simple baseline
- Normalize inputs and tune learning rate
- Use regularization and early stopping
- Leverage transfer learning

**Egyptian Arabic (اللهجة المصرية):**

- ابدأ من نموذج بسيط كمرجع
- طبّع المدخلات واضبط معدل التعلّم
- استخدم التنظيم والإيقاف المبكر
- استفيد من التعلّم بالنقل

### Common Mistakes (الأخطاء الشائعة)

- Training deep nets on tiny data
- Ignoring validation curves
- Wrong learning rate causing divergence
- Leaking test data into training

**Egyptian Arabic (اللهجة المصرية):**

- تدريب شبكات عميقة على بيانات صغيرة
- تجاهل منحنيات التحقق
- معدل تعلّم غلط بيسبب التباعد
- تسريب بيانات الاختبار للتدريب

### Practical Example (مثال عملي)

A CNN trained on labelled photos learns edges, then shapes, then objects - depth lets it build complex features from simple ones.

**Egyptian Arabic (اللهجة المصرية):**

شبكة التفافية مدرّبة على صور موسومة بتتعلم الحواف، وبعدين الأشكال، وبعدين الأجسام - العمق بيخليها تبني خصائص معقدة من بسيطة.

### Hands-On Exercise (تمرين عملي بإيدك)

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Optimization for Deep Learning, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في التحسين للتعلّم العميق، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Optimization for Deep Learning in one sentence of your own words.
2. Give two situations where Optimization for Deep Learning changes a technical decision.
3. Name one limitation of Optimization for Deep Learning and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف التحسين للتعلّم العميق في جملة واحدة بكلامك.
2. ادي موقفين التحسين للتعلّم العميق بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود التحسين للتعلّم العميق واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Optimization for Deep Learning? (a) a formality with no use (b) a working tool inside Deep Learning (c) an unrelated subject.
Q2. True or false: Optimization for Deep Learning has no limitations.
Q3. In one line, why does Optimization for Deep Learning matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـالتحسين للتعلّم العميق؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه التعلّم العميق (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: التحسين للتعلّم العميق مالوش حدود.
س3. في سطر واحد، ليه التحسين للتعلّم العميق مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Deep Learning.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه التعلّم العميق.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Optimization for Deep Learning to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها التحسين للتعلّم العميق على برنامج أو نظام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Optimization for Deep Learning until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف التحسين للتعلّم العميق تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الثالث: أمن المعلومات والتشفير (CS322)

## Key Management and Exchange (إدارة المفاتيح وتبادلها)

Key Management and Exchange (إدارة المفاتيح وتبادلها)
English Definition: Key Management and Exchange is a core topic in Information Security and Cryptography. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: إدارة المفاتيح وتبادلها موضوع أساسي في أمن المعلومات والتشفير. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Key Management and Exchange** is the focus of this lesson. Cryptography protects information using encryption, hashing, signatures and keys, while security engineering defends systems against attacks.

**Egyptian Arabic (اللهجة المصرية):**

**إدارة المفاتيح وتبادلها** هو محور الدرس ده. التشفير بيحمي المعلومات باستخدام التعمية والتقطيع والتوقيعات والمفاتيح، وهندسة الأمن بتدافع عن الأنظمة ضد الهجمات.

### Why It Exists (ليه موجود)

Confidentiality, integrity and authenticity are essential for every system that handles valuable data. Without a clear grasp of Key Management and Exchange, the rest of Information Security and Cryptography has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

السرية والسلامة والأصالة أساسية لكل نظام بيتعامل مع بيانات قيّمة. ومن غير إدراك واضح لموضوع إدارة المفاتيح وتبادلها، باقي أمن المعلومات والتشفير ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Key Management and Exchange is where the theory of Information Security and Cryptography meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع إدارة المفاتيح وتبادلها هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

### Where It Is Used (بنستخدمه فين)

- Secure communication (HTTPS)
- Authentication and passwords
- Digital signatures and certificates
- Blockchain and payments
- Data protection

**Egyptian Arabic (اللهجة المصرية):**

- التواصل الآمن (HTTPS)
- المصادقة وكلمات المرور
- التوقيعات الرقمية والشهادات
- البلوكشين والمدفوعات
- حماية البيانات

### Real-World Usage and Relevance in the Field (الاستخدام والملاءمة في المجال)

When you see the padlock in your browser, TLS is using cryptography to encrypt traffic so nobody can read or tamper with it.

**Egyptian Arabic (اللهجة المصرية):**

لما تشوف القفل في المتصفح، TLS بيستخدم التشفير لتشفير الترافيك عشان محدش يقدر يقراه أو يعدّله.

### Advantages (المميزات)

- Guarantees confidentiality and integrity
- Enables trust without prior contact
- Foundation for secure systems
- Provable security properties

**Egyptian Arabic (اللهجة المصرية):**

- بتضمن السرية والسلامة
- بتمكّن الثقة من غير تعارف مسبق
- أساس للأنظمة الآمنة
- خصائص أمنية قابلة للبرهان

### Limitations (الحدود)

- Key management is hard
- Implementation bugs break security
- Quantum computing threatens some schemes
- Usability often conflicts with security

**Egyptian Arabic (اللهجة المصرية):**

- إدارة المفاتيح صعبة
- أخطاء التنفيذ بتكسر الأمن
- الحوسبة الكمّية بتهدد بعض الأنظمة
- سهولة الاستخدام غالبًا تتعارض مع الأمن

### Best Practices (أحسن الممارسات)

- Never invent your own crypto
- Use vetted libraries and protocols
- Rotate and protect keys
- Validate all inputs and use TLS

**Egyptian Arabic (اللهجة المصرية):**

- ما تخترعش تشفيرك بنفسك
- استخدم مكتبات وبروتوكولات مجرّبة
- بدّل المفاتيح واحميها
- تحقق من كل المدخلات واستخدم TLS

### Common Mistakes (الأخطاء الشائعة)

- Reusing keys and nonces
- Weak password hashing
- Rolling your own algorithm
- Ignoring side channels

**Egyptian Arabic (اللهجة المصرية):**

- إعادة استخدام المفاتيح والأرقام العشوائية
- تقطيع كلمات مرور ضعيف
- اختراع خوارزمية بنفسك
- تجاهل القنوات الجانبية

### Practical Example (مثال عملي)

Storing passwords with a salted hash means even if the database leaks, attackers cannot read the original passwords.

**Egyptian Arabic (اللهجة المصرية):**

تخزين كلمات المرور بتقطيع مع ملح معناه حتى لو قاعدة البيانات اتسرّبت، المهاجمين ما يقدروش يقرأوا كلمات المرور الأصلية.

### Hands-On Exercise (تمرين عملي بإيدك)

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Key Management and Exchange, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في إدارة المفاتيح وتبادلها، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Key Management and Exchange in one sentence of your own words.
2. Give two situations where Key Management and Exchange changes a technical decision.
3. Name one limitation of Key Management and Exchange and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف إدارة المفاتيح وتبادلها في جملة واحدة بكلامك.
2. ادي موقفين إدارة المفاتيح وتبادلها بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود إدارة المفاتيح وتبادلها واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Key Management and Exchange? (a) a formality with no use (b) a working tool inside Information Security and Cryptography (c) an unrelated subject.
Q2. True or false: Key Management and Exchange has no limitations.
Q3. In one line, why does Key Management and Exchange matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـإدارة المفاتيح وتبادلها؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه أمن المعلومات والتشفير (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: إدارة المفاتيح وتبادلها مالوش حدود.
س3. في سطر واحد، ليه إدارة المفاتيح وتبادلها مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Information Security and Cryptography.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه أمن المعلومات والتشفير.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Key Management and Exchange to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها إدارة المفاتيح وتبادلها على برنامج أو نظام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Key Management and Exchange until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف إدارة المفاتيح وتبادلها تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الرابع: معمارية البرمجيات وأنماط التصميم (CS323)

## Event-Driven Architecture (المعمارية القائمة على الأحداث)

Event-Driven Architecture (المعمارية القائمة على الأحداث)
English Definition: Event-Driven Architecture is a core topic in Software Architecture and Design. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: المعمارية القائمة على الأحداث موضوع أساسي في معمارية البرمجيات والتصميم. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Event-Driven Architecture** is the focus of this lesson. Software architecture defines the high-level structure of a system - components, their relationships and the quality attributes they must satisfy.

**Egyptian Arabic (اللهجة المصرية):**

**المعمارية القائمة على الأحداث** هو محور الدرس ده. معمارية البرمجيات بتحدد البنية عالية المستوى للنظام - المكوّنات وعلاقاتها وخصائص الجودة اللي لازم تحققها.

### Why It Exists (ليه موجود)

Architecture determines scalability, maintainability and cost long before code is written. Without a clear grasp of Event-Driven Architecture, the rest of Software Architecture and Design has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

المعمارية بتحدد التوسّع والصيانة والتكلفة قبل ما يتكتب الكود بفترة طويلة. ومن غير إدراك واضح لموضوع المعمارية القائمة على الأحداث، باقي معمارية البرمجيات والتصميم ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Event-Driven Architecture is where the theory of Software Architecture and Design meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع المعمارية القائمة على الأحداث هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

### Where It Is Used (بنستخدمه فين)

- Enterprise and cloud systems
- Microservices and APIs
- Framework and platform design
- Legacy modernization
- System integration

**Egyptian Arabic (اللهجة المصرية):**

- أنظمة المؤسسات والسحابة
- الخدمات المصغّرة وواجهات البرمجة
- تصميم الأطر والمنصات
- تحديث الأنظمة القديمة
- تكامل الأنظمة

### Real-World Usage and Relevance in the Field (الاستخدام والملاءمة في المجال)

Choosing microservices over a monolith changes how a team deploys, scales and debugs for years to come.

**Egyptian Arabic (اللهجة المصرية):**

اختيار الخدمات المصغّرة بدل النظام المتكامل بيغيّر طريقة نشر الفريق وتوسّعه وتنقيحه لسنين جاية.

### Advantages (المميزات)

- Guides long-term structure
- Enables independent scaling
- Improves maintainability
- Documents key decisions

**Egyptian Arabic (اللهجة المصرية):**

- بتوجّه البنية طويلة الأجل
- بتمكّن التوسّع المستقل
- بتحسّن الصيانة
- بتوثّق القرارات المهمة

### Limitations (الحدود)

- Over-architecture adds complexity
- Hard to change once built
- Requires experience to judge
- Trade-offs have no perfect answer

**Egyptian Arabic (اللهجة المصرية):**

- المعمارية الزائدة بتزيد التعقيد
- صعب تغييرها بعد البناء
- محتاجة خبرة للحكم
- المقايضات ملهاش إجابة مثالية

### Best Practices (أحسن الممارسات)

- Document decisions with ADRs
- Choose patterns to fit the problem
- Keep coupling low and cohesion high
- Evaluate quality attributes explicitly

**Egyptian Arabic (اللهجة المصرية):**

- وثّق القرارات بسجلات القرارات
- اختار الأنماط اللي تناسب المشكلة
- خلي الترابط منخفض والتماسك عالي
- قيّم خصائص الجودة بوضوح

### Common Mistakes (الأخطاء الشائعة)

- Choosing architecture by hype
- Ignoring non-functional requirements
- Distributed monolith mistakes
- No documentation of trade-offs

**Egyptian Arabic (اللهجة المصرية):**

- اختيار المعمارية بالموضة
- تجاهل المتطلبات غير الوظيفية
- أخطاء النظام الموزّع المتكامل
- عدم توثيق المقايضات

### Practical Example (مثال عملي)

An e-commerce system separates browsing and payment so payment can be scaled and secured independently of the catalogue.

**Egyptian Arabic (اللهجة المصرية):**

نظام تجارة إلكترونية بيفصل التصفح عن الدفع عشان الدفع يتوسّع ويتأمّن بشكل مستقل عن الكتالوج.

### Hands-On Exercise (تمرين عملي بإيدك)

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Event-Driven Architecture, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في المعمارية القائمة على الأحداث، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Event-Driven Architecture in one sentence of your own words.
2. Give two situations where Event-Driven Architecture changes a technical decision.
3. Name one limitation of Event-Driven Architecture and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف المعمارية القائمة على الأحداث في جملة واحدة بكلامك.
2. ادي موقفين المعمارية القائمة على الأحداث بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود المعمارية القائمة على الأحداث واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Event-Driven Architecture? (a) a formality with no use (b) a working tool inside Software Architecture and Design (c) an unrelated subject.
Q2. True or false: Event-Driven Architecture has no limitations.
Q3. In one line, why does Event-Driven Architecture matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـالمعمارية القائمة على الأحداث؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه معمارية البرمجيات والتصميم (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: المعمارية القائمة على الأحداث مالوش حدود.
س3. في سطر واحد، ليه المعمارية القائمة على الأحداث مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Software Architecture and Design.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه معمارية البرمجيات والتصميم.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Event-Driven Architecture to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها المعمارية القائمة على الأحداث على برنامج أو نظام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Event-Driven Architecture until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف المعمارية القائمة على الأحداث تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الخامس: الحوسبة السحابية (CS324)

## Compute Services and Auto-Scaling (خدمات الحوسبة والتحجيم التلقائي)

Compute Services and Auto-Scaling (خدمات الحوسبة والتحجيم التلقائي)
English Definition: Compute Services and Auto-Scaling is a core topic in Cloud Computing. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: خدمات الحوسبة والتحجيم التلقائي موضوع أساسي في الحوسبة السحابية. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Compute Services and Auto-Scaling** is the focus of this lesson. Cloud computing delivers computing resources - servers, storage, databases, services - on demand over the internet with pay-as-you-go pricing.

**Egyptian Arabic (اللهجة المصرية):**

**خدمات الحوسبة والتحجيم التلقائي** هو محور الدرس ده. الحوسبة السحابية بتوفّر موارد الحوسبة - سيرفرات وتخزين وقواعد بيانات وخدمات - عند الطلب عبر الإنترنت بدفع حسب الاستخدام.

### Why It Exists (ليه موجود)

Cloud removes the need to buy and maintain hardware, letting teams scale instantly. Without a clear grasp of Compute Services and Auto-Scaling, the rest of Cloud Computing has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

السحابة بتلغي الحاجة لشراء وصيانة العتاد، وبتخلي الفرق تتوسّع فورًا. ومن غير إدراك واضح لموضوع خدمات الحوسبة والتحجيم التلقائي، باقي الحوسبة السحابية ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Compute Services and Auto-Scaling is where the theory of Cloud Computing meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع خدمات الحوسبة والتحجيم التلقائي هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

### Where It Is Used (بنستخدمه فين)

- Web and mobile back ends
- Big data and analytics
- Machine learning platforms
- Disaster recovery
- Startups and enterprise IT

**Egyptian Arabic (اللهجة المصرية):**

- الواجهات الخلفية للويب والموبايل
- البيانات الضخمة والتحليلات
- منصات تعلّم الآلة
- التعافي من الكوارث
- الشركات الناشئة وتقنية معلومات المؤسسات

### Real-World Usage and Relevance in the Field (الاستخدام والملاءمة في المجال)

A startup launches on the cloud with no servers of its own; when traffic spikes, capacity scales up automatically, then scales back down.

**Egyptian Arabic (اللهجة المصرية):**

شركة ناشئة بتطلق على السحابة من غير سيرفرات خاصة؛ لما الترافيك يعلى، القدرة بتتوسّع تلقائيًا، وبعدين ترجع تنخفض.

### Advantages (المميزات)

- Elastic scaling
- Pay only for what you use
- Global availability
- Managed services reduce ops

**Egyptian Arabic (اللهجة المصرية):**

- توسّع مرن
- بتدفع بس على اللي تستخدمه
- توافر عالمي
- الخدمات المُدارة بتقلل العمليات

### Limitations (الحدود)

- Vendor lock-in risk
- Costs can spiral if unmanaged
- Security and compliance concerns
- Network dependency

**Egyptian Arabic (اللهجة المصرية):**

- خطر الارتباط بمزوّد واحد
- التكاليف ممكن تتفاقم لو مش منظمة
- مخاوف أمنية وتنظيمية
- الاعتماد على الشبكة

### Best Practices (أحسن الممارسات)

- Design for elasticity and statelessness
- Automate infrastructure as code
- Monitor cost and usage
- Secure identity and data

**Egyptian Arabic (اللهجة المصرية):**

- صمّم للمرونة وانعدام الحالة
- أتمت البنية التحتية ككود
- راقب التكلفة والاستخدام
- أمّن الهوية والبيانات

### Common Mistakes (الأخطاء الشائعة)

- Lifting servers to the cloud without change
- Ignoring cost alerts
- Public buckets leaking data
- No backup strategy

**Egyptian Arabic (اللهجة المصرية):**

- نقل السيرفرات للسحابة من غير تغيير
- تجاهل تنبيهات التكلفة
- حاويات عامة بتسرّب بيانات
- غياب استراتيجية نسخ احتياطي

### Practical Example (مثال عملي)

A photo app stores images in cloud object storage and runs its API on serverless functions that scale with demand.

**Egyptian Arabic (اللهجة المصرية):**

تطبيق صور بيخزّن الصور في تخزين كائنات سحابي وبيشغّل واجهته على دوال بلا خوادم بتتوسّع مع الطلب.

### Hands-On Exercise (تمرين عملي بإيدك)

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Compute Services and Auto-Scaling, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في خدمات الحوسبة والتحجيم التلقائي، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Compute Services and Auto-Scaling in one sentence of your own words.
2. Give two situations where Compute Services and Auto-Scaling changes a technical decision.
3. Name one limitation of Compute Services and Auto-Scaling and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف خدمات الحوسبة والتحجيم التلقائي في جملة واحدة بكلامك.
2. ادي موقفين خدمات الحوسبة والتحجيم التلقائي بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود خدمات الحوسبة والتحجيم التلقائي واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Compute Services and Auto-Scaling? (a) a formality with no use (b) a working tool inside Cloud Computing (c) an unrelated subject.
Q2. True or false: Compute Services and Auto-Scaling has no limitations.
Q3. In one line, why does Compute Services and Auto-Scaling matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـخدمات الحوسبة والتحجيم التلقائي؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه الحوسبة السحابية (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: خدمات الحوسبة والتحجيم التلقائي مالوش حدود.
س3. في سطر واحد، ليه خدمات الحوسبة والتحجيم التلقائي مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Cloud Computing.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه الحوسبة السحابية.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Compute Services and Auto-Scaling to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها خدمات الحوسبة والتحجيم التلقائي على برنامج أو نظام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Compute Services and Auto-Scaling until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف خدمات الحوسبة والتحجيم التلقائي تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم السادس: اختياري: علم البيانات والبيانات الضخمة (ELEC-DS)

## Big Data Concepts and the 5 Vs (مفاهيم البيانات الضخمة ومحدداتها الخمسة)

Big Data Concepts and the 5 Vs (مفاهيم البيانات الضخمة ومحدداتها الخمسة)
English Definition: Big Data Concepts and the 5 Vs is a core topic in Data Science and Big Data. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: مفاهيم البيانات الضخمة ومحدداتها الخمسة موضوع أساسي في علم البيانات والبيانات الضخمة. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Big Data Concepts and the 5 Vs** is the focus of this lesson. Data science extracts insight from data through collection, cleaning, analysis and modelling, while big data handles volumes too large for one machine.

**Egyptian Arabic (اللهجة المصرية):**

**مفاهيم البيانات الضخمة ومحدداتها الخمسة** هو محور الدرس ده. علم البيانات بيستخرج رؤى من البيانات عبر الجمع والتنظيف والتحليل والنمذجة، والبيانات الضخمة بتتعامل مع أحجام أكبر من جهاز واحد.

### Why It Exists (ليه موجود)

Organizations collect huge data and need skills to turn it into decisions and products. Without a clear grasp of Big Data Concepts and the 5 Vs, the rest of Data Science and Big Data has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

المنظمات بتجمع بيانات ضخمة ومحتاجة مهارات تحوّلها لقرارات ومنتجات. ومن غير إدراك واضح لموضوع مفاهيم البيانات الضخمة ومحدداتها الخمسة، باقي علم البيانات والبيانات الضخمة ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Big Data Concepts and the 5 Vs is where the theory of Data Science and Big Data meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع مفاهيم البيانات الضخمة ومحدداتها الخمسة هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

### Where It Is Used (بنستخدمه فين)

- Business analytics
- Recommendation and personalization
- Fraud detection
- Scientific research
- Operations optimization

**Egyptian Arabic (اللهجة المصرية):**

- تحليلات الأعمال
- التوصيات والتخصيص
- كشف الاحتيال
- البحث العلمي
- تحسين العمليات

### Real-World Usage and Relevance in the Field (الاستخدام والملاءمة في المجال)

A retailer analyses billions of transactions in a distributed cluster to decide which products to stock in each branch.

**Egyptian Arabic (اللهجة المصرية):**

تاجر بيحلّل مليارات المعاملات في عنقود موزّع عشان يقرر يخزّن إيه في كل فرع.

### Advantages (المميزات)

- Turns raw data into insight
- Scales to huge datasets
- Combines statistics and engineering
- Drives product decisions

**Egyptian Arabic (اللهجة المصرية):**

- بيحوّل البيانات الخام لرؤى
- بيتوسّع لبيانات ضخمة
- بيدمج الإحصاء والهندسة
- بيوجّه قرارات المنتج

### Limitations (الحدود)

- Garbage in, garbage out
- Distributed tools add complexity
- Privacy and ethics concerns
- Insight needs domain knowledge

**Egyptian Arabic (اللهجة المصرية):**

- مدخلات فاسدة تطلع نتائج فاسدة
- الأدوات الموزّعة بتزيد التعقيد
- مخاوف الخصوصية والأخلاقيات
- الرؤية محتاجة معرفة بالمجال

### Best Practices (أحسن الممارسات)

- Clean and validate data first
- Use distributed tools only when needed
- Document pipelines and assumptions
- Respect privacy and governance

**Egyptian Arabic (اللهجة المصرية):**

- نظّف البيانات وتحقق منها الأول
- استخدم الأدوات الموزّعة عند الحاجة بس
- وثّق الخطوط والفروض
- احترم الخصوصية والحوكمة

### Common Mistakes (الأخطاء الشائعة)

- Jumping to models before cleaning
- Using big data tools on small data
- Ignoring data provenance
- Overfitting to historical patterns

**Egyptian Arabic (اللهجة المصرية):**

- القفز للنماذج قبل التنظيف
- استخدام أدوات البيانات الضخمة على بيانات صغيرة
- تجاهل مصدر البيانات
- الإفراط في التوفيق على الأنماط التاريخية

### Practical Example (مثال عملي)

A streaming pipeline aggregates clicks in real time with Spark, then a dashboard shows live conversion rates.

**Egyptian Arabic (اللهجة المصرية):**

خط تدفق بيجمع النقرات في الزمن الحقيقي بـ Spark، وبعدين لوحة معلومات بتعرض معدلات التحويل لحظيًا.

### Hands-On Exercise (تمرين عملي بإيدك)

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Big Data Concepts and the 5 Vs, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في مفاهيم البيانات الضخمة ومحدداتها الخمسة، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Big Data Concepts and the 5 Vs in one sentence of your own words.
2. Give two situations where Big Data Concepts and the 5 Vs changes a technical decision.
3. Name one limitation of Big Data Concepts and the 5 Vs and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف مفاهيم البيانات الضخمة ومحدداتها الخمسة في جملة واحدة بكلامك.
2. ادي موقفين مفاهيم البيانات الضخمة ومحدداتها الخمسة بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود مفاهيم البيانات الضخمة ومحدداتها الخمسة واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Big Data Concepts and the 5 Vs? (a) a formality with no use (b) a working tool inside Data Science and Big Data (c) an unrelated subject.
Q2. True or false: Big Data Concepts and the 5 Vs has no limitations.
Q3. In one line, why does Big Data Concepts and the 5 Vs matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـمفاهيم البيانات الضخمة ومحدداتها الخمسة؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه علم البيانات والبيانات الضخمة (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: مفاهيم البيانات الضخمة ومحدداتها الخمسة مالوش حدود.
س3. في سطر واحد، ليه مفاهيم البيانات الضخمة ومحدداتها الخمسة مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Data Science and Big Data.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه علم البيانات والبيانات الضخمة.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Big Data Concepts and the 5 Vs to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها مفاهيم البيانات الضخمة ومحدداتها الخمسة على برنامج أو نظام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Big Data Concepts and the 5 Vs until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف مفاهيم البيانات الضخمة ومحدداتها الخمسة تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

## Learning Resources (المصادر الدراسية)

### CS321 — النظم الموزّعة

**Primary Resource (المصدر الأساسي)**

- **Resource Name:** Distributed Systems (Tanenbaum & van Steen)
- **Resource Type:** Textbook
- **Direct Link:** https://www.distributed-systems.net/
- **Difficulty:** Advanced
- **Estimated Time:** 40 hours

- **Why Recommended:** A comprehensive, well-organized distributed systems textbook.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: كتاب نظم موزّعة شامل ومنظّم جيدًا.

- **What to Study From It:** Communication, synchronization, consistency, replication and fault tolerance.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: التواصل والتزامن والاتساق والنسخ وتحمّل الأعطال.

**Optional Resource (المصدر الاختياري)**

- **Resource Name:** MIT 6.824 Distributed Systems
- **Resource Type:** University Course
- **Direct Link:** https://pdos.csail.mit.edu/6.824/
- **Difficulty:** Advanced
- **Estimated Time:** 40 hours

- **Why Recommended:** A famous course where you build a real distributed system in labs.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: كورس شهير بتبني فيه نظام موزّع حقيقي في معامل.

- **What to Study From It:** RPC, consensus, replication, sharding and fault tolerance.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: الاستدعاء عن بُعد والإجماع والنسخ والتقسيم وتحمّل الأعطال.

**Practice Platform (منصة التمرين العملي)**

- **Resource Name:** Jepsen - Distributed Systems Testing
- **Resource Type:** Practice Platform
- **Direct Link:** https://jepsen.io/
- **Difficulty:** Advanced
- **Estimated Time:** 20 hours

- **Why Recommended:** Real analyses of how databases behave under failure.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: تحليلات حقيقية لسلوك قواعد البيانات تحت الفشل.

- **What to Study From It:** Consistency, availability and partition behaviour of real systems.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: الاتساق والتوافر وسلوك التقسيم في أنظمة حقيقية.

### AI302 — التعلّم العميق

**Primary Resource (المصدر الأساسي)**

- **Resource Name:** Deep Learning (Goodfellow, Bengio & Courville)
- **Resource Type:** Textbook
- **Direct Link:** https://www.deeplearningbook.org/
- **Difficulty:** Advanced
- **Estimated Time:** 45 hours

- **Why Recommended:** The authoritative free textbook on deep learning theory.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: الكتاب المرجعي المجاني في نظرية التعلّم العميق.

- **What to Study From It:** Neural networks, optimization, CNNs, RNNs and regularization.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: الشبكات العصبية والتحسين والشبكات الالتفافية والتكرارية والتنظيم.

**Optional Resource (المصدر الاختياري)**

- **Resource Name:** DeepLearning.AI - Deep Learning Specialization
- **Resource Type:** Online Course
- **Direct Link:** https://www.coursera.org/specializations/deep-learning
- **Difficulty:** Intermediate
- **Estimated Time:** 45 hours

- **Why Recommended:** A hands-on specialization by Andrew Ng with practical assignments.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: تخصص عملي من أندرو نج بواجبات تطبيقية.

- **What to Study From It:** CNNs, sequence models, hyperparameter tuning and structuring ML projects.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: الشبكات الالتفافية ونماذج المتسلسلات وضبط المعاملات وهيكلة مشروعات تعلّم الآلة.

**Practice Platform (منصة التمرين العملي)**

- **Resource Name:** PyTorch Tutorials
- **Resource Type:** Practice Platform
- **Direct Link:** https://pytorch.org/tutorials/
- **Difficulty:** Intermediate
- **Estimated Time:** 30 hours

- **Why Recommended:** Official tutorials to build and train real networks step by step.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: دروس رسمية لبناء وتدريب شبكات حقيقية خطوة بخطوة.

- **What to Study From It:** Tensors, autograd, CNNs, RNNs and training loops.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: التنسورات والاشتقاق التلقائي والشبكات الالتفافية والتكرارية وحلقات التدريب.

### CS322 — أمن المعلومات والتشفير

**Primary Resource (المصدر الأساسي)**

- **Resource Name:** Cryptography and Network Security (Stallings)
- **Resource Type:** Textbook
- **Direct Link:** https://www.pearson.com/en-us/subject-catalog/p/cryptography-and-network-security-principles-and-practice/P200000005949
- **Difficulty:** Advanced
- **Estimated Time:** 40 hours

- **Why Recommended:** A thorough textbook covering cryptography and its network use.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: كتاب شامل بيغطي التشفير واستخدامه في الشبكات.

- **What to Study From It:** Ciphers, hashing, key exchange, authentication and protocols.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: أنظمة التشفير والتقطيع وتبادل المفاتيح والمصادقة والبروتوكولات.

**Optional Resource (المصدر الاختياري)**

- **Resource Name:** Crypto101
- **Resource Type:** Open Book
- **Direct Link:** https://www.crypto101.io/
- **Difficulty:** Intermediate
- **Estimated Time:** 20 hours

- **Why Recommended:** A free, friendly introduction to cryptography for developers.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: مقدمة مجانية وودّية في التشفير للمطورين.

- **What to Study From It:** Symmetric and asymmetric crypto, hashes and TLS basics.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: التشفير المتماثل وغير المتماثل والتقطيع وأساسيات TLS.

**Practice Platform (منصة التمرين العملي)**

- **Resource Name:** Cryptohack
- **Resource Type:** Practice Platform
- **Direct Link:** https://cryptohack.org/
- **Difficulty:** Intermediate to Advanced
- **Estimated Time:** 30 hours

- **Why Recommended:** Hands-on cryptography challenges that build real skill.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: تحديات تشفير عملية بتبني مهارة حقيقية.

- **What to Study From It:** Encoding, RSA, block ciphers and protocol attacks.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: الترميز و RSA وتشفير الكتل وهجمات البروتوكولات.

### CS323 — معمارية البرمجيات وأنماط التصميم

**Primary Resource (المصدر الأساسي)**

- **Resource Name:** Software Architecture in Practice (Bass, Clements & Kazman)
- **Resource Type:** Textbook
- **Direct Link:** https://www.sei.cmu.edu/library/software-architecture-in-practice-fourth-edition/
- **Difficulty:** Advanced
- **Estimated Time:** 35 hours

- **Why Recommended:** The definitive guide to architecture and quality attributes.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: الدليل المرجعي للمعمارية وخصائص الجودة.

- **What to Study From It:** Quality attributes, tactics, patterns and architecture evaluation.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: خصائص الجودة والتكتيكات والأنماط وتقييم المعمارية.

**Optional Resource (المصدر الاختياري)**

- **Resource Name:** Microservices.io Patterns
- **Resource Type:** Online Resource
- **Direct Link:** https://microservices.io/patterns/
- **Difficulty:** Intermediate
- **Estimated Time:** 15 hours

- **Why Recommended:** A catalogue of microservice patterns with trade-offs explained.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: كتالوج أنماط الخدمات المصغّرة بمقايضات موضّحة.

- **What to Study From It:** Decomposition, data management, deployment and observability patterns.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: أنماط التفكيك وإدارة البيانات والنشر والمراقبة.

**Practice Platform (منصة التمرين العملي)**

- **Resource Name:** C4 Model for Architecture Diagrams
- **Resource Type:** Practice Tool
- **Direct Link:** https://c4model.com/
- **Difficulty:** Intermediate
- **Estimated Time:** 10 hours

- **Why Recommended:** A simple, widely used way to document architecture at four levels.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: طريقة بسيطة ومستخدمة على نطاق واسع لتوثيق المعمارية على أربع مستويات.

- **What to Study From It:** Context, container, component and code diagrams.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: مخططات السياق والحاوية والمكوّن والكود.

### CS324 — الحوسبة السحابية

**Primary Resource (المصدر الأساسي)**

- **Resource Name:** AWS Cloud Practitioner Essentials
- **Resource Type:** Official Course
- **Direct Link:** https://aws.amazon.com/training/digital/aws-cloud-practitioner-essentials/
- **Difficulty:** Beginner
- **Estimated Time:** 20 hours

- **Why Recommended:** The official foundation course for cloud concepts and AWS services.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: الكورس التأسيسي الرسمي لمفاهيم السحابة وخدمات AWS.

- **What to Study From It:** Cloud concepts, core services, security and pricing.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: مفاهيم السحابة والخدمات الأساسية والأمن والتسعير.

**Optional Resource (المصدر الاختياري)**

- **Resource Name:** Google Cloud Digital Leader
- **Resource Type:** Official Course
- **Direct Link:** https://cloud.google.com/learn/certification/cloud-digital-leader
- **Difficulty:** Beginner
- **Estimated Time:** 18 hours

- **Why Recommended:** A vendor-neutral-ish introduction to cloud value and services.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: مقدمة شبه محايدة لقيمة السحابة وخدماتها.

- **What to Study From It:** Cloud transformation, data, AI and infrastructure options.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: التحول السحابي والبيانات والذكاء الاصطناعي وخيارات البنية التحتية.

**Practice Platform (منصة التمرين العملي)**

- **Resource Name:** AWS Skill Builder Labs
- **Resource Type:** Practice Platform
- **Direct Link:** https://skillbuilder.aws/
- **Difficulty:** Beginner to Intermediate
- **Estimated Time:** 25 hours

- **Why Recommended:** Hands-on labs where you launch and configure real cloud resources.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: معامل عملية بتطلق وتضبط موارد سحابية حقيقية.

- **What to Study From It:** Compute, storage, networking and serverless labs.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: معامل الحوسبة والتخزين والشبكات وبلا خوادم.

### ELEC-DS — اختياري: علم البيانات والبيانات الضخمة

**Primary Resource (المصدر الأساسي)**

- **Resource Name:** Python for Data Analysis (McKinney)
- **Resource Type:** Textbook
- **Direct Link:** https://wesmckinney.com/book/
- **Difficulty:** Intermediate
- **Estimated Time:** 30 hours

- **Why Recommended:** The definitive guide to pandas and data analysis in Python.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: الدليل المرجعي لبانداس وتحليل البيانات في بايثون.

- **What to Study From It:** NumPy, pandas, data wrangling and analysis workflows.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: نمباي وبانداس وتنظيم البيانات وسير عمل التحليل.

**Optional Resource (المصدر الاختياري)**

- **Resource Name:** Spark: The Definitive Guide
- **Resource Type:** Textbook
- **Direct Link:** https://www.oreilly.com/library/view/spark-the-definitive/9781491912201/
- **Difficulty:** Advanced
- **Estimated Time:** 35 hours

- **Why Recommended:** A complete guide to large-scale data processing with Spark.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: دليل شامل لمعالجة البيانات على نطاق واسع بـ Spark.

- **What to Study From It:** RDDs, DataFrames, SQL, streaming and tuning.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه:  RDDs و DataFrames و SQL والتدفق والضبط.

**Practice Platform (منصة التمرين العملي)**

- **Resource Name:** Kaggle Datasets and Notebooks
- **Resource Type:** Practice Platform
- **Direct Link:** https://www.kaggle.com/datasets
- **Difficulty:** Intermediate
- **Estimated Time:** 25 hours

- **Why Recommended:** Real datasets and notebooks to practise end-to-end analysis.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: مجموعات بيانات ودفاتر حقيقية للتمرين على التحليل من الأول للآخر.

- **What to Study From It:** Data cleaning, EDA and reporting on real datasets.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: تنظيف البيانات والتحليل الاستكشافي والتقارير على بيانات حقيقية.


---

## End of Lesson (نهاية الدرس)

### Lesson Summary (ملخص الدرس)

This week covered the following topics across the semester's courses: CS321: Synchronization and Logical Clocks; AI302: Optimization for Deep Learning; CS322: Key Management and Exchange; CS323: Event-Driven Architecture; CS324: Compute Services and Auto-Scaling; ELEC-DS: Big Data Concepts and the 5 Vs. Each topic opened with a bilingual definition, then explained what it is, why it exists, why it matters, where it is used, its advantages and limits, best practices and common mistakes, followed by a practical example and exercises.

**Egyptian Arabic (اللهجة المصرية):**

الأسبوع ده غطّى المواضيع دي في مقررات الفصل: CS321: التزامن والساعات المنطقية؛ AI302: التحسين للتعلّم العميق؛ CS322: إدارة المفاتيح وتبادلها؛ CS323: المعمارية القائمة على الأحداث؛ CS324: خدمات الحوسبة والتحجيم التلقائي؛ ELEC-DS: مفاهيم البيانات الضخمة ومحدداتها الخمسة. كل موضوع بدأ بتعريف ثنائي اللغة، وبعدين شرح يعني إيه وليه موجود وليه مهم وبنستخدمه فين، ومميزاته وحدوده وأحسن الممارسات والأخطاء الشائعة، وبعدين مثال عملي وتمارين.

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

Next week continues the semester's teaching schedule.

**Egyptian Arabic (اللهجة المصرية):**

الأسبوع الجاي بيكمل جدول التدريس.

### Important Terms (مصطلحات مهمة)

#### Replication (النسخ المتماثل)
English Definition: Keeping copies of data on several nodes.
Egyptian Arabic Definition: الاحتفاظ بنسخ من البيانات على عُقد كتير.

#### Consistency (الاتساق)
English Definition: Guarantees about the values read across nodes.
Egyptian Arabic Definition: ضمانات بخصوص القيم المقروءة بين العُقد.

#### Latency (زمن الاستجابة)
English Definition: The time a request takes to complete.
Egyptian Arabic Definition: الوقت اللي الطلب بياخده ليكتمل.

#### Fault Tolerance (تحمّل الأعطال)
English Definition: Continuing to work when parts fail.
Egyptian Arabic Definition: الاستمرار في الشغل لما أجزاء تفشل.

#### Consensus (الإجماع)
English Definition: Agreement among nodes on a value.
Egyptian Arabic Definition: اتفاق العُقد على قيمة.


---

[الدرس السابق: week-05.md](week-05.md) · [رجوع لفصل 6](README.md) · [الدرس الجاي: week-07.md](week-07.md)