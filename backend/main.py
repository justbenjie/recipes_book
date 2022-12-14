from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from .routers import recipe
from . import models
from .database import engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(recipe.router)


@app.get("/")
def get_routers():
    return ["/recipes", "/recipes/{id}"]
