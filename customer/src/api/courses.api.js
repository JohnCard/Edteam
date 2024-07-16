import axios from "axios";

// const URL =
//   process.env.NODE_ENV === "production"
//     ? import.meta.env.VITE_BACKEND_URL
//     : "http://localhost:8000";

const URL = import.meta.env.VITE_BACKEND_URL

const coursesApi = axios.create({
  baseURL: `${URL}/NewApi/`,
});

export const getAllCourses = () => coursesApi.get("/");

export const getCourse = (id) => coursesApi.get(`/${id}`);

export const createCourse = (course) => coursesApi.post("/", course);

export const updateCourse = (id, course) => coursesApi.put(`/${id}/`, course);

export const deleteCourse = (id) => coursesApi.delete(`/${id}`);