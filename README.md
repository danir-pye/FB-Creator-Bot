# Social Media Automation Framework (Safe & Compliant)

<p align="center">
  <img src="https://img.shields.io/badge/status-active-success" />
  <img src="https://img.shields.io/github/license/danir-pye/FB-Creator-Bot" />
  <img src="https://img.shields.io/github/actions/workflow/status/danir-pye/FB-Creator-Bot/ci.yml" />
  <img src="https://img.shields.io/badge/made%20with-❤️-brightgreen" />
</p>

> إطار عمل احترافي **لأتمتة وسائل التواصل الاجتماعي** بشكل **قانوني ومتوافق** مع شروط الاستخدام. يركز على الجدولة، قوالب المحتوى، والتكامل مع **واجهات رسمية** — دون أي إنشاء حسابات أو تجاوزات.

## ✨ ماذا ستحصل؟
- 🧰 هيكل مشروع جاهز للإنتاج (Node.js & Python).
- 📅 جدولة منشورات (cron + queue) مع أمثلة.
- 🧠 قوالب محتوى + prompts جاهزة.
- 🔌 تكاملات مع واجهات رسمية (عند توفرها).
- ✅ توثيق كامل + سياسات أمان وامتثال.

## 🗂️ هيكلة المستودع
```text
.
├── src/
│   ├── node/
│   │   ├── index.ts
│   │   └── scheduler.ts
│   └── python/
│       ├── main.py
│       └── scheduler.py
├── templates/
│   ├── captions.json
│   └── prompts.md
├── integrations/
│   └── README.md
├── .github/
│   ├── workflows/ci.yml
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.md
│       └── feature_request.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── LICENSE
└── README.md
```

## 🚀 تشغيل سريع
### Node.js
```bash
npm i
npm run build
npm run start
```

### Python
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python src/python/main.py
```

## 🔒 الامتثال والأمان
- يمنع أي كود لإنشاء الحسابات أو تجاوز التحقق.
- يسمح فقط بالتكامل مع واجهات رسمية أو أنماط QA تعليمية.
- راجع "SECURITY.md" و"CODE_OF_CONDUCT.md".

## 🧭 خارطة الطريق
- [ ] دعم LinkedIn و X عبر واجهات رسمية.
- [ ] لوحة تحكم تحليلات.
- [ ] قوالب محتوى عربية/إنجليزية.

---

صاحب المشروع: **@danir-pye** — للأعمال الجادة فقط.
