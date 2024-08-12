import { useNavigate } from "react-router-dom"

function Course({id, title, description, qualification, modules, teacher, price, img}) {

  const navigator = useNavigate()

  return (
    <div
    // navigate to main course detail data
    onClick={() => {
      navigator(`/Form/${id}`)
    }}>
      {/* background image course */}
      <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/640px-Python.svg.png' alt={title} />
      {/* course title */}
      <h1>{title}</h1>
      {/* course description */}
      <p>{description}</p>
      {/* score/qualification course */}
      <p>Score: {qualification}</p>
      {/* teacher who leads this course */}
      <p>Teacher: {teacher}</p>
      {/* modules amount */}
      <p>With {modules} modules</p>
      {/* course price $ */}
      <p>Price: ${price}</p>
    </div>
  )
}

export default Course