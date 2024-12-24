import streamlit as st
import random
import json
from datetime import datetime

# Path to the JSON file that stores the meal options
MEAL_OPTIONS_FILE = "meal_options.json"

# Function to load meal options from the JSON file
def load_meal_options():
    try:
        with open(MEAL_OPTIONS_FILE, "r") as f:
            meal_data = json.load(f)
            return meal_data
    except FileNotFoundError:
        # If the file doesn't exist, return default meal options
        return {
            "breakfast": ["Pancakes", "Omelette", "Smoothie", "Cereal", "Avocado Toast"],
            "lunch": ["Grilled Chicken Salad", "Pasta", "Burger", "Sushi", "Vegetable Stir-fry"],
            "dinner": ["Steak", "Fish Tacos", "Vegetarian Chili", "Spaghetti", "Chicken Curry"]
        }

# Function to save meal options to the JSON file
def save_meal_options(meal_data):
    with open(MEAL_OPTIONS_FILE, "w") as f:
        json.dump(meal_data, f)

# Load the meal options from the JSON file
meal_options = load_meal_options()

# Function to generate meal suggestions
def generate_meal_suggestions(meal_type):
    return random.choice(meal_options[meal_type])

# Function to add a new option to the list
def add_option(meal_type, option):
    if option not in meal_options[meal_type]:
        meal_options[meal_type].append(option)
        save_meal_options(meal_options)  # Save updated meal options
    else:
        st.error(f"{option} is already in the {meal_type} options.")

# Function to remove an option from the list
def remove_option(meal_type, option):
    if option in meal_options[meal_type]:
        meal_options[meal_type].remove(option)
        save_meal_options(meal_options)  # Save updated meal options
    else:
        st.error(f"{option} is not in the {meal_type} options.")

# Homepage: Meal suggestions page
def home_page():
    st.title("Daily Meal Suggestions")
    
    # Display the current date
    today = datetime.now().strftime("%Y-%m-%d")
    st.subheader(f"Meal Suggestions for {today}")
    
    # Generate meal suggestions
    breakfast = generate_meal_suggestions('breakfast')
    lunch = generate_meal_suggestions('lunch')
    dinner = generate_meal_suggestions('dinner')
    
    # Display meals and buttons for generating new meals
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write(f"**Breakfast**: {breakfast}")
        if st.button('Generate Breakfast', key="breakfast"):
            breakfast = generate_meal_suggestions('breakfast')
            st.write(f"**Breakfast**: {breakfast}")
    
    with col2:
        st.write(f"**Lunch**: {lunch}")
        if st.button('Generate Lunch', key="lunch"):
            lunch = generate_meal_suggestions('lunch')
            st.write(f"**Lunch**: {lunch}")
    
    with col3:
        st.write(f"**Dinner**: {dinner}")
        if st.button('Generate Dinner', key="dinner"):
            dinner = generate_meal_suggestions('dinner')
            st.write(f"**Dinner**: {dinner}")

# Customization page: Allows the user to add or remove meal options
def customize_page():
    st.title("Customize Meal Lists")

    # Display current meal options
    st.subheader("Current Meal Options")

    st.write("### Breakfast Options")
    st.write(meal_options["breakfast"])
    
    st.write("### Lunch Options")
    st.write(meal_options["lunch"])

    st.write("### Dinner Options")
    st.write(meal_options["dinner"])

    # Add or Remove options for Breakfast, Lunch, Dinner
    meal_type = st.selectbox("Choose a meal to customize", ['breakfast', 'lunch', 'dinner'])
    action = st.radio("Choose action", ["Add", "Remove"])
    option = st.text_input(f"Enter meal option to {action.lower()}", "")

    if action == "Add" and option:
        if option == "":
            st.error("Please enter a meal option to add.")
        elif option in meal_options[meal_type]:
            st.error(f"{option} is already in the {meal_type} options.")
        else:
            if st.button(f"Add {option} to {meal_type.capitalize()}"):
                add_option(meal_type, option)
                st.success(f"Added {option} to {meal_type.capitalize()} options.")
    
    elif action == "Remove" and option:
        if option == "":
            st.error("Please enter a meal option to remove.")
        elif option not in meal_options[meal_type]:
            st.error(f"{option} is not in the {meal_type} options.")
        else:
            if st.button(f"Remove {option} from {meal_type.capitalize()}"):
                remove_option(meal_type, option)
                st.success(f"Removed {option} from {meal_type.capitalize()} options.")
    
    # Display the updated lists
    st.write("### Updated Meal Options")

    st.write("### Breakfast Options")
    st.write(meal_options["breakfast"])
    
    st.write("### Lunch Options")
    st.write(meal_options["lunch"])

    st.write("### Dinner Options")
    st.write(meal_options["dinner"])

# Streamlit app to switch between home page and customize page
def main():
    # Sidebar for navigation
    page = st.sidebar.radio("Select a page", ["Home", "Customize Meal Lists"])
    
    if page == "Home":
        home_page()
    elif page == "Customize Meal Lists":
        customize_page()

# Run the app
if __name__ == "__main__":
    main()
