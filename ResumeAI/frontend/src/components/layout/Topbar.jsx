import { Bell, Search, UserCircle } from "lucide-react";

export default function Topbar() {
  return (
    <header className="h-20 bg-[#193A31]/60 backdrop-blur-xl border-b border-white/10 flex items-center justify-between px-8">

      {/* Left */}

      <div>

        <h2 className="text-3xl font-bold text-white">
          Dashboard
        </h2>

        <p className="text-gray-400">
          Welcome back 👋
        </p>

      </div>

      {/* Right */}

      <div className="flex items-center gap-5">

        {/* Search */}

        <div className="flex items-center gap-3 bg-[#1D6C61] rounded-xl px-4 py-3">

          <Search size={18} className="text-gray-300" />

          <input
            type="text"
            placeholder="Search..."
            className="bg-transparent outline-none text-white placeholder:text-gray-400"
          />

        </div>

        {/* Notification */}

        <button className="w-12 h-12 rounded-xl bg-[#1D6C61] flex items-center justify-center hover:bg-[#3EB9A8] transition-all duration-300">

          <Bell />

        </button>

        {/* Profile */}

        <button className="flex items-center gap-3 bg-[#1D6C61] px-4 py-2 rounded-xl hover:bg-[#3EB9A8] transition-all duration-300">

          <UserCircle size={34} />

          <div>

            <p className="font-semibold">
              Devyani
            </p>

            <p className="text-xs text-gray-300">
              AI Developer
            </p>

          </div>

        </button>

      </div>

    </header>
  );
}