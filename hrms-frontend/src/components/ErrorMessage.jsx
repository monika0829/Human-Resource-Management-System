// components/ErrorMessage.jsx
export default function ErrorMessage({ message }) {
  if (!message) return null;
  return <p style={{ color: "red", marginBottom: "12px" }}>{message}</p>;
}
