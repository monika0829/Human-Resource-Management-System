import { useState } from "react";
import api from "../api/api";

export default function AttendanceForm({ employees, onSuccess }) {
  const [data, setData] = useState({
    employee_id: "",
    status: "PRESENT",
  });
  const [error, setError] = useState("");
  const submit = async (e) => {
    e.preventDefault();
    setError("");
    try {
      const res = await api.post("/attendance/mark", {
        employee_id: data.employee_id,
        status: data.status,
      });

      // build record same as GET /attendance/
      const newRecord = {
        id: res.data.id,
        employee_name: employees.find(
          (e) => e.employee_id === data.employee_id
        )?.full_name,
        date: res.data.date,
        status: res.data.status,
      };

      onSuccess(newRecord);

      setData({
        employee_id: "",
        status: "PRESENT",
      });
    } catch (err) {
      setError(err.response?.data?.detail || "Attendance error");
    }
  };

  return (
    <div className="card">
      <h2>Mark Attendance</h2>
       {error && (
        <div style={{ color: "#dc2626", marginBottom: "12px", fontSize: "14px" }}>
          {error}
        </div>
      )}

      <form onSubmit={submit}>
        <div className="form-group">
          <label>Employee</label>
          <select
            value={data.employee_id}
            onChange={(e) =>
              setData({ ...data, employee_id: Number(e.target.value) })
            }
            required
          >
            <option value="">Select</option>
            {employees.map((emp) => (
              <option key={emp.employee_id} value={emp.employee_id}>
                {emp.full_name}
              </option>
            ))}
          </select>
        </div>

        <div className="form-group">
          <label>Status</label>
          <select
            value={data.status}
            onChange={(e) =>
              setData({ ...data, status: e.target.value })
            }
          >
            <option value="PRESENT">Present</option>
            <option value="ABSENT">Absent</option>
          </select>
        </div>

        <button type="submit" className="primary-btn">
          Submit
        </button>
      </form>
    </div>
  );
}
