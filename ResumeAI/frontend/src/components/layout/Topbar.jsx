import "./Topbar.css";

export default function Topbar() {
  return (
    <header className="topbar">

      <div>
        <h2>Good Evening 👋</h2>
        <p>Let's improve your resume today.</p>
      </div>

      <div className="profile">

        <input
          type="text"
          placeholder="Search..."
        />

        <button>🔔</button>

        <div className="avatar">
          D
        </div>

      </div>

    </header>
  );
}