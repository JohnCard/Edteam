import { getAllCourses } from "./api/courses.api"
import { useEffect, useState } from "react"
import Course from "./components/Course";
import "./App.css"

function App() {

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
    <nav>
      
    </nav>
    <h1>Courses</h1>
    <ul>
      {courses.map(({id, title, description, qualification, modules, price, teacher}) => (
        <li key={id}>
          <Course 
          title={title} 
          description={description} 
          qualification={qualification} 
          modules={modules} 
          price={price} 
          teacher={teacher}
          />
        </li>
      ))}
    </ul>
    </>
  )
}

export default App
