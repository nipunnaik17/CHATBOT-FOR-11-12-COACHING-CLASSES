

# 📘 README.md

Copy this fully into your `README.md`:

---

# 🤖 11–12 Coaching Classes Chatbot

An AI-powered chatbot built using Flask and SpaCy for 11–12 coaching institutes.
The chatbot automatically responds to student queries related to courses, fees, timings, admissions, and facilities.

---

## 🚀 Features

* Handles student queries in real-time
* Covers:

  * Courses (JEE, NEET, CET, Foundation, Boards)
  * Fees structure
  * Class timings
  * Admission process
  * Contact details
  * Location information
* NLP-based intent matching using SpaCy
* Interactive web-based chat interface

---

## 🛠️ Tech Stack

* Python
* Flask
* SpaCy (NLP)
* HTML/CSS
* JSON-based intent system

---

## 📂 Folder Structure

```text
CHATBOT-COACHING/
│
├── templates/
│   └── index.html
│
├── task3.py
│
└── README.md
```

---

## ▶️ How to Run

### 1️⃣ Install Dependencies

```bash
pip install flask spacy
python -m spacy download en_core_web_sm
```

### 2️⃣ Run the Application

```bash
python task3.py
```

### 3️⃣ Open in Browser

```
http://127.0.0.1:5000/
```

---

## 📌 How It Works

1. User types a query in chat interface.
2. Flask processes the message.
3. SpaCy performs basic NLP processing.
4. The chatbot matches the query with predefined intents.
5. A relevant response is returned instantly.

---

👨‍💻 Developed by Nipun Naik
Internship Project | NLP-Based Chatbot Using Flask

---


