import json
import random
import os
import streamlit as st

# Path to meal options JSON file
meal_options_file = "data/meal_options.json"

# Function to load meal options from a JSON file
def load_meal_options():
    if not os.path.exists(meal_options_file):
        raise FileNotFoundError(f"Meal options JSON file not found at {meal_options_file}")
    
    with open(meal_options_file, "r") as file:
        return json.load(file)

# Function to save meal options back to the JSON file
def save_meal_options(meal_options):
    with open(meal_options_file, "w") as file:
        json.dump(meal_options, file, indent=4)
    st.success("Changes saved successfully!")

# Function to display today's meal suggestions
def todays_suggestion_page():
    meal_options = load_meal_options()  # Load meal options from the JSON file
    
    # Initialize suggestions if not set
    if "breakfast_suggestion" not in st.session_state:
        st.session_state.breakfast_suggestion = random.choice(meal_options.get("breakfast", []))
    if "lunch_suggestion" not in st.session_state:
        st.session_state.lunch_suggestion = random.choice(meal_options.get("lunch", []))
    if "dinner_suggestion" not in st.session_state:
        st.session_state.dinner_suggestion = random.choice(meal_options.get("dinner", []))

    # Display today's suggestions
    st.title("🍽️ Today's Meal Suggestions 🍽️")
    st.markdown("## Enjoy your meals for today!")

    st.markdown(f"**Breakfast**: {st.session_state.breakfast_suggestion}")
    st.markdown(f"**Lunch**: {st.session_state.lunch_suggestion}")
    st.markdown(f"**Dinner**: {st.session_state.dinner_suggestion}")
    
    # Change all suggestions at once
    if st.button("Change All Suggestions"):
        st.session_state.breakfast_suggestion = random.choice(meal_options.get("breakfast", []))
        st.session_state.lunch_suggestion = random.choice(meal_options.get("lunch", []))
        st.session_state.dinner_suggestion = random.choice(meal_options.get("dinner", []))

# Function to customize meal options (add or remove options)
def customize_meal_page():
    try:
        meal_options = load_meal_options()  # Load the meal options from the JSON file
        st.write("### Customize Meal Options")
    except Exception as e:
        st.error(f"Error loading meal options: {e}")  # Display error in Streamlit

    st.markdown("Here you can add or remove meal options.")

    # Add new meal options
    new_breakfast = st.text_input("Add a new breakfast option")
    if st.button("Add Breakfast Option"):
        if new_breakfast:
            meal_options["breakfast"].append(new_breakfast)
            save_meal_options(meal_options)  # Save the updated meal options to JSON
        else:
            st.error("Please enter a valid breakfast option.")
    
    new_lunch = st.text_input("Add a new lunch option")
    if st.button("Add Lunch Option"):
        if new_lunch:
            meal_options["lunch"].append(new_lunch)
            save_meal_options(meal_options)  # Save the updated meal options to JSON
        else:
            st.error("Please enter a valid lunch option.")
    
    new_dinner = st.text_input("Add a new dinner option")
    if st.button("Add Dinner Option"):
        if new_dinner:
            meal_options["dinner"].append(new_dinner)
            save_meal_options(meal_options)  # Save the updated meal options to JSON
        else:
            st.error("Please enter a valid dinner option.")

    # Remove meal options (selectbox to choose from available options)
    st.subheader("Remove Meal Options")
    
    remove_breakfast = st.selectbox("Select a breakfast option to remove", meal_options.get("breakfast", []))
    if st.button(f"Remove {remove_breakfast} from Breakfast"):
        if remove_breakfast:
            meal_options["breakfast"].remove(remove_breakfast)
            save_meal_options(meal_options)  # Save the updated meal options to JSON
    
    remove_lunch = st.selectbox("Select a lunch option to remove", meal_options.get("lunch", []))
    if st.button(f"Remove {remove_lunch} from Lunch"):
        if remove_lunch:
            meal_options["lunch"].remove(remove_lunch)
            save_meal_options(meal_options)  # Save the updated meal options to JSON
    
    remove_dinner = st.selectbox("Select a dinner option to remove", meal_options.get("dinner", []))
    if st.button(f"Remove {remove_dinner} from Dinner"):
        if remove_dinner:
            meal_options["dinner"].remove(remove_dinner)
            save_meal_options(meal_options)  # Save the updated meal options to JSON

# Streamlit layout
def main():
    st.set_page_config(page_title="Meal Options", page_icon="🍽️")
    
    menu = ["Today's Suggestion", "Customize Meal Lists"]
    choice = st.sidebar.selectbox("Select a page", menu)

    if choice == "Today's Suggestion":
        todays_suggestion_page()  # Call the function to display today's suggestions
    elif choice == "Customize Meal Lists":
        customize_meal_page()  # Call the customize page function

if __name__ == "__main__":
    main()
