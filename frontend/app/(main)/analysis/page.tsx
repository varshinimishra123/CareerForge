"use client";

import { useEffect, useState } from "react";
import { getResumeAnalysis } from "../../../services/analysis";

export default function AnalysisPage() {
  const [analysis, setAnalysis] = useState<any>(null);

  useEffect(() => {
    const loadAnalysis = async () => {
      try {
        const data = await getResumeAnalysis();
        setAnalysis(data);
      } catch (error) {
        console.error(error);
      }
    };

    loadAnalysis();
  }, []);

  if (!analysis) {
    return <div>Loading...</div>;
  }

  return (
    <div style={{ padding: "30px" }}>
      <h1>Resume Analysis</h1>

      <p>
        <strong>ATS Score:</strong>{" "}
        {analysis.ats_score}
      </p>

      <h2>Skills</h2>

      <ul>
        {analysis.skills?.map(
          (skill: string) => (
            <li key={skill}>{skill}</li>
          )
        )}
      </ul>

      <h2>Strengths</h2>

<ul>
  {analysis.strengths?.map(
    (
      strength: string,
      index: number
    ) => (
      <li key={index}>
        {strength}
      </li>
    )
  )}
</ul>

<h2>Areas to Improve</h2>

<ul>
  {analysis.weaknesses?.map(
    (
      weakness: string,
      index: number
    ) => (
      <li key={index}>
        {weakness}
      </li>
    )
  )}
</ul>
    </div>
  );
}