import dspy
import difflib
from lm import lm
from classes import SearchRecipesRequest
from enums import *

dspy.configure(lm=lm)


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


# Define DSPy Signatures
class ExtractMealCount(dspy.Signature):
    """Given a prompt, determine the total number of meals to plan"""
    text: str = dspy.InputField()
    meal_count: int = dspy.OutputField(desc="An integer that is the total number of meals")

class ExtractPeoplePerMeal(dspy.Signature):
    """Given a prompt and a number of meals, return a list of integers that defines the number of people attending each meal"""
    text: str = dspy.InputField()
    meal_count: int = dspy.InputField()
    people_per_meal: list[int] = dspy.OutputField(desc="A list of integers that defines the number of people attending each meal")

class ExtractMealTypes(dspy.Signature):
    """Given a prompt and a number of meals, determine what, if any, type of meal is described or requested for each meal."""
    text: str = dspy.InputField()
    meal_count: int = dspy.InputField()
    meal_types: str = dspy.OutputField(desc="A list of strings that describe the type of meal for each meal")

class ExtractIncludeCuisines(dspy.Signature):
    """Given a prompt, determine which, if any, cuisines are mentioned as liked or desired."""
    text: str = dspy.InputField()
    include_cuisines: list[str] = dspy.OutputField(desc="A list of strings that defines the cuisines")

class ExtractExcludeCuisines(dspy.Signature):
    """Given a prompt, determine which, if any, cuisines are mentioned as not liked or not desired."""
    text: str = dspy.InputField()
    exclude_cuisines: list[str] = dspy.OutputField(desc="A list of strings that defines the cuisines")

class ExtractDiets(dspy.Signature):
    """Given a prompt, determine what, if any, diets are mentioned as needing to be followed."""
    text: str = dspy.InputField()
    diets: list[str] = dspy.OutputField(desc="A list of strings that defines the diets")

class ExtractIntolerances(dspy.Signature):
    """Given a prompt, determine what, if any, food intolerances or allergies are described."""
    text: str = dspy.InputField()
    intolerances: list[str] = dspy.OutputField(desc="A list of strings that defines the food intolerances and allergies")

class ExtractIncludeIngredients(dspy.Signature):
    """Given a prompt, determine what, if any, foods or ingredients are described as liked, desired, or available."""
    text: str = dspy.InputField()
    include_ingredients: list[str] = dspy.OutputField(desc="A list of strings that defines the ingredients and foods that are liked, desired, or available.")

class ExtractExcludeIngredients(dspy.Signature):
    """Given a prompt, determine what, if any, foods or ingredients are described as disliked, undesired, or unavailable."""
    text: str = dspy.InputField()
    exclude_ingredients: list[str] = dspy.OutputField(desc="A list of strings that defines the ingredients and foods that are disliked, undesired, or unavailable.")

class ExtractHighFiber(dspy.Signature):
    """Given a prompt, determine if it includes a request for high fiber meals or diets."""
    text: str = dspy.InputField()
    high_fiber: bool = dspy.OutputField(desc="A boolean indicating whether or not a high fiber diet is indicated.")

class ExtractHighProtein(dspy.Signature):
    """Given a prompt, determine if it includes a request for high protein meals or diets."""
    text: str = dspy.InputField()
    high_protein: bool = dspy.OutputField(desc="A boolean indicating whether or not a high protein diet is indicated.")

class ExtractLowCalorie(dspy.Signature):
    """Given a prompt, determine if it includes a request for low calories meals or diets."""
    text: str = dspy.InputField()
    low_calorie: bool = dspy.OutputField(desc="A boolean indicating whether or not a low calorie diet is indicated.")

class ExtractLowCarb(dspy.Signature):
    """Given a prompt, determine if it includes a request for low-carb meals or diets."""
    text: str = dspy.InputField()
    low_carb: bool = dspy.OutputField(desc="A boolean indicating whether or not a low carb diet is indicated.")

class ExtractLowFat(dspy.Signature):
    """Given a prompt, determine if it includes a request for low fat meals or diets."""
    text: str = dspy.InputField()
    low_fat: bool = dspy.OutputField(desc="A boolean indicating whether or not a low fat diet is indicated.")

class ExtractLowCholesterol(dspy.Signature):
    """Given a prompt, determine if it includes a request for low cholesterol meals or diets."""
    text: str = dspy.InputField()
    low_cholesterol: bool = dspy.OutputField(desc="A boolean indicating whether or not a low cholesterol diet is indicated.")

class ExtractLowSatFat(dspy.Signature):
    """Given a prompt, determine if it includes a request for meals or diets with low saturated fat."""
    text: str = dspy.InputField()
    low_sat_fat: bool = dspy.OutputField(desc="A boolean indicating whether or not a low saturated fat diet is indicated.")

class ExtractLowSodium(dspy.Signature):
    """Given a prompt, determine if it includes a request for low sodium meals or diets."""
    text: str = dspy.InputField()
    low_sodium: bool = dspy.OutputField(desc="A boolean indicating whether or not a low sodium diet is indicated.")


class ExtractInfoModule(dspy.Module):
    def __init__(self):
        super().__init__()
        # Add each extractor signature
        self.get_meal_count = dspy.Predict(signature=ExtractMealCount)
        self.get_people_per_meal = dspy.Predict(signature=ExtractPeoplePerMeal)
        self.get_meal_types = dspy.Predict(signature=ExtractMealTypes)
        self.get_include_cuisines = dspy.Predict(signature=ExtractIncludeCuisines)
        self.get_exclude_cuisines = dspy.Predict(signature=ExtractExcludeCuisines)
        self.get_diets = dspy.Predict(signature=ExtractDiets)
        self.get_intolerances = dspy.Predict(signature=ExtractIntolerances)
        self.get_include_ingredients = dspy.Predict(signature=ExtractIncludeIngredients)
        self.get_exclude_ingredients = dspy.Predict(signature=ExtractExcludeIngredients)
        self.get_high_fiber = dspy.Predict(signature=ExtractHighFiber)
        self.get_high_protein = dspy.Predict(signature=ExtractHighProtein)
        self.get_low_calorie = dspy.Predict(signature=ExtractLowCalorie)
        self.get_low_carb = dspy.Predict(signature=ExtractLowCarb)
        self.get_low_fat = dspy.Predict(signature=ExtractLowFat)
        self.get_low_cholesterol = dspy.Predict(signature=ExtractLowCholesterol)
        self.get_low_sat_fat = dspy.Predict(signature=ExtractLowSatFat)
        self.get_low_sodium = dspy.Predict(signature=ExtractLowSodium)

    def forward(self, *, text: str) -> list[SearchRecipesRequest]:
        # Get the field values by calling each extractor
        meal_count = self.get_meal_count(text=text).meal_count
        people_per_meal = self.get_people_per_meal(text=text, meal_count=meal_count).people_per_meal
        meal_types = self.get_meal_types(text=text, meal_count=meal_count).meal_types
        include_cuisines = self.get_include_cuisines(text=text).include_cuisines
        exclude_cuisines = self.get_exclude_cuisines(text=text).exclude_cuisines
        diets = self.get_diets(text=text).diets
        intolerances = self.get_intolerances(text=text).intolerances
        include_ingredients = self.get_include_ingredients(text=text).include_ingredients
        exclude_ingredients = self.get_exclude_ingredients(text=text).exclude_ingredients
        high_fiber = self.get_high_fiber(text=text).high_fiber
        high_protein = self.get_high_protein(text=text).high_protein
        low_calorie = self.get_low_calorie(text=text).low_calorie
        low_carb = self.get_low_carb(text=text).low_carb
        low_fat = self.get_low_fat(text=text).low_fat
        low_cholesterol = self.get_low_cholesterol(text=text).low_cholesterol
        low_sat_fat = self.get_low_sat_fat(text=text).low_sat_fat
        low_sodium = self.get_low_sodium(text=text).low_sodium

        # Translate values into matched enum values
        include_cuisines = match_cuisine(include_cuisines)
        exclude_cuisines = match_cuisine(exclude_cuisines)
        diets = match_diet(diets)
        intolerances = match_intolerance(intolerances)
        meal_types = match_meal_type(meal_types)

        # Return the result as a list of pydantic models
        requests = []
        for m in range(meal_count):
            request = SearchRecipesRequest(
                cuisine = include_cuisines,
                excludeCuisine = exclude_cuisines,
                diet = diets,
                intolerances = intolerances,
                includeIngredients = include_ingredients,
                excludeIngredients = exclude_ingredients,
                type = meal_types[m] if m < len(meal_types) else None,
                minServings = people_per_meal[m] if m < len(people_per_meal) else None,
                minFiber = Nutrition.HIGH_FIBER if high_fiber else None,
                minProtein = Nutrition.HIGH_PROTEIN if high_protein else None,
                maxCalories = Nutrition.LOW_CALORIE if low_calorie else None,
                maxCarbs = Nutrition.LOW_CARB if low_carb else None,
                maxFat = Nutrition.LOW_FAT if low_fat else None,
                maxCholesterol = Nutrition.LOW_CHOLESTEROL if low_cholesterol else None,
                maxSaturatedFat = Nutrition.LOW_SATURATED_FAT if low_sat_fat else None,
                maxSodium = Nutrition.LOW_SODIUM if low_sodium else None
            )
            requests.append(request)

        return requests
