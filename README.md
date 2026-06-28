# 🚀 AI Career Copilot

An AI-powered Resume Analyzer that helps users evaluate their resumes based on their career goals. The application extracts relevant skills, identifies missing skills, generates a personalized learning roadmap, and provides interview questions using AI.

---

## 📌 Features

* 🔐 User Authentication (Signup & Login)
* 📄 Upload Resume (PDF / DOCX)
* 🤖 AI Resume Analysis using Gemini AI
* 💡 Extract Relevant Skills
* 📉 Detect Missing Skills
* 🗺️ Personalized Learning Roadmap
* ❓ AI Generated Interview Questions
* 🕒 Resume Analysis History
* 💾 Database Storage using SQLAlchemy & TiDB

---

## 🛠️ Tech Stack

### Backend

* Python
* Flask
* SQLAlchemy
* Gemini AI API

### Frontend

* HTML5
* CSS3
* Jinja2 Templates

### Database

* TiDB Cloud
* SQLAlchemy ORM

### Libraries

* PyPDF2
* python-docx
* python-dotenv
* JSON

---

## 📂 Project Structure

```text
resume-ai-assistant/
│
├── app.py
├── ai.py
├── db.py
├── models.py
├── .env
├── requirements.txt
│
├── static/
│   └── style.css
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   └── history.html
│
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Shubhamyadav72782/resume-ai-assistant.git
```

Go to the project folder:

```bash
cd resume-ai-assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your Gemini API Key:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application:

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 🎯 Future Improvements

* Resume Score (0–100)
* ATS Compatibility Checker
* Resume Keyword Optimization
* Download Analysis Report as PDF
* Dark Mode
* Admin Dashboard

---

## 👨‍💻 Author

**Shubham Yadav**

GitHub: https://github.com/Shubhamyadav72782
