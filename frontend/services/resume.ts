import { API_BASE_URL } from "../lib/config";

export async function uploadResume(
  file: File
) {
  const formData = new FormData();

  formData.append(
    "file",
    file
  );

  const response = await fetch(
    `${API_BASE_URL}/resume/upload`,
    {
      method: "POST",
      body: formData,
    }
  );

  return response.json();
}