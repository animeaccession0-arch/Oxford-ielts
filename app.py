import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="IELTS Scorer", layout="centered")

st.title("📝 REAL IELTS AI Examiner")
st.write("Essay paste kar aur REAL IELTS Band Score paa")

# 1. ESSAY INPUT
essay = st.text_area("paste essay here:", height=350, placeholder="Your essay...")

if st.button("Get REAL Band Score"):
    if not essay:
        st.warning("first fill the essay")
        st.stop()
    
    else:
        try:
            # API Key secrets se aa rahi hai
            api_key = st.secrets["GEMINI_API_KEY"]
            genai.configure(api_key=api_key)
            
            model = genai.GenerativeModel('gemini-2.0-flash')
            
            prompt = f"""
            You are a REAL IELTS Examiner. Check this essay strictly by IELTS Band Descriptors.
            Give Band Score 1-9 for: Task Response, Coherence, Lexical Resource, Grammar.
            Then give Overall Band Score. Also give 3 feedback points.
            
            Essay: {essay}
            
            Format: 
            **Overall Band: X.X**
            **Task Response: X.X**
            **Coherence: X.X** 
            **Lexical Resource: X.X**
            **Grammar: X.X**
            **Feedback:**
            1. ...
            """
            
            response = model.generate_content(prompt)
            st.success("Evaluation Done!")
            st.markdown(response.text)
            
        except Exception as e:
            st.error(f"Error: {e}")
            st.info("Agar '429 quota' error hai to kal try karna. Aaj quota khatam hai.")

st.caption("Made with Gemini 2.0 Flash")





st.markdown("\n---\nMade with ❤️ — Oxford IELTS ESSAY TESTER (heuristic scorer).")
