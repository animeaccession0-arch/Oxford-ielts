import streamlit as st
import re
from collections import Counter

st.set_page_config(page_title="Oxford IELTS Essay Scorer", layout="centered")

st.title("Oxford IELTS — Essay Scorer (demo)")
st.write("Paste your essay below and click 'Score essay' to get a heuristic band score and writing tips.")

essay = st.text_area("Your essay", height=360, placeholder="Paste your essay here...")

if 'attempt_count' not in st.session_state:
    st.session_state.attempt_count = 0

def preprocess(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip())

def compute_metrics(text: str):
    text = preprocess(text)
    words = re.findall(r"\b\w+\b", text)
    sentences = re.split(r'[.!?]+', text)
    sentences = [s for s in sentences if s.strip()]
    
    word_count = len(words)
    
    return {
        "word_count": word_count,
        "sentence_count": len(sentences),
        "lexical_diversity": len(set(words))/word_count if word_count > 0 else 0
    }
def is_valid_essay(text):
    text_lower = text.lower()
    bad_words = ["ignore", "system", "prompt", "you are", "forget", "instructions", "roleplay", "act as"]
    for word in bad_words:
        if word in text_lower:
            return False, "Sorry I can't help you with this"
    if len(text.split()) < 10:
        return False, "Please enter a proper essay with at least 10 words"
    if text.strip().endswith("?") or text_lower.startswith(("write", "tell me", "what is", "how to")):
        return False, "Sorry I can't help you with this. Please paste an IELTS essay only"
    return True, "ok"

    


      
  
def compute_metrics(text):
    words = text.split()
    word_count = len(words)
    unique_words = set(words)
    lexical_diversity = len(unique_words) / word_count if word_count > 0 else 0
    
    metrics = {
        'word_count': word_count,
        'lexical_diversity': lexical_diversity,
        'avg_sentence_len': 0,
        'grammar_errors': 0
    }
    return metrics

def generate_tips(metrics):
    tips = []
    
    if metrics['lexical_diversity'] < 0.5:
        tips.append("use different words. don't repeat same words")
    
    if len(tips) == 0:
        tips.append("good structure! now work on grammar and complex sentences for band 7+")
    
    return tips

def compute_metrics(text: str):
    text = preprocess(text)
    words = re.findall(r"\b\w+\b", text)
    if not words:
        return {}
            
            
            
        
        
    
        
    sentences = [s.strip() for s in re.split(r"[.!?]+", text) if s.strip()]
    word_count = len(words)
    sentence_count = len(sentences) if len(sentences) > 0 else 1
    avg_sentence_len = word_count / sentence_count
    unique_words = len(set(w.lower() for w in words))
    lexical_diversity = unique_words / word_count
    long_words = sum(1 for w in words if len(w) >= 7)
    long_word_ratio = long_words / word_count
    avg_word_len = sum(len(w) for w in words) / word_count
    return {}
    


def heuristic_score(metrics: dict) -> float:
    # Calculate a 0-100 raw score from heuristics, then map to 0-9 band
    raw = 0.0

    # Length: prefer 250-400 words for a full response
    wc = metrics["word_count"]
    if wc >= 350:
        raw += 20
    elif wc >= 250:
        raw += 16
    elif wc >= 200:
        raw += 12
    elif wc >= 150:
        raw += 8
    elif wc >= 100:
        raw += 4
    else:
        raw += 0

    # Sentence complexity: avg sentence length between 12-24 is OK
    asl = metrics["avg_sentence_len"]
    if 12 <= asl <= 24:
        raw += 20
    elif 8 <= asl < 12 or 24 < asl <= 30:
        raw += 12
    else:
        raw += 6

    # Lexical diversity
    ld = metrics["lexical_diversity"]
    if ld >= 0.55:
        raw += 25
    elif ld >= 0.45:
        raw += 18
    elif ld >= 0.35:
        raw += 10
    else:
        raw += 4

    # Use of longer (academic) words
    lwr = metrics["long_word_ratio"]
    if lwr >= 0.12:
        raw += 20
    elif lwr >= 0.09:
        raw += 14
    elif lwr >= 0.06:
        raw += 8
    else:
        raw += 2

    # avg word length small bonus
    awl = metrics["avg_word_len"]
    if awl >= 5.0:
        raw += 5
    elif awl >= 4.5:
        raw += 3

    # Clamp raw to 0-100
    raw = max(0.0, min(100.0, raw))

    # Map to IELTS band roughly: 0-9 (use thresholds)
    # 0-29 -> <=4.0, 30-39 -> 4.5, 40-49 -> 5.0-5.5, 50-59 -> 6.0-6.5, 60-74 -> 7.0-7.5, 75-89 -> 8.0-8.5, 90+ -> 9.0
    if raw >= 90:
        band = 9.0
    elif raw >= 75:
        band = 8.0 if raw < 82 else 8.5
    elif raw >= 60:
        band = 7.5 if raw >= 68 else 7.0
    elif raw >= 50:
        band = 6.5 if raw >= 55 else 6.0
    elif raw >= 40:
        band = 5.5 if raw >= 45 else 5.0
    elif raw >= 30:
        band = 4.5
    elif raw >= 10:
        band = 4.0
    else:
        band = 3.0

    return band


def generate_tips(metrics: dict):
    tips = []
    wc = metrics["word_count"]
    ld = metrics["lexical_diversity"]
    asl = metrics["avg_sentence_len"]
    lwr = metrics["long_word_ratio"]

    # Tip 1: content/length
    if wc < 250:
        tips.append("Expand your essay with more relevant ideas and examples to reach ~250–400 words; this helps develop coherence and task response.")
    else:
        tips.append("Your length is good — focus on developing ideas clearly and supporting them with examples.")

    # Tip 2: vocabulary
    if ld < 0.4:
        tips.append("Work on vocabulary variety: paraphrase, use synonyms and topic-specific words to increase lexical diversity.")
    elif lwr < 0.08:
        tips.append("Incorporate more precise/academic words (avoid repeating simple words) to raise the level of expression.")
    else:
        tips.append("Good range of vocabulary — keep using varied and precise words.")

    # Tip 3: sentence structure
    if asl < 10:
        tips.append("Try combining short sentences and using complex structures (subordinate clauses) for better cohesion and grammar demonstration.")
    elif asl > 30:
        tips.append("Some sentences are very long — shorten or split them to improve clarity and reduce risk of grammar errors.")
    else:
        tips.append("Aim for a mix of simple and complex sentences; use linking words to improve flow.")

    return tips


if st.button("Score essay"):
  
    # SECURITY CHECK 1: 5 attempts cross
    if st.session_state.attempt_count >= 5:
        st.error("🚫 Too many invalid attempts. Access blocked.")
        st.stop()
    
    # SECURITY CHECK 2: Valid essay or not
    is_valid, msg = is_valid_essay(essay)
    if not is_valid:
        st.session_state.attempt_count += 1
        st.error(f"{msg} \n\nAttempt {st.session_state.attempt_count}/5")
        st.stop()    
    m = compute_metrics(essay)
    word_count = m['word_count']

   st.write(Debug)     
        
# REAL IELTS SCORING

if word_count == 0:
    band = 0.0
elif word_count < 100:
    band = 3.0
elif word_count < 200:
    band = 5.0   
elif word_count < 250:
    band = 5.5
elif word_count < 300:
    band = 6.0
else:
    band = 6.5



st.subheader(f"Estimated IELTS band: {band}")
st.markdown("**Metrics**")
st.write(
        f"Words: {m['word_count']} — Sentences: {m['sentence_count']} — Avg sentence length: {m['avg_sentence_len']:.1f} words"
    )
st.write(
f"Lexical diversity: {m['lexical_diversity']:.2f} — Long-word ratio: {m['long_word_ratio']:.2f} — Avg word length: {m['avg_word_len']:.2f}"
    )

tips = generate_tips(m)
st.markdown("**Top 3 tips to improve your band**")
for i, t in enumerate(tips, 1):
    st.write(f"{i}. {t}")

    st.markdown("---")
    st.info("This is a heuristic estimator for quick feedback only. For an official band, submit to an accredited tester or trained examiner.")
else:
    st.write("Click 'Score essay' when you have pasted your essay.")


st.markdown("\n---\nMade with ❤️ — Oxford IELTS demo (heuristic scorer).")
