from pydantic import BaseModel
from typing import List, Optional, Literal
from enums import *


# Pydantic models for Spoonacular Search Recipes endpoint
class RecipeSummary(BaseModel):
    id: int
    title: str
    image: str
    imageType: str
    servings: int
    readyInMinutes: int
    cookingMinutes: int


class UnitMeasure(BaseModel):
    amount: float
    unitLong: str
    unitShort: str


class Measures(BaseModel):
    us: UnitMeasure
    metric: UnitMeasure


class ExtendedIngredient(BaseModel):
    aisle: str
    amount: float
    consistency: Optional[Literal["solid", "liquid"]]
    id: int
    image: str
    measures: Measures
    meta: List[str]
    name: str
    original: str
    originalName: str
    unit: str


class ProductMatch(BaseModel):
    id: int
    title: str
    description: str
    price: str
    imageUrl: str
    averageRating: float
    ratingCount: float
    score: float
    link: str


class WinePairing(BaseModel):
    pairedWines: List[str]
    pairingText: str
    productMatches: List[ProductMatch]


class RecipeDetail(RecipeSummary):
    preparationMinutes: Optional[int]
    license: Optional[str]
    sourceName: Optional[str]
    sourceUrl: Optional[str]
    spoonacularSourceUrl: Optional[str]
    healthScore: Optional[float]
    spoonacularScore: Optional[float]
    pricePerServing: Optional[float]
    cheap: bool
    creditsText: Optional[str]
    cuisines: List[Cuisine]
    dairyFree: bool
    diets: List[Diet]
    gaps: Optional[str]
    glutenFree: bool
    instructions: Optional[str]
    ketogenic: bool
    lowFodmap: bool
    occasions: List[str]
    sustainable: bool
    vegan: bool
    vegetarian: bool
    veryHealthy: bool
    veryPopular: bool
    whole30: bool
    weightWatcherSmartPoints: int
    dishTypes: List[str]
    extendedIngredients: List[ExtendedIngredient]
    summary: str
    winePairing: Optional[WinePairing]


class SearchRecipesResponse(BaseModel):
    results: List[RecipeDetail]
    offset: int
    number: int
    totalResults: int


class SearchRecipesRequest(BaseModel):
    apiKey: Optional[str] = None
    query: Optional[str] = None
    cuisine: Optional[List[Cuisine]] = None
    excludeCuisine: Optional[List[Cuisine]] = None
    diet: Optional[List[Diet]] = None
    intolerances: Optional[List[Intolerance]] = None
    includeIngredients: Optional[List[str]] = None
    excludeIngredients: Optional[List[str]] = None
    type: Optional[MealType] = None
    minServings: Optional[int] = None
    minFiber: Optional[int] = None
    minProtein: Optional[int] = None
    maxCalories: Optional[int] = None
    maxCarbs: Optional[int] = None
    maxFat: Optional[int] = None
    maxCholesterol: Optional[int] = None
    maxSaturatedFat: Optional[int] = None
    maxSodium: Optional[int] = None
    instructionsRequired: bool = True
    addRecipeInstructions: bool = True
    addRecipeNutrition: bool = True
    offset: int = 0
    number: int = 1

    # Include this inner class to force enums to be printed as values instead of enums
    class Config:
        use_enum_values = True
