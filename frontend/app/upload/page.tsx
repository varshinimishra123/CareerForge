"use client";

import { useState } from "react";
import { uploadResume } from "../../services/resume";

export default function UploadPage() {
  const [file, setFile] = useState<File | null>(null);
  const [result, setResult] = useState<any>(null);

  const handleUpload = async (
    e: React.FormEvent
  ) => {
    e.preventDefault();

    if (!file) {
      alert("Please select a PDF");
      return;
    }

    try {
      const data = await uploadResume(file);
      setResult(data);
    } catch (error) {
      console.error(error);
      alert("Upload failed");
    }
  };

  return (
    <div style={{ padding: "30px" }}>
      <h1>Upload Resume</h1>

      <form onSubmit={handleUpload}>
        <input
          type="file"
          accept=".pdf"
          onChange={(e) =>
            setFile(
              e.target.files?.[0] || null
            )
          }
        />

        <br />
        <br />

        <button type="submit">
          Upload Resume
        </button>
      </form>

      {result && (
        <div style={{ marginTop: "20px" }}>
          <h2>Upload Successful</h2>

          <p>
            Resume ID: {result.resume_id}
          </p>

          <p>
            Filename: {result.filename}
          </p>

          <h3>Extracted Skills</h3>

          <ul>
            {result.skills?.map(
              (skill: string) => (
                <li key={skill}>
                  {skill}
                </li>
              )
            )}
          </ul>
        </div>
      )}
    </div>
  );
}