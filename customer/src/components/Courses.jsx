import { getAllCourses } from "../api/courses.api"
import { useEffect, useState } from "react"
import Course from "./Course";

function Courses() {
  // define your courses data array
  const [courses, setCourses] = useState([]);

  useEffect(() => {
    async function loadCourses() {
      // pull all courses data from api
      const res = await getAllCourses();
      // set data for courses array
      setCourses(res.data);
    }
    loadCourses();
  }, []);

  return (
    <>
    {/* font family link */}
    <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet"></link>
    <h1>Courses</h1>
    {/* main content page */}
    <ul>
      {/* we start mapping all components */}
      {courses.map(({id, title, description, qualification, modules, price, teacher, img}) => (
        <li key={id}>
          <Course 
          // id component
          id={id}
          // component title
          title={title} 
          // component description
          description={description}
          // component qualifitcation 
          qualification={qualification}
          // component modules 
          modules={modules} 
          // component price
          price={price} 
          // component teacher
          teacher={teacher}
          // component background image
          img={img}
          />
        </li>
      ))}
    </ul>
    </>
  )
}

export default Courses