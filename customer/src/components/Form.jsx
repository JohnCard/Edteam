import { useForm } from "react-hook-form";
import { createCourse, getTeachers, getCourse, deleteCourse, updateCourse } from "../api/courses.api";
import toast from "react-hot-toast";
import { useState, useEffect } from 'react';
import { useNavigate, useParams } from "react-router-dom";
import './Form.css'

function FormCourse() {

  // define your mainly form properties
  const {
    register,
    handleSubmit,
    formState: { errors },
    setValue,
    reset
  } = useForm(
    {
      // default form values
      defaultValues : {
        title: 'New python'
      }
    }
  );
  // define your navigator variable
  const navigate = useNavigate()
  // get page params
  const params = useParams()
  // your teachers array
  const [teachers, setTeachers] = useState([]);
  // define your main actions to load your page
  useEffect(() => {
    // pull teachers data
    async function loadTeachers() {
      const res = await getTeachers();
      // set to your teachers array
      setTeachers(res.data);
      //? ¿exist an id course?
      if (params.id) {
        // extract course data
        const { data } = await getCourse(params.id);
        // set your main parameters
        setValue("title", data.title);
        setValue("teacher", data.teacher);
      }
    }
    // extract data
    loadTeachers();
  }, []);

  // define submit action
  const onSubmit = handleSubmit(async (data) => {
  try {
    //? ¿exist id course? 
    if (params.id) {
      // update course
      await updateCourse(params.id, data);
      // send a succes message/notification
      toast.success("Course updated", {
        position: "bottom-right",
        style: {
          background: "#101010",
          color: "#fff",
        },
      });
    } else{
    // create a new course
    await createCourse(data);
    // send a succes message/notification
    toast.success("New Course Added", {
    position: "bottom-right",
    style: {
      background: "#101010",
      color: "#fff",
    },
    });
  }
    // go to main page
    navigate('/')
  }
  //! ¡something went wrong! 
  catch (error) {
    // show a console error message
    throw new Error(`Error ${error.response.data}`)
  }
  finally {
    // reset your form data
    reset()
  }
  });

  return (
    <>
    {/* main form */}
    <form onSubmit={onSubmit}>
      {/* font family link */}
      <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet"></link>
      {/* title input */}
      <input
        type="text"
        placeholder="Title"
      // register title
        {...register("title", 
            { 
              // define your error messages
            required: {
              value: true,
              message: 'Title required'
            },
            minLength: {
              value: 10,
              message: 'less than allowed'
            },
            maxLength: {
              value: 20,
              message: 'more than allowed'
            }})}
        // focus your main field inmediatly
        autoFocus
      />
      {/* wrong parameters  */}
      {errors.title && <span>{errors.title.message}</span>}
      {/* teacher field */}
      <select {
      // register teacher
        ...register("teacher",
        { 
          // define error message
          required: {
            value: true,
            message: 'Teacher required'
          }
        })}>
          {/* travel all teachers data/array */}
      {teachers.map(teacher => (
        <option key={teacher.id} value={teacher.id}>
          {teacher.name}
        </option>
      ))}
      </select>
      {/* throw error message */}
      {errors.teacher && <span>{errors.teacher.message}</span>}
      {/* score field */}
      <input 
      type="number" 
      placeholder="Qualification"
      // register qualification
      {...register('qualification',
        {
          // define error messages
          min: {
            value: 0,
            message: 'No puede ser menor a 0'
          },
          max: {
            value: 10,
            message: 'No puede exceder a 10'
          }
        })}
      />
      {/* throw error message */}
      {errors.qualification && <span>{errors.qualification.message}</span>}
      {/* modules amount field */}
      <input 
      type="number" 
      placeholder="Modules"
      // register amount
      {...register('modules')}
      />
      {/* description field */}
      <textarea cols="30" rows="10" placeholder="Description"></textarea>
      {/* price field */}
      <input
      type="number"
      placeholder="Price"
      // register price
      {...register('price')}
      />
      {/* save your data */}
      <button>
        Save
      </button>
      {/* exist an id course? */}
      {params.id && (
        //! ¡button delete!
          <button
            onClick={async () => {
              // confirm alert
              const accepted = window.confirm("Are you sure?");
              //? ¿true?
              if (accepted) {
                // delete course action
                await deleteCourse(params.id);
                // throw a succes message
                toast.success("Course Removed", {
                  position: "bottom-right",
                  style: {
                    background: "#101010",
                    color: "#fff",
                  },
                });
                // go to courses page
                navigate(`/`);
              }
            }}
        >delete</button>
      )}
    </form>
    </>
  )
}

export default FormCourse
