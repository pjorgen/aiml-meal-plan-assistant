import difflib
from pydantic import BaseModel
from typing import List, Optional, Literal
from enums import *


# Define field validators
def match_cuisine(value: list[str]) -> list[Cuisine] | None:
    if value is None: return None
    matched = []
    for val in value:
        matches = difflib.get_close_matches(val, [c.value for c in Cuisine], n=1, cutoff=0.7)
        if matches:
            matched.append(Cuisine(matches[0]))
    return matched

def match_diet(value: list[str]) -> list[Diet] | None:
    if value is None: return None
    matched = []
    for val in value:
        matches = difflib.get_close_matches(val, [d.value for d in Diet], n=1, cutoff=0.7)
        if matches:
            matched.append(Diet(matches[0]))
    return matched

def match_intolerance(value: list[str]) -> list[Intolerance] | None:
    if value is None: return None
    matched = []
    for val in value:
        matches = difflib.get_close_matches(val, [i.value for i in Intolerance], n=1, cutoff=0.7)
        if matches:
            matched.append(Intolerance(matches[0]))
    return matched

def match_meal_type(value: list[str]) -> list[MealType] | None:
    if value is None: return None
    matched = []
    for val in value:
        matches = difflib.get_close_matches(val, [m.value for m in MealType], n=1, cutoff=0.7)
        if matches:
            matched.append(MealType(matches[0]))
    return matched


# Pydantic models for recipe requests and responses
class RecipeSummary(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    image: Optional[str] = None
    imageType: Optional[str] = None
    servings: Optional[int] = None
    readyInMinutes: Optional[int] = None
    cookingMinutes: Optional[int] = None


class UnitMeasure(BaseModel):
    amount: Optional[float] = None
    unitLong: Optional[str] = None
    unitShort: Optional[str] = None


class Measures(BaseModel):
    us: Optional[UnitMeasure] = None
    metric: Optional[UnitMeasure] = None


class ExtendedIngredient(BaseModel):
    aisle: Optional[str] = None
    amount: Optional[float] = None
    consistency: Optional[Literal["solid", "liquid"]] = None
    id: Optional[int] = None
    image: Optional[str] = None
    measures: Optional[Measures] = None
    meta: Optional[List[str]] = None
    name: Optional[str] = None
    original: Optional[str] = None
    originalName: Optional[str] = None
    unit: Optional[str] = None


class ProductMatch(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[str] = None
    imageUrl: Optional[str] = None
    averageRating: Optional[float] = None
    ratingCount: Optional[float] = None
    score: Optional[float] = None
    link: Optional[str] = None


class WinePairing(BaseModel):
    pairedWines: Optional[List[str]] = None
    pairingText: Optional[str] = None
    productMatches: Optional[List[ProductMatch]] = None


class RecipeDetail(RecipeSummary):
    preparationMinutes: Optional[int] = None
    license: Optional[str] = None
    sourceName: Optional[str] = None
    sourceUrl: Optional[str] = None
    spoonacularSourceUrl: Optional[str] = None
    healthScore: Optional[float] = None
    spoonacularScore: Optional[float] = None
    pricePerServing: Optional[float] = None
    cheap: Optional[bool] = None
    creditsText: Optional[str] = None
    cuisines: Optional[List[Cuisine]] = None
    dairyFree: Optional[bool] = None
    diets: Optional[List[Diet]] = None
    gaps: Optional[str] = None
    glutenFree: Optional[bool] = None
    instructions: Optional[str] = None
    ketogenic: Optional[bool] = None
    lowFodmap: Optional[bool] = None
    occasions: Optional[List[str]] = None
    sustainable: Optional[bool] = None
    vegan: Optional[bool] = None
    vegetarian: Optional[bool] = None
    veryHealthy: Optional[bool] = None
    veryPopular: Optional[bool] = None
    whole30: Optional[bool] = None
    weightWatcherSmartPoints: Optional[int] = None
    dishTypes: Optional[List[str]] = None
    extendedIngredients: Optional[List[ExtendedIngredient]] = None
    summary: Optional[str] = None
    winePairing: Optional[WinePairing] = None

    # Include this inner class to force enums to be printed as values instead of enums
    class Config:
        use_enum_values = True


class SearchRecipesResponse(BaseModel):
    results: Optional[List[RecipeDetail]] = None
    offset: Optional[int] = None
    number: Optional[int] = None
    totalResults: Optional[int] = None


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


class ExtractedInfo(BaseModel):
    meal_count: int
    people_per_meal: int
    meal_types: list[str]
    include_cuisines: list[str]
    exclude_cuisines: list[str]
    diets: list[str]
    intolerances: list[str]
    include_ingredients: list[str]
    exclude_ingredients: list[str]
    high_fiber: bool
    high_protein: bool
    low_calorie: bool
    low_carb: bool
    low_fat: bool
    low_cholesterol: bool
    low_sat_fat: bool
    low_sodium: bool

    # Include this inner class to force enums to be printed as values instead of enums
    class Config:
        use_enum_values = True


def info_to_requests( info: ExtractedInfo) -> list[SearchRecipesRequest] | None:
    requests = []
    meal_types = match_meal_type(info.meal_types)
    for m in range(info.meal_count):
        request = SearchRecipesRequest(
            cuisine = match_cuisine(info.include_cuisines),
            excludeCuisine = match_cuisine(info.exclude_cuisines),
            diet = match_diet(info.diets),
            intolerances = match_intolerance(info.intolerances),
            includeIngredients = info.include_ingredients,
            excludeIngredients = info.exclude_ingredients,
            type = meal_types[m % len(meal_types)] if len(meal_types) > 0 else None,
            minServings = info.people_per_meal,
            minFiber = Nutrition.HIGH_FIBER if info.high_fiber else None,
            minProtein = Nutrition.HIGH_PROTEIN if info.high_protein else None,
            maxCalories = Nutrition.LOW_CALORIE if info.low_calorie else None,
            maxCarbs = Nutrition.LOW_CARB if info.low_carb else None,
            maxFat = Nutrition.LOW_FAT if info.low_fat else None,
            maxCholesterol = Nutrition.LOW_CHOLESTEROL if info.low_cholesterol else None,
            maxSaturatedFat = Nutrition.LOW_SATURATED_FAT if info.low_sat_fat else None,
            maxSodium = Nutrition.LOW_SODIUM if info.low_sodium else None
        )
        requests.append(request)
        return requests
