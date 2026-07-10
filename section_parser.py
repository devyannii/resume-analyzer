import re

HEADINGS = {
    "summary": "summary",
    "career objective": "summary",
    "professional summary": "summary",
    "objective": "summary",
    "profile": "summary",

    "education": "education",
    "academic background": "education",
    "qualification": "education",

    "experience": "experience",
    "work experience": "experience",
    "professional experience": "experience",
    "relevant experience": "experience",
    "employment history": "experience",

    "projects": "projects",
    "project": "projects",
    "academic projects": "projects",
    "personal projects": "projects",

    "skills": "skills",
    "technical skills": "skills",
    "technical proficiencies": "skills",

    "certifications": "certifications",

    "internships": "internships",

    "achievements": "achievements"
}


def normalize(text: str) -> str:
    return re.sub(r"[^a-z ]", "", text.lower()).strip()


def extract_sections(text: str):

    sections = {"other": []}

    current = "other"

    for line in text.splitlines():

        clean = line.strip()

        if not clean:
            continue

        normalized = normalize(clean)

        if normalized in HEADINGS:

            current = HEADINGS[normalized]

            sections.setdefault(current, [])

            continue

        sections.setdefault(current, []).append(clean)

    return sections