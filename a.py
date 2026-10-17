
import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv(override=True)
API_KEY = os.getenv("GROQ_API_KEY")

st.set_page_config(
    page_title="Answer Generator",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- CUSTOM DESIGN ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f5f7ff, #eef5ff);
}
.block-container {
    padding-top: 2rem;
    max-width: 1200px;
}
.hero {
    background: linear-gradient(120deg, #172554, #4338ca, #6366f1);
    padding: 32px;
    border-radius: 22px;
    color: white;
    margin-bottom: 24px;
    box-shadow: 0 10px 30px rgba(49,46,129,0.18);
}
.hero h1 {
    color: white;
    font-size: 38px;
    margin-bottom: 8px;
}
.hero p {
    color: #e0e7ff;
    font-size: 17px;
}
.info-card {
    background: white;
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #e0e7ff;
    margin-bottom: 14px;
    box-shadow: 0 4px 15px rgba(30,41,59,0.05);
}
.section-title {
    color: #312e81;
    font-size: 23px;
    font-weight: 700;
    margin: 20px 0 12px 0;
}
.stButton > button {
    background: linear-gradient(90deg, #4338ca, #6366f1);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 12px;
    font-weight: 700;
    min-height: 48px;
}
.stButton > button:hover {
    color: white;
    border: 1px solid #818cf8;
}
div[data-testid="stTextArea"] textarea {
    border-radius: 12px;
}
div[data-testid="stSelectbox"] {
    border-radius: 10px;
}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.markdown("## 🎓  Answer Generator ")
    st.caption("Your personal exam preparation assistant")
    st.divider()

    subject = st.selectbox(
        "📚 Choose Subject",
        [
            "Computer Science", "English", "Kannada",
            "Mathematics", "Science", "Social Science",
            "Commerce", "Other"
        ]
    )

    marks = st.select_slider(
        "📝 Answer Marks",
        options=[2, 5, 10, 15],
        value=5
    )

    language = st.selectbox(
        "🌐 Answer Language",
        ["English", "Kannada", "Hindi","Tamil","Telugu","Marathi","Malyalam","Urdu"]
    )

    style = st.selectbox(
        "✍️ Answer Style",
        [
            "Exam-friendly points",
            "Paragraph format",
            "Definition with example"
        ]
    )

    include_example = st.checkbox(
        "Include examples where useful", value=True
    )

    st.divider()
    st.caption("Powered by Python, Streamlit and Groq AI")

# ---------- HEADER ----------
st.markdown("""
<div class="hero">
    <h1>🎓 Answer Generator </h1>
    <p>Your smart companion for exam preparation.</p>
    <p>Generate clear, simple and mark-oriented answers in seconds.</p>
</div>
""", unsafe_allow_html=True)

# ---------- FEATURE CARDS ----------
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="info-card">
        <h3>📖 Smart Answers</h3>
        <p>Understand difficult topics in simple language.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="info-card">
        <h3>🎯 Marks-Based</h3>
        <p>Prepare answers for 2, 5, 10 or 15 marks.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="info-card">
        <h3>⚡ Quick Revision</h3>
        <p>Get organized points for exam preparation.</p>
    </div>
    """, unsafe_allow_html=True)

# ---------- QUESTION INPUT ----------
st.markdown(
    '<div class="section-title">✍️ Enter Your Exam Question</div>',
    unsafe_allow_html=True
)

question = st.text_area(
    "Question",
    placeholder="Example: Explain the OOP concepts in Java...",
    height=130,
    label_visibility="collapsed"
)

notes = st.text_area(
    "Additional notes (optional)",
    placeholder="Paste your textbook notes here to guide the answer...",
    height=90
)

left, right = st.columns([1, 1])

with left:
    st.caption(f"📚 Subject: {subject}  |  📝 Marks: {marks}")

with right:
    st.caption(f"🌐 Language: {language}")

# ---------- GENERATE ANSWER ----------
if st.button("✨ Generate My Exam Answer", use_container_width=True):

    if not question.strip():
        st.warning("Please enter your question first.")

    elif not API_KEY:
        st.error(
            "API key not found. Check your .env file and "
            "make sure GROQ_API_KEY is set correctly."
        )

    else:
        prompt = f"""
You are an expert student exam preparation assistant.

Subject: {subject}
Question: {question}
Marks: {marks}
Language: {language}
Answer style: {style}
Include examples: {include_example}

Student notes:
{notes if notes.strip() else "No notes provided."}

Instructions:
- Answer in the selected language.
- Use clear, simple, student-friendly language.
- Match the detail to the marks.
- For 2 marks, provide a concise answer.
- For 5 marks, provide an introduction and key points.
- For 10 or 15 marks, provide a detailed, structured answer.
- Use headings, numbered points and examples where appropriate.
- Do not invent facts.
- Use student notes when relevant, but correct mistakes.
- Make the response suitable for exam revision.
"""

        try:
            client = Groq(api_key=API_KEY)

            with st.spinner("✨ Preparing your exam-ready answer..."):
                response = client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are a helpful educational assistant. "
                                "Generate accurate, well-structured answers."
                            )
                        },
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.4,
                    max_tokens=2200,
                    stream=True
                )

                st.markdown("---")
                st.markdown(
                    '<div class="section-title">📘 Your Generated Answer</div>',
                    unsafe_allow_html=True
                )

                def stream_answer():
                    for chunk in response:
                        text = chunk.choices[0].delta.content
                        if text:
                            yield text

                st.write_stream(stream_answer())

            st.success("Your answer is ready!")
            st.caption(
                "Study tip: Review important facts with your textbook."
            )

        except Exception as error:
            st.error(f"Unable to generate answer: {error}")

# ---------- FOOTER ----------
st.markdown("---")
st.markdown(
    "<center>🎓 <b>ExamGenius AI</b> | Learn smarter. "
    "Revise faster. Prepare better.</center>",
    unsafe_allow_html=True
)
