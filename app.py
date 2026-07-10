import streamlit as st
from pathlib import Path

from parser import extract_text
from skills import extract_skills
from section_parser import extract_sections
from jd_parser import parse_job_description
from ats import calculate_ats_score


# ---------------------------------
# Page Config
# ---------------------------------
st.set_page_config(...)

def load_css():

    css = Path("assets/style.css").read_text()

    st.markdown(
        f"<style>{css}</style>",
        unsafe_allow_html=True
    )

load_css()
st.set_page_config(
    page_title="Resume Analyzer",
    page_icon="📄",
    layout="wide"
)
st.markdown("""
# 📄 ResumeAI

### AI Powered Resume Analyzer & ATS Checker
""")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

# ---------------------------------
# Resume Processing
# ---------------------------------

if uploaded_file:

    text = extract_text(uploaded_file)

    skills = extract_skills(text)

    sections = extract_sections(text)

    st.success("Resume Uploaded Successfully!")

    # Resume Content
    with st.expander("📄 Resume Content"):
        st.text_area(
            "Extracted Text",
            text,
            height=250
        )

    # Skills
    st.subheader("🛠 Detected Skills")

    if skills:

        cols = st.columns(3)

        for i, skill in enumerate(skills):
            cols[i % 3].success(skill)

    else:
        st.warning("No skills detected.")

    # Resume Sections
    st.subheader("📑 Resume Sections")
    st.subheader("📑 Resume Sections")

for section, content in sections.items():

    if content:

        with st.expander(f"📂 {section.title()}"):

            for line in content:

                st.markdown(f"- {line}")

    st.divider()

    # ---------------------------------
    # Job Description
    # ---------------------------------

    st.header("💼 Job Description")

    job_description = st.text_area(
        "Paste the Job Description",
        height=220
    )

    if job_description:

        jd = parse_job_description(job_description)

        result = calculate_ats_score(
            skills,
            jd["skills"]
        )

        st.subheader("📊 ATS Score")

        col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("ATS Score", f"{result['score']}%")

with col2:
    st.metric("Skills Found", len(skills))

with col3:
    st.metric("Matched", len(result["matched"]))

with col4:
    st.metric("Missing", len(result["missing"]))
        )

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("✅ Matched Skills")

            if result["matched"]:
                for skill in result["matched"]:
                    st.success(skill.title())
            else:
                st.info("No matching skills.")

        with col2:

            st.subheader("❌ Missing Skills")

            if result["missing"]:
                for skill in result["missing"]:
                    st.error(skill.title())
            else:
                st.success("No missing skills!")

        with st.expander("Job Description Skills"):
            st.write(jd["skills"])