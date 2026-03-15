# AI Code Review Assistant

A minimal web app that reviews short code snippets using Google's Gemini API. Paste your code and receive AI-powered feedback on readability, structure, and maintainability.

## Features

- **3 improvements** related to readability, structure, or maintainability
- **1 positive observation** about your code
- **Optional refactored snippet** when meaningful improvements can be suggested

## Setup

1. **Clone or download** this project.

2. **Create a virtual environment** (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Get a Google API key** for Gemini:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create an API key
   - Enter it in the app when prompted, or set `GOOGLE_API_KEY` in your environment

## How to Run

From the project directory:

```bash
streamlit run app.py
```

The app will open in your browser. Paste your code, enter your API key, and click **Review Code**.

## Project Structure

```
ai-code-review-assistant/
├── app.py          # Single-file app (UI, prompt, Gemini integration)
├── requirements.txt
└── README.md
```
