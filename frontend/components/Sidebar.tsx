"use client";

import Link from "next/link";
import {
  LayoutDashboard,
  Upload,
  FileText,
  Briefcase,
  Sparkles,
} from "lucide-react";

export default function Sidebar() {
  return (
    <aside className="w-64 bg-slate-900 text-white min-h-screen p-5">
      <h1 className="text-2xl font-bold mb-8">
        CareerForge
      </h1>

      <nav className="space-y-4">
        <Link href="/dashboard" className="flex gap-3 items-center">
          <LayoutDashboard size={18} />
          Dashboard
        </Link>

        <Link href="/upload" className="flex gap-3 items-center">
          <Upload size={18} />
          Upload Resume
        </Link>

        <Link href="/analysis" className="flex gap-3 items-center">
          <FileText size={18} />
          Analysis
        </Link>

        <Link href="/jobs" className="flex gap-3 items-center">
          <Briefcase size={18} />
          Jobs
        </Link>

        <Link href="/recommendations" className="flex gap-3 items-center">
          <Sparkles size={18} />
          Recommendations
        </Link>
      </nav>
    </aside>
  );
}