from enum import Enum
from typing import Literal

class Cuisine(Enum):
    AFRICAN = "African"
    ASIAN = "Asian"
    AMERICAN = "American"
    BRITISH = "British"
    CAJUN = "Cajun"
    CARIBBEAN = "Caribbean"
    CHINESE = "Chinese"
    EASTERN_EUROPEAN = "Eastern European"
    EUROPEAN = "European"
    FRENCH = "French"
    GERMAN = "German"
    GREEK = "Greek"
    INDIAN = "Indian"
    IRISH = "Irish"
    ITALIAN = "Italian"
    JAPANESE = "Japanese"
    JEWISH = "Jewish"
    KOREAN = "Korean"
    LATIN_AMERICAN = "Latin American"
    MEDITERRANEAN = "Mediterranean"
    MEXICAN = "Mexican"
    MIDDLE_EASTERN = "Middle Eastern"
    NORDIC = "Nordic"
    SOUTHERN = "Southern"
    SPANISH = "Spanish"
    THAI = "Thai"
    VIETNAMESE = "Vietnamese"

class Diet(Enum):
    GLUTEN_FREE = "gluten free"
    KETOGENIC = "ketogenic"
    VEGETARIAN = "vegetarian"
    LACTO_VEGETARIAN = "lacto vegetarian"
    OVO_VEGETARIAN = "ovo vegetarian"
    VEGAN = "vegan"
    PESCATARIAN = "pescatarian"
    PALEO = "paleo"
    PRIMAL = "primal"
    LOW_FODMAP = "low fodmap"
    WHOLE30 = "whole30"

class Intolerance(Enum):
    DAIRY = "Dairy"
    EGG = "Egg"
    GLUTEN = "Gluten"
    GRAIN = "Grain"
    PEANUT = "Peanut"
    SEAFOOD = "Seafood"
    SESAME = "Sesame"
    SHELLFISH = "Shellfish"
    SOY = "Soy"
    SULFITE = "Sulfite"
    TREE_NUT = "Tree Nut"
    WHEAT = "Wheat"

class MealType(Enum):
    MAIN = "main course"
    SIDE = "side dish"
    DESSERT = "dessert"
    APPETIZER = "appetizer"
    SALAD = "salad"
    BREAD = "bread"
    BREAKFAST = "breakfast"
    SOUP = "soup"
    BEVERAGE = "beverage"
    SAUCE = "sauce"
    MARINADE = "marinade"
    FINGERFOOD = "fingerfood"
    SNACK = "snack"
    DRINK = "drink"

class Nutrition(Enum):
    HIGH_FIBER = 5
    HIGH_PROTEIN = 25
    LOW_CALORIE = 500
    LOW_CARB = 30
    LOW_FAT = 15
    LOW_CHOLESTEROL = 100
    LOW_SATURATED_FAT = 3
    LOW_SODIUM = 500

CuisineLiteral = Literal[
    "African", "Asian", "American", "British", "Cajun", "Caribbean", "Chinese",
    "Eastern European", "European", "French", "German", "Greek", "Indian", "Irish",
    "Italian", "Japanese", "Jewish", "Korean", "Latin American", "Mediterranean",
    "Mexican", "Middle Eastern", "Nordic", "Southern", "Spanish", "Thai", "Vietnamese"
]

DietLiteral = Literal[
    "gluten free", "ketogenic", "vegetarian", "lacto vegetarian", "ovo vegetarian",
    "vegan", "pescatarian", "paleo", "primal", "low fodmap", "whole30"
]

IntoleranceLiteral = Literal[
    "Dairy", "Egg", "Gluten", "Grain", "Peanut", "Seafood", "Sesame", "Shellfish",
    "Soy", "Sulfite", "Tree Nut", "Wheat"
]

MealTypeLiteral = Literal[
    "main course", "side dish", "dessert", "appetizer", "salad", "bread", "breakfast",
    "soup", "beverage", "sauce", "marinade", "fingerfood", "snack", "drink"
]