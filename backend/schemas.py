from datetime import datetime
from pydantic import BaseModel, Field


class RecipeBase(BaseModel):
    title: str
    ingredients: str
    directions: str
    # calories: float


class RecipeCreate(RecipeBase):
    pass


class RecipesOut(RecipeBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
