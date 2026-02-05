import { useEffect, useState } from "react";
import api from "../api/api";

export default function Dashboard() {
  const [summary, setSummary] = useState({
    employees: 0,
    presentToday: 0,
    absentToday: 0,
  });

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchData() {
      try {
        const empRes = await api.get("/employees");
        const attRes = await api.get("/attendance");

        const today = new Date().toISOString().split("T")[0];
        const totalEmployees = empRes.data.length;
        const presentToday = attRes.data.filter(
          (a) =>
            a.status === "Present" &&
            a.date === today
        ).length;
        const absentCount=totalEmployees-presentToday;
        setSummary({
          employees: empRes.data.length,
          presentToday,
          absentToday: absentCount,
        });
      } catch (err) {
        console.error(err);
        setError("Failed to load dashboard data");
      } finally {
        setLoading(false);
      }
    }

    fetchData();
  }, []);

  if (loading) return <p>Loading dashboard...</p>;
  if (error) return <p style={{ color: "red" }}>{error}</p>;

  return (
    <div className="page">
      <div className="section">
        <h1>Dashboard</h1>

        <div style={{ display: "flex", gap: "24px" }}>
          <div className="card">
            <h2>Total Employees</h2>
            <p style={{ fontSize: "32px", fontWeight: "bold" }}>
              {summary.employees}
            </p>
          </div>

          <div className="card">
            <h2>Present Today</h2>
            <p style={{ fontSize: "32px", fontWeight: "bold" }}>
              {summary.presentToday}
            </p>
          </div>
           <div className="card">
            <h2>Absent Today</h2>
            <p style={{ fontSize: "32px", fontWeight: "bold" }}>
              {summary.absentToday}
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
