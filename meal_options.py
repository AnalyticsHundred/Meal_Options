import streamlit as st
import json
import random
from datetime import datetime

# Meal options stored as a JSON file for persistence
meal_options_file = "meal_options.json"

# Function to load the meal options from the JSON file
def load_meal_options():
    try:
        with open(meal_options_file, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Return a default structure if the file does not exist or is empty
        return {
            "breakfast": ["Pancakes", "Omelette", "Smoothie"],
            "lunch": ["Salad", "Sandwich", "Pizza"],
            "dinner": ["Pasta", "Steak", "Soup"]
        }

# Function to save the updated meal options back to the JSON file
def save_meal_options(meal_options):
    with open(meal_options_file, "w") as f:
        json.dump(meal_options, f, indent=4)

# Function to get today's meal suggestions
def get_today_meal_suggestions(meal_options):
    today = datetime.today().strftime('%Y-%m-%d')
    breakfast = random.choice(meal_options["breakfast"])
    lunch = random.choice(meal_options["lunch"])
    dinner = random.choice(meal_options["dinner"])
    return today, breakfast, lunch, dinner

# Function to inject custom CSS for Starbucks theme
def apply_custom_css():
    st.markdown(
        """
        <style>
        body {
            background-color: #F2F2F2; /* Light Beige background */
        }
        .stApp {
            color: #4A3C31; /* Dark Brown text color */
        }
        .stTitle {
            color: #00704A; /* Starbucks Green for titles */
        }
        .stSubheader {
            color: #00704A; /* Starbucks Green for subheaders */
        }
        .stButton>button {
            background-color: #00704A; /* Green background for buttons */
            color: white; /* White text color for buttons */
        }
        .stButton>button:hover {
            background-color: #4A3C31; /* Dark Brown hover for buttons */
        }
        .stTextInput>div>input {
            background-color: #FFFFFF; /* White background for input fields */
            color: #4A3C31; /* Dark Brown text for inputs */
        }
        .stSelectbox>div>div>input {
            background-color: #FFFFFF; /* White background for dropdowns */
            color: #4A3C31; /* Dark Brown text for dropdowns */
        }
        .stForm>div>div>input {
            background-color: #FFFFFF;
            color: #4A3C31;
        }
     
