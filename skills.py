from pathlib import Path
import pandas as pd
import re

# -------------------------------
# Load Skills
# -------------------------------

BASE_DIR = Path(__file__).resolve().parent
SKILLS_FILE = BASE_DIR / "data" / "skills.csv"

skills_df = pd.read_csv(SKILLS_FILE)

SKILLS = (
    skills_df["skill"]
    .dropna()
    .astype(str)
    .str.strip()
    .unique()
    .tolist()
)

# Compile regex patterns once
SKILL_PATTERNS = {
    skill: re.compile(r"\b" + re.escape(skill.lower()) + r"\b")
    for skill in SKILLS
}


def extract_skills(text: str) -> list[str]:
    """
    Extract matching skills from resume text.
    """

    text = text.lower()

    found_skills = set()

    for skill, pattern in SKILL_PATTERNS.items():

        if pattern.search(text):
            found_skills.add(skill)

    return sorted(found_skills, key=str.lower)