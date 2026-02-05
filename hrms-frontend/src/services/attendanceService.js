import axios from "axios";

const API = axios.create({
  baseURL: "https://human-resource-management-system-b13f.onrender.com/",  headers: {
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
