import dspy
from lm import lm
from pathlib import Path
from classes import ExtractedInfo
from enums import *


# Define DSPy Signatures
class ExtractMealCount(dspy.Signature):
    """Given a prompt, determine the total number of meals to plan"""
    meal_plan_prompt: str = dspy.InputField()
    meal_count: int = dspy.OutputField(desc="An integer that is the total number of meals")

class ExtractPeoplePerMeal(dspy.Signature):
    """Given a prompt and a number of meals, return an integer that defines the number of people attending each meal"""
    meal_plan_prompt: str = dspy.InputField()
    meal_count: int = dspy.InputField()
    people_per_meal: int = dspy.OutputField(desc="An integer that defines the number of people attending each meal")

class ExtractMealTypes(dspy.Signature):
    """Given a prompt and a number of meals, determine what, if any, type of meal is described or requested for each meal."""
    meal_plan_prompt: str = dspy.InputField()
    meal_count: int = dspy.InputField()
    meal_types: list[MealTypeLiteral] = dspy.OutputField(desc="A list of strings that describe the type of meal for each meal")

class ExtractIncludeCuisines(dspy.Signature):
    """Given a prompt, determine which, if any, cuisines are mentioned as liked or desired."""
    meal_plan_prompt: str = dspy.InputField()
    include_cuisines: list[CuisineLiteral] = dspy.OutputField(desc="A list of strings that defines the cuisines")

class ExtractExcludeCuisines(dspy.Signature):
    """Given a prompt, determine which, if any, cuisines are mentioned as not liked or not desired."""
    meal_plan_prompt: str = dspy.InputField()
    exclude_cuisines: list[CuisineLiteral] = dspy.OutputField(desc="A list of strings that defines the cuisines")

class ExtractDiets(dspy.Signature):
    """Given a prompt, determine what, if any, diets are mentioned as needing to be followed."""
    meal_plan_prompt: str = dspy.InputField()
    diets: list[DietLiteral] = dspy.OutputField(desc="A list of strings that defines the diets")

class ExtractIntolerances(dspy.Signature):
    """Given a prompt, determine what, if any, food intolerances or allergies are described."""
    meal_plan_prompt: str = dspy.InputField()
    intolerances: list[IntoleranceLiteral] = dspy.OutputField(desc="A list of strings that defines the food intolerances and allergies")

class ExtractIncludeIngredients(dspy.Signature):
    """Given a prompt, determine what, if any, foods or ingredients are described as liked, desired, or available. Do not add any that are not explicitly mentioned in the prompt."""
    meal_plan_prompt: str = dspy.InputField()
    include_ingredients: list[str] = dspy.OutputField(desc="A list of strings that defines the ingredients and foods that are liked, desired, or available as specified in the prompt.")

class ExtractExcludeIngredients(dspy.Signature):
    """Given a prompt, determine what, if any, foods or ingredients are described as disliked, undesired, or unavailable."""
    meal_plan_prompt: str = dspy.InputField()
    exclude_ingredients: list[str] = dspy.OutputField(desc="A list of strings that defines the ingredients and foods that are disliked, undesired, or unavailable as specified in the prompt.")

class ExtractHighFiber(dspy.Signature):
    """Given a prompt, determine if it includes a request for high fiber meals or diets."""
    meal_plan_prompt: str = dspy.InputField()
    high_fiber: bool = dspy.OutputField(desc="A boolean indicating whether or not a high fiber diet is indicated.")

class ExtractHighProtein(dspy.Signature):
    """Given a prompt, determine if it includes a request for high protein meals or diets."""
    meal_plan_prompt: str = dspy.InputField()
    high_protein: bool = dspy.OutputField(desc="A boolean indicating whether or not a high protein diet is indicated.")

class ExtractLowCalorie(dspy.Signature):
    """Given a prompt, determine if it includes a request for low calories meals or diets."""
    meal_plan_prompt: str = dspy.InputField()
    low_calorie: bool = dspy.OutputField(desc="A boolean indicating whether or not a low calorie diet is indicated.")

class ExtractLowCarb(dspy.Signature):
    """Given a prompt, determine if it includes a request for low-carb meals or diets."""
    meal_plan_prompt: str = dspy.InputField()
    low_carb: bool = dspy.OutputField(desc="A boolean indicating whether or not a low carb diet is indicated.")

class ExtractLowFat(dspy.Signature):
    """Given a prompt, determine if it includes a request for low fat meals or diets."""
    meal_plan_prompt: str = dspy.InputField()
    low_fat: bool = dspy.OutputField(desc="A boolean indicating whether or not a low fat diet is indicated.")

class ExtractLowCholesterol(dspy.Signature):
    """Given a prompt, determine if it includes a request for low cholesterol meals or diets."""
    meal_plan_prompt: str = dspy.InputField()
    low_cholesterol: bool = dspy.OutputField(desc="A boolean indicating whether or not a low cholesterol diet is indicated.")

class ExtractLowSatFat(dspy.Signature):
    """Given a prompt, determine if it includes a request for meals or diets with low saturated fat."""
    meal_plan_prompt: str = dspy.InputField()
    low_sat_fat: bool = dspy.OutputField(desc="A boolean indicating whether or not a low saturated fat diet is indicated.")

class ExtractLowSodium(dspy.Signature):
    """Given a prompt, determine if it includes a request for low sodium meals or diets."""
    meal_plan_prompt: str = dspy.InputField()
    low_sodium: bool = dspy.OutputField(desc="A boolean indicating whether or not a low sodium diet is indicated.")


# Collect DSPy signatures into a module
class ExtractInfoModule(dspy.Module):
    def __init__(self):
        super().__init__()

        # Configure dspy
        dspy.configure(lm=lm)

        # Load optimized module from file
        #path = Path("optimized", "extract_optimized.json")
        #self.load(str(path))

        # Add each extractor signature
        self.get_meal_count = dspy.ChainOfThought(signature=ExtractMealCount)
        self.get_people_per_meal = dspy.ChainOfThought(signature=ExtractPeoplePerMeal)
        self.get_meal_types = dspy.ChainOfThought(signature=ExtractMealTypes)
        self.get_include_cuisines = dspy.ChainOfThought(signature=ExtractIncludeCuisines)
        self.get_exclude_cuisines = dspy.ChainOfThought(signature=ExtractExcludeCuisines)
        self.get_diets = dspy.ChainOfThought(signature=ExtractDiets)
        self.get_intolerances = dspy.ChainOfThought(signature=ExtractIntolerances)
        self.get_include_ingredients = dspy.ChainOfThought(signature=ExtractIncludeIngredients)
        self.get_exclude_ingredients = dspy.ChainOfThought(signature=ExtractExcludeIngredients)
        self.get_high_fiber = dspy.ChainOfThought(signature=ExtractHighFiber)
        self.get_high_protein = dspy.ChainOfThought(signature=ExtractHighProtein)
        self.get_low_calorie = dspy.ChainOfThought(signature=ExtractLowCalorie)
        self.get_low_carb = dspy.ChainOfThought(signature=ExtractLowCarb)
        self.get_low_fat = dspy.ChainOfThought(signature=ExtractLowFat)
        self.get_low_cholesterol = dspy.ChainOfThought(signature=ExtractLowCholesterol)
        self.get_low_sat_fat = dspy.ChainOfThought(signature=ExtractLowSatFat)
        self.get_low_sodium = dspy.ChainOfThought(signature=ExtractLowSodium)

    def extract_meal_criteria(self, text: str) -> ExtractedInfo:
        meal_count = self.get_meal_count(meal_plan_prompt=text).meal_count

        # Get the field values by calling each extractor
        model = ExtractedInfo(
            meal_count = meal_count,
            people_per_meal = self.get_people_per_meal(meal_plan_prompt=text, meal_count=meal_count).people_per_meal,
            meal_types = self.get_meal_types(meal_plan_prompt=text, meal_count=meal_count).meal_types,
            include_cuisines = self.get_include_cuisines(meal_plan_prompt=text).include_cuisines,
            exclude_cuisines = self.get_exclude_cuisines(meal_plan_prompt=text).exclude_cuisines,
            diets = self.get_diets(meal_plan_prompt=text).diets,
            intolerances = self.get_intolerances(meal_plan_prompt=text).intolerances,
            include_ingredients = self.get_include_ingredients(meal_plan_prompt=text).include_ingredients,
            exclude_ingredients = self.get_exclude_ingredients(meal_plan_prompt=text).exclude_ingredients,
            high_fiber = self.get_high_fiber(meal_plan_prompt=text).high_fiber,
            high_protein = self.get_high_protein(meal_plan_prompt=text).high_protein,
            low_calorie = self.get_low_calorie(meal_plan_prompt=text).low_calorie,
            low_carb = self.get_low_carb(meal_plan_prompt=text).low_carb,
            low_fat = self.get_low_fat(meal_plan_prompt=text).low_fat,
            low_cholesterol = self.get_low_cholesterol(meal_plan_prompt=text).low_cholesterol,
            low_sat_fat = self.get_low_sat_fat(meal_plan_prompt=text).low_sat_fat,
            low_sodium = self.get_low_sodium(meal_plan_prompt=text).low_sodium
        )

        return model

    def forward(self, *, text: str) -> ExtractedInfo:
        return self.extract_meal_criteria(text=text)
