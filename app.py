import html
from pathlib import Path

import streamlit as st

from ats import calculate_ats_score
from jd_parser import parse_job_description
from parser import extract_text
from section_parser import extract_sections
from skills import extract_skills


st.set_page_config(
    page_title="ResumeAI | Resume Analyzer",
    page_icon="📄",
    layout="wide",
)


def load_css() -> None:
    css_path = Path(__file__).parent / "assets" / "style.css"
    st.markdown(f"<style>{css_path.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)


load_css()
st.markdown(
    """
    <section class="hero">
        <div class="eyebrow">Career intelligence, simplified</div>
        <h1>Make every resume count.</h1>
        <p>Upload your resume, compare it with a role, and find the strongest next edits.</p>
    </section>
    """,
    unsafe_allow_html=True,
)

uploaded_file = st.file_uploader("Upload a resume", type=["pdf"])

if not uploaded_file:
    st.info("Start by uploading a PDF resume to unlock your personalized analysis.")
    st.stop()

resume_text = extract_text(uploaded_file)
skills = extract_skills(resume_text)
sections = extract_sections(resume_text)

st.success("Resume uploaded successfully. Your analysis is ready.")

st.subheader("Resume dashboard")
resume_words = len(resume_text.split())
populated_sections = sum(1 for content in sections.values() if content)
dashboard_columns = st.columns(4)
dashboard_columns[0].metric("Detected skills", len(skills))
dashboard_columns[1].metric("Resume sections", populated_sections)
dashboard_columns[2].metric("Resume length", f"{resume_words} words")
dashboard_columns[3].metric("Profile status", "Ready")

st.subheader("Detected skills")
if skills:
    skill_columns = st.columns(3)
    for index, skill in enumerate(skills):
        skill_columns[index % 3].success(skill.title())
else:
    st.warning("No skills were detected in this resume.")

st.subheader("Resume sections")
available_sections = [
    (section, content) for section, content in sections.items() if content
]
if available_sections:
    for index in range(0, len(available_sections), 2):
        card_columns = st.columns(2)
        for column, (section, content) in zip(card_columns, available_sections[index : index + 2]):
            preview = html.escape(" ".join(content[:2]))
            with column:
                st.markdown(
                    f"""
                    <article class="section-card">
                        <div class="section-card__label">{html.escape(section)}</div>
                        <div class="section-card__count">{len(content)} entries</div>
                        <p>{preview[:180]}</p>
                    </article>
                    """,
                    unsafe_allow_html=True,
                )
                with st.expander(f"View {section.title()}"):
                    for line in content:
                        st.markdown(f"- {line}")
else:
    st.info("No standard resume sections were identified.")

st.subheader("Resume content")
with st.expander("View extracted text"):
    st.text_area("Extracted text", resume_text, height=260, disabled=True)

st.subheader("Job description")
job_description = st.text_area(
    "Paste the job description to compare your resume",
    height=220,
    placeholder="Paste a role description here...",
)

if job_description.strip():
    job_data = parse_job_description(job_description)
    analysis = calculate_ats_score(skills, job_data["skills"])
    st.write(f"**{analysis['verdict']}** — ATS score: {analysis['score']}%")
