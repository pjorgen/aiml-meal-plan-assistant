import dspy
from lm import lm
from pathlib import Path
from classes import ExtractedInfo
from enums import *


# Define DSPy Signatures
class ExtractMealCount(dspy.Signature):
    """
    You are an information-extraction specialist. Always:
    - Read the entire input carefully
    - Extract only the fields and information requested
    - Return them exactly as a single integer, with no additional commentary
    - Think in terms of entire meals only, not recipes or courses
    - Your response should answer the question, "How many meals are being requested?"
    """
    meal_plan_prompt: str = dspy.InputField()
    meal_count: int = dspy.OutputField()

class ExtractPeoplePerMeal(dspy.Signature):
    """
    You are an information-extraction specialist. Always:
    - Read the entire input carefully
    - Extract only the fields and information requested
    - Return them exactly as a single integer, with no additional commentary
    - Think in terms of entire meals only, not recipes or courses
    - Your response should answer the question, "How many people are attending each meal?"
    """
    meal_plan_prompt: str = dspy.InputField()
    meal_count: int = dspy.InputField()
    people_per_meal: int = dspy.OutputField()

class ExtractMealTypes(dspy.Signature):
    """
    You are an information-extraction specialist. Always:
    - Read the entire input carefully
    - Extract only the fields and information requested
    - Return them exactly as a list of strings, with no additional commentary
    - Think in terms of entire meals only, not recipes or courses
    - Your response should answer the question, "What meal types are requested?"
    - If no meal types are requested, return an empty list
    """
    meal_plan_prompt: str = dspy.InputField()
    meal_count: int = dspy.InputField()
    meal_types: list[str] = dspy.OutputField()

class ExtractIncludeCuisines(dspy.Signature):
    """
    You are an information-extraction specialist. Always:
    - Read the entire input carefully
    - Extract only the fields and information requested
    - Return them exactly as a list of strings, with no additional commentary
    - Think in terms of entire meals only, not recipes or courses
    - Your response should answer the question, "What cuisines are desired, liked, or requested?"
    - If no cuisines are desired, return an empty list
    """
    meal_plan_prompt: str = dspy.InputField()
    include_cuisines: list[str] = dspy.OutputField()

class ExtractExcludeCuisines(dspy.Signature):
    """
    You are an information-extraction specialist. Always:
    - Read the entire input carefully
    - Extract only the fields and information requested
    - Return them exactly as a list of strings, with no additional commentary
    - Think in terms of entire meals only, not recipes or courses
    - Your response should answer the question, "What cuisines are not desired or disliked?"
    - If no cuisines match, return an empty list
    """
    meal_plan_prompt: str = dspy.InputField()
    exclude_cuisines: list[str] = dspy.OutputField()

class ExtractDiets(dspy.Signature):
    """
    You are an information-extraction specialist. Always:
    - Read the entire input carefully
    - Extract only the fields and information requested
    - Return them exactly as a list of strings, with no additional commentary
    - Think in terms of entire meals only, not recipes or courses
    - Your response should answer the question, "What diets are desired, liked, requested, or being followed?"
    - If there are no diets mentioned, return an empty list
    """
    meal_plan_prompt: str = dspy.InputField()
    diets: list[str] = dspy.OutputField()

class ExtractIntolerances(dspy.Signature):
    """
    You are an information-extraction specialist. Always:
    - Read the entire input carefully
    - Extract only the fields and information requested
    - Return them exactly as a list of strings, with no additional commentary
    - Think in terms of entire meals only, not recipes or courses
    - Your response should answer the question, "What food intolerances or allergies are specified, noted, or indicated?"
    - If there are no food intolerances, return an empty list
    """
    meal_plan_prompt: str = dspy.InputField()
    intolerances: list[str] = dspy.OutputField()

class ExtractIncludeIngredients(dspy.Signature):
    """
    You are an information-extraction specialist. Always:
    - Read the entire input carefully
    - Extract only the fields and information requested
    - Do not include any ingredients not specifically described in the prompt
    - Return them exactly as a list of strings, with no additional commentary
    - Your response should answer the question, "What ingredients are requested, available, or desired?"
    """
    meal_plan_prompt: str = dspy.InputField()
    include_ingredients: list[str] = dspy.OutputField()

class ExtractExcludeIngredients(dspy.Signature):
    """
    You are an information-extraction specialist. Always:
    - Read the entire input carefully
    - Extract only the fields and information requested
    - Do not include any ingredients not specifically described in the prompt
    - Return them exactly as a list of strings, with no additional commentary
    - Your response should answer the question, "What ingredients are unavailable or disliked?"
    """
    meal_plan_prompt: str = dspy.InputField()
    exclude_ingredients: list[str] = dspy.OutputField()

class ExtractHighFiber(dspy.Signature):
    """
    You are an information-extraction specialist. Always:
    - Read the entire input carefully
    - Extract only the fields and information requested
    - Return them exactly as a single boolean, with no additional commentary
    - Think in terms of entire meals only, not recipes or courses
    - Your response should answer the question, "True or false, does the given prompt include a request for a high fiber diet?"
    - Return a default value of False if no mention is made of fiber
    """
    meal_plan_prompt: str = dspy.InputField()
    high_fiber: bool = dspy.OutputField()

class ExtractHighProtein(dspy.Signature):
    """
    You are an information-extraction specialist. Always:
    - Read the entire input carefully
    - Extract only the fields and information requested
    - Return them exactly as a single boolean, with no additional commentary
    - Think in terms of entire meals only, not recipes or courses
    - Your response should answer the question, "True or false, does the given prompt include a request for a high protein diet?"
    - Return a default value of False if no mention is made of protein
    """
    meal_plan_prompt: str = dspy.InputField()
    high_protein: bool = dspy.OutputField()

class ExtractLowCalorie(dspy.Signature):
    """
    You are an information-extraction specialist. Always:
    - Read the entire input carefully
    - Extract only the fields and information requested
    - Return them exactly as a single boolean, with no additional commentary
    - Think in terms of entire meals only, not recipes or courses
    - Your response should answer the question, "True or false, does the given prompt include a request for a low calorie diet?"
    - Return a default value of False if no mention is made of calories
    """
    meal_plan_prompt: str = dspy.InputField()
    low_calorie: bool = dspy.OutputField()

class ExtractLowCarb(dspy.Signature):
    """
    You are an information-extraction specialist. Always:
    - Read the entire input carefully
    - Extract only the fields and information requested
    - Return them exactly as a single boolean, with no additional commentary
    - Think in terms of entire meals only, not recipes or courses
    - Your response should answer the question, "True or false, does the given prompt include a request for a low carb diet?"
    - Return a default value of False if no mention is made of carbs
    """
    meal_plan_prompt: str = dspy.InputField()
    low_carb: bool = dspy.OutputField()

class ExtractLowFat(dspy.Signature):
    """
    You are an information-extraction specialist. Always:
    - Read the entire input carefully
    - Extract only the fields and information requested
    - Return them exactly as a single boolean, with no additional commentary
    - Think in terms of entire meals only, not recipes or courses
    - Your response should answer the question, "True or false, does the given prompt include a request for a low fat diet?"
    - Return a default value of False if no mention is made of fat
    """
    meal_plan_prompt: str = dspy.InputField()
    low_fat: bool = dspy.OutputField()

class ExtractLowCholesterol(dspy.Signature):
    """
    You are an information-extraction specialist. Always:
    - Read the entire input carefully
    - Extract only the fields and information requested
    - Return them exactly as a single boolean, with no additional commentary
    - Think in terms of entire meals only, not recipes or courses
    - Your response should answer the question, "True or false, does the given prompt include a request for a low cholesterol diet?"
    - Return a default value of False if no mention is made of cholesterol
    """
    meal_plan_prompt: str = dspy.InputField()
    low_cholesterol: bool = dspy.OutputField()

class ExtractLowSatFat(dspy.Signature):
    """
    You are an information-extraction specialist. Always:
    - Read the entire input carefully
    - Extract only the fields and information requested
    - Return them exactly as a single boolean, with no additional commentary
    - Think in terms of entire meals only, not recipes or courses
    - Your response should answer the question, "True or false, does the given prompt include a request for a diet low in saturated fat?"
    - Return a default value of False if no mention is made of saturated fat
    """
    meal_plan_prompt: str = dspy.InputField()
    low_sat_fat: bool = dspy.OutputField()

class ExtractLowSodium(dspy.Signature):
    """
    You are an information-extraction specialist. Always:
    - Read the entire input carefully
    - Extract only the fields and information requested
    - Return them exactly as a single boolean, with no additional commentary
    - Think in terms of entire meals only, not recipes or courses
    - Your response should answer the question, "True or false, does the given prompt include a request for a low sodium diet?"
    - Return a default value of False if no mention is made of sodium or salt
    """
    meal_plan_prompt: str = dspy.InputField()
    low_sodium: bool = dspy.OutputField()


# Collect DSPy signatures into a module
class ExtractInfoModule(dspy.Module):
    def __init__(self):
        super().__init__()

        # Configure dspy
        dspy.configure(lm=lm)

        # Load optimized module from file
        path = Path("optimized", "extract_optimized.json")
        self.load(str(path))

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
