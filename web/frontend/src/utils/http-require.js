import axios from "axios";

export default axios.create({
  // baseURL: "http://127.0.0.1:8081/",
  baseURL: "http://117.20.198.19:8000/",
  
  headers: {
    "Content-type": "application/json"
  }
});