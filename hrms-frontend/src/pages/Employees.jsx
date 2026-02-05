import { useEffect, useState } from "react";
import api from "../api/api";
import EmployeeForm from "../components/EmployeeForm";
import EmployeeTable from "../components/EmployeeTable";

export default function Employees() {
  const [employees, setEmployees] = useState([]);
  const [loading, setLoading] = useState(true);

  const fetchEmployees = async () => {
    setLoading(true);
    const res = await api.get("/employees/");
    setEmployees(res.data);
    setLoading(false);
  };

  const deleteEmployee = async (employee_id) => {
    if (!window.confirm("Are you sure you want to delete this employee?")) return;

    try {
      await api.delete(`/employees/${employee_id}`);
      setEmployees((prev) =>
        prev.filter((e) => e.employee_id !== employee_id)
      );
    } catch (err) {
      alert(err.response?.data?.detail || "Delete failed");
    }
  };

  useEffect(() => {
    fetchEmployees();
  }, []);

  return (
    <div className="page-container">
      <div className="page-title">Employees</div>

      <div className="content-grid">
        <div className="card">
          <EmployeeForm onSuccess={fetchEmployees} />
        </div>

        <div className="card">
          {loading ? (
            <p>Loading...</p>
          ) : (
            <EmployeeTable
              employees={employees}
              onDelete={deleteEmployee}
            />
          )}
        </div>
      </div>
    </div>
  );
}
