"use client";

import { useEffect, useState } from "react";
import { getResumeAnalysis } from "../../../services/analysis";

import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

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
    return (
      <div className="flex items-center justify-center h-screen">
        Loading analysis...
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold">
          Resume Analysis
        </h1>

        <p className="text-muted-foreground">
          AI-powered ATS evaluation and skill analysis
        </p>
      </div>

      {/* ATS Score */}
      <Card>
        <CardHeader>
          <CardTitle>ATS Score</CardTitle>
        </CardHeader>

        <CardContent>
          <div className="text-5xl font-bold">
            {analysis.ats_score}%
          </div>
        </CardContent>
      </Card>

      {/* Skills */}
      <Card>
        <CardHeader>
          <CardTitle>Extracted Skills</CardTitle>
        </CardHeader>

        <CardContent>
          <div className="flex flex-wrap gap-2">
            {analysis.skills?.map(
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
        </CardContent>
      </Card>

      {/* Strengths */}
      <Card>
        <CardHeader>
          <CardTitle>
            Strengths
          </CardTitle>
        </CardHeader>

        <CardContent>
          <ul className="space-y-2">
            {analysis.strengths?.map(
              (
                strength: string,
                index: number
              ) => (
                <li
                  key={index}
                  className="flex items-center gap-2"
                >
                  ✅ {strength}
                </li>
              )
            )}
          </ul>
        </CardContent>
      </Card>

      {/* Weaknesses */}
      <Card>
        <CardHeader>
          <CardTitle>
            Areas to Improve
          </CardTitle>
        </CardHeader>

        <CardContent>
          <ul className="space-y-2">
            {analysis.weaknesses?.map(
              (
                weakness: string,
                index: number
              ) => (
                <li
                  key={index}
                  className="flex items-center gap-2"
                >
                  ⚠️ {weakness}
                </li>
              )
            )}
          </ul>
        </CardContent>
      </Card>
    </div>
  );
}