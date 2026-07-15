import "./Sidebar.css";

import {
  LayoutDashboard,
  FileText,
  Target,
  Sparkles,
  BarChart3,
  Settings,
} from "lucide-react";

import { NavLink } from "react-router-dom";

const menu = [
  {
    title: "Dashboard",
    icon: LayoutDashboard,
    path: "/",
  },
  {
    title: "Resume",
    icon: FileText,
    path: "/resume",
  },
  {
    title: "ATS Report",
    icon: Target,
    path: "/ats",
  },
  {
    title: "AI Review",
    icon: Sparkles,
    path: "/ai",
  },
  {
    title: "Analytics",
    icon: BarChart3,
    path: "/analytics",
  },
];

export default function Sidebar() {
  return (
    <aside className="sidebar">

      <div className="logo">

        <div className="logo-circle">
          ✨
        </div>

        <div>

          <h2>ResumeAI</h2>

          <p>AI Resume Assistant</p>

        </div>

      </div>

      <div className="divider" />

      <nav>

        {menu.map((item) => {

          const Icon = item.icon;

          return (

            <NavLink
              key={item.title}
              to={item.path}
              className={({ isActive }) =>
                isActive
                  ? "nav-item active"
                  : "nav-item"
              }
            >

              <Icon size={20} />

              <span>{item.title}</span>

            </NavLink>

          );
        })}

      </nav>

      <div className="bottom">

        <div className="divider" />

        <NavLink
          to="/settings"
          className={({ isActive }) =>
            isActive
              ? "nav-item active"
              : "nav-item"
          }
        >

          <Settings size={20} />

          <span>Settings</span>

        </NavLink>

        <div className="version">

          Version 1.0

        </div>

      </div>

    </aside>
  );
}