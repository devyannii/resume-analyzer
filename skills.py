import re

SKILLS = [
    "python",
    "java",
    "c",
    "c++",
    "sql",
    "mysql",
    "mongodb",
    "postgresql",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "opencv",
    "streamlit",
    "flask",
    "fastapi",
    "django",
    "react",
    "spring boot",
    "docker",
    "kubernetes",
    "aws",
    "git",
    "github",
    "html",
    "css",
    "javascript"
]

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        if re.search(r'\b' + re.escape(skill) + r'\b', text):
            found_skills.append(skill.title())

    return sorted(found_skills)