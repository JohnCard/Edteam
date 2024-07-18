import { useNavigate } from "react-router-dom"

function Course({id, title, description, qualification, modules, teacher, price, img}) {

  const navigator = useNavigate()

  return (
    <div
    onClick={() => {
      navigator(`/Form/${id}`)
    }}>
      <img src='https://edteam-media.s3.amazonaws.com/courses/medium/c498682a-3622-4f5e-80bc-2cc299a47f89.png' alt={title} />
      <h1>{title}</h1>
      <p>{description}</p>
      <p>Score: {qualification}</p>
      <p>Teacher: {teacher}</p>
      <p>With {modules} modules</p>
      <p>Price: ${price}</p>
    </div>
  )
}

export default Course