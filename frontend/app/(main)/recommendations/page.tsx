"use client";

import { useEffect, useState } from "react";
import { getRecommendations } from "../../../services/recommendations";

export default function RecommendationsPage() {
  const [jobs, setJobs] = useState<any[]>([]);

  useEffect(() => {
    const loadRecommendations = async () => {
      try {
        const data =
          await getRecommendations();

        setJobs(
          data.recommended_jobs || []
        );
      } catch (error) {
        console.error(error);
      }
    };

    loadRecommendations();
  }, []);

  return (
    <div style={{ padding: "30px" }}>
      <h1>
        AI Job Recommendations
      </h1>

      {jobs.length === 0 ? (
        <p>
          No recommendations found.
        </p>
      ) : (
        jobs.map((job) => (
          <div
            key={job.job_id}
            style={{
              border: "1px solid gray",
              padding: "15px",
              marginBottom: "10px",
            }}
          >
            <h3>{job.title}</h3>

            <p>
              Company: {job.company}
            </p>
          </div>
        ))
      )}
    </div>
  );
}