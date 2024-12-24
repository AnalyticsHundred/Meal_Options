import streamlit as st
import json

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

# Display the current meal options in a more user-friendly format
def display_meal_options(meal_options):
    st.header("Customize Meal Options")

    st.subheader("Breakfast Options")
    st.write(meal_options["breakfast"])

    st.subheader("Lunch Options")
    st.write(meal_options["lunch"])

    st.subheader("Dinner Options")
    st.write(meal_options["dinner"])

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

    display_meal_options(meal_options)  # Display current meal options

    # Form to add or remove meal options
    with st.form(key="meal_form"):
        meal_type = st.selectbox("Select meal type", ["breakfast", "lunch", "dinner"])
        action = st.radio("What would you like to do?", ("Add a new option", "Remove an existing option"))
        meal_option = st.text_input(f"Enter the meal option to {'add' if action == 'Add a new option' else 'remove'}:")

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

# Streamlit Page Selection
def main():
    menu = ["Homepage", "Customize Meal Lists"]
    choice = st.sidebar.selectbox("Select a page", menu)

    if choice == "Homepage":
        st.title("Welcome to Your Meal Planner!")
        st.write("On the **Customize Meal Lists** page, you can modify your meal options.")
        # Add your homepage content here
    elif choice == "Customize Meal Lists":
        customize_meal_page()

if __name__ == "__main__":
    main()
