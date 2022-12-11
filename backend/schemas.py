from datetime import datetime
from pydantic import BaseModel, Field


class RecipeBase(BaseModel):
    title: str = Field(..., max_length=30)
    ingredients: str = Field(...)
    directions: str = Field(...)
    calories: float = Field(..., ge=0)


class RecipeCreate(BaseModel):
    pass


class RecipesOut(RecipeBase):
    created_at: datetime
