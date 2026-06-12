import { API_BASE_URL } from "../lib/config";

export async function getRecommendations() {
  const response = await fetch(
    `${API_BASE_URL}/jobs/recommend`
  );

  return response.json();
}