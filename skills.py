from pathlib import Path
import pandas as pd
import re

# -------------------------------
# Load skills from CSV
# -------------------------------

BASE_DIR = Path(__file__).resolve().parent
SKILLS_FILE = BASE_DIR / "data" / "skills.csv"

skills_df = pd.read_csv(SKILLS_FILE)

# Remove empty values and convert to a list
SKILLS = (
    skills_df["skill"]
    .dropna()
    .astype(str)
    .tolist()
)

# -------------------------------
# Extract Skills
# -------------------------------

def extract_skills(text):
    """
    Extract matching skills from resume text.

    Args:
        text (str): Resume text

    Returns:
        list: Sorted list of detected skills
    """

    text = text.lower()
    found_skills = set()

    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text):
            found_skills.add(skill)

    return sorted(found_skills)