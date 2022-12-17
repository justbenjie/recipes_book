import React from 'react'
import { Link } from 'react-router-dom'

let getTimestamp = (recipe) => {
  return new Date(recipe.created_at).toLocaleDateString()
}

let trimmedContent = (recipe) => {
  //Slice content and add three dots in over 45 characters to show there is more
  let content = recipe.title

  if (content.length > 45) {
    return content.slice(0, 45) + '...'
  } else {
      return content
  }
}

const ListItem = ({recipe}) => {
  return (

    <Link to={`/${recipe.id}`}>
      <div className="notes-list-item">
        <h3>{trimmedContent(recipe)}</h3>
        <p><span>{getTimestamp(recipe)}</span></p>
      </div>
    </Link>
  )
}

export default ListItem