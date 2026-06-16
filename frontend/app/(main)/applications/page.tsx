"use client";

import { useEffect, useState } from "react";

import {
  getApplications,
  createApplication,
  updateApplication,
} from "@/services/applications";

import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";


import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

export default function ApplicationsPage() {
  const [applications, setApplications] =
    useState<any[]>([]);

  const [company, setCompany] =
    useState("");

  const [role, setRole] =
    useState("");

    const loadApplications =
    async () => {
    try {
      const data =
        await getApplications();

      setApplications(data);
    } catch (error) {
      console.error(error);
    }
  };

useEffect(() => {
  loadApplications();
}, []);

const handleCreate =
  async () => {
    try {
      await createApplication(
        company,
        role
      );

      setCompany("");
      setRole("");

      loadApplications();
    } catch (error) {
      console.error(error);
    }
  };

  const handleStatusChange =
  async (
    id: number,
    status: string
  ) => {
    try {
      await updateApplication(
        id,
        status
      );

      loadApplications();
    } catch (error) {
      console.error(error);
    }
  };
  const getStatusVariant = (
  status: string
) => {
  switch (status) {
    case "Offer":
      return "default";

    case "Rejected":
      return "destructive";

    default:
      return "secondary";
  }
};
const getStatusColor = (
  status: string
) => {
  switch (status) {
    case "Applied":
      return "bg-blue-100 text-blue-800";

    case "OA":
      return "bg-yellow-100 text-yellow-800";

    case "Interview":
      return "bg-purple-100 text-purple-800";

    case "Offer":
      return "bg-green-100 text-green-800";

    case "Rejected":
      return "bg-red-100 text-red-800";

    default:
      return "";
  }
};

  return (
  <div className="space-y-6">
    <div>
      <h1 className="text-3xl font-bold">
        Application Tracker
      </h1>

      <p className="text-muted-foreground">
        Track all your job applications.
      </p>
    </div>

    <Card>
      <CardHeader>
        <CardTitle>
          Add Application
        </CardTitle>
      </CardHeader>

      <CardContent className="space-y-3">
        <input
          className="border p-2 rounded w-full"
          placeholder="Company"
          value={company}
          onChange={(e) =>
            setCompany(
              e.target.value
            )
          }
        />

        <input
          className="border p-2 rounded w-full"
          placeholder="Role"
          value={role}
          onChange={(e) =>
            setRole(
              e.target.value
            )
          }
        />

        <Button
          onClick={handleCreate}
        >
          Add Application
        </Button>
      </CardContent>
    </Card>

    <Card>
      <CardHeader>
        <CardTitle>
          Applications
        </CardTitle>
      </CardHeader>

      <CardContent>
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>
                Company
              </TableHead>

              <TableHead>
                Role
              </TableHead>

              <TableHead>
                Status
              </TableHead>
            </TableRow>
          </TableHeader>

          <TableBody>
            {applications.map(
              (
                application
              ) => (
                <TableRow
                  key={
                    application.id
                  }
                >
                  <TableCell>
                    {
                      application.company
                    }
                  </TableCell>

                  <TableCell>
                    {
                      application.role
                    }
                  </TableCell>

                  <TableCell>
                    <Badge
                    className={getStatusColor(
                        application.status
                    )}
                    >
                    {application.status}
                    </Badge>
                    <select
                      value={
                        application.status
                      }
                      onChange={(
                        e
                      ) =>
                        handleStatusChange(
                          application.id,
                          e.target
                            .value
                        )
                      }
                    >
                      <option>
                        Applied
                      </option>

                      <option>
                        OA
                      </option>

                      <option>
                        Interview
                      </option>

                      <option>
                        Rejected
                      </option>

                      <option>
                        Offer
                      </option>
                    </select>
                  </TableCell>
                </TableRow>
              )
            )}
          </TableBody>
        </Table>
      </CardContent>
    </Card>
  </div>

)};