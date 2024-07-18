import { getAllCourses } from "../api/courses.api"
import { useEffect, useState } from "react"
import Course from "./Course";

function Courses() {

  const [courses, setCourses] = useState([]);

  useEffect(() => {
    async function loadCourses() {
      const res = await getAllCourses();
      setCourses(res.data);
    }
    loadCourses();
  }, []);

  return (
    <>
    <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet"></link>
    <h1>Courses</h1>
    <ul>
      {courses.map(({id, title, description, qualification, modules, price, teacher, img}) => (
        <li key={id}>
          <Course 
          id={id}
          title={title} 
          description={description} 
          qualification={qualification} 
          modules={modules} 
          price={price} 
          teacher={teacher}
          img={img}
          />
        </li>
      ))}
    </ul>
    </>
  )
}

export default Courses