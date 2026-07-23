import "./Resume.css";
import { useState } from "react";
import {
  Upload,
  Eye,
  Trash2,
  FileText,
  FileUp,
} from "lucide-react";
import { motion } from "framer-motion";

export default function Resume() {
  const [selectedFile, setSelectedFile] = useState(null);

  const resumes = [
    {
      id: 1,
      name: "Software_Engineer_Resume.pdf",
      score: 82,
      date: "Today",
    },
    {
      id: 2,
      name: "Frontend_Developer.pdf",
      score: 91,
      date: "Yesterday",
    },
    {
      id: 3,
      name: "Intern_Resume.pdf",
      score: 76,
      date: "2 days ago",
    },
  ];

  const handleFileChange = (e) => {
    if (e.target.files.length > 0) {
      setSelectedFile(e.target.files[0]);
    }
  };

  return (
    <div className="resume-page">

      <div className="resume-header">
        <h1>Resume Management</h1>
        <p>Upload and manage your resumes</p>
      </div>

      <div className="resume-content">

        <motion.div
          whileHover={{ y: -5 }}
          className="upload-section"
        >
          <FileUp size={60} />

          <h2>Upload Resume</h2>

          <p>
            Drag & Drop your resume
            <br />
            PDF • DOC • DOCX
          </p>

          <label className="browse-btn">
            <Upload size={18} />
            Browse Files

            <input
              type="file"
              accept=".pdf,.doc,.docx"
              hidden
              onChange={handleFileChange}
            />
          </label>

          {selectedFile && (
            <div className="selected-file">
              ✔ {selectedFile.name}
            </div>
          )}

          <button className="analyze-btn">
            Analyze Resume
          </button>
        </motion.div>

        <motion.div
          whileHover={{ y: -5 }}
          className="history-section"
        >
          <div className="history-header">
            <h2>Recent Uploads</h2>
          </div>

          <div className="history-list">

            {resumes.map((resume) => (

              <div className="resume-card" key={resume.id}>

                <div className="resume-info">

                  <div className="pdf-icon">
                    <FileText size={22} />
                  </div>

                  <div>
                    <h3>{resume.name}</h3>
                    <span>{resume.date}</span>
                  </div>

                </div>

                <div className="resume-score">
                  {resume.score}%
                </div>

                <div className="resume-actions">

                  <button>
                    <Eye size={18}/>
                  </button>

                  <button>
                    <Trash2 size={18}/>
                  </button>

                </div>

              </div>

            ))}

          </div>

        </motion.div>

      </div>

    </div>
  );
}