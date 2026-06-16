"use client";

import { useEffect, useState } from "react";
import { getDashboardStats } from "@/services/dashboard";

import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

import { Button } from "@/components/ui/button";
import Link from "next/link";

interface DashboardStats {
  ats_score: number;
  jobs_available: number;
  recommended_jobs: number;
  resume_uploaded: boolean;
}

export default function DashboardPage() {
  const [stats, setStats] = useState<DashboardStats>({
    ats_score: 0,
    jobs_available: 0,
    recommended_jobs: 0,
    resume_uploaded: false,
  });

  useEffect(() => {
    async function loadStats() {
      try {
        const data = await getDashboardStats();
        setStats(data);
      } catch (error) {
        console.error("Failed to load dashboard stats:", error);
      }
    }

    loadStats();
  }, []);

  return (
    <div>
      <h1 className="text-3xl font-bold mb-8">
        Welcome to CareerForge 🚀
      </h1>

      <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
          <Card>
            <CardHeader>
              <CardTitle>ATS Score</CardTitle>
            </CardHeader>

            <CardContent>
              <p className="text-3xl font-bold">
                {stats.ats_score}%
              </p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>Resume Uploaded</CardTitle>
            </CardHeader>

            <CardContent>
              <p className="text-3xl font-bold">
                {stats.resume_uploaded ? "Yes" : "No"}
              </p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>Jobs Available</CardTitle>
            </CardHeader>

            <CardContent>
              <p className="text-3xl font-bold">
                {stats.jobs_available}
              </p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>Recommended Jobs</CardTitle>
            </CardHeader>

            <CardContent>
              <p className="text-3xl font-bold">
                {stats.recommended_jobs}
              </p>
            </CardContent>
          </Card>
        </div>
          <div className="mt-8">
  <h2 className="text-xl font-semibold mb-4">
    Quick Actions
  </h2>

  <div className="flex flex-wrap gap-4">
    <Link href="/upload">
      <Button>
        Upload Resume
      </Button>
    </Link>

    <Link href="/analysis">
      <Button variant="outline">
        Analyze Resume
      </Button>
    </Link>

    <Link href="/jobs">
      <Button variant="secondary">
        View Jobs
      </Button>
    </Link>

    <Link href="/recommendations">
      <Button variant="default">
        Recommendations
      </Button>
    </Link>
  </div>
</div>
        </div>
        
  );
}