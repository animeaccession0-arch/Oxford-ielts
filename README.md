# Oxford IELTS — Streamlit essay scorer (demo)

This repository contains a simple Streamlit app that provides a heuristic IELTS band estimate for an essay and three quick tips to improve writing.

Files
- app.py — Streamlit application (essay input, scoring heuristics, tips)
- requirements.txt — minimal dependencies

Run locally
1. Create a virtual environment (optional but recommended):
   python -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   .venv\Scripts\activate     # Windows PowerShell

2. Install requirements:
   pip install -r requirements.txt

3. Run the app:
   streamlit run app.py

Open the URL shown by Streamlit (usually http://localhost:8501)

Notes
- This is a demo heuristic scorer for quick feedback only. It is not an official IELTS band prediction.
- For production use, integrate a trained model or human rater for higher accuracy.
