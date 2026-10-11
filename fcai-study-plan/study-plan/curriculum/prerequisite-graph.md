# شجرة المقررات السابقة

الرسم ده بيوضّح إيه اللي لازم تخلّصه قبل إيه. اقراه من فوق لتحت: السهم معناه "لازم الأول".

---

## الرسم الكامل

```mermaid
graph TD
    CS112[CS112] --> CS113[CS113]
    CS112[CS112] --> CS114[CS114]
    MATH101[MATH101] --> MATH103[MATH103]
    MATH101[MATH101] --> MATH104[MATH104]
    PHYS101[PHYS101] --> PHYS102[PHYS102]
    ENG101[ENG101] --> ENG102[ENG102]
    CS114[CS114] --> CS211[CS211]
    MATH102[MATH102] --> CS211[CS211]
    CS111[CS111] --> CS212[CS212]
    CS114[CS114] --> CS213[CS213]
    MATH101[MATH101] --> MATH201[MATH201]
    CS111[CS111] --> IS201[IS201]
    ENG102[ENG102] --> ENG201[ENG201]
    CS212[CS212] --> CS214[CS214]
    MATH102[MATH102] --> CS215[CS215]
    CS113[CS113] --> CS216[CS216]
    CS212[CS212] --> CS217[CS217]
    CS114[CS114] --> AI201[AI201]
    MATH104[MATH104] --> AI201[AI201]
    MATH104[MATH104] --> ST201[ST201]
    CS215[CS215] --> CS311[CS311]
    CS114[CS114] --> CS311[CS311]
    MATH103[MATH103] --> CS312[CS312]
    CS113[CS113] --> CS312[CS312]
    CS213[CS213] --> CS313[CS313]
    AI201[AI201] --> AI301[AI301]
    MATH104[MATH104] --> AI301[AI301]
    CS216[CS216] --> CS314[CS314]
    CS214[CS214] --> CS321[CS321]
    CS217[CS217] --> CS321[CS321]
    AI301[AI301] --> AI302[AI302]
    CS217[CS217] --> CS322[CS322]
    MATH102[MATH102] --> CS322[CS322]
    CS216[CS216] --> CS323[CS323]
    CS217[CS217] --> CS324[CS324]
    ST201[ST201] --> ELEC-DS[ELEC-DS]
    AI301[AI301] --> AI401[AI401]
    AI301[AI301] --> AI402[AI402]
    CS213[CS213] --> CS411[CS411]
    CS216[CS216] --> CS412[CS412]
    CS216[CS216] --> CS413[CS413]
    CS217[CS217] --> ELEC-CY[ELEC-CY]
    AI301[AI301] --> AI403[AI403]
    CS211[CS211] --> CS421[CS421]
    CS413[CS413] --> CS423[CS423]
    CS113[CS113] --> ELEC-MOBILE[ELEC-MOBILE]
    CS312[CS312] --> ELEC-GAME[ELEC-GAME]
```

---

## السلاسل الحرجة — خد بالك منها

السلاسل دي لو وقعت فيها في مقرر، بتتأخر فصل كامل على الأقل.

### سلسلة البرمجة وهياكل البيانات

```
CS112 → CS113
CS112 → CS114 → {CS211, CS213, AI201}
CS211 → CS421
```

### سلسلة الأنظمة والشبكات

```
CS111 → CS212 → {CS214, CS217}
CS214 → CS321
CS217 → {CS322, CS324, CS321}
```

### سلسلة الذكاء الاصطناعي

```
MATH104 → AI201 → AI301 → {AI302, AI401, AI402, AI403}
```

### سلسلة هندسة البرمجيات

```
CS113 → CS216 → {CS314, CS323, CS412, CS413} → CS423
```

### سلسلة الرياضيات

```
MATH101 → {MATH102, MATH103, MATH104, MATH201}
MATH104 → ST201 → ELEC-DS
```

### سلسلة قواعد البيانات

```
CS114 → CS213 → CS411
CS213 → CS313
```

### سلسلة مشروع التخرج

```
CS413 → CS423
```

---

## جدول مبسّط: كل مقرر وفصله

| الفصل | المقررات |
|---|---|
| 1 | CS111, CS112, MATH101, MATH102, PHYS101, ENG101 |
| 2 | CS113, CS114, MATH103, MATH104, PHYS102, ENG102 |
| 3 | CS211, CS212, CS213, MATH201, IS201, ENG201 |
| 4 | CS214, CS215, CS216, CS217, AI201, ST201 |
| 5 | CS311, CS312, CS313, AI301, CS314, IS301 |
| 6 | CS321, AI302, CS322, CS323, CS324, ELEC-DS |
| 7 | AI401, AI402, CS411, CS412, CS413, ELEC-CY |
| 8 | AI403, CS421, CS422, CS423, ELEC-MOBILE, ELEC-GAME |

الرسم ده مطابق تمامًا لجدول المقررات في ملف `course-inventory.md`.