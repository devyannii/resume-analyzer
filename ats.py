from typing import List, Dict


def calculate_ats_score(
    resume_skills: List[str],
    jd_skills: List[str]
) -> Dict:

    resume_set = {
        skill.lower().strip()
        for skill in resume_skills
    }

    jd_set = {
        skill.lower().strip()
        for skill in jd_skills
    }

    matched = sorted(resume_set & jd_set)

    missing = sorted(jd_set - resume_set)

    extra = sorted(resume_set - jd_set)

    score = 0

    if jd_set:
        score = round(
            (len(matched) / len(jd_set)) * 100
        )

    # Overall interpretation
    if score >= 85:
        verdict = "Excellent Match"

    elif score >= 70:
        verdict = "Good Match"

    elif score >= 50:
        verdict = "Average Match"

    else:
        verdict = "Poor Match"

    return {

        "score": score,

        "verdict": verdict,

        "matched": matched,

        "missing": missing,

        "extra": extra,

        "matched_count": len(matched),

        "missing_count": len(missing),

        "required_skills": len(jd_set)
    }