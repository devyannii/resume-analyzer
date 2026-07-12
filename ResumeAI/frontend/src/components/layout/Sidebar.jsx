import { NavLink } from "react-router-dom"
import     {
    LayoutDashboard,
    FileText,
    BarChart3,
    Bot,
    LineChart,
    Settings,
}   from "lucide-react";

const menuItems = [
  {
    title: "Dashboard",
    path: "/",
    icon: LayoutDashboard,
  },
  {
    title: "Resume",
    path: "/resume",
    icon: FileText,
  },
  {
    title: "ATS Report",
    path: "/ats",
    icon: BarChart3,
  },
  {
    title: "AI Review",
    path: "/ai",
    icon: Bot,
  },
  {
    title: "Analytics",
    path: "/analytics",
    icon: LineChart,
  },
  {
    title: "Settings",
    path: "/settings",
    icon: Settings,
  },
];

export default function Sidebar() {
  return (
    <aside className="w-72 bg-[#193A31] h-screen flex flex-col p-6">

      {/* Logo */}

      <h1 className="text-3xl font-bold text-[#3EB9A8] mb-12">
        ResumeAI
      </h1>

      {/* Navigation */}

      <nav className="flex flex-col gap-3">

        {menuItems.map((item) => {

          const Icon = item.icon;

          return (

            <NavLink
              key={item.title}
              to={item.path}
              className={({ isActive }) =>
                `
                flex
                items-center
                gap-4
                px-5
                py-4
                rounded-xl
                transition-all
                duration-300

                ${
                  isActive
                    ? "bg-[#3EB9A8] text-black"
                    : "text-gray-300 hover:bg-[#1D6C61]"
                }
                `
              }
            >
              <Icon size={22} />

              <span className="font-medium">
                {item.title}
              </span>

            </NavLink>

          );
        })}
      </nav>

      {/* Footer */}

      <div className="mt-auto text-gray-400 text-sm">

        ResumeAI v1.0

      </div>

    </aside>
  );
}