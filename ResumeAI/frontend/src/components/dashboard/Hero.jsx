import "./Hero.css";
import { Upload, CheckCircle2 } from "lucide-react";
import { motion } from "framer-motion";

export default function Hero() {
  return (
    <motion.section
      className="hero"
      initial={{ opacity: 0, y: 25 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
    >
      {/* LEFT */}

      <div className="hero-left">

        <span className="hero-badge">
          ✨ AI Resume Assistant
        </span>

        <h1>
          Welcome back,
          <span> Devyani 👋</span>
        </h1>

        <p>
          Upload your resume and receive ATS scoring,
          AI-powered feedback and personalized suggestions.
        </p>

        <button className="upload-btn">
          <Upload size={18}/>
          Upload Resume
        </button>

      </div>

      {/* RIGHT */}

      <div className="hero-right">

        <div className="score-card">

          <p className="score-title">
            Resume Score
          </p>

          <h2>82%</h2>

          <div className="status">

            <div>
              <CheckCircle2 size={18}/>
              ATS Passed
            </div>

            <div>
              <CheckCircle2 size={18}/>
              AI Review Complete
            </div>

            <div>
              <CheckCircle2 size={18}/>
              Skills Extracted
            </div>

          </div>

        </div>

      </div>

    </motion.section>
  );
}