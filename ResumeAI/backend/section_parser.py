import re
from typing import Dict, List

HEADINGS = {
    "summary": [
        "summary",
        "professional summary",
        "career objective",
        "objective",
        "profile",
    ],
    "education": [
        "education",
        "academic background",
        "academic qualifications",
        "qualification",
        "qualifications",
    ],
    "experience": [
        "experience",
        "work experience",
        "professional experience",
        "employment",
        "employment history",
        "work history",
        "career history",
        "relevant experience",
    ],
    "projects": [
        "projects",
        "project",
        "academic projects",
        "personal projects",
    ],
    "skills": [
        "skills",
        "technical skills",
        "technical expertise",
        "technical proficiencies",
        "core competencies",
        "technologies",
    ],
    "certifications": [
        "certifications",
        "certificates",
        "licenses",
    ],
    "internships": [
        "internship",
        "internships",
    ],
    "achievements": [
        "achievements",
        "awards",
        "honors",
    ],
}


def normalize(text: str) -> str:
    """
    Normalize a line for heading comparison.
    """
    return re.sub(r"[^a-z ]", "", text.lower()).strip()


def get_section(normalized_line: str) -> str | None:
    """
    Return the matching section if the line is a heading.
    """

    for section, aliases in HEADINGS.items():

        for alias in aliases:

            if normalized_line == alias:
                return section

    return None


def extract_sections(text: str) -> Dict[str, List[str]]:
    """
    Split resume into logical sections.
    """

    sections = {
        "summary": [],
        "education": [],
        "experience": [],
        "projects": [],
        "skills": [],
        "certifications": [],
        "internships": [],
        "achievements": [],
        "other": [],
    }

    current_section = "other"

    for line in text.splitlines():

        clean = line.strip()

        if not clean:
            continue

        normalized = normalize(clean)

        detected = get_section(normalized)

        if detected:

            current_section = detected
            continue

        sections[current_section].append(clean)

    return sections