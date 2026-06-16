"use client";

import { useEffect, useState } from "react";
import { getRecommendations } from "../../../services/recommendations";

import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

import { Badge } from "@/components/ui/badge";

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
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold">
          AI Job Recommendations
        </h1>

        <p className="text-muted-foreground">
          Personalized opportunities based
          on your resume, skills, and ATS analysis.
        </p>
      </div>

      {jobs.length === 0 ? (
        <Card>
          <CardContent className="py-8 text-center">
            No recommendations found.
          </CardContent>
        </Card>
      ) : (
        <div className="grid md:grid-cols-2 gap-6">
          {jobs.map((job) => (
            <Card key={job.job_id}>
              <CardHeader>
                <CardTitle>
                  {job.title}
                </CardTitle>
              </CardHeader>

              <CardContent className="space-y-3">
                <p className="text-muted-foreground">
                  {job.company}
                </p>

                <Badge>
                  AI Recommended
                </Badge>

                <p className="text-sm text-muted-foreground">
                  Based on your resume skills
                  and career profile.
                </p>
              </CardContent>
            </Card>
          ))}
        </div>
      )}
    </div>
  );
}