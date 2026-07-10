import html
from pathlib import Path

import streamlit as st

from ats import calculate_ats_score
from jd_parser import parse_job_description
from parser import extract_text
from section_parser import extract_sections
from skills import extract_skills


st.set_page_config(page_title="ResumeAI", page_icon="R", layout="wide")


def load_css() -> None:
    css_path = Path(__file__).parent / "assets" / "style.css"
    st.markdown(f"<style>{css_path.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)


def render_section_card(section: str, content: list[str]) -> None:
    preview = html.escape(" ".join(content[:2]))
    st.markdown(
        f"""
        <article class="section-card">
            <span>{html.escape(section)}</span>
            <strong>{len(content)} entries</strong>
            <p>{preview[:150]}</p>
        </article>
        """,
        unsafe_allow_html=True,
    )


load_css()
st.markdown(
    """
    <header class="topbar">
        <div class="brand-mark">R</div>
        <div><strong>ResumeAI</strong><small>Resume workspace</small></div>
        <div class="topbar-status">Smart resume analysis</div>
    </header>
    <section class="hero">
        <div>
            <p class="eyebrow">Your career workspace</p>
            <h1>Build a resume that<br>gets noticed.</h1>
            <p class="hero-copy">Understand your resume, surface your strongest skills, and tailor it for the role you want.</p>
        </div>
        <div class="hero-orb"><span>ATS</span><strong>Ready</strong></div>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="upload-card">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Drop your resume here", type=["pdf"])
st.caption("PDF only. Your resume stays in this session.")
st.markdown("</div>", unsafe_allow_html=True)

if not uploaded_file:
    st.markdown(
        """
        <div class="empty-state">
            <strong>Start with your resume</strong>
            <span>Upload a PDF to see your skills, sections, and role match in one place.</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.stop()

resume_text = extract_text(uploaded_file)
skills = extract_skills(resume_text)
sections = extract_sections(resume_text)
available_sections = [(section, content) for section, content in sections.items() if content]

overview_tab, resume_tab, match_tab = st.tabs(["Overview", "My resume", "Role match"])

with overview_tab:
    st.markdown('<p class="section-kicker">Resume overview</p>', unsafe_allow_html=True)
    metrics = st.columns(4)
    metrics[0].metric("Skills found", len(skills))
    metrics[1].metric("Sections", len(available_sections))
    metrics[2].metric("Word count", len(resume_text.split()))
    metrics[3].metric("Status", "Ready")

    st.markdown("#### Highlighted skills")
    if skills:
        st.markdown(
            "".join(f'<span class="skill-pill">{html.escape(skill.title())}</span>' for skill in skills[:18]),
            unsafe_allow_html=True,
        )
    else:
        st.info("No known skills were detected. Try a resume with a dedicated skills section.")

with resume_tab:
    st.markdown("#### Resume sections")
    if available_sections:
        for index in range(0, len(available_sections), 2):
            columns = st.columns(2)
            for column, (section, content) in zip(columns, available_sections[index : index + 2]):
                with column:
                    render_section_card(section, content)
                    with st.expander(f"View {section.title()}"):
                        for line in content:
                            st.markdown(f"- {line}")
    else:
        st.info("No standard sections were identified in this resume.")

    with st.expander("View extracted text"):
        st.text_area("Extracted text", resume_text, height=260, disabled=True)

with match_tab:
    st.markdown("#### Match your next role")
    job_description = st.text_area(
        "Paste a job description",
        height=190,
        placeholder="Paste the job description here...",
        label_visibility="collapsed",
    )
    if job_description.strip():
        job_data = parse_job_description(job_description)
        analysis = calculate_ats_score(skills, job_data["skills"])
        score, matched, missing = st.columns(3)
        score.metric("ATS score", f"{analysis['score']}%")
        matched.metric("Matched", analysis["matched_count"])
        missing.metric("To improve", analysis["missing_count"])
        st.progress(analysis["score"] / 100)

        if analysis["missing"]:
            st.markdown("#### Skills to consider adding")
            st.markdown(
                "".join(f'<span class="skill-pill muted-pill">{html.escape(skill.title())}</span>' for skill in analysis["missing"]),
                unsafe_allow_html=True,
            )
    else:
        st.info("Add a job description to see your ATS score and skill gaps.")
