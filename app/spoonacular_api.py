import requests
import os
from classes import *
from pprint import pprint

# Function to search recipes using Spoonacular API
def search_recipes(model: list[SearchRecipesRequest]) -> list[SearchRecipesResponse]:
    """
    Search for recipes using Spoonacular API.

    Parameters:
    - SearchRecipesRequest: Spoonacular API request object

    Returns:
    - SearchRecipesResponse: Parsed response model
    """
    url = "https://api.spoonacular.com/recipes/complexSearch"

    recipes = []
    for meal in model:
        meal.apiKey = os.getenv("SPOONAPIKEY")
        params = meal.model_dump(exclude_none=True)
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()
        # pprint(data)
        recipe = SearchRecipesResponse(**data)
        recipes.append(recipe)
    return recipes