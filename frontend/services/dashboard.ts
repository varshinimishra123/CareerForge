const API_BASE_URL = "http://localhost:8000";

export async function getDashboardStats() {
  const [analysisRes, jobsRes, recommendationsRes] =
    await Promise.all([
      fetch(`${API_BASE_URL}/resume/analyze`),
      fetch(`${API_BASE_URL}/jobs`),
      fetch(`${API_BASE_URL}/jobs/recommend`),
    ]);

  const analysis = await analysisRes.json();
  const jobs = await jobsRes.json();
  const recommendations = await recommendationsRes.json();

  return {
    ats_score: analysis.ats_score ?? 0,
    jobs_available: jobs.length ?? 0,
    recommended_jobs:
      recommendations.recommended_jobs?.length ?? 0,
    resume_uploaded: true,
  };
}