from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from .routers import recipe
from pymongo import MongoClient
from .config import settings

app = FastAPI()

client = MongoClient(settings.HOST, settings.PORT)
db = 
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
    post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"]}

    
    return ["/recipes", "/recipes/{id}"]
