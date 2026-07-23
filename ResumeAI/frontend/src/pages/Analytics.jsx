import "./Analytics.css";
import { motion } from "framer-motion";
import {
  BarChart3,
  TrendingUp,
  FileText,
  Target,
} from "lucide-react";

export default function Analytics() {
  return (
    <div className="analytics-page">

      <div className="analytics-header">
        <h1>Analytics</h1>
        <p>Track your resume performance over time.</p>
      </div>

      <div className="analytics-cards">

        <motion.div whileHover={{ y: -5 }} className="analytics-card">
          <BarChart3 size={30}/>
          <h2>12</h2>
          <p>Total Resumes</p>
        </motion.div>

        <motion.div whileHover={{ y: -5 }} className="analytics-card">
          <Target size={30}/>
          <h2>82%</h2>
          <p>Average ATS Score</p>
        </motion.div>

        <motion.div whileHover={{ y: -5 }} className="analytics-card">
          <TrendingUp size={30}/>
          <h2>+14%</h2>
          <p>Improvement</p>
        </motion.div>

        <motion.div whileHover={{ y: -5 }} className="analytics-card">
          <FileText size={30}/>
          <h2>28</h2>
          <p>AI Reviews</p>
        </motion.div>

      </div>

      <motion.div whileHover={{ y: -5 }} className="chart-card">

        <h2>Resume Performance</h2>

        <div className="fake-chart">

          <div style={{height:"45%"}}></div>
          <div style={{height:"60%"}}></div>
          <div style={{height:"72%"}}></div>
          <div style={{height:"82%"}}></div>
          <div style={{height:"76%"}}></div>
          <div style={{height:"90%"}}></div>

        </div>

      </motion.div>

    </div>
  );
}