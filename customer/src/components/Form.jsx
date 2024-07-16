import { useForm } from "react-hook-form";
import { createCourse } from "../api/courses.api";
import toast from "react-hot-toast";

function FormCourse() {

    const {
        register,
        handleSubmit,
        formState: { errors },
        setValue,
        } = useForm();

    const onSubmit = handleSubmit(async (data) => {
        
        await createCourse(data);
        toast.success("New Course Added", {
        position: "bottom-right",
        style: {
            background: "#101010",
            color: "#fff",
        },
        });
    
    });

  return (
    <form onSubmit={onSubmit}>
        <input
          type="text"
          placeholder="Title"
          {...register("title", { required: true })}
          autoFocus
        />

        {errors.title && <span>We need the course title</span>}

        <button>
          Save
        </button>
    </form>
  )
}

export default FormCourse
