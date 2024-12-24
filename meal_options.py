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

# Function to inject custom CSS for Starbucks theme and hover effects
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
        
        /* Add CSS for buttons showing meal options */
        .meal-option-btn {
            position: relative;
            display: inline-block;
            padding: 10px 20px;
            margin: 10px;
            font-size: 16px;
            background-color: #00704A; /* Green background */
            color: white;
            border: none;
            cursor: pointer;
            border-radius: 5px;
        }

        .meal-option-btn:hover .meal-option-menu {
            display: block; /* Show options on hover */
        }

        .meal-option-menu {
            display: none; /* Hide options by default */
            position: absolute;
            background-color: #ffffff;
            color: #4A3C31;
            border: 1px solid #4A3C31;
            padding: 10px;
            border-radius: 5px;
            top: 100%;
            left: 0;
            z-index: 10;
        }
        </style>
        """, unsafe_allow_html=True
    )

# Display the meal options in a more user-friendly format (Hoverable buttons)
def display_meal_options(meal_options):
    st.header("Customize Meal Options")

    # Buttons with hoverable menus for breakfast, lunch, and dinner
    meal_types = ['breakfast', 'lunch', 'dinner']
    meal_labels = ['Breakfast', 'Lunch', 'Dinner']

    for i in range(3):
        meal_type = meal_types[i]
        meal_label = meal_labels[i]
        options = ", ".join(meal_options[meal_type])
        
        # Create buttons with hover effect using custom CSS
        with st.markdown(f"""
        <button class="meal-option-btn">
            {meal_label} Options
            <div class="meal-option-menu">
                {options}
            </div>
        </button>
        """, unsafe_allow_html=True):
            pass  # Empty pass to allow CSS styling and interaction

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

    display_meal_options(meal_options)  # Display current meal options with hoverable menus

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
