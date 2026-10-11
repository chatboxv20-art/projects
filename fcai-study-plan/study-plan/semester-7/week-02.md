# الأسبوع 2 — الفصل 7

> الدرس ده بيغطّي موضوع واحد في كل مقرر من مقررات الفصل، وكل الشرح مكتوب بالعامية المصرية مع البلوك الإنجليزي الكامل جنبه.

**المقررات اللي في الدرس ده:** AI401 (معالجة اللغات الطبيعية)، AI402 (الرؤية بالحاسب)، CS411 (قواعد البيانات المتقدمة والبيانات الضخمة)، CS412 (اختبار البرمجيات وضمان الجودة)، CS413 (مشروع التخرج 1)، ELEC-CY (اختياري: الأمن السيبراني)

---

# القسم الأول: معالجة اللغات الطبيعية (AI401)

## Text Preprocessing and Normalization (المعالجة المسبقة للنصوص وتوحيدها)

Text Preprocessing and Normalization (المعالجة المسبقة للنصوص وتوحيدها)
English Definition: Text Preprocessing and Normalization is a core topic in Natural Language Processing. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: المعالجة المسبقة للنصوص وتوحيدها موضوع أساسي في معالجة اللغات الطبيعية. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Text Preprocessing and Normalization** is the focus of this lesson. Natural language processing enables computers to understand and generate human language, from tokenization to transformers and large language models.

**Egyptian Arabic (اللهجة المصرية):**

**المعالجة المسبقة للنصوص وتوحيدها** هو محور الدرس ده. معالجة اللغات الطبيعية بتمكّن الحاسب من فهم وتوليد لغة الإنسان، من التقطيع للمحوّلات والنماذج اللغوية الضخمة.

### Why It Exists (ليه موجود)

Text is the largest source of human knowledge, and language interfaces are becoming the main way we use computers. Without a clear grasp of Text Preprocessing and Normalization, the rest of Natural Language Processing has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

النص أكبر مصدر لمعرفة الإنسان، والواجهات اللغوية بقت الطريقة الأساسية لاستخدام الحاسبات. ومن غير إدراك واضح لموضوع المعالجة المسبقة للنصوص وتوحيدها، باقي معالجة اللغات الطبيعية ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Text Preprocessing and Normalization is where the theory of Natural Language Processing meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع المعالجة المسبقة للنصوص وتوحيدها هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

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

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Text Preprocessing and Normalization, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في المعالجة المسبقة للنصوص وتوحيدها، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Text Preprocessing and Normalization in one sentence of your own words.
2. Give two situations where Text Preprocessing and Normalization changes a technical decision.
3. Name one limitation of Text Preprocessing and Normalization and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف المعالجة المسبقة للنصوص وتوحيدها في جملة واحدة بكلامك.
2. ادي موقفين المعالجة المسبقة للنصوص وتوحيدها بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود المعالجة المسبقة للنصوص وتوحيدها واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Text Preprocessing and Normalization? (a) a formality with no use (b) a working tool inside Natural Language Processing (c) an unrelated subject.
Q2. True or false: Text Preprocessing and Normalization has no limitations.
Q3. In one line, why does Text Preprocessing and Normalization matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـالمعالجة المسبقة للنصوص وتوحيدها؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه معالجة اللغات الطبيعية (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: المعالجة المسبقة للنصوص وتوحيدها مالوش حدود.
س3. في سطر واحد، ليه المعالجة المسبقة للنصوص وتوحيدها مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Natural Language Processing.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه معالجة اللغات الطبيعية.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Text Preprocessing and Normalization to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها المعالجة المسبقة للنصوص وتوحيدها على برنامج أو نظام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Text Preprocessing and Normalization until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف المعالجة المسبقة للنصوص وتوحيدها تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الثاني: الرؤية بالحاسب (AI402)

## Digital Image Formation and Representation (تكوين الصورة الرقمية وتمثيلها)

Digital Image Formation and Representation (تكوين الصورة الرقمية وتمثيلها)
English Definition: Digital Image Formation and Representation is a core topic in Computer Vision. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: تكوين الصورة الرقمية وتمثيلها موضوع أساسي في الرؤية بالحاسب. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Digital Image Formation and Representation** is the focus of this lesson. Computer vision lets computers extract meaning from images and video using filtering, features, geometry and deep networks.

**Egyptian Arabic (اللهجة المصرية):**

**تكوين الصورة الرقمية وتمثيلها** هو محور الدرس ده. الرؤية بالحاسب بتخلي الحاسبات تستخرج المعنى من الصور والفيديو باستخدام التصفية والخصائص والهندسة والشبكات العميقة.

### Why It Exists (ليه موجود)

Cameras are everywhere, and vision powers safety, medicine, autonomy and manufacturing. Without a clear grasp of Digital Image Formation and Representation, the rest of Computer Vision has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

الكاميرات في كل مكان، والرؤية بتشغّل السلامة والطب والاستقلالية والتصنيع. ومن غير إدراك واضح لموضوع تكوين الصورة الرقمية وتمثيلها، باقي الرؤية بالحاسب ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Digital Image Formation and Representation is where the theory of Computer Vision meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع تكوين الصورة الرقمية وتمثيلها هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

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

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Digital Image Formation and Representation, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في تكوين الصورة الرقمية وتمثيلها، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Digital Image Formation and Representation in one sentence of your own words.
2. Give two situations where Digital Image Formation and Representation changes a technical decision.
3. Name one limitation of Digital Image Formation and Representation and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف تكوين الصورة الرقمية وتمثيلها في جملة واحدة بكلامك.
2. ادي موقفين تكوين الصورة الرقمية وتمثيلها بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود تكوين الصورة الرقمية وتمثيلها واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Digital Image Formation and Representation? (a) a formality with no use (b) a working tool inside Computer Vision (c) an unrelated subject.
Q2. True or false: Digital Image Formation and Representation has no limitations.
Q3. In one line, why does Digital Image Formation and Representation matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـتكوين الصورة الرقمية وتمثيلها؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه الرؤية بالحاسب (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: تكوين الصورة الرقمية وتمثيلها مالوش حدود.
س3. في سطر واحد، ليه تكوين الصورة الرقمية وتمثيلها مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Computer Vision.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه الرؤية بالحاسب.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Digital Image Formation and Representation to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها تكوين الصورة الرقمية وتمثيلها على برنامج أو نظام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Digital Image Formation and Representation until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف تكوين الصورة الرقمية وتمثيلها تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الثالث: قواعد البيانات المتقدمة والبيانات الضخمة (CS411)

## Query Processing and Optimization (معالجة الاستعلامات وتحسينها)

Query Processing and Optimization (معالجة الاستعلامات وتحسينها)
English Definition: Query Processing and Optimization is a core topic in Database Systems. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: معالجة الاستعلامات وتحسينها موضوع أساسي في نظم قواعد البيانات. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Query Processing and Optimization** is the focus of this lesson. Database systems store, organize and query large amounts of structured data using the relational model, SQL, transactions and indexing.

**Egyptian Arabic (اللهجة المصرية):**

**معالجة الاستعلامات وتحسينها** هو محور الدرس ده. نظم قواعد البيانات بتخزّن وتنظّم وتستعلم عن كميات كبيرة من البيانات المنظّمة باستخدام النموذج العلائقي و SQL والمعاملات والفهرسة.

### Why It Exists (ليه موجود)

Almost every application needs durable, consistent, concurrent access to data. Without a clear grasp of Query Processing and Optimization, the rest of Database Systems has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

تقريبًا كل تطبيق محتاج وصول دائم ومتسق ومتزامن للبيانات. ومن غير إدراك واضح لموضوع معالجة الاستعلامات وتحسينها، باقي نظم قواعد البيانات ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Query Processing and Optimization is where the theory of Database Systems meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع معالجة الاستعلامات وتحسينها هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

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

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Query Processing and Optimization, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في معالجة الاستعلامات وتحسينها، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Query Processing and Optimization in one sentence of your own words.
2. Give two situations where Query Processing and Optimization changes a technical decision.
3. Name one limitation of Query Processing and Optimization and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف معالجة الاستعلامات وتحسينها في جملة واحدة بكلامك.
2. ادي موقفين معالجة الاستعلامات وتحسينها بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود معالجة الاستعلامات وتحسينها واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Query Processing and Optimization? (a) a formality with no use (b) a working tool inside Database Systems (c) an unrelated subject.
Q2. True or false: Query Processing and Optimization has no limitations.
Q3. In one line, why does Query Processing and Optimization matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـمعالجة الاستعلامات وتحسينها؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه نظم قواعد البيانات (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: معالجة الاستعلامات وتحسينها مالوش حدود.
س3. في سطر واحد، ليه معالجة الاستعلامات وتحسينها مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Database Systems.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه نظم قواعد البيانات.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Query Processing and Optimization to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها معالجة الاستعلامات وتحسينها على برنامج أو نظام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Query Processing and Optimization until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف معالجة الاستعلامات وتحسينها تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الرابع: اختبار البرمجيات وضمان الجودة (CS412)

## The Testing Life Cycle and the V-Model (دورة حياة الاختبار ونموذج V)

The Testing Life Cycle and the V-Model (دورة حياة الاختبار ونموذج V)
English Definition: The Testing Life Cycle and the V-Model is a core topic in Software Engineering. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: دورة حياة الاختبار ونموذج V موضوع أساسي في هندسة البرمجيات. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**The Testing Life Cycle and the V-Model** is the focus of this lesson. Software engineering applies engineering discipline to building software: requirements, design, construction, testing and maintenance at scale.

**Egyptian Arabic (اللهجة المصرية):**

**دورة حياة الاختبار ونموذج V** هو محور الدرس ده. هندسة البرمجيات بتطبّق الانضباط الهندسي على بناء البرمجيات: المتطلبات والتصميم والبناء والاختبار والصيانة على نطاق واسع.

### Why It Exists (ليه موجود)

Large software fails without process: unclear requirements and untested code cost the most. Without a clear grasp of The Testing Life Cycle and the V-Model, the rest of Software Engineering has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

البرمجيات الكبيرة بتفشل من غير عملية: المتطلبات الغامضة والكود غير المختبر هما الأغلى. ومن غير إدراك واضح لموضوع دورة حياة الاختبار ونموذج V، باقي هندسة البرمجيات ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, The Testing Life Cycle and the V-Model is where the theory of Software Engineering meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع دورة حياة الاختبار ونموذج V هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

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

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in The Testing Life Cycle and the V-Model, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في دورة حياة الاختبار ونموذج V، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define The Testing Life Cycle and the V-Model in one sentence of your own words.
2. Give two situations where The Testing Life Cycle and the V-Model changes a technical decision.
3. Name one limitation of The Testing Life Cycle and the V-Model and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف دورة حياة الاختبار ونموذج V في جملة واحدة بكلامك.
2. ادي موقفين دورة حياة الاختبار ونموذج V بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود دورة حياة الاختبار ونموذج V واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes The Testing Life Cycle and the V-Model? (a) a formality with no use (b) a working tool inside Software Engineering (c) an unrelated subject.
Q2. True or false: The Testing Life Cycle and the V-Model has no limitations.
Q3. In one line, why does The Testing Life Cycle and the V-Model matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـدورة حياة الاختبار ونموذج V؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه هندسة البرمجيات (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: دورة حياة الاختبار ونموذج V مالوش حدود.
س3. في سطر واحد، ليه دورة حياة الاختبار ونموذج V مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Software Engineering.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه هندسة البرمجيات.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying The Testing Life Cycle and the V-Model to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها دورة حياة الاختبار ونموذج V على برنامج أو نظام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of The Testing Life Cycle and the V-Model until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف دورة حياة الاختبار ونموذج V تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم الخامس: مشروع التخرج 1 (CS413)

## Problem Identification and Idea Generation (تحديد المشكلة وتوليد الأفكار)

Problem Identification and Idea Generation (تحديد المشكلة وتوليد الأفكار)
English Definition: Problem Identification and Idea Generation is a core topic in Graduation Project. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: تحديد المشكلة وتوليد الأفكار موضوع أساسي في مشروع التخرج. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Problem Identification and Idea Generation** is the focus of this lesson. The graduation project is a year-long capstone where you take a real problem from idea to a working, tested and documented system.

**Egyptian Arabic (اللهجة المصرية):**

**تحديد المشكلة وتوليد الأفكار** هو محور الدرس ده. مشروع التخرج هو مشروع السنة الأخيرة اللي بتاخد فيه مشكلة حقيقية من الفكرة لنظام شغّال ومختبر وموثّق.

### Why It Exists (ليه موجود)

It integrates everything you learned and produces a portfolio piece employers and graduate schools value. Without a clear grasp of Problem Identification and Idea Generation, the rest of Graduation Project has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

بيدمج كل اللي اتعلمته وبيطلع قطعة في ملف أعمالك بتقيّمها جهات العمل والدراسات العليا. ومن غير إدراك واضح لموضوع تحديد المشكلة وتوليد الأفكار، باقي مشروع التخرج ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Problem Identification and Idea Generation is where the theory of Graduation Project meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع تحديد المشكلة وتوليد الأفكار هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

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

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Problem Identification and Idea Generation, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في تحديد المشكلة وتوليد الأفكار، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Problem Identification and Idea Generation in one sentence of your own words.
2. Give two situations where Problem Identification and Idea Generation changes a technical decision.
3. Name one limitation of Problem Identification and Idea Generation and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف تحديد المشكلة وتوليد الأفكار في جملة واحدة بكلامك.
2. ادي موقفين تحديد المشكلة وتوليد الأفكار بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود تحديد المشكلة وتوليد الأفكار واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Problem Identification and Idea Generation? (a) a formality with no use (b) a working tool inside Graduation Project (c) an unrelated subject.
Q2. True or false: Problem Identification and Idea Generation has no limitations.
Q3. In one line, why does Problem Identification and Idea Generation matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـتحديد المشكلة وتوليد الأفكار؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه مشروع التخرج (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: تحديد المشكلة وتوليد الأفكار مالوش حدود.
س3. في سطر واحد، ليه تحديد المشكلة وتوليد الأفكار مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Graduation Project.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه مشروع التخرج.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Problem Identification and Idea Generation to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها تحديد المشكلة وتوليد الأفكار على برنامج أو نظام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Problem Identification and Idea Generation until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف تحديد المشكلة وتوليد الأفكار تاني لحد ما تقدر تقوله من غير ما تبص.
- افتكر ميزة واحدة وحد واحد.
- خلّي المثال العملي هو حالتك المرجعية.


---

# القسم السادس: اختياري: الأمن السيبراني (ELEC-CY)

## Security Architecture and Defence in Depth (معمارية الأمن والدفاع متعدد الطبقات)

Security Architecture and Defence in Depth (معمارية الأمن والدفاع متعدد الطبقات)
English Definition: Security Architecture and Defence in Depth is a core topic in Information Security and Cryptography. It is the part of the subject that explains what this idea is, why it exists, and how a software system actually uses it in practice.
Egyptian Arabic Definition: معمارية الأمن والدفاع متعدد الطبقات موضوع أساسي في أمن المعلومات والتشفير. هو الجزء من المادة اللي بيوضّح إيه الفكرة دي، وليه موجودة، وإزاي النظام البرمجي فعلًا بيستخدمها في الشغل.

### What It Is (يعني إيه)

**Security Architecture and Defence in Depth** is the focus of this lesson. Cryptography protects information using encryption, hashing, signatures and keys, while security engineering defends systems against attacks.

**Egyptian Arabic (اللهجة المصرية):**

**معمارية الأمن والدفاع متعدد الطبقات** هو محور الدرس ده. التشفير بيحمي المعلومات باستخدام التعمية والتقطيع والتوقيعات والمفاتيح، وهندسة الأمن بتدافع عن الأنظمة ضد الهجمات.

### Why It Exists (ليه موجود)

Confidentiality, integrity and authenticity are essential for every system that handles valuable data. Without a clear grasp of Security Architecture and Defence in Depth, the rest of Information Security and Cryptography has no anchor to hang on.

**Egyptian Arabic (اللهجة المصرية):**

السرية والسلامة والأصالة أساسية لكل نظام بيتعامل مع بيانات قيّمة. ومن غير إدراك واضح لموضوع معمارية الأمن والدفاع متعدد الطبقات، باقي أمن المعلومات والتشفير ما لوش مرتكز يتعلّق بيه.

### Why It Matters (ليه مهم)

In practice, Security Architecture and Defence in Depth is where the theory of Information Security and Cryptography meets a real decision, and that is why it is studied before the more advanced material.

**Egyptian Arabic (اللهجة المصرية):**

في الواقع، موضوع معمارية الأمن والدفاع متعدد الطبقات هو المكان اللي النظرية فيه بتقابل قرار حقيقي، وعشان كده بيتدرّس قبل المادة الأعمق.

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

Take the example above and apply it to a small program or system you know. Write down: (1) the situation in Security Architecture and Defence in Depth, (2) the numbers or facts involved, (3) the decision it supports, and (4) one risk you would watch.

**Egyptian Arabic (اللهجة المصرية):**

خد المثال اللي فوق وطبّقه على برنامج أو نظام صغير تعرفه. اكتب: (1) الموقف في معمارية الأمن والدفاع متعدد الطبقات، (2) الأرقام أو الحقائق المعنية، (3) القرار اللي بيدعمه، (4) خطر واحد تراقبه.

### Practice Questions (أسئلة تدريب)

1. Define Security Architecture and Defence in Depth in one sentence of your own words.
2. Give two situations where Security Architecture and Defence in Depth changes a technical decision.
3. Name one limitation of Security Architecture and Defence in Depth and explain it briefly.

**Egyptian Arabic (اللهجة المصرية):**

1. عرّف معمارية الأمن والدفاع متعدد الطبقات في جملة واحدة بكلامك.
2. ادي موقفين معمارية الأمن والدفاع متعدد الطبقات بيغيّر فيهم قرار تقني.
3. اذكر حد واحد من حدود معمارية الأمن والدفاع متعدد الطبقات واشرحه بإيجاز.

### Quiz (اختبار قصير)

Q1. Which statement best describes Security Architecture and Defence in Depth? (a) a formality with no use (b) a working tool inside Information Security and Cryptography (c) an unrelated subject.
Q2. True or false: Security Architecture and Defence in Depth has no limitations.
Q3. In one line, why does Security Architecture and Defence in Depth matter to a developer?

**Egyptian Arabic (اللهجة المصرية):**

س1. أنهي وصف أدق لـمعمارية الأمن والدفاع متعدد الطبقات؟ (أ) شكلية بدون فايدة (ب) أداة شغّالة جوه أمن المعلومات والتشفير (ج) موضوع مالوش علاقة.
س2. صح أم خطأ: معمارية الأمن والدفاع متعدد الطبقات مالوش حدود.
س3. في سطر واحد، ليه معمارية الأمن والدفاع متعدد الطبقات مهم للمطوّر؟

### Quiz Answers (إجابات الاختبار)

A1. (b) - it is a working tool inside Information Security and Cryptography.
A2. False - it has clear limitations.
A3. Because it turns a general principle into a concrete, defensible decision.

**Egyptian Arabic (اللهجة المصرية):**

ج1. (ب) - أداة شغّالة جوه أمن المعلومات والتشفير.
ج2. خطأ - ليه حدود واضحة.
ج3. لأنه بيحوّل المبدأ العام لقرار ملموس قابل للدفاع عنه.

### Homework (الواجب)

Write half a page applying Security Architecture and Defence in Depth to a real program or system you choose. Include the situation, the analysis and your recommendation.

**Egyptian Arabic (اللهجة المصرية):**

اكتب نص صفحة بتطبّق فيها معمارية الأمن والدفاع متعدد الطبقات على برنامج أو نظام حقيقي تختاره. ضمّن الموقف والتحليل والتوصية بتاعتك.

### Revision Notes (ملاحظات مراجعة)

- Re-read the definition of Security Architecture and Defence in Depth until you can say it without looking.
- Remember one advantage and one limitation.
- Keep the practical example as your reference case.

**Egyptian Arabic (اللهجة المصرية):**

- اقرا تعريف معمارية الأمن والدفاع متعدد الطبقات تاني لحد ما تقدر تقوله من غير ما تبص.
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

This week covered the following topics across the semester's courses: AI401: Text Preprocessing and Normalization; AI402: Digital Image Formation and Representation; CS411: Query Processing and Optimization; CS412: The Testing Life Cycle and the V-Model; CS413: Problem Identification and Idea Generation; ELEC-CY: Security Architecture and Defence in Depth. Each topic opened with a bilingual definition, then explained what it is, why it exists, why it matters, where it is used, its advantages and limits, best practices and common mistakes, followed by a practical example and exercises.

**Egyptian Arabic (اللهجة المصرية):**

الأسبوع ده غطّى المواضيع دي في مقررات الفصل: AI401: المعالجة المسبقة للنصوص وتوحيدها؛ AI402: تكوين الصورة الرقمية وتمثيلها؛ CS411: معالجة الاستعلامات وتحسينها؛ CS412: دورة حياة الاختبار ونموذج V؛ CS413: تحديد المشكلة وتوليد الأفكار؛ ELEC-CY: معمارية الأمن والدفاع متعدد الطبقات. كل موضوع بدأ بتعريف ثنائي اللغة، وبعدين شرح يعني إيه وليه موجود وليه مهم وبنستخدمه فين، ومميزاته وحدوده وأحسن الممارسات والأخطاء الشائعة، وبعدين مثال عملي وتمارين.

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

Next week continues with: AI401: Regular Expressions and Rule-Based NLP; AI402: Image Filtering and Convolution; CS411: Advanced Indexing and Storage; CS412: Static Testing and Reviews; CS413: Literature Review and Background Research; ELEC-CY: Vulnerability Assessment.

**Egyptian Arabic (اللهجة المصرية):**

الأسبوع الجاي بيكمل بـ: AI401: التعبيرات النمطية ومعالجة اللغات بالقواعد؛ AI402: تصفية الصور والالتفاف؛ CS411: الفهرسة والتخزين المتقدم؛ CS412: الاختبار الساكن والمراجعات؛ CS413: مراجعة الأدبيات والبحث في الخلفية؛ ELEC-CY: تقييم الثغرات.

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

[الدرس السابق: week-01.md](week-01.md) · [رجوع لفصل 7](README.md) · [الدرس الجاي: week-03.md](week-03.md)