import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
  headers: {
    "Content-Type": "application/json",
  },
});

export const markAttendance = async (payload) => {
  try {
    const response = await API.post("/attendance/mark", payload);
    return response.data;
  } catch (error) {
    throw error.response;
  }
};
