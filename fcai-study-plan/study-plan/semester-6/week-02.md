# الأسبوع 2 — الفصل 6

> الدرس ده بيغطّي موضوع واحد في كل مقرر من مقررات الفصل، وكل الشرح مكتوب بالعامية المصرية مع البلوك الإنجليزي الكامل جنبه.

**المقررات اللي في الدرس ده:** CS321 (النظم الموزّعة)، AI302 (التعلّم العميق)، CS322 (أمن المعلومات والتشفير)، CS323 (معمارية البرمجيات وأنماط التصميم)، CS324 (الحوسبة السحابية)، ELEC-DS (اختياري: علم البيانات والبيانات الضخمة)

---

# القسم الأول: النظم الموزّعة (CS321)

## Distributed System Models and Architectures (نماذج النظم الموزّعة ومعمارياتها)

Distributed System Models and Architectures (نماذج النظم الموزّعة ومعمارياتها)
English Definition: Distributed System Models and Architectures is a core topic in Distributed Systems. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: نماذج النظم الموزّعة ومعمارياتها موضوع أساسي في النظم الموزّعة. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Distributed System Models and Architectures** is the focus of this lesson. Distributed systems run across many machines that coordinate over a network to appear as one coherent system.

**Egyptian Arabic (اللهجة المصرية):**

**نماذج النظم الموزّعة ومعمارياتها** هو محور الدرس ده. النظم الموزّعة بتشتغل على أجهزة كتير بتتنسّق عبر شبكة عشان تبان كنظام واحد متماسك.

### Why It Exists (ليه موجود)

Scale, fault tolerance and global reach require spreading work across many machines. Without a clear grasp of Distributed System Models and Architectures, the rest of Distributed Systems has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

النطاق الواسع وتحمّل الأعطال والانتشار العالمي بيحتاجوا توزيع الشغل على أجهزة كتير. ومن غير إدراك واضح لموضوع نماذج النظم الموزّعة ومعمارياتها، باقي النظم الموزّعة ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Distributed System Models and Architectures is where the theory of Distributed Systems meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع نماذج النظم الموزّعة ومعمارياتها هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

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

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Distributed System Models and Architectures, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في نماذج النظم الموزّعة ومعمارياتها، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Distributed System Models and Architectures in one sentence of your own words.
2. Give two situations where Distributed System Models and Architectures changes a technical decision.
3. Name one limitation of Distributed System Models and Architectures and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف نماذج النظم الموزّعة ومعمارياتها في جملة واحدة بكلامك.
2. ادي موقفين نماذج النظم الموزّعة ومعمارياتها بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود نماذج النظم الموزّعة ومعمارياتها واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Distributed System Models and Architectures? (a) a formality with no use (b) a working tool inside Distributed Systems (c) an unrelated subject.
Q2. True or false: Distributed System Models and Architectures has no limitations.
Q3. In one line, why does Distributed System Models and Architectures matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـنماذج النظم الموزّعة ومعمارياتها؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه النظم الموزّعة (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: نماذج النظم الموزّعة ومعمارياتها مالوش حدود.
س3. في سطر واحد، ليه نماذج النظم الموزّعة ومعمارياتها مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Distributed Systems.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه النظم الموزّعة.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Distributed System Models and Architectures to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها نماذج النظم الموزّعة ومعمارياتها على برنامج أو نظام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Distributed System Models and Architectures until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف نماذج النظم الموزّعة ومعمارياتها تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الثاني: التعلّم العميق (AI302)

## Neural Networks and Perceptrons (الشبكات العصبية والبيرسيبترون)

Neural Networks and Perceptrons (الشبكات العصبية والبيرسيبترون)
English Definition: Neural Networks and Perceptrons is a core topic in Deep Learning. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: الشبكات العصبية والبيرسيبترون موضوع أساسي في التعلّم العميق. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Neural Networks and Perceptrons** is the focus of this lesson. Deep learning uses multi-layer neural networks to learn representations from raw data like images, text and audio.

**Egyptian Arabic (اللهجة المصرية):**

**الشبكات العصبية والبيرسيبترون** هو محور الدرس ده. التعلّم العميق بيستخدم شبكات عصبية متعددة الطبقات عشان تتعلم تمثيلات من البيانات الخام زي الصور والنصوص والصوت.

### Why It Exists (ليه موجود)

Deep learning broke records in vision, speech and language and drives modern AI products. Without a clear grasp of Neural Networks and Perceptrons, the rest of Deep Learning has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

التعلّم العميق كسر أرقام قياسية في الرؤية والكلام واللغة وبيشغّل منتجات الذكاء الاصطناعي الحديثة. ومن غير إدراك واضح لموضوع الشبكات العصبية والبيرسيبترون، باقي التعلّم العميق ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Neural Networks and Perceptrons is where the theory of Deep Learning meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع الشبكات العصبية والبيرسيبترون هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

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

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Neural Networks and Perceptrons, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في الشبكات العصبية والبيرسيبترون، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Neural Networks and Perceptrons in one sentence of your own words.
2. Give two situations where Neural Networks and Perceptrons changes a technical decision.
3. Name one limitation of Neural Networks and Perceptrons and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف الشبكات العصبية والبيرسيبترون في جملة واحدة بكلامك.
2. ادي موقفين الشبكات العصبية والبيرسيبترون بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود الشبكات العصبية والبيرسيبترون واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Neural Networks and Perceptrons? (a) a formality with no use (b) a working tool inside Deep Learning (c) an unrelated subject.
Q2. True or false: Neural Networks and Perceptrons has no limitations.
Q3. In one line, why does Neural Networks and Perceptrons matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـالشبكات العصبية والبيرسيبترون؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه التعلّم العميق (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: الشبكات العصبية والبيرسيبترون مالوش حدود.
س3. في سطر واحد، ليه الشبكات العصبية والبيرسيبترون مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Deep Learning.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه التعلّم العميق.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Neural Networks and Perceptrons to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها الشبكات العصبية والبيرسيبترون على برنامج أو نظام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Neural Networks and Perceptrons until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف الشبكات العصبية والبيرسيبترون تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الثالث: أمن المعلومات والتشفير (CS322)

## Classical Cryptography (التشفير الكلاسيكي)

Classical Cryptography (التشفير الكلاسيكي)
English Definition: Classical Cryptography is a core topic in Information Security and Cryptography. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: التشفير الكلاسيكي موضوع أساسي في أمن المعلومات والتشفير. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Classical Cryptography** is the focus of this lesson. Cryptography protects information using encryption, hashing, signatures and keys, while security engineering defends systems against attacks.

**Egyptian Arabic (اللهجة المصرية):**

**التشفير الكلاسيكي** هو محور الدرس ده. التشفير بيحمي المعلومات باستخدام التعمية والتقطيع والتوقيعات والمفاتيح، وهندسة الأمن بتدافع عن الأنظمة ضد الهجمات.

### Why It Exists (ليه موجود)

Confidentiality, integrity and authenticity are essential for every system that handles valuable data. Without a clear grasp of Classical Cryptography, the rest of Information Security and Cryptography has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

السرية والسلامة والأصالة أساسية لكل نظام بيتعامل مع بيانات قيّمة. ومن غير إدراك واضح لموضوع التشفير الكلاسيكي، باقي أمن المعلومات والتشفير ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Classical Cryptography is where the theory of Information Security and Cryptography meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع التشفير الكلاسيكي هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

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

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Classical Cryptography, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في التشفير الكلاسيكي، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Classical Cryptography in one sentence of your own words.
2. Give two situations where Classical Cryptography changes a technical decision.
3. Name one limitation of Classical Cryptography and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف التشفير الكلاسيكي في جملة واحدة بكلامك.
2. ادي موقفين التشفير الكلاسيكي بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود التشفير الكلاسيكي واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Classical Cryptography? (a) a formality with no use (b) a working tool inside Information Security and Cryptography (c) an unrelated subject.
Q2. True or false: Classical Cryptography has no limitations.
Q3. In one line, why does Classical Cryptography matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـالتشفير الكلاسيكي؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه أمن المعلومات والتشفير (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: التشفير الكلاسيكي مالوش حدود.
س3. في سطر واحد، ليه التشفير الكلاسيكي مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Information Security and Cryptography.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه أمن المعلومات والتشفير.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Classical Cryptography to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها التشفير الكلاسيكي على برنامج أو نظام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Classical Cryptography until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف التشفير الكلاسيكي تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الرابع: معمارية البرمجيات وأنماط التصميم (CS323)

## Architectural Views and Documentation (وجهات النظر المعمارية وتوثيقها)

Architectural Views and Documentation (وجهات النظر المعمارية وتوثيقها)
English Definition: Architectural Views and Documentation is a core topic in Software Architecture and Design. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: وجهات النظر المعمارية وتوثيقها موضوع أساسي في معمارية البرمجيات والتصميم. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Architectural Views and Documentation** is the focus of this lesson. Software architecture defines the high-level structure of a system - components, their relationships and the quality attributes they must satisfy.

**Egyptian Arabic (اللهجة المصرية):**

**وجهات النظر المعمارية وتوثيقها** هو محور الدرس ده. معمارية البرمجيات بتحدد البنية عالية المستوى للنظام - المكوّنات وعلاقاتها وخصائص الجودة اللي لازم تحققها.

### Why It Exists (ليه موجود)

Architecture determines scalability, maintainability and cost long before code is written. Without a clear grasp of Architectural Views and Documentation, the rest of Software Architecture and Design has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

المعمارية بتحدد التوسّع والصيانة والتكلفة قبل ما يتكتب الكود بفترة طويلة. ومن غير إدراك واضح لموضوع وجهات النظر المعمارية وتوثيقها، باقي معمارية البرمجيات والتصميم ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Architectural Views and Documentation is where the theory of Software Architecture and Design meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع وجهات النظر المعمارية وتوثيقها هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

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

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Architectural Views and Documentation, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في وجهات النظر المعمارية وتوثيقها، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Architectural Views and Documentation in one sentence of your own words.
2. Give two situations where Architectural Views and Documentation changes a technical decision.
3. Name one limitation of Architectural Views and Documentation and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف وجهات النظر المعمارية وتوثيقها في جملة واحدة بكلامك.
2. ادي موقفين وجهات النظر المعمارية وتوثيقها بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود وجهات النظر المعمارية وتوثيقها واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Architectural Views and Documentation? (a) a formality with no use (b) a working tool inside Software Architecture and Design (c) an unrelated subject.
Q2. True or false: Architectural Views and Documentation has no limitations.
Q3. In one line, why does Architectural Views and Documentation matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـوجهات النظر المعمارية وتوثيقها؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه معمارية البرمجيات والتصميم (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: وجهات النظر المعمارية وتوثيقها مالوش حدود.
س3. في سطر واحد، ليه وجهات النظر المعمارية وتوثيقها مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Software Architecture and Design.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه معمارية البرمجيات والتصميم.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Architectural Views and Documentation to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها وجهات النظر المعمارية وتوثيقها على برنامج أو نظام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Architectural Views and Documentation until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف وجهات النظر المعمارية وتوثيقها تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الخامس: الحوسبة السحابية (CS324)

## Service Models: IaaS, PaaS, SaaS (نماذج الخدمة: IaaS و PaaS و SaaS)

Service Models: IaaS, PaaS, SaaS (نماذج الخدمة: IaaS و PaaS و SaaS)
English Definition: Service Models: IaaS, PaaS, SaaS is a core topic in Cloud Computing. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: نماذج الخدمة: IaaS و PaaS و SaaS موضوع أساسي في الحوسبة السحابية. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Service Models: IaaS, PaaS, SaaS** is the focus of this lesson. Cloud computing delivers computing resources - servers, storage, databases, services - on demand over the internet with pay-as-you-go pricing.

**Egyptian Arabic (اللهجة المصرية):**

**نماذج الخدمة: IaaS و PaaS و SaaS** هو محور الدرس ده. الحوسبة السحابية بتوفّر موارد الحوسبة - سيرفرات وتخزين وقواعد بيانات وخدمات - عند الطلب عبر الإنترنت بدفع حسب الاستخدام.

### Why It Exists (ليه موجود)

Cloud removes the need to buy and maintain hardware, letting teams scale instantly. Without a clear grasp of Service Models: IaaS, PaaS, SaaS, the rest of Cloud Computing has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

السحابة بتلغي الحاجة لشراء وصيانة العتاد، وبتخلي الفرق تتوسّع فورًا. ومن غير إدراك واضح لموضوع نماذج الخدمة: IaaS و PaaS و SaaS، باقي الحوسبة السحابية ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Service Models: IaaS, PaaS, SaaS is where the theory of Cloud Computing meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع نماذج الخدمة: IaaS و PaaS و SaaS هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

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

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Service Models: IaaS, PaaS, SaaS, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في نماذج الخدمة: IaaS و PaaS و SaaS، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Service Models: IaaS, PaaS, SaaS in one sentence of your own words.
2. Give two situations where Service Models: IaaS, PaaS, SaaS changes a technical decision.
3. Name one limitation of Service Models: IaaS, PaaS, SaaS and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف نماذج الخدمة: IaaS و PaaS و SaaS في جملة واحدة بكلامك.
2. ادي موقفين نماذج الخدمة: IaaS و PaaS و SaaS بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود نماذج الخدمة: IaaS و PaaS و SaaS واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Service Models: IaaS, PaaS, SaaS? (a) a formality with no use (b) a working tool inside Cloud Computing (c) an unrelated subject.
Q2. True or false: Service Models: IaaS, PaaS, SaaS has no limitations.
Q3. In one line, why does Service Models: IaaS, PaaS, SaaS matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـنماذج الخدمة: IaaS و PaaS و SaaS؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه الحوسبة السحابية (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: نماذج الخدمة: IaaS و PaaS و SaaS مالوش حدود.
س3. في سطر واحد، ليه نماذج الخدمة: IaaS و PaaS و SaaS مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Cloud Computing.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه الحوسبة السحابية.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Service Models: IaaS, PaaS, SaaS to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها نماذج الخدمة: IaaS و PaaS و SaaS على برنامج أو نظام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Service Models: IaaS, PaaS, SaaS until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف نماذج الخدمة: IaaS و PaaS و SaaS تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم السادس: اختياري: علم البيانات والبيانات الضخمة (ELEC-DS)

## Data Collection and Web Scraping (جمع البيانات وكشط الويب)

Data Collection and Web Scraping (جمع البيانات وكشط الويب)
English Definition: Data Collection and Web Scraping is a core topic in Data Science and Big Data. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: جمع البيانات وكشط الويب موضوع أساسي في علم البيانات والبيانات الضخمة. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Data Collection and Web Scraping** is the focus of this lesson. Data science extracts insight from data through collection, cleaning, analysis and modelling, while big data handles volumes too large for one machine.

**Egyptian Arabic (اللهجة المصرية):**

**جمع البيانات وكشط الويب** هو محور الدرس ده. علم البيانات بيستخرج رؤى من البيانات عبر الجمع والتنظيف والتحليل والنمذجة، والبيانات الضخمة بتتعامل مع أحجام أكبر من جهاز واحد.

### Why It Exists (ليه موجود)

Organizations collect huge data and need skills to turn it into decisions and products. Without a clear grasp of Data Collection and Web Scraping, the rest of Data Science and Big Data has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

المنظمات بتجمع بيانات ضخمة ومحتاجة مهارات تحوّلها لقرارات ومنتجات. ومن غير إدراك واضح لموضوع جمع البيانات وكشط الويب، باقي علم البيانات والبيانات الضخمة ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Data Collection and Web Scraping is where the theory of Data Science and Big Data meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع جمع البيانات وكشط الويب هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

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

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Data Collection and Web Scraping, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في جمع البيانات وكشط الويب، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Data Collection and Web Scraping in one sentence of your own words.
2. Give two situations where Data Collection and Web Scraping changes a technical decision.
3. Name one limitation of Data Collection and Web Scraping and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف جمع البيانات وكشط الويب في جملة واحدة بكلامك.
2. ادي موقفين جمع البيانات وكشط الويب بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود جمع البيانات وكشط الويب واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Data Collection and Web Scraping? (a) a formality with no use (b) a working tool inside Data Science and Big Data (c) an unrelated subject.
Q2. True or false: Data Collection and Web Scraping has no limitations.
Q3. In one line, why does Data Collection and Web Scraping matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـجمع البيانات وكشط الويب؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه علم البيانات والبيانات الضخمة (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: جمع البيانات وكشط الويب مالوش حدود.
س3. في سطر واحد، ليه جمع البيانات وكشط الويب مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Data Science and Big Data.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه علم البيانات والبيانات الضخمة.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Data Collection and Web Scraping to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها جمع البيانات وكشط الويب على برنامج أو نظام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Data Collection and Web Scraping until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف جمع البيانات وكشط الويب تاني لحد ما تقدر تقوله من غير ما تبص.
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

This week covered the following topics across the semester's courses: CS321: Distributed System Models and Architectures; AI302: Neural Networks and Perceptrons; CS322: Classical Cryptography; CS323: Architectural Views and Documentation; CS324: Service Models: IaaS, PaaS, SaaS; ELEC-DS: Data Collection and Web Scraping. Each topic opened with a bilingual definition, then explained what it is, why it exists, why it matters, where it is used, its advantages and limits, best practices and common mistakes, followed by a practical example and exercises.

**Egyptian Arabic (اللهجة المصرية):**

الأسبوع ده غطّى المواضيع دي في مقررات الفصل: CS321: نماذج النظم الموزّعة ومعمارياتها؛ AI302: الشبكات العصبية والبيرسيبترون؛ CS322: التشفير الكلاسيكي؛ CS323: وجهات النظر المعمارية وتوثيقها؛ CS324: نماذج الخدمة: IaaS و PaaS و SaaS؛ ELEC-DS: جمع البيانات وكشط الويب. كل موضوع بدأ بتعريف ثنائي اللغة، وبعدين شرح يعني إيه وليه موجود وليه مهم وبنستخدمه فين، ومميزاته وحدوده وأحسن الممارسات والأخطاء الشائعة، وبعدين مثال عملي وتمارين.

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

Next week continues with: CS321: Processes and Threads in Distributed Systems; AI302: Activation Functions and Forward Propagation; CS322: Symmetric Encryption and Block Ciphers; CS323: Quality Attributes and Trade-offs; CS324: Deployment Models and Providers; ELEC-DS: Data Cleaning and Preprocessing.

**Egyptian Arabic (اللهجة المصرية):**

الأسبوع الجاي بيكمل بـ: CS321: العمليات والخيوط في النظم الموزّعة؛ AI302: دوال التنشيط والانتشار الأمامي؛ CS322: التشفير المتماثل وتشفير الكتل؛ CS323: خصائص الجودة والمقايضات؛ CS324: نماذج النشر ومزوّدو الخدمة؛ ELEC-DS: تنظيف البيانات والمعالجة المسبقة.

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

[الدرس السابق: week-01.md](week-01.md) · [رجوع لفصل 6](README.md) · [الدرس الجاي: week-03.md](week-03.md)