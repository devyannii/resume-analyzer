import "./Dashboard.css";

import Hero from "../components/dashboard/Hero";
import StatsCard from "../components/dashboard/StatsCard";

import {
  Target,
  FileText,
  Brain,
  Sparkles,
} from "lucide-react";

export default function Dashboard() {
  return (
    <div className="dashboard">

      <Hero />

      <div className="stats-grid">

        <StatsCard
          icon={<Target size={24} />}
          title="ATS Score"
          value="82%"
          progress={82}
          change="+6% since last upload"
          color="#80A1D4"
        />

        <StatsCard
          icon={<FileText size={24} />}
          title="Resumes"
          value="12"
          progress={40}
          change="Uploaded this month"
          color="#75C9C8"
        />

        <StatsCard
          icon={<Brain size={24} />}
          title="AI Reviews"
          value="28"
          progress={90}
          change="Completed"
          color="#C089DD"
        />

        <StatsCard
          icon={<Sparkles size={24} />}
          title="Skills"
          value="94%"
          progress={94}
          change="Skills matched"
          color="#D8D0E8"
        />

      </div>

      <div className="bottom-grid">

        <div className="coming-soon">
          Recent Activity
        </div>

        <div className="coming-soon">
          AI Suggestions
        </div>

      </div>

    </div>
  );
}