from skills import extract_skills


def parse_job_description(job_description: str | None) -> dict[str, object]:
    """
    Parse a job description and extract useful information.

    Args:
        job_description: Raw job description text.

    Returns:
        Dictionary containing the cleaned job description
        and extracted skills.
    """

    job_description = (job_description or "").strip()

    if not job_description:
        return {
            "text": "",
            "skills": [],
            "word_count": 0,
            "character_count": 0,
        }

    cleaned_text = " ".join(job_description.split())

    skills = extract_skills(cleaned_text)

    return {
        "text": cleaned_text,
        "skills": skills,
        "word_count": len(cleaned_text.split()),
        "character_count": len(cleaned_text),
    }