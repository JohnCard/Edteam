function Course({title, description, qualification, modules, teacher, price}) {
  return (
    <div>
        <h1>{title}</h1>
        <p>{description}</p>
        <p>Score: {qualification}</p>
        <p>Teacher: {teacher}</p>
        <p>$ {price}</p>
        <p>With {modules} modules</p>
    </div>
  )
}

export default Course