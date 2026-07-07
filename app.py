import streamlit as st
import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

from interview import generate_questions
from evaluator import evaluate_answer

# ----------------------------------------------------
# Configuration
# ----------------------------------------------------

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error("❌ GEMINI_API_KEY not found in .env")
    st.stop()

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

os.makedirs("reports", exist_ok=True)

# ----------------------------------------------------
# Page Config
# ----------------------------------------------------

st.set_page_config(
    page_title="AI Interview Agent",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Interview Agent")
st.markdown("### Practice AI-powered technical interviews")

# ----------------------------------------------------
# User Input
# ----------------------------------------------------

role = st.selectbox(
    "Select Job Role",
    [
        "AI Engineer",
        "Machine Learning Engineer",
        "Data Scientist",
        "Python Developer",
        "Frontend Developer",
        "Backend Developer",
        "Custom"
    ]
)

experience = st.selectbox(
    "Experience",
    [
        "Fresher",
        "1-3 Years",
        "3-5 Years",
        "5+ Years"
    ]
)

# ----------------------------------------------------
# Generate Questions
# ----------------------------------------------------

if st.button("🚀 Start Interview"):

    with st.spinner("Generating interview questions..."):

        try:
            questions = generate_questions(model, role, experience)
            st.session_state.questions = questions

        except Exception as e:

            st.error("❌ Unable to generate interview questions.")

            if "429" in str(e):
                st.warning(
                    """
Gemini API quota exceeded.

Please wait for the quota to reset
or use another API key.
"""
                )
            else:
                st.error(str(e))

            st.stop()

# ----------------------------------------------------
# Interview Questions
# ----------------------------------------------------

if "questions" in st.session_state:

    st.header("📝 Interview Questions")

    for i, question in enumerate(st.session_state.questions, 1):

        st.markdown(f"### Question {i}")

        st.write(question)

        st.text_area(
            "Your Answer",
            key=f"answer_{i}",
            height=150
        )

    # ------------------------------------------------
    # Evaluate Interview
    # ------------------------------------------------

    if st.button("📊 Evaluate Interview"):

        st.header("📊 Interview Evaluation")

        total_score = 0

        report = {
            "role": role,
            "experience": experience,
            "overall_score": 0,
            "questions": []
        }

        for i, question in enumerate(st.session_state.questions, 1):

            answer = st.session_state.get(f"answer_{i}", "")

            # ----------------------------
            # Gemini Evaluation
            # ----------------------------

            try:

                result = evaluate_answer(
                    model,
                    question,
                    answer
                )

            except Exception as e:

                if "429" in str(e):

                    result = """
Score: 0/10

Evaluation unavailable because the Gemini API quota has been exceeded.
"""

                else:

                    result = f"""
Score: 0/10

Error:

{e}
"""

            # ----------------------------
            # Score Extraction
            # ----------------------------

            try:

                score_line = result.split("\n")[0]

                score = int(
                    score_line.split(":")[1]
                    .split("/")[0]
                    .strip()
                )

            except:

                score = 0

            total_score += score

            report["questions"].append(
                {
                    "question": question,
                    "answer": answer,
                    "evaluation": result,
                    "score": score
                }
            )

            # ----------------------------
            # Display
            # ----------------------------

            with st.expander(
                f"📋 Question {i}",
                expanded=False
            ):

                st.markdown("### ❓ Question")
                st.write(question)

                st.markdown("### ✍️ Your Answer")
                st.write(answer)

                st.markdown("### 🤖 AI Evaluation")
                st.markdown(result)

        # ------------------------------------------------
        # Overall Score
        # ------------------------------------------------

        report["overall_score"] = total_score

        percentage = (total_score / 50) * 100

        st.divider()

        st.metric(
            label="Overall Interview Score",
            value=f"{total_score}/50",
            delta=f"{percentage:.1f}%"
        )

        # ------------------------------------------------
        # Recommendation
        # ------------------------------------------------

        if percentage >= 80:

            st.success("✅ Hiring Recommendation: Hire")

        elif percentage >= 60:

            st.info("🟡 Hiring Recommendation: Consider")

        else:

            st.error("🔴 Hiring Recommendation: Needs Improvement")

        # ------------------------------------------------
        # Save Report
        # ------------------------------------------------

        report_path = "reports/interview_report.json"

        with open(report_path, "w") as f:

            json.dump(report, f, indent=4)

        st.success("✅ Interview report saved successfully!")

        # ------------------------------------------------
        # Download
        # ------------------------------------------------

        json_string = json.dumps(
            report,
            indent=4
        )

        st.download_button(
            label="📥 Download Interview Report",
            data=json_string,
            file_name="interview_report.json",
            mime="application/json"
        )

        st.caption(f"Saved locally: {report_path}")