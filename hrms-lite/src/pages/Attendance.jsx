import { useEffect, useState } from "react";
import api from "../api/api";
import AttendanceForm from "../components/AttendanceForm";

export default function Attendance() {
  const [employees, setEmployees] = useState([]);
  const [records, setRecords] = useState([]);

  const fetchAll = async () => {
    const emp = await api.get("/employees/");
    const att = await api.get("/attendance/");
    setEmployees(emp.data);
    setRecords(att.data);
  };

  useEffect(() => {
    fetchAll();
  }, []);
    return (
  <div className="app-bg">
    <h1>Attendance</h1>

    <div className="page-center">
      <div className="form-wrapper">
        <AttendanceForm
          employees={employees}
        //   onSuccess={fetchAll}
        onSuccess={(newRecord) => {
    setRecords((prev) => [newRecord, ...prev]);
  }}
        />
      </div>

      <div className="list-wrapper">
        <div className="card">
          <h2>Attendance Records</h2>
          {!records.length ? (
            <p>No records found.</p>
          ) : (
            <table>
              <thead>
                <tr>
                  <th>Employee</th>
                  <th>Date</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                {records.map((r) => (
                  <tr key={r.id}>
                    <td>{r.employee_name}</td>
                    <td>{r.date}</td>
                    <td>{r.status}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </div>
      </div>
    </div>
  </div>
);
}
