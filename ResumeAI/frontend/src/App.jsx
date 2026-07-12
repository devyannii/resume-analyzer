import { BrowserRouter, Routes, Route } from "react-router-dom";

import Layout from "./components/layout/Layout";

import Dashboard from "./pages/Dashboard";
import Resume from "./pages/Resume";
import ATS from "./pages/ATS";
import AIReview from "./pages/AIReview";
import Analytics from "./pages/Analytics";
import Settings from "./pages/Settings";

export default function App() {
  return (
    <BrowserRouter>

      <Layout>

        <Routes>

          <Route path="/" element={<Dashboard />} />

          <Route path="/resume" element={<Resume />} />

          <Route path="/ats" element={<ATS />} />

          <Route path="/ai" element={<AIReview />} />

          <Route path="/analytics" element={<Analytics />} />

          <Route path="/settings" element={<Settings />} />

        </Routes>

      </Layout>

    </BrowserRouter>
  );
}