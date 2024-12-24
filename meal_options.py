import streamlit as st
import json
import random
from datetime import datetime
import pandas as pd

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
        </style>
        """, unsafe_allow_html=True
    )

# Display the meal options in a more user-friendly format (Tabular Format)
def display_meal_options(meal_options):
    st.header("Customize Meal Options")

    # Convert meal options dictionary to a pandas DataFrame for tabular display
    meal_df = pd.DataFrame({
        "Meal Type": ["Breakfast", "Lunch", "Dinner"],
        "Options": [", ".join(meal_options["breakfast"]),
                    ", ".join(meal_options["lunch"]),
                    ", ".join(meal_options["dinner"])]
    })

    # Display meal options in a tabular format
    st.table(meal_df)

# Add meal options to the list
def add_meal_option(meal_type, new_option, meal_options):
    if new_option and new_option not in meal_options[meal_type]:
        meal_options[meal_type].append(new_option)
        st.success(f"{new_option} added to {meal_type.capitalize()} options!")
    else:
        st.warning(f"{new_option} is already in the {meal_type.capitalize()} options or invalid!")

# Remove meal options from the list
def remove_meal_option(meal_type, option_to_remove, meal_options):
    if option_to_remove in meal_options[meal_type]:
        meal_options[meal_type].remove(option_to_remove)
        st.success(f"{option_to_remove} removed from {meal_type.capitalize()} options!")
    else:
        st.warning(f"{option_to_remove} not found in {meal_type.capitalize()} options!")

# Streamlit layout for Customize Meal Lists
def customize_meal_page():
    st.title("Customize Your Meal Options")

    meal_options = load_meal_options()  # Load current meal options

    # Button to toggle JSON display
    show_json = st.button("Show Available Options in JSON format")
    if show_json:
        st.json(meal_options)  # Display current meal options in JSON format

    display_meal_options(meal_options)  # Display current meal options in a tabular format

    # Form to add or remove meal options
    with st.form(key="meal_form"):
        meal_type = st.selectbox("Select meal type", ["breakfast", "lunch", "dinner"])
        action = st.radio("What would you like to do?", ("Add a new option", "Remove an existing option"))
        meal_option = st.text_input(f"Enter the meal option to {'add' if action == 'Add a new option' else 'remove'}:")

        if action == "Remove an existing option":
            # Create a dropdown to select meal option to remove
            meal_option = st.selectbox(f"Select a meal option to remove from {meal_type.capitalize()}:",
                                      meal_options[meal_type])

        submit_button = st.form_submit_button(label="Submit")

        if submit_button:
            if action == "Add a new option":
                add_meal_option(meal_type, meal_option, meal_options)
            elif action == "Remove an existing option":
                remove_meal_option(meal_type, meal_option, meal_options)

            # After modification, show only updated meal options
            st.subheader(f"Updated {meal_type.capitalize()} Options")
            st.write(meal_options[meal_type])

            # Save changes
            save_meal_options(meal_options)

    st.info("Remember to update your meal options regularly to keep your meals diverse and fresh!")

# Homepage: Show breakfast, lunch and dinner options for the current date
def homepage():
    meal_options = load_meal_options()
    today, breakfast, lunch, dinner = get_today_meal_suggestions(meal_options)

    st.title("Today's Meal Suggestions")
    st.write(f"Today's Date: {today}")
    st.write(f"**Breakfast**: {breakfast}")
    st.write(f"**Lunch**: {lunch}")
    st.write(f"**Dinner**: {dinner}")

# Streamlit Page Selection
def main():
    apply_custom_css()  # Apply custom styling

    menu = ["Homepage", "Customize Meal Lists"]
    choice = st.sidebar.selectbox("Select a page", menu)

    if choice == "Homepage":
        homepage()  # Show today's meal suggestions
    elif choice == "Customize Meal Lists":
        customize_meal_page()  # Customize meal options

if __name__ == "__main__":
    main()
