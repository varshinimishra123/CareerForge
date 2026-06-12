import { API_BASE_URL } from "../lib/config";

export async function getJobs() {
  const response = await fetch(
    `${API_BASE_URL}/jobs`
  );

  return response.json();
}
export async function matchJob(
  jobId: number
) {
  const response = await fetch(
    `${API_BASE_URL}/jobs/${jobId}/match`,
    {
      method: "POST",
    }
  );

  return response.json();
}