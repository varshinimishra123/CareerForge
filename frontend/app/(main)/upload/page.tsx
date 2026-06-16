"use client";

import { useState } from "react";
import { uploadResume } from "../../../services/resume";

import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

import { Button } from "@/components/ui/button";

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
    <div className="space-y-6">
      {/* Header */}
      <div>
        <h1 className="text-3xl font-bold">
          Upload Resume
        </h1>

        <p className="text-muted-foreground">
          Upload your latest resume to
          generate ATS analysis and job
          recommendations.
        </p>
      </div>

      {/* Upload Card */}
      <Card>
        <CardHeader>
          <CardTitle>
            Resume Upload
          </CardTitle>
        </CardHeader>

        <CardContent>
          <form
            onSubmit={handleUpload}
            className="space-y-4"
          >
            <input
              type="file"
              accept=".pdf"
              className="block w-full border rounded-md p-2"
              onChange={(e) =>
                setFile(
                  e.target.files?.[0] || null
                )
              }
            />

            <Button type="submit">
              Upload Resume
            </Button>
          </form>
        </CardContent>
      </Card>

      {/* Upload Result */}
      {result && (
        <Card>
          <CardHeader>
            <CardTitle>
              Upload Successful 🎉
            </CardTitle>
          </CardHeader>

          <CardContent className="space-y-4">
            <div>
              <p>
                <strong>
                  Resume ID:
                </strong>{" "}
                {result.resume_id}
              </p>

              <p>
                <strong>
                  Filename:
                </strong>{" "}
                {result.filename}
              </p>
            </div>

            <div>
              <h3 className="font-semibold mb-2">
                Extracted Skills
              </h3>

              <div className="flex flex-wrap gap-2">
                {result.skills?.map(
                  (skill: string) => (
                    <span
                      key={skill}
                      className="bg-slate-900 text-white px-3 py-1 rounded-full text-sm"
                    >
                      {skill}
                    </span>
                  )
                )}
              </div>
            </div>
          </CardContent>
        </Card>
      )}
    </div>
  );
}