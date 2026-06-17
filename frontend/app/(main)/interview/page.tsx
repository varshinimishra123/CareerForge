"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

import { Button } from "@/components/ui/button";

import { startInterview } from "@/services/interview";

export default function InterviewPage() {
  const router = useRouter();

  const [role, setRole] = useState("frontend");
  const [loading, setLoading] = useState(false);

  async function handleStart() {
    try {
      setLoading(true);

      const data = await startInterview(role);

      router.push(
        `/interview/session/${data.session_id}`
      );
    } catch (error) {
      console.error(error);
      alert("Failed to start interview");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="max-w-2xl mx-auto">
      <Card>
        <CardHeader>
          <CardTitle>
            AI Interview Simulator
          </CardTitle>
        </CardHeader>

        <CardContent className="space-y-4">
          <div>
            <label className="block mb-2">
              Select Role
            </label>

            <select
              value={role}
              onChange={(e) =>
                setRole(e.target.value)
              }
              className="
                w-full
                border
                rounded-md
                p-2
              "
            >
              <option value="frontend">
                Frontend
              </option>

              <option value="backend">
                Backend
              </option>

              <option value="ml">
                Machine Learning
              </option>

              <option value="hr">
                HR
              </option>
            </select>
          </div>

          <Button
            className="w-full"
            onClick={handleStart}
            disabled={loading}
          >
            {loading
              ? "Starting..."
              : "Start Interview"}
          </Button>
        </CardContent>
      </Card>
    </div>
  );
}