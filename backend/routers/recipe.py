from fastapi import Response, status, HTTPException, Depends, APIRouter
from typing import List
from .. import models, schemas
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(prefix="/recipes", tags=["Recipes"])


@router.get("/", response_model=List[schemas.RecipesOut])
def get_recipes(
    db: Session = Depends(get_db),
    limit: int | None = None,
    skip: int = 0,
    search: str | None = "",
):

    recipes = (
        db.query(models.Recipe)
        .filter(models.Recipe.title.contains(search))
        .order_by(models.Recipe.created_at.desc())
    )

    results = recipes.limit(limit).offset(skip).all()

    return results


@router.get("/{id}", response_model=schemas.RecipesOut)
def get_recipe(id: int, db: Session = Depends(get_db)):

    recipe = db.query(models.Recipe).filter(models.Recipe.id == id).first()

    if recipe is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Recipe with id: {id} was not found!",
        )

    return recipe


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=schemas.RecipesOut
)
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):

    new_recipe = models.Recipe(**recipe.dict())
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)

    return new_recipe


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_recipe(id: int, db: Session = Depends(get_db)):

    recipe = db.query(models.Recipe).filter(models.Recipe.id == id)

    result = recipe.first()

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Recipe with id: {id} doesn't exist",
        )

    recipe.delete(synchronize_session=False)

    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.RecipesOut)
def update_recipe(
    id: int, updated_recipe: schemas.RecipeCreate, db: Session = Depends(get_db)
):

    recipe = db.query(models.Recipe).filter(models.Recipe.id == id)
    result = recipe.first()

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Recipe with id: {id} doesn't exist",
        )

    recipe.update(updated_recipe.dict(), synchronize_session=False)
    db.commit()

    return result
