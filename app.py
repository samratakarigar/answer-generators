
import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Load API key from .env file
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

# Page settings
st.set_page_config(
    page_title="Answer Generator",
    page_icon="📚",
    layout="centered"
)

# Application heading
st.title("📚  Answer Generator")
st.write(
    "Generate simple, exam-ready answers using Artificial Intelligence."
)

st.divider()

# Sidebar settings
st.sidebar.header("Answer Settings")

subject = st.sidebar.selectbox(
    "Select Subject",
    [
        "Computer Science",
        "English",
        "Kannada",
        "Mathematics",
        "Science",
        "Social Science",
        "Commerce",
        "Other"
    ]
)

marks = st.sidebar.selectbox(
    "Select Marks",
    [2, 5, 10, 15]
)

language = st.sidebar.selectbox(
    "Select Language",
    ["English", "Kannada", "Hindi","Marathi","Tamil","Telugu"]
)

answer_style = st.sidebar.selectbox(
    "Answer Format",
    [
        "Exam-friendly points",
        "Paragraph",
        "Definition with example"
    ]
)

# User question
question = st.text_area(
    "Enter your exam question",
    placeholder="Example: Explain OOP concepts in Java.",
    height=120
)

# Optional class notes
notes = st.text_area(
    "Add your class notes (optional)",
    placeholder="Paste your notes here...",
    height=100
)

# Generate answer
if st.button("✨ Generate Exam Answer", type="primary"):

    if not question.strip():
        st.warning("Please enter a question.")

    elif not API_KEY:
        st.error(
            "API key not found. Please add GROQ_API_KEY "
            "to your .env file."
        )

    else:
        try:
            client = Groq(api_key=API_KEY)

            prompt = f"""
You are an exam preparation assistant.

Subject: {subject}
Question: {question}
Marks: {marks}
Language: {language}
Answer format: {answer_style}

Student notes:
{notes if notes.strip() else "No notes provided."}

Instructions:
1. Give an accurate answer in the selected language.
2. Use simple, student-friendly language.
3. Match the length to the selected marks.
4. Use headings and numbered points where suitable.
5. Include examples when useful.
6. For 2 marks, give a concise answer.
7. For 5 marks, give an introduction and key points.
8. For 10 or 15 marks, give a detailed, organized answer.
9. Do not invent facts.
10. Make the answer suitable for exam preparation.
"""

            st.subheader("📝 Generated Answer")

            response = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a helpful educational assistant "
                            "that creates clear exam answers."
                        )
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.4,
                max_tokens=2200,
                stream=True
            )

            # Display answer as it is generated
            def generate_text():
                for chunk in response:
                    content = chunk.choices[0].delta.content
                    if content:
                        yield content

            st.write_stream(generate_text())

            st.success("Answer generated successfully!")
            st.info(
                "Please verify important facts with your textbook."
            )

        except Exception as error:
            st.error(
                f"Unable to generate answer: {error}"
            )

st.divider()

st.caption(
    "Student Exam Answer Generator | Python + Streamlit + Groq AI"
)
