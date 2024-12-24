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
    breakfast = rand
