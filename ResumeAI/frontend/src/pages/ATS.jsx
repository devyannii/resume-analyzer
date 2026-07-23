import "./ATS.css";
import { CheckCircle2, XCircle, Sparkles } from "lucide-react";
import { motion } from "framer-motion";

const matchedSkills = [
  "React",
  "JavaScript",
  "HTML",
  "CSS",
  "Git",
  "REST API",
];

const missingSkills = [
  "Docker",
  "AWS",
  "TypeScript",
  "CI/CD",
];

export default function ATS() {
  return (
    <div className="ats-page">

      <div className="ats-header">
        <h1>ATS Report</h1>
        <p>Analyze how well your resume matches the job description.</p>
      </div>

      <div className="ats-grid">

        {/* Score Card */}

        <motion.div
          whileHover={{ y: -5 }}
          className="score-card"
        >

          <div className="score-circle">
            <span>82%</span>
          </div>

          <h2>Excellent Match</h2>

          <p>
            Your resume matches most ATS requirements.
          </p>

        </motion.div>

        {/* Breakdown */}

        <motion.div
          whileHover={{ y: -5 }}
          className="breakdown-card"
        >

          <h2>Score Breakdown</h2>

          <div className="progress-item">
            <span>Skills</span>
            <progress value="90" max="100"></progress>
          </div>

          <div className="progress-item">
            <span>Experience</span>
            <progress value="82" max="100"></progress>
          </div>

          <div className="progress-item">
            <span>Projects</span>
            <progress value="78" max="100"></progress>
          </div>

          <div className="progress-item">
            <span>Education</span>
            <progress value="95" max="100"></progress>
          </div>

        </motion.div>

      </div>

      <div className="skills-grid">

        <motion.div
          whileHover={{ y: -5 }}
          className="skills-card"
        >

          <h2>
            <CheckCircle2 size={20} />
            Matched Skills
          </h2>

          <div className="skill-list">

            {matchedSkills.map((skill) => (
              <span key={skill}>{skill}</span>
            ))}

          </div>

        </motion.div>

        <motion.div
          whileHover={{ y: -5 }}
          className="skills-card"
        >

          <h2>
            <XCircle size={20} />
            Missing Skills
          </h2>

          <div className="skill-list">

            {missingSkills.map((skill) => (
              <span key={skill}>{skill}</span>
            ))}

          </div>

        </motion.div>

        <motion.div
          whileHover={{ y: -5 }}
          className="skills-card suggestions"
        >

          <h2>
            <Sparkles size={20} />
            AI Suggestions
          </h2>

          <ul>
            <li>Add Docker to your projects.</li>
            <li>Include measurable achievements.</li>
            <li>Mention cloud technologies.</li>
            <li>Use stronger action verbs.</li>
          </ul>

        </motion.div>

      </div>

    </div>
  );
}