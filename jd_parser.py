import re

from skills import extract_skills


def parse_job_description(job_description: str) -> dict:
    """
    Parse a job description and extract useful information.

    Args:
        job_description (str): Raw job description.

    Returns:
        dict: Parsed job description.
    """

    if not job_description.strip():
        return {
            "text": "",
            "skills": []
        }

    # Remove extra blank lines and spaces
    cleaned_text = re.sub(r"\s+", " ", job_description).strip()

    skills = extract_skills(cleaned_text)

    return {
        "text": cleaned_text,
        "skills": skills
    }