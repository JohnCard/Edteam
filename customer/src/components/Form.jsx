import { useForm } from "react-hook-form";
import { createCourse, getTeachers, getCourse, deleteCourse, updateCourse } from "../api/courses.api";
import toast from "react-hot-toast";
import { useState, useEffect } from 'react';
import { useNavigate, useParams } from "react-router-dom";

function FormCourse() {

  const {
    register,
    handleSubmit,
    formState: { errors },
    setValue,
    reset
  } = useForm(
    {
      defaultValues : {
        title: 'New python'
      }
    }
  );
  const navigate = useNavigate()
  const params = useParams()

  const [teachers, setTeachers] = useState([]);

  useEffect(() => {
    async function loadTeachers() {
      const res = await getTeachers();
      setTeachers(res.data);
      if (params.id) {
        const { data } = await getCourse(params.id);
        setValue("title", data.title);
        setValue("teacher", data.teacher);
      }
    }
    loadTeachers();
  }, []);

  const onSubmit = handleSubmit(async (data) => {
  try{
    if (params.id) {
      await updateCourse(params.id, data);
      toast.success("Course updated", {
        position: "bottom-right",
        style: {
          background: "#101010",
          color: "#fff",
        },
      });
    } else{
    await createCourse(data);
    toast.success("New Course Added", {
    position: "bottom-right",
    style: {
      background: "#101010",
      color: "#fff",
    },
    });
  }
    navigate('/')
  }
  catch (error) {
    toast.success(`Something went wrong! ${error}`, {
      position: "bottom-right",
      style: {
        background: "blue",
        color: "red",
      },
      });
  }
  finally{
    reset()
  }
  });

  return (
    <>
    <form onSubmit={onSubmit}>
      <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet"></link>
      <input
        type="text"
        placeholder="Title"
        {
          ...register("title", 
            { 
            required: {
              value: true,
              message: 'Title required'
            },
            minLength: {
              value: 10,
              message: 'Menor de lo permitido'
            },
            maxLength: {
              value: 20,
              message: 'Mayor a lo permitido'
            }
          })}
        autoFocus
      />
      {errors.title && <span>{errors.title.message}</span>}

      <select {
        ...register("teacher",
        { 
          required: {
            value: true,
            message: 'Teacher required'
          }
        })}>
      {teachers.map(teacher => (
        <option key={teacher.id} value={teacher.id}>
          {teacher.name}
        </option>
      ))}
      </select>
      {errors.teacher && <span>{errors.teacher.message}</span> }
      <button>
        Save
      </button>
    </form>
    {params.id && (
          <button
            onClick={async () => {
              const accepted = window.confirm("Are you sure?");
              if (accepted) {
                await deleteCourse(params.id);
                toast.success("Course Removed", {
                  position: "bottom-right",
                  style: {
                    background: "#101010",
                    color: "#fff",
                  },
                });
                navigate(`/`);
              }
            }}
        >delete</button>
      )}
    </>
  )
}

export default FormCourse
