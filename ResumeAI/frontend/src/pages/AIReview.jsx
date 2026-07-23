import "./AIReview.css";
import { motion } from "framer-motion";
import { CheckCircle2, AlertTriangle, Sparkles } from "lucide-react";

export default function AIReview() {
  return (
    <div className="review-page">

      <div className="review-header">
        <h1>AI Resume Review</h1>
        <p>Personalized feedback to improve your resume.</p>
      </div>

      <div className="review-grid">

        <motion.div whileHover={{ y: -5 }} className="review-card">
          <h2>
            <CheckCircle2 size={20} />
            Strengths
          </h2>

          <ul>
            <li>Strong technical skills.</li>
            <li>Projects are well described.</li>
            <li>Good ATS keyword coverage.</li>
            <li>Clean formatting.</li>
          </ul>
        </motion.div>

        <motion.div whileHover={{ y: -5 }} className="review-card">
          <h2>
            <AlertTriangle size={20} />
            Improvements
          </h2>

          <ul>
            <li>Add more measurable achievements.</li>
            <li>Improve work experience section.</li>
            <li>Add certifications.</li>
            <li>Reduce lengthy descriptions.</li>
          </ul>
        </motion.div>

      </div>

      <motion.div whileHover={{ y: -5 }} className="suggestion-card">

        <h2>
          <Sparkles size={20} />
          AI Suggestions
        </h2>

        <div className="tips">

          <div className="tip">
            Use action verbs like <b>Developed</b>, <b>Designed</b>, and <b>Implemented</b>.
          </div>

          <div className="tip">
            Mention tools such as Docker, AWS, and CI/CD if you've worked with them.
          </div>

          <div className="tip">
            Quantify your achievements whenever possible.
          </div>

          <div className="tip">
            Keep your resume to one page for fresher and internship roles.
          </div>

        </div>

      </motion.div>

    </div>
  );
}