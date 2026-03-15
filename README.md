<div align="center">

# 🔍 AI Code Review Assistant

**Get instant, senior-level code feedback powered by Google Gemini**

Paste your code → Get 3 improvements, 1 positive note, and an optional refactored snippet

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Gemini](https://img.shields.io/badge/Google-Gemini-4285F4?style=flat&logo=google&logoColor=white)](https://ai.google.dev)

</div>

---

## ✨ What it does

AI Code Review Assistant uses Google's Gemini API to review your code like a senior software engineer. For any snippet you paste, you get:

| Output | Description |
|--------|-------------|
| **3 Improvements** | Actionable suggestions for readability, structure, and maintainability |
| **1 Positive Note** | What you did well—no nitpicking without recognition |
| **Refactored Example** | Optional improved code when meaningful changes can be suggested |

---

## 📸 Screenshots

### Input — Paste your code and hit Review

<img src="image 1.png" alt="App interface with code input" width="700">

### Output — Improvements, positive feedback, and refactored code

<img src="image 3.png" alt="Full code review with improvements" width="700">

<img src="image 2.png" alt="Positive note and refactored example" width="700">

---

## 🚀 Quick Start

### 1. Clone & setup

```bash
git clone git@github.com:khubaib-ctrl/ai-code-assistant.git
cd ai-code-assistant

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

### 2. Get a Gemini API key

- Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
- Create an API key (free tier available)
- Enter it in the app, or set `GOOGLE_API_KEY` in your environment

### 3. Run the app

```bash
streamlit run app.py
```

Paste your code, enter your API key, and click **Review Code**.

---

## 📁 Project Structure

```
ai-code-assistant/
├── app.py           # Single-file app (UI, prompt, Gemini integration)
├── requirements.txt
├── README.md
└── image *.png      # Screenshots
```

---

## 📄 License

MIT
