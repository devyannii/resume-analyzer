from pathlib import Path

from flask import Flask, jsonify, request, send_from_directory

from ats import calculate_ats_score
from jd_parser import parse_job_description
from parser import extract_text
from section_parser import extract_sections
from skills import extract_skills

BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__, static_folder=str(BASE_DIR / "assets"))


@app.get("/")
def index():
    return send_from_directory(BASE_DIR, "index.html")


@app.post("/api/analyze")
def analyze_resume():
    resume = request.files.get("resume")
    if resume is None or not resume.filename.lower().endswith(".pdf"):
        return jsonify(error="Please upload a PDF resume."), 400
    try:
        text = extract_text(resume)
    except RuntimeError as error:
        return jsonify(error=str(error)), 400
    sections = extract_sections(text)
    return jsonify(
        skills=extract_skills(text),
        sections={name: content for name, content in sections.items() if content},
        word_count=len(text.split()),
    )


@app.post("/api/match")
def match_role():
    payload = request.get_json(silent=True) or {}
    description = str(payload.get("job_description", "")).strip()
    resume_skills = payload.get("resume_skills", [])
    if not description:
        return jsonify(error="Paste a job description to continue."), 400
    if not isinstance(resume_skills, list):
        return jsonify(error="Resume skills must be a list."), 400
    return jsonify(calculate_ats_score(resume_skills, parse_job_description(description)["skills"]))


if __name__ == "__main__":
    app.run(debug=True)
