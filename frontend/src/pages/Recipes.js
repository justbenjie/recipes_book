import React, {useState, useEffect} from 'react'
import ListItem from '../components/ListItem'
import { Link } from 'react-router-dom'
import { ReactComponent as AddIcon } from '../assets/add.svg'

const Recipes = () => {
  let [recipes, setRecipes] = useState([])

  useEffect(() => {
    getRecipes()
  }, [])

  let getRecipes = async () => {
    let response = await fetch('/recipes/')
    let data = await response.json()
    setRecipes(data)
  }

  return (
    <div className='notes'>
      <div className='notes-header'>
        <div className='notes-title'>&#9782; Recipes</div>
        <div className='notes-count'>{recipes.length}</div>
      </div>
      
      <div className="notes-list">
        {recipes.map((recipe) => (
          <ListItem key={recipe.id} recipe={recipe} />
        ))}
      </div>

      <Link className="floating-button" to={'/add'}>
        <AddIcon />
      </Link>

    </div>
  )
}

export default Recipes