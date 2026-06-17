import { API_BASE_URL } from "../lib/config";

export async function startInterview(
  role: string
) {
  const response = await fetch(
    `${API_BASE_URL}/interview/start`,
    {
      method: "POST",
      headers: {
        "Content-Type":
          "application/json",
      },
      body: JSON.stringify({
        role,
      }),
    }
  );

  if (!response.ok) {
    throw new Error(
      "Failed to start interview"
    );
  }

  return response.json();
}

export async function getInterviewReport(
  sessionId: string
) {
  const response = await fetch(
    `${API_BASE_URL}/interview/${sessionId}`
  );

  if (!response.ok) {
    throw new Error(
      "Failed to load interview"
    );
  }

  return response.json();
}