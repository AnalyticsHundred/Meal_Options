import json
import random
import os
import streamlit as st

# Function to load meal options from a JSON file
def load_meal_options():
    meal_options_file = "data/meal_options.json"
    
    # Check if the file exists
    if not os.path.exists(meal_options_file):
        raise FileNotFoundError(f"Meal options JSON file not found at {meal_options_file}")
    
    # Try to load the JSON file
    try:
        with open(meal_options_file, "r") as file:
            meal_options = json.load(file)
        return meal_options
    except json.JSONDecodeError:
        raise ValueError("Error decoding JSON from the meal options file")

# Function to save the meal options back to the JSON file
def save_meal_options(meal_options):
    try:
        with open("data/meal_options.json", "w") as file:
            json.dump(meal_options, file, indent=4)
        st.success("Changes saved successfully!")
    except Exception as e:
        st.error(f"Error saving meal options: {e}")

# Function to display Today's Suggestion page
def todays_suggestion_page():
    meal_options = load_meal_options()  # Load the meal options from the JSON file
    
    # Check if the session state exists for today's suggestions
    if "breakfast_suggestion" not in st.session_state:
        st.session_state.breakfast_suggestion = random.choice(meal_options.get("breakfast", []))
    if "lunch_suggestion" not in st.session_state:
        st.session_state.lunch_suggestion = random.choice(meal_options.get("lunch", []))
    if "dinner_suggestion" not in st.session_state:
        st.session_state.dinner_suggestion = random.choice(meal_options.get("dinner", []))
    
    # Add a fun and visually appealing design
    st.title("🍽️ Today's Meal Suggestions 🍽️")
    st.markdown("## Enjoy your meals for today!")

    # Display today's suggestions with a fun design
    st.markdown(f"**Breakfast**: {st.session_state.breakfast_suggestion}")
    st.markdown(f"**Lunch**: {st.session_state.lunch_suggestion}")
    st.markdown(f"**Dinner**: {st.session_state.dinner_suggestion}")
    
    # Allow user to change all suggestions by clicking the button
    st.markdown("### Don't like what you see?")
    
    if st.button("Change Suggestions"):
        st.session_state.breakfast_suggestion = random.choice(meal_options.get("breakfast", []))
        st.session_state.lunch_suggestion = random.choice(meal_options.get("lunch", []))
        st.session_state.dinner_suggestion = random.choice(meal_options.get("dinner", []))

# Function to customize meal options
def customize_meal_page():
    try:
        meal_options = load_meal_options()  # Load the meal options
        st.write("### Customize Meal Options")
    except Exception as e:
        st.error(f"Error loading meal options: {e}")  # Display error in Streamlit
    
    st.markdown("Here you can add or remove meal options.")
    
    # Add new meal options using text inputs
    new_breakfast = st.text_input("Add a new breakfast option")
    if st.button("Add Breakfast Option"):
        if new_breakfast:
            meal_options["breakfast"].append(new_breakfast)
            save_meal_options(meal_options)
        else:
            st.error("Please enter a valid breakfast option.")
    
    new_lunch = st.text_input("Add a new lunch option")
    if st.button("Add Lunch Option"):
        if new_lunch:
            meal_options["lunch"].append(new_lunch)
            save_meal_options(meal_options)
        else:
            st.error("Please enter a valid lunch option.")
    
    new_dinner = st.text_input("Add a new dinner option")
    if st.button("Add Dinner Option"):
        if new_dinner:
            meal_options["dinner"].append(new_dinner)
            save_meal_options(meal_options)
        else:
            st.error("Please enter a valid dinner option.")
    
    # Remove meal options using selectboxes
    st.subheader("Remove Meal Options")
    remove_breakfast = st.selectbox("Select a breakfast option to remove", meal_options.get("breakfast", []))
    if st.button(f"Remove {remove_breakfast} from Breakfast"):
        meal_options["breakfast"].remove(remove_breakfast)
        save_meal_options(meal_options)
    
    remove_lunch = st.selectbox("Select a lunch option to remove", meal_options.get("lunch", []))
    if st.button(f"Remove {remove_lunch} from Lunch"):
        meal_options["lunch"].remove(remove_lunch)
        save_meal_options(meal_options)
    
    remove_dinner = st.selectbox("Select a dinner option to remove", meal_options.get("dinner", []))
    if st.button(f"Remove {remove_dinner} from Dinner"):
        meal_options["dinner"].remove(remove_dinner)
        save_meal_options(meal_options)

# Streamlit layout
def main():
    # Set page configuration for Streamlit
    st.set_page_config(page_title="Meal Options", page_icon="🍽️")
    
    menu = ["Today's Suggestion", "Customize Meal Lists"]
    choice = st.sidebar.selectbox("Select a page", menu)

    if choice == "Today's Suggestion":
        todays_suggestion_page()  # Call the function to display today's suggestions
    elif choice == "Customize Meal Lists":
        customize_meal_page()  # Call the customize page function

if __name__ == "__main__":
    main()
