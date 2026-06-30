import streamlit as st
from parser import extract_text

st.set_page_config(page_title="Resume Analyzer")

st.title("📄 Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    text = extract_text(uploaded_file)

    st.success("Resume Uploaded Successfully!")

    st.subheader("Extracted Text")

    st.text_area(
        "Resume Content",
        text,
        height=300
    )