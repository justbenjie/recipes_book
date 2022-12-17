import React, {useState, useEffect} from 'react'
import { useParams, Link, useNavigate } from 'react-router-dom'
import { ReactComponent as ArrowLeft } from '../assets/arrow-left.svg'
import { ReactComponent as SaveIcon } from '../assets/save.svg'


const Recipe = () => {
  let navigate = useNavigate()
  let params = useParams()
  let recipeId = params.id

  let [recipe, setRecipe] = useState(null)

  useEffect(() => {
    if(recipeId !== 'add') getRecipe()
  }, [recipeId])

  let getRecipe = async () => {
    let response = await fetch(`/recipes/${params.id}`)
    let data = await response.json()
    setRecipe(data)
  }
  
  let submitData = async (e) => {
    e.preventDefault()

    let url = '/recipes/'
    let method = 'POST'

    
    if (params.id !== 'add') {
      url = `/recipes/${params.id}`
      method = 'PUT'
    }
    

    if (recipe.title === '' || recipe.title === undefined || recipe.ingredients === '' || recipe.ingredients === undefined || recipe.directions === '' || recipe.directions === undefined) {
      alert('All fields are required!')
      return 
    }

    await fetch (url, {
      method:method,
        headers:{
          'Content-Type': 'application/json',
        }, body:JSON.stringify(recipe)
    })

    navigate('/')
  }

  let deleteRecipe = async (e) => {
    e.preventDefault()
    await fetch(`/recipes/${params.id}`, {method:'DELETE'})
    navigate('/')
  }


  return (
    <div className="note">
      <div className='note-header'>
        <h3>
          <Link to="/">
              <ArrowLeft />
          </Link>
        </h3>

        {recipeId !== 'add' && (<button onClick={deleteRecipe}>Delete</button>)}

      </div>

        
        <textarea className='textareatitle' onChange={(e) => setRecipe({...recipe, title: e.target.value})} value={recipe?.title} placeholder="Enter title..."></textarea>
        <textarea className='textarea' onChange={(e) => setRecipe({...recipe, ingredients: e.target.value})} value={recipe?.ingredients} placeholder="Enter ingredients..."></textarea>
        <textarea className='textarea' onChange={(e) => setRecipe({...recipe, directions: e.target.value})} value={recipe?.directions} placeholder="Enter directions..."></textarea>
        
          

        <div onClick={submitData} className="floating-button">
            <SaveIcon  />
        </div>
    </div>
  )
}

export default Recipe