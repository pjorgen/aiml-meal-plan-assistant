# Meal Planning Assistant
#### An AI project for the MSSE program, completed by Phil Jorgensen

## Problem Statement
Meal planning can be difficult, especially when you try to find recipes for ingredients you have on hand or are trying
to eat more nutritional and balanced foods, but don't have a lot of time or knowledge to spend on creating the perfect 
meal or set of meals.

This tool aims to solve that problem by incorporating user preferences and dietary restrictions and targets to craft the
desired number of meals for the required number of people, all while ensuring balanced nutrition and using ingredients
already on hand as much as possible.

The result given back is a set of recipes that include ingredients, preparation instructions, nutritional information, 
and a shopping list of ingredients.

## Process Planning
The request from the user comes in and undergoes a series of transformations and enhancements to return the meal plan
requested. The process is outlined generally here.

### Request Processing Flowchart
```mermaid
flowchart
    A(["Request"])
    A --> B["Parse natural language request"]
    B --> ide1
    subgraph ide1 ["Recipes"]
        direction TB
        C["Choose or develop recipes"]
        C <--> D[("Recipe Store")]
        C --> K{{"Recipe API"}}
    end
    L["Validate recipes"]
    ide1 --> L --> ide2
    subgraph ide2 ["Shopping List"]
        direction TB
        E["Create shopping list"]
        E --> F["Shopping list tabulator (Tool)"]
        F --> G["Organize shopping list"]
    end
    ide2 --> I("Response")
```

### Request Format
The request is a natural language request, such as
```
Plan five meals for my partner and I, and one meal for a party of 8. 
My partner is a vegetarian, and I am trying to reduce my cholesterol. 
We have basmati rice and diced tomatoes on hand.
It's been a while since we tried cooking chinese food and would like to try it again.
```

### Request Parsing
The request needs to be parsed to find some or all of the following information:
- Number of meals
- Number of people for each meal
- Dietary restrictions for each meal
- Nutritional targets or restrictions for each meal
- Available ingredients
- Cuisine likes and dislikes
- Ingredient likes and dislikes

### Recipe development
We will use the [Spoonacular API](https://spoonacular.com/food-api/docs) for recipe development. While Spoonacular has existing functionality for meal planning,
for the purposes of this project we will limit our API usage to the Recipe endpoints to make the project more interesting
and to limit the depth of integration to Spoonacular.

Note that we registered to use the Spoonacular API with an educational license, which also required setting up a Rapid
API account.

### Validation
We need a layer to ensure the recipes returned adhere to the restrictions and criteria given as inputs. While Spoonacular
does some validation themselves, we want to make sure that between the remote recipes and the ones retrieved from the 
cache that we are consistently in compliance. We will check:
- Ingredients for adherence to diet, allergen restrictions, and likes and dislikes
- Nutrition for adherence to diet and nutrition targets and restrictions
- Recipe for cuisine likes and dislikes
- Recipe for proper scaling to number of people
- Correct number of recipes

### Shopping List
Generation of the shopping list for the meal plan will be done via external tool to tabulate the food items and quantity
needed. A further pass through an LLM will be made to organize the shopping list into categories for efficient shopping.

### User Interface
A simple user interface will be created that provides a Chat GPT-like experience for entering a natural lanugage prompt
and receiving a streamed response from the system.

### Implementation
The project will be implemented in Python and make use of the following tools:
- Ollama model for local processing of prompts
- DSPy for orchestration and evaluation
- Streamlit for IO and UI
- Weaviate as a vector database

### Deployment
The application will be deployed to Docker containers, and part of the project will be to develop the deployment scripts
and packages to fully implement the application.

## Development and Implementation Log
To follow.


## Future Development
There is limited time and effort available to complete this project at this time, which leaves several features for future
consideration. These are parked here for reference.
- Static site for viewing, referencing, and rating recipes in the cache
- Inventory management system for automatic integration into recipes, including auto-updating inventory after meal planning
- Multi-user support for saving preferences, dietary restrictions, and nutritional targets
