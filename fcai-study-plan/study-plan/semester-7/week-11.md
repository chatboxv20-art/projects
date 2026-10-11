# الأسبوع 11 — الفصل 7

> الدرس ده بيغطّي موضوع واحد في كل مقرر من مقررات الفصل، وكل الشرح مكتوب بالعامية المصرية مع البلوك الإنجليزي الكامل جنبه.

**المقررات اللي في الدرس ده:** AI401 (معالجة اللغات الطبيعية)، AI402 (الرؤية بالحاسب)، CS411 (قواعد البيانات المتقدمة والبيانات الضخمة)، CS412 (اختبار البرمجيات وضمان الجودة)، CS413 (مشروع التخرج 1)، ELEC-CY (اختياري: الأمن السيبراني)

---

# القسم الأول: معالجة اللغات الطبيعية (AI401)

## Sentiment Analysis and Text Classification (تحليل المشاعر وتصنيف النصوص)

Sentiment Analysis and Text Classification (تحليل المشاعر وتصنيف النصوص)
English Definition: Sentiment Analysis and Text Classification is a core topic in Natural Language Processing. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: تحليل المشاعر وتصنيف النصوص موضوع أساسي في معالجة اللغات الطبيعية. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Sentiment Analysis and Text Classification** is the focus of this lesson. Natural language processing enables computers to understand and generate human language, from tokenization to transformers and large language models.

**Egyptian Arabic (اللهجة المصرية):**

**تحليل المشاعر وتصنيف النصوص** هو محور الدرس ده. معالجة اللغات الطبيعية بتمكّن الحاسب من فهم وتوليد لغة الإنسان، من التقطيع للمحوّلات والنماذج اللغوية الضخمة.

### Why It Exists (ليه موجود)

Text is the largest source of human knowledge, and language interfaces are becoming the main way we use computers. Without a clear grasp of Sentiment Analysis and Text Classification, the rest of Natural Language Processing has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

النص أكبر مصدر لمعرفة الإنسان، والواجهات اللغوية بقت الطريقة الأساسية لاستخدام الحاسبات. ومن غير إدراك واضح لموضوع تحليل المشاعر وتصنيف النصوص، باقي معالجة اللغات الطبيعية ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Sentiment Analysis and Text Classification is where the theory of Natural Language Processing meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع تحليل المشاعر وتصنيف النصوص هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

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

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Sentiment Analysis and Text Classification, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في تحليل المشاعر وتصنيف النصوص، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Sentiment Analysis and Text Classification in one sentence of your own words.
2. Give two situations where Sentiment Analysis and Text Classification changes a technical decision.
3. Name one limitation of Sentiment Analysis and Text Classification and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف تحليل المشاعر وتصنيف النصوص في جملة واحدة بكلامك.
2. ادي موقفين تحليل المشاعر وتصنيف النصوص بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود تحليل المشاعر وتصنيف النصوص واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Sentiment Analysis and Text Classification? (a) a formality with no use (b) a working tool inside Natural Language Processing (c) an unrelated subject.
Q2. True or false: Sentiment Analysis and Text Classification has no limitations.
Q3. In one line, why does Sentiment Analysis and Text Classification matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـتحليل المشاعر وتصنيف النصوص؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه معالجة اللغات الطبيعية (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: تحليل المشاعر وتصنيف النصوص مالوش حدود.
س3. في سطر واحد، ليه تحليل المشاعر وتصنيف النصوص مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Natural Language Processing.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه معالجة اللغات الطبيعية.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Sentiment Analysis and Text Classification to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها تحليل المشاعر وتصنيف النصوص على برنامج أو نظام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Sentiment Analysis and Text Classification until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف تحليل المشاعر وتصنيف النصوص تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الثاني: الرؤية بالحاسب (AI402)

## Object Detection (كشف الأجسام)

Object Detection (كشف الأجسام)
English Definition: Object Detection is a core topic in Computer Vision. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: كشف الأجسام موضوع أساسي في الرؤية بالحاسب. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Object Detection** is the focus of this lesson. Computer vision lets computers extract meaning from images and video using filtering, features, geometry and deep networks.

**Egyptian Arabic (اللهجة المصرية):**

**كشف الأجسام** هو محور الدرس ده. الرؤية بالحاسب بتخلي الحاسبات تستخرج المعنى من الصور والفيديو باستخدام التصفية والخصائص والهندسة والشبكات العميقة.

### Why It Exists (ليه موجود)

Cameras are everywhere, and vision powers safety, medicine, autonomy and manufacturing. Without a clear grasp of Object Detection, the rest of Computer Vision has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

الكاميرات في كل مكان، والرؤية بتشغّل السلامة والطب والاستقلالية والتصنيع. ومن غير إدراك واضح لموضوع كشف الأجسام، باقي الرؤية بالحاسب ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Object Detection is where the theory of Computer Vision meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع كشف الأجسام هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

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

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Object Detection, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في كشف الأجسام، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Object Detection in one sentence of your own words.
2. Give two situations where Object Detection changes a technical decision.
3. Name one limitation of Object Detection and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف كشف الأجسام في جملة واحدة بكلامك.
2. ادي موقفين كشف الأجسام بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود كشف الأجسام واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Object Detection? (a) a formality with no use (b) a working tool inside Computer Vision (c) an unrelated subject.
Q2. True or false: Object Detection has no limitations.
Q3. In one line, why does Object Detection matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـكشف الأجسام؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه الرؤية بالحاسب (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: كشف الأجسام مالوش حدود.
س3. في سطر واحد، ليه كشف الأجسام مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Computer Vision.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه الرؤية بالحاسب.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Object Detection to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها كشف الأجسام على برنامج أو نظام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Object Detection until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف كشف الأجسام تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الثالث: قواعد البيانات المتقدمة والبيانات الضخمة (CS411)

## NoSQL Databases and CAP (قواعد بيانات NoSQL ونظرية CAP)

NoSQL Databases and CAP (قواعد بيانات NoSQL ونظرية CAP)
English Definition: NoSQL Databases and CAP is a core topic in Database Systems. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: قواعد بيانات NoSQL ونظرية CAP موضوع أساسي في نظم قواعد البيانات. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**NoSQL Databases and CAP** is the focus of this lesson. Database systems store, organize and query large amounts of structured data using the relational model, SQL, transactions and indexing.

**Egyptian Arabic (اللهجة المصرية):**

**قواعد بيانات NoSQL ونظرية CAP** هو محور الدرس ده. نظم قواعد البيانات بتخزّن وتنظّم وتستعلم عن كميات كبيرة من البيانات المنظّمة باستخدام النموذج العلائقي و SQL والمعاملات والفهرسة.

### Why It Exists (ليه موجود)

Almost every application needs durable, consistent, concurrent access to data. Without a clear grasp of NoSQL Databases and CAP, the rest of Database Systems has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

تقريبًا كل تطبيق محتاج وصول دائم ومتسق ومتزامن للبيانات. ومن غير إدراك واضح لموضوع قواعد بيانات NoSQL ونظرية CAP، باقي نظم قواعد البيانات ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, NoSQL Databases and CAP is where the theory of Database Systems meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع قواعد بيانات NoSQL ونظرية CAP هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

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

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in NoSQL Databases and CAP, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في قواعد بيانات NoSQL ونظرية CAP، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define NoSQL Databases and CAP in one sentence of your own words.
2. Give two situations where NoSQL Databases and CAP changes a technical decision.
3. Name one limitation of NoSQL Databases and CAP and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف قواعد بيانات NoSQL ونظرية CAP في جملة واحدة بكلامك.
2. ادي موقفين قواعد بيانات NoSQL ونظرية CAP بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود قواعد بيانات NoSQL ونظرية CAP واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes NoSQL Databases and CAP? (a) a formality with no use (b) a working tool inside Database Systems (c) an unrelated subject.
Q2. True or false: NoSQL Databases and CAP has no limitations.
Q3. In one line, why does NoSQL Databases and CAP matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـقواعد بيانات NoSQL ونظرية CAP؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه نظم قواعد البيانات (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: قواعد بيانات NoSQL ونظرية CAP مالوش حدود.
س3. في سطر واحد، ليه قواعد بيانات NoSQL ونظرية CAP مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Database Systems.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه نظم قواعد البيانات.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying NoSQL Databases and CAP to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها قواعد بيانات NoSQL ونظرية CAP على برنامج أو نظام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of NoSQL Databases and CAP until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف قواعد بيانات NoSQL ونظرية CAP تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الرابع: اختبار البرمجيات وضمان الجودة (CS412)

## Automated Testing and Frameworks (الاختبار الآلي وأطر العمل)

Automated Testing and Frameworks (الاختبار الآلي وأطر العمل)
English Definition: Automated Testing and Frameworks is a core topic in Software Engineering. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: الاختبار الآلي وأطر العمل موضوع أساسي في هندسة البرمجيات. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Automated Testing and Frameworks** is the focus of this lesson. Software engineering applies engineering discipline to building software: requirements, design, construction, testing and maintenance at scale.

**Egyptian Arabic (اللهجة المصرية):**

**الاختبار الآلي وأطر العمل** هو محور الدرس ده. هندسة البرمجيات بتطبّق الانضباط الهندسي على بناء البرمجيات: المتطلبات والتصميم والبناء والاختبار والصيانة على نطاق واسع.

### Why It Exists (ليه موجود)

Large software fails without process: unclear requirements and untested code cost the most. Without a clear grasp of Automated Testing and Frameworks, the rest of Software Engineering has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

البرمجيات الكبيرة بتفشل من غير عملية: المتطلبات الغامضة والكود غير المختبر هما الأغلى. ومن غير إدراك واضح لموضوع الاختبار الآلي وأطر العمل، باقي هندسة البرمجيات ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Automated Testing and Frameworks is where the theory of Software Engineering meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع الاختبار الآلي وأطر العمل هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

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

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Automated Testing and Frameworks, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في الاختبار الآلي وأطر العمل، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Automated Testing and Frameworks in one sentence of your own words.
2. Give two situations where Automated Testing and Frameworks changes a technical decision.
3. Name one limitation of Automated Testing and Frameworks and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف الاختبار الآلي وأطر العمل في جملة واحدة بكلامك.
2. ادي موقفين الاختبار الآلي وأطر العمل بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود الاختبار الآلي وأطر العمل واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Automated Testing and Frameworks? (a) a formality with no use (b) a working tool inside Software Engineering (c) an unrelated subject.
Q2. True or false: Automated Testing and Frameworks has no limitations.
Q3. In one line, why does Automated Testing and Frameworks matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـالاختبار الآلي وأطر العمل؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه هندسة البرمجيات (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: الاختبار الآلي وأطر العمل مالوش حدود.
س3. في سطر واحد، ليه الاختبار الآلي وأطر العمل مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Software Engineering.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه هندسة البرمجيات.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Automated Testing and Frameworks to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها الاختبار الآلي وأطر العمل على برنامج أو نظام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Automated Testing and Frameworks until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف الاختبار الآلي وأطر العمل تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الخامس: مشروع التخرج 1 (CS413)

## Second Implementation Sprint (ثاني دورة تنفيذ)

Second Implementation Sprint (ثاني دورة تنفيذ)
English Definition: Second Implementation Sprint is a core topic in Graduation Project. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: ثاني دورة تنفيذ موضوع أساسي في مشروع التخرج. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Second Implementation Sprint** is the focus of this lesson. The graduation project is a year-long capstone where you take a real problem from idea to a working, tested and documented system.

**Egyptian Arabic (اللهجة المصرية):**

**ثاني دورة تنفيذ** هو محور الدرس ده. مشروع التخرج هو مشروع السنة الأخيرة اللي بتاخد فيه مشكلة حقيقية من الفكرة لنظام شغّال ومختبر وموثّق.

### Why It Exists (ليه موجود)

It integrates everything you learned and produces a portfolio piece employers and graduate schools value. Without a clear grasp of Second Implementation Sprint, the rest of Graduation Project has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

بيدمج كل اللي اتعلمته وبيطلع قطعة في ملف أعمالك بتقيّمها جهات العمل والدراسات العليا. ومن غير إدراك واضح لموضوع ثاني دورة تنفيذ، باقي مشروع التخرج ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Second Implementation Sprint is where the theory of Graduation Project meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع ثاني دورة تنفيذ هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

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

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Second Implementation Sprint, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في ثاني دورة تنفيذ، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Second Implementation Sprint in one sentence of your own words.
2. Give two situations where Second Implementation Sprint changes a technical decision.
3. Name one limitation of Second Implementation Sprint and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف ثاني دورة تنفيذ في جملة واحدة بكلامك.
2. ادي موقفين ثاني دورة تنفيذ بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود ثاني دورة تنفيذ واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Second Implementation Sprint? (a) a formality with no use (b) a working tool inside Graduation Project (c) an unrelated subject.
Q2. True or false: Second Implementation Sprint has no limitations.
Q3. In one line, why does Second Implementation Sprint matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـثاني دورة تنفيذ؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه مشروع التخرج (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: ثاني دورة تنفيذ مالوش حدود.
س3. في سطر واحد، ليه ثاني دورة تنفيذ مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Graduation Project.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه مشروع التخرج.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Second Implementation Sprint to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها ثاني دورة تنفيذ على برنامج أو نظام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Second Implementation Sprint until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف ثاني دورة تنفيذ تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم السادس: اختياري: الأمن السيبراني (ELEC-CY)

## Identity and Access Management (إدارة الهوية والوصول)

Identity and Access Management (إدارة الهوية والوصول)
English Definition: Identity and Access Management is a core topic in Information Security and Cryptography. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: إدارة الهوية والوصول موضوع أساسي في أمن المعلومات والتشفير. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Identity and Access Management** is the focus of this lesson. Cryptography protects information using encryption, hashing, signatures and keys, while security engineering defends systems against attacks.

**Egyptian Arabic (اللهجة المصرية):**

**إدارة الهوية والوصول** هو محور الدرس ده. التشفير بيحمي المعلومات باستخدام التعمية والتقطيع والتوقيعات والمفاتيح، وهندسة الأمن بتدافع عن الأنظمة ضد الهجمات.

### Why It Exists (ليه موجود)

Confidentiality, integrity and authenticity are essential for every system that handles valuable data. Without a clear grasp of Identity and Access Management, the rest of Information Security and Cryptography has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

السرية والسلامة والأصالة أساسية لكل نظام بيتعامل مع بيانات قيّمة. ومن غير إدراك واضح لموضوع إدارة الهوية والوصول، باقي أمن المعلومات والتشفير ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Identity and Access Management is where the theory of Information Security and Cryptography meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع إدارة الهوية والوصول هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

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

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Identity and Access Management, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في إدارة الهوية والوصول، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Identity and Access Management in one sentence of your own words.
2. Give two situations where Identity and Access Management changes a technical decision.
3. Name one limitation of Identity and Access Management and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف إدارة الهوية والوصول في جملة واحدة بكلامك.
2. ادي موقفين إدارة الهوية والوصول بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود إدارة الهوية والوصول واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Identity and Access Management? (a) a formality with no use (b) a working tool inside Information Security and Cryptography (c) an unrelated subject.
Q2. True or false: Identity and Access Management has no limitations.
Q3. In one line, why does Identity and Access Management matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـإدارة الهوية والوصول؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه أمن المعلومات والتشفير (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: إدارة الهوية والوصول مالوش حدود.
س3. في سطر واحد، ليه إدارة الهوية والوصول مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Information Security and Cryptography.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه أمن المعلومات والتشفير.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Identity and Access Management to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها إدارة الهوية والوصول على برنامج أو نظام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Identity and Access Management until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف إدارة الهوية والوصول تاني لحد ما تقدر تقوله من غير ما تبص.
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

This week covered the following topics across the semester's courses: AI401: Sentiment Analysis and Text Classification; AI402: Object Detection; CS411: NoSQL Databases and CAP; CS412: Automated Testing and Frameworks; CS413: Second Implementation Sprint; ELEC-CY: Identity and Access Management. Each topic opened with a bilingual definition, then explained what it is, why it exists, why it matters, where it is used, its advantages and limits, best practices and common mistakes, followed by a practical example and exercises.

**Egyptian Arabic (اللهجة المصرية):**

الأسبوع ده غطّى المواضيع دي في مقررات الفصل: AI401: تحليل المشاعر وتصنيف النصوص؛ AI402: كشف الأجسام؛ CS411: قواعد بيانات NoSQL ونظرية CAP؛ CS412: الاختبار الآلي وأطر العمل؛ CS413: ثاني دورة تنفيذ؛ ELEC-CY: إدارة الهوية والوصول. كل موضوع بدأ بتعريف ثنائي اللغة، وبعدين شرح يعني إيه وليه موجود وليه مهم وبنستخدمه فين، ومميزاته وحدوده وأحسن الممارسات والأخطاء الشائعة، وبعدين مثال عملي وتمارين.

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

Next week continues with: AI401: Sequence Models and Transformers for NLP; AI402: Image Segmentation; CS411: Big Data Processing Frameworks; CS412: Defect Management and Metrics; CS413: Testing and Validation; ELEC-CY: Security Operations and SIEM.

**Egyptian Arabic (اللهجة المصرية):**

الأسبوع الجاي بيكمل بـ: AI401: نماذج المتسلسلات والمحوّلات لمعالجة اللغات؛ AI402: تقسيم الصور؛ CS411: أطر معالجة البيانات الضخمة؛ CS412: إدارة العيوب والمقاييس؛ CS413: الاختبار والتحقق؛ ELEC-CY: عمليات الأمن وأنظمة SIEM.

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

[الدرس السابق: week-10.md](week-10.md) · [رجوع لفصل 7](README.md) · [الدرس الجاي: week-12.md](week-12.md)