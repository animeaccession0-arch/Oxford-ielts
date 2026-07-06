import streamlit as st
import re

st.set_page_config(page_title="Oxford IELTS Scorer", layout="centered")
st.title("📝 Oxford IELTS Essay Scorer")

if 'attempt_count' not in st.session_state:
    st.session_state.attempt_count = 0

essay = st.text_area("Enter your essay here:", height=300, placeholder="Write minimum 50 words...")

def compute_metrics(text):
    words = re.findall(r'\w+', text.lower())
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    word_count = len(words)
    sentence_count = len(sentences)
    avg_sentence_len = word_count / sentence_count if sentence_count > 0 else 0
    unique_words = len(set(words))
    lexical_diversity = unique_words / word_count if word_count > 0 else 0
    long_words = [w for w in words if len(w) > 6]
    long_word_ratio = len(long_words) / word_count if word_count > 0 else 0
    avg_word_len = sum(len(w) for w in words) / word_count if word_count > 0 else 0
    return {
        'word_count': word_count,
        'sentence_count': sentence_count,
        'avg_sentence_len': avg_sentence_len,
        'lexical_diversity': lexical_diversity,
        'long_word_ratio': long_word_ratio,
        'avg_word_len': avg_word_len
    }

def calculate_band(m):
    band = 5.0
    if m['word_count'] >= 250: band += 0.5
    if m['word_count'] >= 300: band += 0.5
    if m['avg_sentence_len'] >= 15: band += 0.5
    if m['lexical_diversity'] >= 0.5: band += 0.5
    if m['long_word_ratio'] >= 0.15: band += 0.5
    return min(round(band * 2) / 2, 9.0)

def generate_tips(m):
    tips = []
    if m['word_count'] < 250:
        tips.append(("Task Response", "Write at least 250 words.", "Example: Instead of 180 words, add 1 more body paragraph with 2-3 examples."))
    if m['avg_sentence_len'] < 15:
        tips.append(("Grammar", "Use complex sentences with connectors.", "Example: 'I agree. It is good.' → 'I agree because it provides many benefits such as...'"))
    if m['lexical_diversity'] < 0.5:
        tips.append(("Vocabulary", "Avoid repeating same words. Use synonyms.", "Example: Instead of 'good' 5 times, use 'beneficial, effective, positive, advantageous'"))
    if m['long_word_ratio'] < 0.15:
        tips.append(("Lexical Resource", "Use less common academic words.", "Example: 'big problem' → 'significant issue', 'help' → 'facilitate'"))
    if not tips:
        tips.append(("Overall", "Great job! Your essay is strong.", "Example: Keep practicing with timed writing to maintain this level."))
    return tips

def is_valid_essay(text):
    if len(text.strip()) < 50:
        return False, "Essay too short. Minimum 50 characters required."
    if len(re.findall(r'\w+', text)) < 20:
        return False, "Essay too short. Minimum 20 words required."
    return True, "OK"

if st.button("Score essay"):
    if st.session_state.attempt_count >= 10:
        st.error("🚫 Too many invalid attempts. Please refresh page.")
        st.stop()

    is_valid, msg = is_valid_essay(essay)
    if not is_valid:
        st.session_state.attempt_count += 1
        st.error(f"❌ {msg} \n\nAttempt {st.session_state.attempt_count}/10")
        st.stop()
    
    m = compute_metrics(essay)
    band = calculate_band(m)
    tips = generate_tips(m)
    
    st.success(f"### Estimated IELTS Band: {band}")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Word Count", m['word_count'])
    col2.metric("Sentences", m['sentence_count'])
    col3.metric("Avg Sentence Length", f"{m['avg_sentence_len']:.1f}")

    st.subheader("📈 Tips to Improve with Examples:")
    for i, (category, tip, example) in enumerate(tips, 1):
        st.markdown(f"**{i}. {category}:** {tip}")
        st.info(f"💡 {example}")



st.markdown("\n---\nMade with ❤️ — Oxford IELTS ESSAY TESTER (heuristic scorer).")
