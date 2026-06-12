import { API_BASE_URL } from "../lib/config";

export async function getResumeAnalysis() {
  const response = await fetch(
    `${API_BASE_URL}/resume/analyze`
  );

  return response.json();
}