"use client";

import { useEffect, useState } from "react";

import { Button } from "@/components/ui/button";

import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

import { Badge } from "@/components/ui/badge";

import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

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
  <div className="space-y-6">
    <div>
      <h1 className="text-3xl font-bold">
        Available Jobs
      </h1>

      <p className="text-muted-foreground">
        Browse opportunities and check
        your resume compatibility.
      </p>
    </div>

    <Card>
      <CardHeader>
        <CardTitle>
          Job Listings
        </CardTitle>
      </CardHeader>

      <CardContent>
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>
                Title
              </TableHead>
              <TableHead>
                Company
              </TableHead>
              <TableHead>
                Skills
              </TableHead>
              <TableHead>
                Action
              </TableHead>
            </TableRow>
          </TableHeader>

          <TableBody>
            {jobs.map((job) => (
              <TableRow key={job.id}>
                <TableCell>
                  {job.title}
                </TableCell>

                <TableCell>
                  {job.company}
                </TableCell>

                <TableCell>
                  <div className="flex flex-wrap gap-1">
                    {job.skills
                      ?.split(",")
                      .slice(0, 4)
                      .map(
                        (
                          skill: string
                        ) => (
                          <Badge
                            key={skill}
                          >
                            {skill}
                          </Badge>
                        )
                      )}
                  </div>
                </TableCell>

                <TableCell>
                  <Button
                    onClick={() =>
                      handleMatch(
                        job.id
                      )
                    }
                  >
                    Match
                  </Button>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </CardContent>
    </Card>

    {matchResult && (
      <Card>
        <CardHeader>
          <CardTitle>
            Match Result
          </CardTitle>
        </CardHeader>

        <CardContent className="space-y-6">
          <div className="grid md:grid-cols-2 gap-6">

            <div>
              <h3 className="font-semibold">
                Match Score
              </h3>

              <p className="text-4xl font-bold">
                {
                  matchResult.job_match_score
                }
                %
              </p>
            </div>

            <div>
              <h3 className="font-semibold">
                Readiness
              </h3>

              <p className="text-xl">
                {
                  matchResult.readiness
                }
              </p>
            </div>

          </div>

          <div>
            <h3 className="font-semibold mb-2">
              Matched Skills
            </h3>

            <div className="flex flex-wrap gap-2">
              {matchResult.matched_skills?.map(
                (
                  skill: string
                ) => (
                  <Badge
                    key={skill}
                  >
                    {skill}
                  </Badge>
                )
              )}
            </div>
          </div>

          <div>
            <h3 className="font-semibold mb-2">
              Missing Skills
            </h3>

            <div className="flex flex-wrap gap-2">
              {matchResult.missing_skills?.map(
                (
                  skill: string
                ) => (
                  <Badge
                    variant="destructive"
                    key={skill}
                  >
                    {skill}
                  </Badge>
                )
              )}
            </div>
          </div>

          <div>
            <h3 className="font-semibold mb-2">
              Recommendations
            </h3>

            <ul className="space-y-2">
              {matchResult.recommendations?.map(
                (
                  item: any,
                  index: number
                ) => (
                  <li
                    key={index}
                  >
                    <strong>
                      {
                        item.skill
                      }
                    </strong>
                    :{" "}
                    {
                      item.recommendation
                    }
                  </li>
                )
              )}
            </ul>
          </div>
        </CardContent>
      </Card>
    )}
  </div>
);
}