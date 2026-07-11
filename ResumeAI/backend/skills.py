from pathlib import Path
from typing import List
import pandas as pd
import re

# ---------------------------------
# Load Skills Database
# ---------------------------------

BASE_DIR = Path(__file__).resolve().parent
SKILLS_FILE = BASE_DIR / "data" / "skills.csv"

skills_df = pd.read_csv(SKILLS_FILE)

if "skill" not in skills_df.columns:
    raise ValueError(
        "skills.csv must contain a 'skill' column."
    )

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
    skill: re.compile(
        rf"\b{re.escape(skill.lower())}\b"
    )
    for skill in SKILLS
}


def extract_skills(text: str | None) -> List[str]:
    """
    Extract matching skills from resume text.

    Args:
        text: Resume or Job Description text.

    Returns:
        Alphabetically sorted list of detected skills.
    """

    text = (text or "").lower()
    text = " ".join(text.split())

    if not text:
        return []

    found = set()

    for skill, pattern in SKILL_PATTERNS.items():

        if pattern.search(text):
            found.add(skill)

    return sorted(found, key=str.lower)