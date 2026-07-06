import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="IELTS Scorer", layout="centered")
st.title("📝 REAL IELTS AI Examiner")

# 1. API KEY INPUT - SECURE
api_key = st.text_input("1. Gemini API Key:", type="password")

# 2. ESSAY INPUT  
essay = st.text_area("2. Essay yahan paste karo:", height=350)

if st.button("Get REAL Band Score"):
    if not api_key or not essay:
        st.error("Dono bharo")
        st.stop()
        
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.0-flash')
        
        # ====== YE PROMPT USER KO NAHI DIKHEGA ======
        # YE SIRF BACKEND ME CHALEGA
        PROMPT = f"""You are a strict IELTS examiner. Score this essay out of Band 9.
        CRITICAL RULE: If word count < 250, Overall Band max is 5.0
        
        Give answer in this format:
        ### OVERALL BAND: X.X
        **Task Response:** X.X/9 - reason
        **Coherence & Cohesion:** X.X/9 - reason
        **Lexical Resource:** X.X/9 - reason  
        **Grammar:** X.X/9 - reason
        ### 3 TIPS TO IMPROVE WITH EXAMPLES:
        1. **Tip:** ... **Example:** ...
        
        ESSAY: {essay}"""
        # =============================================
        
        with st.spinner("Checking..."):
            response = model.generate_content(PROMPT)
        
        st.success("RESULT")
        st.markdown(response.text) # Sirf result dikhega, prompt nahi
        
    except Exception as e:
        st.error(f"Error: {e}")





st.markdown("\n---\nMade with ❤️ — Oxford IELTS ESSAY TESTER (heuristic scorer).")
