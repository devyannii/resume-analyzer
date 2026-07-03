import streamlit as st
from parser import extract_text
from skills import extract_skills

st.set_page_config(page_title="Resume Analyzer")

st.title("📄 Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    # Extract text
    text = extract_text(uploaded_file)

    st.success("Resume Uploaded Successfully!")

    # Display extracted text
    st.subheader("Resume Content")
    st.text_area(
        "Resume Content",
        text,
        height=300
    )

    # Extract skills
    skills = extract_skills(text)

    st.subheader("Detected Skills")

    if skills:
        st.success(f"{len(skills)} Skills Found")

        cols = st.columns(3)

        for i, skill in enumerate(skills):
            cols[i % 3].success(skill)

    else:
        st.error("No Skills Found")