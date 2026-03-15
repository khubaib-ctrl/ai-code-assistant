"""AI Code Review Assistant - single-file Streamlit app."""

import os

import google.generativeai as genai
import streamlit as st

CODE_REVIEW_PROMPT = """You are a senior software engineer conducting a code review. Review the following code snippet and provide feedback.

Code to review:
```
{code}
```

Respond in this exact format:

### Improvements

1.
2.
3.

### Positive Note

...

### Refactored Example

(optional code snippet - only include if you have meaningful improvements to suggest)

Be concise and actionable. Focus on readability, structure, and maintainability."""


def review_code(code: str, api_key: str) -> str:
    """Review code using Google Gemini API."""
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")
    prompt = CODE_REVIEW_PROMPT.format(code=code)
    response = model.generate_content(prompt)
    return response.text


def main():
    st.set_page_config(page_title="AI Code Review Assistant", page_icon="🔍")
    st.title("🔍 AI Code Review Assistant")
    st.markdown("Paste your code below and get feedback from an AI senior engineer.")

    code = st.text_area(
        "Code to review",
        placeholder="def hello():\n    print('Hello, World!')",
        height=200,
    )

    default_key = os.environ.get("GOOGLE_API_KEY", "")
    api_key = st.text_input(
        "Google API Key",
        type="password",
        value=default_key,
        placeholder="Enter your Gemini API key (or set GOOGLE_API_KEY)",
        help="Get your key at https://makersuite.google.com/app/apikey",
    )

    if st.button("Review Code"):
        if not code.strip():
            st.warning("Please enter some code to review.")
        elif not api_key.strip():
            st.warning("Please enter your Google API key.")
        else:
            with st.spinner("Reviewing your code..."):
                try:
                    feedback = review_code(code, api_key)
                    st.markdown("---")
                    st.markdown("### Review")
                    st.markdown(feedback)
                except Exception as e:
                    st.error(f"Review failed: {e}")


if __name__ == "__main__":
    main()
