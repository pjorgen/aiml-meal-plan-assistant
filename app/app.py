# Run the following command once in powershell to set the value for the session
# This works around a bug in litellm where it uses the wrong encoding.
# $env:PYTHONUTF8="1"

import pathlib
from extract_info import ExtractInfoModule
from spoonacular_api import search_recipes

extract_module = ExtractInfoModule()
# path = pathlib.Path("optimized", "extract_optimized.json")
# extract_module.load(str(path))

text = "Plan a dinner for 4 people. We like Chinese and Italian and do not like American. I am vegan and my brother is pescatarian. We love peaches and dislike blueberries."

model = extract_module.forward(text=text)

dump = []

for m in model:
    dump.append(m.model_dump())

# for d in dump:
#     print("**************************************")
#     print(d)

for m in model:
    response = search_recipes(m)
    print("**************************************")
    print(response.model_dump())