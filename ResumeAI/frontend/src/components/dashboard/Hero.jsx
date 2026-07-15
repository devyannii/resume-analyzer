import "./Hero.css";

import { motion } from "framer-motion";

export default function Hero() {
  return (
    <motion.section
      className="hero"
      initial={{ opacity: 0, y: 25 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: .6 }}
    >

      <div className="hero-left">

        <p className="badge">
          ✨ AI Resume Assistant
        </p>

        <h1>

          Good Evening,
          <span> Devyani 👋</span>

        </h1>

        <p className="subtitle">

          Upload your resume and receive
          ATS scoring, AI feedback and
          personalized suggestions in seconds.

        </p>

        <button>

          Upload Resume

        </button>

      </div>

      <div className="hero-right">

        <div className="blob"></div>

      </div>

    </motion.section>
  );
}