export default function DashboardPage() {
  return (
    <div>
      <h1 className="text-3xl font-bold mb-8">
        Welcome to CareerForge 🚀
      </h1>

      <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">

        <div className="bg-white p-6 rounded-xl shadow">
          <h2 className="text-gray-500">ATS Score</h2>
          <p className="text-3xl font-bold">78%</p>
        </div>

        <div className="bg-white p-6 rounded-xl shadow">
          <h2 className="text-gray-500">Resume Uploaded</h2>
          <p className="text-3xl font-bold">Yes</p>
        </div>

        <div className="bg-white p-6 rounded-xl shadow">
          <h2 className="text-gray-500">Jobs Available</h2>
          <p className="text-3xl font-bold">50</p>
        </div>

        <div className="bg-white p-6 rounded-xl shadow">
          <h2 className="text-gray-500">
            Recommended Jobs
          </h2>
          <p className="text-3xl font-bold">12</p>
        </div>

      </div>
    </div>
  );
}