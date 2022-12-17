from backend import schemas
import pytest


def validate(data):
    return schemas.RecipesOut(**data)


def test_get_recipes(client, test_recipes):
    res = client.get("/recipes/")
    recipes = list(map(validate, res.json()))

    assert res.status_code == 200
    assert len(recipes) == len(test_recipes)


def test_get_recipe(client, test_recipes):
    res = client.get(f"recipes/{test_recipes[0].id}")
    recipe = validate(res.json())

    assert res.status_code == 200
    assert recipe.id == test_recipes[0].id
    assert recipe.title == test_recipes[0].title
    assert recipe.ingredients == test_recipes[0].ingredients
    assert recipe.directions == test_recipes[0].directions


def test_get_recipe_doesnt_exist(client):
    res = client.get(f"recipes/-1")

    assert res.status_code == 404


@pytest.mark.parametrize(
    "title, ingredients, directions",
    [
        ("title1", "ingredients1", "directions1"),
        ("title2", "ingredients2", "directions2"),
        ("title3", "ingredients3", "directions3"),
    ],
)
def test_create_recipe(client, title, ingredients, directions):

    res = client.post(
        "/recipes/",
        json={"title": title, "ingredients": ingredients, "directions": directions},
    )

    created_recipe = schemas.RecipesOut(**res.json())

    assert res.status_code == 201
    assert created_recipe.title == title
    assert created_recipe.ingredients == ingredients
    assert created_recipe.directions == directions


def test_delete_recipe(client, test_recipes):
    res = client.delete(f"recipes/{test_recipes[0].id}")

    assert res.status_code == 204


def test_delete_recipe_doesnt_exist(client):
    res = client.delete("recipes/-1")

    assert res.status_code == 404


@pytest.mark.parametrize(
    "title, ingredients, directions",
    [
        ("title1", "ingredients1", "directions1"),
        ("title2", "ingredients2", "directions2"),
        ("title3", "ingredients3", "directions3"),
    ],
)
def test_update_recipes(client, test_recipes, title, ingredients, directions):
    res = client.put(
        f"recipes/{test_recipes[0].id}",
        json={"title": title, "ingredients": ingredients, "directions": directions},
    )
    updated_post = schemas.RecipesOut(**res.json())

    assert res.status_code == 200
    assert updated_post.title == title
    assert updated_post.ingredients == ingredients
    assert updated_post.directions == directions


def test_update_recipe_doesnt_exist(client):
    recipe_data = {
        "title": "updated_title",
        "ingredients": "updated_ingredients",
        "directions": "updated_directions",
    }
    res = client.put("recipes/-1", json=recipe_data)

    assert res.status_code == 404
