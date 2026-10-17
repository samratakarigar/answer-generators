# 🎓 ExamGenius AI – Student Exam Answer Generator

## 📌 About the Project

**ExamGenius AI** is an AI-powered web application that helps students generate exam-oriented answers quickly and easily. Students can enter a question, select the subject, choose the marks, and specify their preferred language and answer style.

The application uses Generative AI to produce clear, structured, and easy-to-understand answers suitable for exam preparation.

## 🎯 Objectives

- Generate answers automatically using Artificial Intelligence.
- Provide answers according to the marks allotted.
- Help students understand difficult topics in simple language.
- Save time during exam preparation.
- Provide a user-friendly and interactive interface.

## ✨ Features

- **AI Answer Generation:** Generates answers based on user questions.
- **Marks-Based Answers:** Supports different answer lengths, such as 2, 5, and 10 marks.
- **Multiple Subjects:** Supports subjects such as Python, Java, DBMS, and other topics.
- **Multiple Languages:** Can generate answers in supported languages, depending on the application configuration.
- **Exam-Friendly Format:** Produces structured explanations and key points.
- **Interactive Interface:** Uses Streamlit for an easy-to-use web application.
- **AI Integration:** Connects to an AI language model through the Groq API.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Web application interface |
| Groq API | AI-powered answer generation |
| Groq Python SDK | Communication with the AI model |
| python-dotenv | Loading environment variables |
| Python os module | Accessing environment variables |

## 📂 Project Structure

```text
ExamGenius-AI/
│
├── app.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

- `app.py` – Contains the main application code.
- `.env` – Stores the API key securely.
- `.gitignore` – Prevents sensitive and unnecessary files from being uploaded to Git.
- `requirements.txt` – Lists the Python packages required by the project.
- `README.md` – Provides project documentation.

## ⚙️ Installation and Setup

### Step 1: Install Python

Download and install Python from:

https://www.python.org/downloads/

### Step 2: Open the project folder

Open your project folder in Visual Studio Code.

Open the terminal using **Terminal → New Terminal**.

### Step 3: Install the required packages

Run the following command:

```bash
pip install streamlit groq python-dotenv
```

Alternatively, if you have a `requirements.txt` file, run:

```bash
pip install -r requirements.txt
```

### Step 4: Configure the API key

Create a `.env` file in the project folder and add your Groq API key:

```env
GROQ_API_KEY=your_actual_api_key
```

Get your API key from:

https://console.groq.com/

Replace `your_actual_api_key` with your own valid API key. Never share your API key publicly.

### Step 5: Run the application

Execute this command in the terminal:

```bash
python -m streamlit run app.py
```

Streamlit will start the local web server and provide a URL, usually:

```text
http://localhost:8501
```

Open the URL in your browser to use the application.

## 🚀 How to Use

1. Open the ExamGenius AI web application.
2. Enter your exam question in the input box.
3. Select the relevant subject.
4. Choose the required marks or answer length.
5. Select the preferred language and answer style, if available.
6. Click the Generate Answer button.
7. Read the generated answer displayed on the screen.

## 🔄 Working Principle

1. **User Input:** The student enters a question and selects the required options.
2. **Prompt Creation:** The Python program combines the question and selected options into a prompt.
3. **API Request:** The application sends the prompt to the Groq API.
4. **AI Processing:** The configured AI model processes the prompt and generates an answer.
5. **Output Display:** Streamlit displays the generated answer to the student.

## 💡 Example

**Input Question:** Explain the features of Python.

**Subject:** Python

**Marks:** 5

**Expected Output:**
- Simple and easy-to-learn language.
- Interpreted programming language.
- Supports object-oriented programming.
- Portable across different operating systems.
- Provides a large standard library.

*The actual answer may vary depending on the prompt and AI model.*

## ⚠️ Limitations

- An internet connection is generally required for AI answer generation.
- A valid API key is required.
- API usage limits and service availability may affect answer generation.
- Generated answers may occasionally contain incorrect or incomplete information.
- Students should verify important facts using textbooks or reliable educational sources.

## 🔮 Future Enhancements

- Upload PDF notes and generate answers from them.
- Generate multiple-choice questions and quizzes.
- Add voice input for questions.
- Allow students to download answers as PDF files.
- Add a question history feature.
- Provide personalized study plans.
- Improve answer formatting with headings, examples, and important keywords.

## 🔐 Security

- Store API keys in the `.env` file.
- Never upload `.env` to a public GitHub repository.
- Add `.env` to `.gitignore`.
- Do not expose API keys in screenshots, presentations, or source code.

## 👩‍🎓 Conclusion

ExamGenius AI demonstrates how Generative AI can be used to support students in exam preparation. By combining Python, Streamlit, and the Groq API, the project provides an interactive way to generate structured answers and understand academic topics more efficiently.

**Project Name:** ExamGenius AI – Student Exam Answer Generator

**Developed Using:** Python, Streamlit, and Groq API

**Purpose:** To make exam preparation easier, faster, and more accessible for students.

---

