from typing import List, Dict


def calculate_ats_score(
    resume_skills: List[str],
    jd_skills: List[str]
) -> Dict[str, object]:
    """
    Calculate ATS score by comparing resume skills
    with job description skills.
    """

    resume_skills = resume_skills or []
    jd_skills = jd_skills or []

    resume_set = {
        skill.lower().strip()
        for skill in resume_skills
        if skill and skill.strip()
    }

    jd_set = {
        skill.lower().strip()
        for skill in jd_skills
        if skill and skill.strip()
    }

    matched = sorted(resume_set & jd_set)
    missing = sorted(jd_set - resume_set)
    additional = sorted(resume_set - jd_set)

    score = (
        round((len(matched) / len(jd_set)) * 100)
        if jd_set
        else 0
    )

    if score >= 90:
        verdict = "Excellent Match"
    elif score >= 75:
        verdict = "Good Match"
    elif score >= 60:
        verdict = "Average Match"
    else:
        verdict = "Poor Match"

    return {
        "score": score,
        "verdict": verdict,
        "matched": matched,
        "missing": missing,
        "additional": additional,
        "matched_count": len(matched),
        "missing_count": len(missing),
        "required_skills": len(jd_set),
    }