# Run the following command once in powershell to set the value for the session
# This works around a bug in litellm where it uses the wrong encoding.
# $env:PYTHONUTF8="1"

import json
import streamlit as st
from requests import HTTPError
from extract_info import ExtractInfoModule
from format_output import FormatOutputModule
from spoonacular_api import search_recipes
from classes import info_to_requests

# Initialize extraction module to global cache
@st.cache_resource
def get_extractor():
    return ExtractInfoModule()

# Initialize formatter module to global cache
@st.cache_resource
def get_formatter():
    return FormatOutputModule()

# Use the local method to get from streamlit cache if doing a rerun
extract_module = get_extractor()
format_module = get_formatter()

# Define a helper function to auto submit demo prompts
def auto_send(text: str):
    st.session_state.auto_prompt = text
    st.session_state.send_prompt = True

# Setup demo buttons
demo_1, demo_2 = st.columns(2)
if demo_1.button("Dinner for two", use_container_width=True):
    auto_send("Plan a dinner for two that does not include asparagus. My partner is allergic to peanuts and I am on a low sodium diet.")

if demo_2.button("Meals for family of four", use_container_width=True):
    auto_send("Plan two lunches and two dinners for a family of four. Pears and cheese sticks are favorites, and we do not like peanut butter. Try to keep the meals high in protein and low in fat.")

# Setup streamlit title
st.title("💬 Meal Planner Chatbot")

# If button is pressed, simulate prompt otherwise allow user input
if "send_prompt" in st.session_state and st.session_state.send_prompt:
    user_input = st.session_state.auto_prompt
    st.session_state.send_prompt = False
else:
    st.chat_message("assistant").markdown("Hello! Click a demo button up top or enter a meal planning request below to get started.")
    user_input = st.chat_input()


# React to user input
if user_input:

    # Display user message in chat container
    st.chat_message("user").markdown(user_input)

    # Start spinner to indicate processing
    with st.spinner("Extracting meal criteria..."):
        meal_info = extract_module.extract_meal_criteria(text=user_input)
        requests = info_to_requests(meal_info)
        json_string = meal_info.model_dump_json()
        markdown_meal_info = format_module.format_as_markdown(text=json_string)

    st.chat_message("assistant").markdown(json_string)
    st.chat_message("assistant").markdown(markdown_meal_info)
    # st.chat_message("assistant").markdown(requests)

    with st.spinner("Searching recipes..."):
        try:
            recipes = search_recipes(model=requests)
        except HTTPError:
            st.write("An error occurred in the search: ", HTTPError )

    for r in recipes:
        json_string = json.dumps(r.model_dump())
        #st.chat_message("assistant").markdown(json_string)
        recipe_markdown = format_module.format_as_markdown(text=json_string)
        st.chat_message("assistant").markdown(recipe_markdown)

# Run program with streamlit run app.py
