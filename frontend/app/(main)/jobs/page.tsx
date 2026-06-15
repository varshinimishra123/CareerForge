"use client";

import { useEffect, useState } from "react";
import {
  getJobs,
  matchJob,
} from "../../../services/jobs";

export default function JobsPage() {
  const [jobs, setJobs] = useState<any[]>([]);
  const [matchResult, setMatchResult] =
    useState<any>(null);

  const handleMatch = async (
    jobId: number
  ) => {
    try {
      const data = await matchJob(jobId);
      setMatchResult(data);
    } catch (error) {
      console.error(error);
      alert("Failed to match job");
    }
  };

  useEffect(() => {
    const loadJobs = async () => {
      try {
        const data = await getJobs();
        setJobs(data);
      } catch (error) {
        console.error(error);
      }
    };

    loadJobs();
  }, []);

  return (
    <div style={{ padding: "30px" }}>
      <h1>Available Jobs</h1>

      {jobs.map((job) => (
        <div
          key={job.id}
          style={{
            border: "1px solid gray",
            padding: "15px",
            marginBottom: "10px",
          }}
        >
          <h3>{job.title}</h3>

          <p>
            <strong>Company:</strong>{" "}
            {job.company}
          </p>

          <p>{job.description}</p>

          <button
            onClick={() =>
              handleMatch(job.id)
            }
          >
            Match Resume
          </button>
        </div>
      ))}

      {matchResult && (
        <div
          style={{
            marginTop: "30px",
            border: "1px solid gray",
            padding: "20px",
          }}
        >
          <h2>Match Result</h2>

          <p>
            <strong>Score:</strong>{" "}
            {matchResult.job_match_score}%
          </p>

          <p>
            <strong>Readiness:</strong>{" "}
            {matchResult.readiness}
          </p>

          <h3>Matched Skills</h3>

          <ul>
            {matchResult.matched_skills?.map(
              (skill: string) => (
                <li key={skill}>
                  {skill}
                </li>
              )
            )}
          </ul>

          <h3>Missing Skills</h3>

          <ul>
            {matchResult.missing_skills?.map(
              (skill: string) => (
                <li key={skill}>
                  {skill}
                </li>
              )
            )}
          </ul>

         <h3>Recommendations</h3>

        <ul>
        {matchResult.recommendations?.map(
            (
            item: any,
            index: number
            ) => (
            <li key={index}>
                <strong>
                {item.skill}
                </strong>
                : {item.recommendation}
            </li>
            )
        )}
        </ul>
        </div>
      )}
    </div>
  );
}