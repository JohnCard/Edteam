import { useNavigate } from "react-router-dom"

function Course({id, title, description, qualification, modules, teacher, price, img}) {

  const navigator = useNavigate()

  return (
    <div
    onClick={() => {
      navigator(`/Form/${id}`)
    }}>
      <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/640px-Python.svg.png' alt={title} />
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