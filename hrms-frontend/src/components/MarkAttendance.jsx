import { useState } from "react";
import { markAttendance } from "../services/attendanceService";

const MarkAttendance = ({ employeeId }) => {
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState(null);
  const [error, setError] = useState(null);

  const handleMarkAttendance = async () => {
    setLoading(true);
    setMessage(null);
    setError(null);

    try {
      const res = await markAttendance({
        employee_id: employeeId,
        status: "Present",
      });

      setMessage("Attendance marked successfully ✅");
    } catch (err) {
      if (err?.status === 400) {
        setError(err.data.detail); 
      } else {
        setError("Something went wrong. Please try again.");
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: 300 }}>
      <button
        onClick={handleMarkAttendance}
        disabled={loading}
        style={{
          padding: "10px",
          width: "100%",
          cursor: loading ? "not-allowed" : "pointer",
        }}
      >
        {loading ? "Marking..." : "Mark Attendance"}
      </button>

      {message && <p style={{ color: "green" }}>{message}</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}
    </div>
  );
};

export default MarkAttendance;
