import axios from "axios";

// define your main url
const URL = import.meta.env.VITE_BACKEND_URL
// define base url
const coursesApi = axios.create({
  baseURL: `${URL}/course-new-api/`,
})
// define teachers api url
const teachersApi = axios.create({
  baseURL: `${URL}/teacher`
})
// get teachers function
export const getTeachers = () => teachersApi.get('/')
// get all courses function
export const getAllCourses = () => coursesApi.get("/");
// get course function
export const getCourse = (id) => coursesApi.get(`/${id}`);
// create course function
export const createCourse = (course) => coursesApi.post("/", course);
// update course function
export const updateCourse = (id, course) => coursesApi.put(`/${id}/`, course);
// delete course function
export const deleteCourse = (id) => coursesApi.delete(`/${id}`);