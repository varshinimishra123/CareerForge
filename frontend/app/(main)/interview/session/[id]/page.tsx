"use client";

import { useEffect, useState } from "react";
import { useParams } from "next/navigation";

import { getInterviewReport } from "@/services/interview";

export default function InterviewSessionPage() {
  const params = useParams();

  const [loading, setLoading] =
    useState(true);

  const [data, setData] =
    useState<any>(null);

  useEffect(() => {
    async function loadInterview() {
      try {
        const result =
          await getInterviewReport(
            params.id as string
          );

        setData(result);
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    }

    loadInterview();
  }, [params.id]);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (!data) {
    return (
      <div>
        Failed to load interview
      </div>
    );
  }

  return (
    <div className="max-w-4xl mx-auto">

      <h1 className="text-3xl font-bold mb-6">
        {data.role} Interview
      </h1>

      <div className="space-y-4">
        {data.questions.map(
          (question: any) => (
            <div
              key={question.question_id}
              className="
                border
                rounded-lg
                p-4
              "
            >
              <p className="font-medium">
                {question.question}
              </p>
            </div>
          )
        )}
      </div>

    </div>
  );
}