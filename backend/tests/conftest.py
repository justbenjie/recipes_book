from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.main import app
from backend.database import get_db, Base
from backend import models

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@localhost:5432/recipes_test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def session():

    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

    Base.metadata.drop_all(bind=engine)


@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db

    yield TestClient(app)


@pytest.fixture
def test_recipes(session):
    recipes_data = [
        {
            "title": "test_title",
            "ingredients": "test_ingredients",
            "directions": "test_directions",
        },
        {
            "title": "test_title1",
            "ingredients": "test_ingredients1",
            "directions": "test_directions1",
        },
        {
            "title": "test_title2",
            "ingredients": "test_ingredients2",
            "directions": "test_directions2",
        },
    ]

    def create_recipe_model(data):
        return models.Recipe(**data)

    recipes = list(map(create_recipe_model, recipes_data))
    session.add_all(recipes)
    session.commit()

    return session.query(models.Recipe).all()
