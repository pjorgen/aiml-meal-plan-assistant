import requests
import os
from pydantic import BaseModel
from typing import List, Optional

# Pydantic models for Spoonacular Search Recipes endpoint
class RecipeSummary(BaseModel):
    id: int
    title: str
    image: str
    imageType: str

class SearchRecipesResponse(BaseModel):
    results: List[RecipeSummary]
    offset: int
    number: int
    totalResults: int

# Function to search recipes using Spoonacular API
def search_recipes(api_key: str,
                   query: Optional[str] = None,
                   cuisine: Optional[str] = None,
                   diet: Optional[str] = None,
                   intolerances: Optional[str] = None,
                   includeIngredients: Optional[str] = None,
                   excludeIngredients: Optional[str] = None,
                   type: Optional[str] = None,
                   instructionsRequired: Optional[bool] = None,
                   limitLicense: Optional[bool] = None,
                   offset: int = 0,
                   number: int = 10) -> SearchRecipesResponse:
    """
    Search for recipes using Spoonacular API.

    Parameters:
    - api_key: Your Spoonacular API key
    - query: The (natural language) search query.
    - cuisine: The cuisine(s) of recipes (e.g., "Italian, Mexican").
    - diet: The diet to which the recipes must adhere (e.g., "vegetarian").
    - intolerances: A comma-separated list of intolerances (e.g., "dairy, gluten").
    - includeIngredients: A comma-separated list of ingredients that must be included.
    - excludeIngredients: A comma-separated list of ingredients that must be excluded.
    - type: The type of recipe (e.g., "main course").
    - instructionsRequired: Whether instructions are required.
    - limitLicense: Whether to only include recipes with an open license.
    - offset: The number of results to skip (for pagination).
    - number: The number of results to return.

    Returns:
    - SearchRecipesResponse: Parsed response model
    """
    url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "apiKey": api_key,
        "query": query,
        "cuisine": cuisine,
        "diet": diet,
        "intolerances": intolerances,
        "includeIngredients": includeIngredients,
        "excludeIngredients": excludeIngredients,
        "type": type,
        "instructionsRequired": instructionsRequired,
        "limitLicense": limitLicense,
        "offset": offset,
        "number": number
    }
    # Remove None values
    params = {k: v for k, v in params.items() if v is not None}

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()
    return SearchRecipesResponse(**data)

# Example usage:
if __name__ == "__main__":
    API_KEY = os.environ.get("SPOONAPIKEY")
    result = search_recipes(
        api_key=API_KEY,
        query="chocolate cake",
        diet="vegetarian",
        number=1
    )
    print(result)
