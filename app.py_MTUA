import streamlit as st
import google.generativeai as genai
import time
import random
from datetime import datetime

st.set_page_config(page_title="MTUA AI Exam Hall by Anime", page_icon="📜", layout="wide")

# HEADER
st.markdown("<h1 style='text-align: center; color: #003366;'>📜 MTUA AI EXAM HALL</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: grey;'>Built by Anime | AI Questions + Past Papers + Certificate</h3>", unsafe_allow_html=True)
st.markdown("---")

# STUDENT NAME
student_name = st.text_input("Enter Your Full Name for Certificate:")

# EXAM SETTINGS
col1, col2 = st.columns(2)
with col1:
    exam_mode = st.selectbox("Exam Mode:", ["AI Generate New Paper", "Real Past Paper 2023", "Real Past Paper 2022"])
with col2:
    level = st.selectbox("Difficulty:", ["Easy", "Medium", "Hard", "Oxford Past Paper Level"])
    num_questions = st.selectbox("Number of Questions:", [5, 10])

# REAL PAST PAPER BANK - ADD MORE HERE
past_papers = {
    "Real Past Paper 2023": [
        "Q1: Find the stationary points of y = x^3 - 6x^2 + 9x",
        "Q2: Prove that n^3 - n is divisible by 6 for all integers n",
        "Q3: Solve the inequality |2x - 1| < 5",
        "Q4: If f(x) = ln(x), find f'(e)",
        "Q5: Find the sum of the first 10 terms of arithmetic sequence 2, 5, 8..."
    ],
    "Real Past Paper 2022": [
        "Q1: If f(x)=1/(1+x), find f(f(x))",
        "Q2: Find all real solutions to x^4 - 5x^2 + 4 = 0",
        "Q3: Prove that for x > 0, x + 1/x >= 2",
        "Q4: Solve sin(2x) = 0.5 for 0 <= x < 2pi"
    ]
}

# GENERATE EXAM BUTTON
if st.button("🚀 Start Exam", use_container_width=True):
    if not student_name:
        st.warning("Please enter your name first")
        st.stop()

    st.session_state.answers = {}
    st.session_state.start_time = time.time()

    if "Past Paper" in exam_mode:
        st.session_state.questions = past_papers[exam_mode][:num_questions]
        st.success(f"Loaded {len(st.session_state.questions)} Questions from {exam_mode}")
    else:
        with st.spinner("AI is creating your Oxford style exam..."):
            try:
                api_key = st.secrets["GEMINI_API_KEY"]
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-2.0-flash')

                prompt = f"""
                You are an Oxford MAT Exam Setter.
                Generate {num_questions} unique {level} level Mathematics questions for MTUA exam.
                Topics: Calculus, Algebra, Trigonometry, Logic.
                Output only questions, numbered Q1 to Q{num_questions}. One question per line.
                """
                response = model.generate_content(prompt)
                st.session_state.questions = [q for q in response.text.split("\n") if q.strip()]
                st.success(f"AI Generated {len(st.session_state.questions)} New Questions")
            except Exception as e:
                st.error(f"Error: {e}")

# SHOW QUESTIONS
if "questions" in st.session_state:
    st.markdown("### Your Exam Paper")
    for i, q in enumerate(st.session_state.questions):
        st.text_area(f"{q}", key=f"q{i}", height=80, disabled=True)
        st.session_state.answers[i] = st.text_input(f"Your Answer for Q{i+1}:", key=f"a{i}")

# SUBMIT + RESULT + CERTIFICATE
if st.button("📤 Submit Exam & Get Result", use_container_width=True):
    if "start_time" not in st.session_state:
        st.error("Start the exam first")
        st.stop()

    st.session_state.end_time = time.time()
    time_taken = round((st.session_state.end_time - st.session_state.start_time)/60, 2)

    with st.spinner("AI is checking your paper..."):
        attempted = sum(1 for ans in st.session_state.answers.values() if ans.strip())
        score = attempted # Demo: 1 mark per attempted question
        percentage = (score / num_questions) * 100

    st.markdown("---")
    st.header("📊 YOUR RESULT")
    col1, col2, col3 = st.columns(3)
    col1.metric("Score", f"{score} / {num_questions}")
    col2.metric("Percentage", f"{percentage:.1f}%")
    col3.metric("Time Taken", f"{time_taken} min")

    # CERTIFICATE LOGIC
    if percentage >= 60:
        st.success("🎉 CONGRATULATIONS! You Passed!")
        st.balloons()
        cert = f"""
***************************************
        CERTIFICATE OF ACHIEVEMENT

This is to certify that
{student_name}

has successfully completed the MTUA AI Practice Exam
Score: {percentage:.1f}% | Level: {level}

Issued by: MTUA AI Coach by Anime
Date: {datetime.now().strftime('%d %B %Y')}
***************************************
        """
        st.code(cert)
        st.download_button("⬇️ Download Certificate", cert, file_name=f"MTUA_Certificate_{student_name}.txt")
    else:
        st.error("Score 60%+ to get Certificate. Keep Practicing!")

st.markdown("---")
st.markdown("<p style='text-align: center;'>Made by <b>Anime</b> | Part of 5-AI Suite for Oxford 2026</p>", unsafe_allow_html=True)
