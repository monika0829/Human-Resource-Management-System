import { useState } from "react";
import api from "../api/api";
import ErrorMessage from "./ErrorMessage";

export default function EmployeeForm({ onSuccess }) {
  const [form, setForm] = useState({
    employee_id: "",
    full_name: "",
    email: "",
    department: "",
  });
  const [error, setError] = useState("");

  const handleChange = (e) =>
    setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    try {
      await api.post("/employees/", {
        employee_id: Number(form.employee_id),
        full_name: form.full_name,
        email: form.email,
        department: form.department,
      });

      onSuccess?.(); // safe call
      setForm({ employee_id: "", full_name: "", email: "", department: "" });

    } catch (err) {
      console.error(err.response?.data);
      setError(
        err.response?.data?.detail || "Error adding employee" 
      );
    }
  };

  return (
    <div className="card">
      <h2>Add Employee</h2>
      <ErrorMessage message={error} />

      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Employee ID</label>
          <input
            name="employee_id"
            value={form.employee_id}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-group">
          <label>Full Name</label>
          <input
            name="full_name"
            value={form.full_name}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-group">
          <label>Email</label>
          <input
            name="email"
            type="email"
            value={form.email}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-group">
          <label>Department</label>
          <input
            name="department"
            value={form.department}
            onChange={handleChange}
            required
          />
        </div>

        <button type="submit" className="primary-btn">Add Employee</button>
      </form>
    </div>
  );
}
