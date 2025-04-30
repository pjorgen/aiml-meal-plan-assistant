import requests
import os
from classes import *

# Function to search recipes using Spoonacular API
def search_recipes(model: SearchRecipesRequest) -> SearchRecipesResponse:
    """
    Search for recipes using Spoonacular API.

    Parameters:
    - SearchRecipesRequest: Spoonacular API request object

    Returns:
    - SearchRecipesResponse: Parsed response model
    """
    url = "https://api.spoonacular.com/recipes/complexSearch"
    model.apiKey = os.getenv("SPOONAPIKEY")
    params = model.model_dump(exclude_none=True)
    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()
    return SearchRecipesResponse(**data)