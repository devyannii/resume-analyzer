import "./UploadCard.css";
import { UploadCloud } from "lucide-react";

export default function UploadCard() {
  return (
    <div className="upload-card">
      <UploadCloud size={60} />

      <h3>Upload Resume</h3>

      <p>
        Drag & Drop your resume here
        <br />
        or click Browse Files.
      </p>

      <button>Browse Files</button>

      <span>PDF • DOCX • Max 5MB</span>
    </div>
  );
}