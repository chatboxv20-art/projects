# الأسبوع 14 — الفصل 7

> الدرس ده بيغطّي موضوع واحد في كل مقرر من مقررات الفصل، وكل الشرح مكتوب بالعامية المصرية مع البلوك الإنجليزي الكامل جنبه.

**المقررات اللي في الدرس ده:** AI401 (معالجة اللغات الطبيعية)، AI402 (الرؤية بالحاسب)، CS411 (قواعد البيانات المتقدمة والبيانات الضخمة)، CS412 (اختبار البرمجيات وضمان الجودة)، CS413 (مشروع التخرج 1)، ELEC-CY (اختياري: الأمن السيبراني)

---

# القسم الأول: معالجة اللغات الطبيعية (AI401)

## Large Language Models and an NLP Project (النماذج اللغوية الضخمة ومشروع معالجة لغات)

Large Language Models and an NLP Project (النماذج اللغوية الضخمة ومشروع معالجة لغات)
English Definition: Large Language Models and an NLP Project is a core topic in Natural Language Processing. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: النماذج اللغوية الضخمة ومشروع معالجة لغات موضوع أساسي في معالجة اللغات الطبيعية. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Large Language Models and an NLP Project** is the focus of this lesson. Natural language processing enables computers to understand and generate human language, from tokenization to transformers and large language models.

**Egyptian Arabic (اللهجة المصرية):**

**النماذج اللغوية الضخمة ومشروع معالجة لغات** هو محور الدرس ده. معالجة اللغات الطبيعية بتمكّن الحاسب من فهم وتوليد لغة الإنسان، من التقطيع للمحوّلات والنماذج اللغوية الضخمة.

### Why It Exists (ليه موجود)

Text is the largest source of human knowledge, and language interfaces are becoming the main way we use computers. Without a clear grasp of Large Language Models and an NLP Project, the rest of Natural Language Processing has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

النص أكبر مصدر لمعرفة الإنسان، والواجهات اللغوية بقت الطريقة الأساسية لاستخدام الحاسبات. ومن غير إدراك واضح لموضوع النماذج اللغوية الضخمة ومشروع معالجة لغات، باقي معالجة اللغات الطبيعية ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Large Language Models and an NLP Project is where the theory of Natural Language Processing meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع النماذج اللغوية الضخمة ومشروع معالجة لغات هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

### Where It Is Used (بنستخدمه فين)

- Chatbots and assistants
- Search and question answering
- Machine translation
- Sentiment and text analytics
- Document understanding

**Egyptian Arabic (اللهجة المصرية):**

- روبوتات المحادثة والمساعدين
- البحث والإجابة على الأسئلة
- الترجمة الآلية
- تحليل المشاعر والنصوص
- فهم المستندات

### Real-World Usage and Relevance in the Field (الاستخدام والملاءمة في المجال)

When a search engine answers a question directly, an NLP model has read and understood the query and the documents.

**Egyptian Arabic (اللهجة المصرية):**

لما محرّك بحث يجاوب على سؤال مباشرة، نموذج معالجة لغات قرا وفهم الاستعلام والمستندات.

### Advantages (المميزات)

- Handles unstructured text at scale
- Powers modern assistants and search
- Transfer learning works with little data
- Multilingual potential

**Egyptian Arabic (اللهجة المصرية):**

- بتتعامل مع النص غير المنظّم على نطاق واسع
- بتشغّل المساعدين والبحث الحديثين
- التعلّم بالنقل بيشتغل ببيانات قليلة
- إمكانات متعددة اللغات

### Limitations (الحدود)

- Language is ambiguous
- Needs large corpora
- Models can hallucinate
- Bias and toxicity risks

**Egyptian Arabic (اللهجة المصرية):**

- اللغة غامضة
- محتاجة مدوّنات نصية كبيرة
- النماذج ممكن تتوهم
- مخاطر التحيّز والسموم

### Best Practices (أحسن الممارسات)

- Preprocess and normalize text carefully
- Use pretrained models and fine-tune
- Evaluate with task-specific metrics
- Guard against bias and misuse

**Egyptian Arabic (اللهجة المصرية):**

- عالج النص وطبّعه بعناية
- استخدم نماذج مدربة مسبقًا واضبطها
- قيّم بمقاييس خاصة بالمهمة
- احترس من التحيّز وإساءة الاستخدام

### Common Mistakes (الأخطاء الشائعة)

- Ignoring tokenization differences
- Evaluating only on accuracy
- Training from scratch when transfer learning works
- Overlooking language-specific issues

**Egyptian Arabic (اللهجة المصرية):**

- تجاهل اختلافات التقطيع
- التقييم بالدقة بس
- التدريب من الصفر لما التعلّم بالنقل بيشتغل
- إغفال قضايا اللغة المحددة

### Practical Example (مثال عملي)

A sentiment model splits a review into tokens, embeds them as vectors, and a classifier predicts positive or negative.

**Egyptian Arabic (اللهجة المصرية):**

نموذج مشاعر بيقسّم مراجعة لرموز، ويمثلها كمتجهات، ومصنّف بيتنبأ إيجابي أو سلبي.

### Hands-On Exercise (تمرين عملي بإيدك)

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Large Language Models and an NLP Project, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نطام صغير تعرفه. اكتب: (1) الموقف في النماذج اللغوية الضخمة ومشروع معالجة لغات، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Large Language Models and an NLP Project in one sentence of your own words.
2. Give two situations where Large Language Models and an NLP Project changes a technical decision.
3. Name one limitation of Large Language Models and an NLP Project and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف النماذج اللغوية الضخمة ومشروع معالجة لغات في جملة واحدة بكلامك.
2. ادي موقفين النماذج اللغوية الضخمة ومشروع معالجة لغات بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود النماذج اللغوية الضخمة ومشروع معالجة لغات واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Large Language Models and an NLP Project? (a) a formality with no use (b) a working tool inside Natural Language Processing (c) an unrelated subject.
Q2. True or false: Large Language Models and an NLP Project has no limitations.
Q3. In one line, why does Large Language Models and an NLP Project matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـالنماذج اللغوية الضخمة ومشروع معالجة لغات؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه معالجة اللغات الطبيعية (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: النماذج اللغوية الضخمة ومشروع معالجة لغات مالوش حدود.
س3. في سطر واحد، ليه النماذج اللغوية الضخمة ومشروع معالجة لغات مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Natural Language Processing.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه معالجة اللغات الطبيعية.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Large Language Models and an NLP Project to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها النماذج اللغوية الضخمة ومشروع معالجة لغات على برنامج أو نطام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Large Language Models and an NLP Project until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف النماذج اللغوية الضخمة ومشروع معالجة لغات تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الثاني: الرؤية بالحاسب (AI402)

## Vision Applications and a Project (تطبيقات الرؤية ومشروع)

Vision Applications and a Project (تطبيقات الرؤية ومشروع)
English Definition: Vision Applications and a Project is a core topic in Computer Vision. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: تطبيقات الرؤية ومشروع موضوع أساسي في الرؤية بالحاسب. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Vision Applications and a Project** is the focus of this lesson. Computer vision lets computers extract meaning from images and video using filtering, features, geometry and deep networks.

**Egyptian Arabic (اللهجة المصرية):**

**تطبيقات الرؤية ومشروع** هو محور الدرس ده. الرؤية بالحاسب بتخلي الحاسبات تستخرج المعنى من الصور والفيديو باستخدام التصفية والخصائص والهندسة والشبكات العميقة.

### Why It Exists (ليه موجود)

Cameras are everywhere, and vision powers safety, medicine, autonomy and manufacturing. Without a clear grasp of Vision Applications and a Project, the rest of Computer Vision has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

الكاميرات في كل مكان، والرؤية بتشغّل السلامة والطب والاستقلالية والتصنيع. ومن غير إدراك واضح لموضوع تطبيقات الرؤية ومشروع، باقي الرؤية بالحاسب ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Vision Applications and a Project is where the theory of Computer Vision meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع تطبيقات الرؤية ومشروع هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

### Where It Is Used (بنستخدمه فين)

- Face and object recognition
- Autonomous vehicles
- Medical imaging
- Industrial inspection
- Augmented reality

**Egyptian Arabic (اللهجة المصرية):**

- التعرّف على الوجوه والأجسام
- العربات ذاتية القيادة
- التصوير الطبي
- الفحص الصناعي
- الواقع المعزّز

### Real-World Usage and Relevance in the Field (الاستخدام والملاءمة في المجال)

A phone unlocks by recognizing your face: a vision model detects the face, aligns it and verifies identity in milliseconds.

**Egyptian Arabic (اللهجة المصرية):**

الموبايل بيتفتح بالتعرّف على وشك: نموذج رؤية بيكتشف الوش ويحاذيه ويتحقق من الهوية في أجزاء من الثانية.

### Advantages (المميزات)

- Automates visual inspection
- Works at scale and speed
- Complements human perception
- Rich deep learning tools

**Egyptian Arabic (اللهجة المصرية):**

- بتأتمت الفحص البصري
- بتشتغل على نطاق وسرعة
- بتكمّل الإدراك البشري
- أدوات تعلّم عميق غنية

### Limitations (الحدود)

- Sensitive to lighting and angle
- Needs large labelled datasets
- Privacy concerns
- Adversarial vulnerability

**Egyptian Arabic (اللهجة المصرية):**

- حسّاسة للإضاءة والزاوية
- محتاجة مجموعات بيانات موسومة كبيرة
- مخاوف خصوصية
- قابلية للهجوم التضليلي

### Best Practices (أحسن الممارسات)

- Augment data for robustness
- Use pretrained backbones
- Evaluate with the right metrics
- Consider privacy and consent

**Egyptian Arabic (اللهجة المصرية):**

- عزّز البيانات للمتانة
- استخدم شبكات أساس مدربة مسبقًا
- قيّم بالمقاييس الصحيحة
- راعي الخصوصية والموافقة

### Common Mistakes (الأخطاء الشائعة)

- Ignoring class imbalance
- Evaluating detection with accuracy alone
- Assuming fixed lighting
- Overlooking data privacy

**Egyptian Arabic (اللهجة المصرية):**

- تجاهل اختلال الفئات
- تقييم الكشف بالدقة بس
- افتراض إضاءة ثابتة
- إغفال خصوصية البيانات

### Practical Example (مثال عملي)

An object detector draws boxes around cars and pedestrians in each video frame, using a CNN to propose and classify regions.

**Egyptian Arabic (اللهجة المصرية):**

كاشف أجسام بيرسم مستطيلات حول العربيات والمشاة في كل إطار، باستخدام شبكة التفافية لتقترح وتصنّف المناطق.

### Hands-On Exercise (تمرين عملي بإيدك)

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Vision Applications and a Project, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نطام صغير تعرفه. اكتب: (1) الموقف في تطبيقات الرؤية ومشروع، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Vision Applications and a Project in one sentence of your own words.
2. Give two situations where Vision Applications and a Project changes a technical decision.
3. Name one limitation of Vision Applications and a Project and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف تطبيقات الرؤية ومشروع في جملة واحدة بكلامك.
2. ادي موقفين تطبيقات الرؤية ومشروع بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود تطبيقات الرؤية ومشروع واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Vision Applications and a Project? (a) a formality with no use (b) a working tool inside Computer Vision (c) an unrelated subject.
Q2. True or false: Vision Applications and a Project has no limitations.
Q3. In one line, why does Vision Applications and a Project matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـتطبيقات الرؤية ومشروع؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه الرؤية بالحاسب (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: تطبيقات الرؤية ومشروع مالوش حدود.
س3. في سطر واحد، ليه تطبيقات الرؤية ومشروع مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Computer Vision.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه الرؤية بالحاسب.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Vision Applications and a Project to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها تطبيقات الرؤية ومشروع على برنامج أو نطام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Vision Applications and a Project until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف تطبيقات الرؤية ومشروع تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الثالث: قواعد البيانات المتقدمة والبيانات الضخمة (CS411)

## Modern Data Architecture Case Study (دراسة حالة معمارية بيانات حديثة)

Modern Data Architecture Case Study (دراسة حالة معمارية بيانات حديثة)
English Definition: Modern Data Architecture Case Study is a core topic in Database Systems. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: دراسة حالة معمارية بيانات حديثة موضوع أساسي في نظم قواعد البيانات. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Modern Data Architecture Case Study** is the focus of this lesson. Database systems store, organize and query large amounts of structured data using the relational model, SQL, transactions and indexing.

**Egyptian Arabic (اللهجة المصرية):**

**دراسة حالة معمارية بيانات حديثة** هو محور الدرس ده. نظم قواعد البيانات بتخزّن وتنظّم وتستعلم عن كميات كبيرة من البيانات المنظّمة باستخدام النموذج العلائقي و SQL والمعاملات والفهرسة.

### Why It Exists (ليه موجود)

Almost every application needs durable, consistent, concurrent access to data. Without a clear grasp of Modern Data Architecture Case Study, the rest of Database Systems has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

تقريبًا كل تطبيق محتاج وصول دائم ومتسق ومتزامن للبيانات. ومن غير إدراك واضح لموضوع دراسة حالة معمارية بيانات حديثة، باقي نظم قواعد البيانات ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Modern Data Architecture Case Study is where the theory of Database Systems meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع دراسة حالة معمارية بيانات حديثة هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

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

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Modern Data Architecture Case Study, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نطام صغير تعرفه. اكتب: (1) الموقف في دراسة حالة معمارية بيانات حديثة، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Modern Data Architecture Case Study in one sentence of your own words.
2. Give two situations where Modern Data Architecture Case Study changes a technical decision.
3. Name one limitation of Modern Data Architecture Case Study and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف دراسة حالة معمارية بيانات حديثة في جملة واحدة بكلامك.
2. ادي موقفين دراسة حالة معمارية بيانات حديثة بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود دراسة حالة معمارية بيانات حديثة واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Modern Data Architecture Case Study? (a) a formality with no use (b) a working tool inside Database Systems (c) an unrelated subject.
Q2. True or false: Modern Data Architecture Case Study has no limitations.
Q3. In one line, why does Modern Data Architecture Case Study matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـدراسة حالة معمارية بيانات حديثة؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه نظم قواعد البيانات (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: دراسة حالة معمارية بيانات حديثة مالوش حدود.
س3. في سطر واحد، ليه دراسة حالة معمارية بيانات حديثة مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Database Systems.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه نظم قواعد البيانات.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Modern Data Architecture Case Study to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها دراسة حالة معمارية بيانات حديثة على برنامج أو نطام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Modern Data Architecture Case Study until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف دراسة حالة معمارية بيانات حديثة تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الرابع: اختبار البرمجيات وضمان الجودة (CS412)

## Testing Project and Continuous Quality (مشروع اختبار والجودة المستمرة)

Testing Project and Continuous Quality (مشروع اختبار والجودة المستمرة)
English Definition: Testing Project and Continuous Quality is a core topic in Software Engineering. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: مشروع اختبار والجودة المستمرة موضوع أساسي في هندسة البرمجيات. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Testing Project and Continuous Quality** is the focus of this lesson. Software engineering applies engineering discipline to building software: requirements, design, construction, testing and maintenance at scale.

**Egyptian Arabic (اللهجة المصرية):**

**مشروع اختبار والجودة المستمرة** هو محور الدرس ده. هندسة البرمجيات بتطبّق الانضباط الهندسي على بناء البرمجيات: المتطلبات والتصميم والبناء والاختبار والصيانة على نطاق واسع.

### Why It Exists (ليه موجود)

Large software fails without process: unclear requirements and untested code cost the most. Without a clear grasp of Testing Project and Continuous Quality, the rest of Software Engineering has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

البرمجيات الكبيرة بتفشل من غير عملية: المتطلبات الغامضة والكود غير المختبر هما الأغلى. ومن غير إدراك واضح لموضوع مشروع اختبار والجودة المستمرة، باقي هندسة البرمجيات ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Testing Project and Continuous Quality is where the theory of Software Engineering meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع مشروع اختبار والجودة المستمرة هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

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

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Testing Project and Continuous Quality, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نطام صغير تعرفه. اكتب: (1) الموقف في مشروع اختبار والجودة المستمرة، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Testing Project and Continuous Quality in one sentence of your own words.
2. Give two situations where Testing Project and Continuous Quality changes a technical decision.
3. Name one limitation of Testing Project and Continuous Quality and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف مشروع اختبار والجودة المستمرة في جملة واحدة بكلامك.
2. ادي موقفين مشروع اختبار والجودة المستمرة بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود مشروع اختبار والجودة المستمرة واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Testing Project and Continuous Quality? (a) a formality with no use (b) a working tool inside Software Engineering (c) an unrelated subject.
Q2. True or false: Testing Project and Continuous Quality has no limitations.
Q3. In one line, why does Testing Project and Continuous Quality matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـمشروع اختبار والجودة المستمرة؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه هندسة البرمجيات (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: مشروع اختبار والجودة المستمرة مالوش حدود.
س3. في سطر واحد، ليه مشروع اختبار والجودة المستمرة مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Software Engineering.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه هندسة البرمجيات.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Testing Project and Continuous Quality to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها مشروع اختبار والجودة المستمرة على برنامج أو نطام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Testing Project and Continuous Quality until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف مشروع اختبار والجودة المستمرة تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الخامس: مشروع التخرج 1 (CS413)

## First Milestone Presentation and Demo (عرض وتسليم أول مرحلة)

First Milestone Presentation and Demo (عرض وتسليم أول مرحلة)
English Definition: First Milestone Presentation and Demo is a core topic in Graduation Project. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: عرض وتسليم أول مرحلة موضوع أساسي في مشروع التخرج. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**First Milestone Presentation and Demo** is the focus of this lesson. The graduation project is a year-long capstone where you take a real problem from idea to a working, tested and documented system.

**Egyptian Arabic (اللهجة المصرية):**

**عرض وتسليم أول مرحلة** هو محور الدرس ده. مشروع التخرج هو مشروع السنة الأخيرة اللي بتاخد فيه مشكلة حقيقية من الفكرة لنظام شغّال ومختبر وموثّق.

### Why It Exists (ليه موجود)

It integrates everything you learned and produces a portfolio piece employers and graduate schools value. Without a clear grasp of First Milestone Presentation and Demo, the rest of Graduation Project has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

بيدمج كل اللي اتعلمته وبيطلع قطعة في ملف أعمالك بتقيّمها جهات العمل والدراسات العليا. ومن غير إدراك واضح لموضوع عرض وتسليم أول مرحلة، باقي مشروع التخرج ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, First Milestone Presentation and Demo is where the theory of Graduation Project meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع عرض وتسليم أول مرحلة هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

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

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in First Milestone Presentation and Demo, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نطام صغير تعرفه. اكتب: (1) الموقف في عرض وتسليم أول مرحلة، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define First Milestone Presentation and Demo in one sentence of your own words.
2. Give two situations where First Milestone Presentation and Demo changes a technical decision.
3. Name one limitation of First Milestone Presentation and Demo and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف عرض وتسليم أول مرحلة في جملة واحدة بكلامك.
2. ادي موقفين عرض وتسليم أول مرحلة بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود عرض وتسليم أول مرحلة واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes First Milestone Presentation and Demo? (a) a formality with no use (b) a working tool inside Graduation Project (c) an unrelated subject.
Q2. True or false: First Milestone Presentation and Demo has no limitations.
Q3. In one line, why does First Milestone Presentation and Demo matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـعرض وتسليم أول مرحلة؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه مشروع التخرج (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: عرض وتسليم أول مرحلة مالوش حدود.
س3. في سطر واحد، ليه عرض وتسليم أول مرحلة مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Graduation Project.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه مشروع التخرج.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying First Milestone Presentation and Demo to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها عرض وتسليم أول مرحلة على برنامج أو نطام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of First Milestone Presentation and Demo until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف عرض وتسليم أول مرحلة تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم السادس: اختياري: الأمن السيبراني (ELEC-CY)

## Security Lab and Capture-the-Flag (معمل أمن ومسابقة التقاط الأعلام)

Security Lab and Capture-the-Flag (معمل أمن ومسابقة التقاط الأعلام)
English Definition: Security Lab and Capture-the-Flag is a core topic in Information Security and Cryptography. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: معمل أمن ومسابقة التقاط الأعلام موضوع أساسي في أمن المعلومات والتشفير. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Security Lab and Capture-the-Flag** is the focus of this lesson. Cryptography protects information using encryption, hashing, signatures and keys, while security engineering defends systems against attacks.

**Egyptian Arabic (اللهجة المصرية):**

**معمل أمن ومسابقة التقاط الأعلام** هو محور الدرس ده. التشفير بيحمي المعلومات باستخدام التعمية والتقطيع والتوقيعات والمفاتيح، وهندسة الأمن بتدافع عن الأنظمة ضد الهجمات.

### Why It Exists (ليه موجود)

Confidentiality, integrity and authenticity are essential for every system that handles valuable data. Without a clear grasp of Security Lab and Capture-the-Flag, the rest of Information Security and Cryptography has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

السرية والسلامة والأصالة أساسية لكل نظام بيتعامل مع بيانات قيّمة. ومن غير إدراك واضح لموضوع معمل أمن ومسابقة التقاط الأعلام، باقي أمن المعلومات والتشفير ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Security Lab and Capture-the-Flag is where the theory of Information Security and Cryptography meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع معمل أمن ومسابقة التقاط الأعلام هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

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

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Security Lab and Capture-the-Flag, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نطام صغير تعرفه. اكتب: (1) الموقف في معمل أمن ومسابقة التقاط الأعلام، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Security Lab and Capture-the-Flag in one sentence of your own words.
2. Give two situations where Security Lab and Capture-the-Flag changes a technical decision.
3. Name one limitation of Security Lab and Capture-the-Flag and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف معمل أمن ومسابقة التقاط الأعلام في جملة واحدة بكلامك.
2. ادي موقفين معمل أمن ومسابقة التقاط الأعلام بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود معمل أمن ومسابقة التقاط الأعلام واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Security Lab and Capture-the-Flag? (a) a formality with no use (b) a working tool inside Information Security and Cryptography (c) an unrelated subject.
Q2. True or false: Security Lab and Capture-the-Flag has no limitations.
Q3. In one line, why does Security Lab and Capture-the-Flag matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـمعمل أمن ومسابقة التقاط الأعلام؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه أمن المعلومات والتشفير (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: معمل أمن ومسابقة التقاط الأعلام مالوش حدود.
س3. في سطر واحد، ليه معمل أمن ومسابقة التقاط الأعلام مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Information Security and Cryptography.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه أمن المعلومات والتشفير.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Security Lab and Capture-the-Flag to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها معمل أمن ومسابقة التقاط الأعلام على برنامج أو نطام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Security Lab and Capture-the-Flag until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف معمل أمن ومسابقة التقاط الأعلام تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

## Learning Resources (المصادر الدراسية)

### AI401 — معالجة اللغات الطبيعية

**Primary Resource (المصدر الأساسي)**

- **Resource Name:** Speech and Language Processing (Jurafsky & Martin)
- **Resource Type:** Textbook
- **Direct Link:** https://web.stanford.edu/~jurafsky/slp3/
- **Difficulty:** Advanced
- **Estimated Time:** 40 hours

- **Why Recommended:** The standard, continuously updated NLP textbook.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: كتاب معالجة اللغات المعياري المحدّث باستمرار.

- **What to Study From It:** Tokenization, embeddings, sequence models, transformers and LLMs.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: التقطيع والتمثيلات ونماذج المتسلسلات والمحوّلات والنماذج الضخمة.

**Optional Resource (المصدر الاختياري)**

- **Resource Name:** Hugging Face NLP Course
- **Resource Type:** Online Course
- **Direct Link:** https://huggingface.co/learn/nlp-course
- **Difficulty:** Intermediate
- **Estimated Time:** 30 hours

- **Why Recommended:** Hands-on course using the transformers library on real tasks.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: كورس عملي بيستخدم مكتبة المحوّلات على مهام حقيقية.

- **What to Study From It:** Transformers, fine-tuning, tokenizers and pipelines.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: المحوّلات والضبط والتقطيع والخطوط الجاهزة.

**Practice Platform (منصة التمرين العملي)**

- **Resource Name:** Kaggle NLP Competitions
- **Resource Type:** Practice Platform
- **Direct Link:** https://www.kaggle.com/competitions
- **Difficulty:** Intermediate
- **Estimated Time:** 25 hours

- **Why Recommended:** Real text problems to practise classification and embeddings.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: مشكلات نصية حقيقية للتمرين على التصنيف والتمثيلات.

- **What to Study From It:** Text classification, sentiment and topic tasks.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: مهام تصنيف النصوص والمشاعر والمواضيع.

### AI402 — الرؤية بالحاسب

**Primary Resource (المصدر الأساسي)**

- **Resource Name:** Computer Vision: Algorithms and Applications (Szeliski)
- **Resource Type:** Open Textbook
- **Direct Link:** https://szeliski.org/Book/
- **Difficulty:** Advanced
- **Estimated Time:** 40 hours

- **Why Recommended:** A free, comprehensive textbook covering classical and deep vision.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: كتاب مجاني شامل بيغطي الرؤية الكلاسيكية والعميقة.

- **What to Study From It:** Filtering, features, geometry, recognition and deep learning.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: التصفية والخصائص والهندسة والتعرّف والتعلّم العميق.

**Optional Resource (المصدر الاختياري)**

- **Resource Name:** CS231n Convolutional Neural Networks for Visual Recognition
- **Resource Type:** University Course
- **Direct Link:** https://cs231n.stanford.edu/
- **Difficulty:** Advanced
- **Estimated Time:** 40 hours

- **Why Recommended:** The famous Stanford course on deep learning for vision.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: كورس ستانفورد الشهير في التعلّم العميق للرؤية.

- **What to Study From It:** CNNs, detection, segmentation and visualization.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: الشبكات الالتفافية والكشف والتقسيم والتصوير.

**Practice Platform (منصة التمرين العملي)**

- **Resource Name:** OpenCV Tutorials
- **Resource Type:** Practice Platform
- **Direct Link:** https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html
- **Difficulty:** Intermediate
- **Estimated Time:** 25 hours

- **Why Recommended:** Hands-on image processing and vision with the OpenCV library.

**Egyptian Arabic (اللهجة المصرية):**

- السبب إنه مرشّح: معالجة صور ورؤية عملية بمكتبة OpenCV.

- **What to Study From It:** Filtering, edges, features, contours and video processing.

**Egyptian Arabic (اللهجة المصرية):**

- اللي تذاكره منه: التصفية والحواف والخصائص والكنتورات ومعالجة الفيديو.

### CS411 — قواعد البيانات المتقدمة والبيانات الضخمة

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

### CS412 — اختبار البرمجيات وضمان الجودة

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

### CS413 — مشروع التخرج 1

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

### ELEC-CY — اختياري: الأمن السيبراني

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


---

## End of Lesson (نهاية الدرس)

### Lesson Summary (ملخص الدرس)

This week covered the following topics across the semester's courses: AI401: Large Language Models and an NLP Project; AI402: Vision Applications and a Project; CS411: Modern Data Architecture Case Study; CS412: Testing Project and Continuous Quality; CS413: First Milestone Presentation and Demo; ELEC-CY: Security Lab and Capture-the-Flag. Each topic opened with a bilingual definition, then explained what it is, why it exists, why it matters, where it is used, its advantages and limits, best practices and common mistakes, followed by a practical example and exercises.

**Egyptian Arabic (اللهجة المصرية):**

الأسبوع ده غطّى المواضيع دي في مقررات الفصل: AI401: النماذج اللغوية الضخمة ومشروع معالجة لغات؛ AI402: تطبيقات الرؤية ومشروع؛ CS411: دراسة حالة معمارية بيانات حديثة؛ CS412: مشروع اختبار والجودة المستمرة؛ CS413: عرض وتسليم أول مرحلة؛ ELEC-CY: معمل أمن ومسابقة التقاط الأعلام. كل موضوع بدأ بتعريف ثنائي اللغة، وبعدين شرح يعني إيه وليه موجود وليه مهم وبنستخدمه فين، ومميزاته وحدوده وأحسن الممارسات والأخطاء الشائعة، وبعدين مثال عملي وتمارين.

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

Next week is general revision for the final exam.

**Egyptian Arabic (اللهجة المصرية):**

الأسبوع الجاي مراجعة عامة استعدادًا للفاينل.

### Important Terms (مصطلحات مهمة)

#### Tokenization (التقطيع)
English Definition: Splitting text into tokens.
Egyptian Arabic Definition: تقسيم النص لرموز.

#### Embedding (تمثيل متجهي)
English Definition: A dense vector representing meaning.
Egyptian Arabic Definition: متجه كثيف بيمثّل المعنى.

#### Corpus (مدوّنة نصية)
English Definition: A large collection of text.
Egyptian Arabic Definition: تجميع كبير من النصوص.

#### Language Model (نموذج لغوي)
English Definition: A model that predicts text.
Egyptian Arabic Definition: نموذج بيتنبأ بالنص.

#### Transformer (محوّل)
English Definition: An attention-based neural architecture.
Egyptian Arabic Definition: معمارية عصبية قائمة على الانتباه.


---

[الدرس السابق: week-13.md](week-13.md) · [رجوع لفصل 7](README.md) · [الدرس الجاي: week-15.md](week-15.md)