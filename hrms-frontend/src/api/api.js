import axios from "axios";

const api = axios.create({
  baseURL: "https://human-resource-management-system-b13f.onrender.com",
  headers: {
    "Content-Type": "application/json",
  },

});

export default api;
