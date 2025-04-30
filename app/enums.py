from enum import Enum

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
    GLUTEN_FREE = "Gluten Free"
    KETOGENIC = "Ketogenic"
    VEGETARIAN = "Vegetarian"
    LACTO_VEGETARIAN = "Lacto Vegetarian"
    OVO_VEGETARIAN = "Ovo Vegetarian"
    VEGAN = "Vegan"
    PESCATARIAN = "Pescatarian"
    PALEO = "Paleo"
    PRIMAL = "Primal"
    LOW_FODMAP = "Low FODMAP"
    WHOLE30 = "Whole30"

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
