import { API_BASE_URL } from "@/lib/config";

export async function getApplications() {
  const response = await fetch(
    `${API_BASE_URL}/applications`
  );

  return response.json();
}

export async function createApplication(
  company: string,
  role: string
) {
  const response = await fetch(
    `${API_BASE_URL}/applications`,
    {
      method: "POST",
      headers: {
        "Content-Type":
          "application/json",
      },
      body: JSON.stringify({
        company,
        role,
      }),
    }
  );

  return response.json();
}

export async function updateApplication(
  id: number,
  status: string
) {
  const response = await fetch(
    `${API_BASE_URL}/applications/${id}`,
    {
      method: "PUT",
      headers: {
        "Content-Type":
          "application/json",
      },
      body: JSON.stringify({
        status,
      }),
    }
  );

  return response.json();
}