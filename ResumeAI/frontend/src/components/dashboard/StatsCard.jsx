import "./StatsCard.css";
import { motion } from "framer-motion";

export default function StatsCard({
  icon,
  title,
  value,
  progress,
  change,
  color
}) {
  return (
    <motion.div
      className="stats-card"
      whileHover={{ y: -6 }}
      transition={{ duration: .25 }}
    >
      <div
        className="icon-box"
        style={{ background: color }}
      >
        {icon}
      </div>

      <h2>{value}</h2>

      <h4>{title}</h4>

      <div className="progress">

        <div
          className="progress-fill"
          style={{
            width: `${progress}%`,
            background: color
          }}
        />

      </div>

      <p>{change}</p>

    </motion.div>
  );
}