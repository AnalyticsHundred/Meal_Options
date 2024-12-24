import json
import os
import streamlit as st

# Function to load meal options from a JSON file
def load_meal_options():
    meal_options_file = "data/meal_options.json"
    
    if not os.path.exists(meal_options_file):
        raise FileNotFoundError(f"Meal options JSON file not found at {meal_options_file}")
    
    try:
        with open(meal_options_file, "r") as file:
            meal_options = json.load(file)
        return meal_options
    except json.JSONDecodeError:
        raise ValueError("Error decoding JSON from the meal options file")

# Customize meal page
def customize_meal_page():
    try:
        meal_options = load_meal_options()  # Load the meal options
        print(meal_options)  # Print meal options for debugging
    except Exception as e:
        print(f"Error: {e}")
        st.error(f"Error loading meal options: {e}")  # Display error in Streamlit

    # Customization logic for meal options
    st.subheader("Customize Your Meal Options")
    st.write("Here you can add or remove meal options.")

    # Display the meal options for customization (Example: For breakfast)
    breakfast = meal_options.get("breakfast", [])
    st.write("Current breakfast options:", breakfast)

    # Add customization buttons, inputs, etc.
    new_breakfast = st.text_input("Add a new breakfast option")
    if st.button("Add Breakfast Option"):
        if new_breakfast:
            breakfast.append(new_breakfast)
            st.write("Updated breakfast options:", breakfast)
        else:
            st.error("Please enter a valid breakfast option.")
    
    # Continue similarly for lunch and dinner options
    lunch = meal_options.get("lunch", [])
    dinner = meal_options.get("dinner", [])

    # For saving the changes
    if st.button("Save Changes"):
        try:
            with open("data/meal_options.json", "w") as file:
                json.dump(meal_options, file)
            st.success("Changes saved successfully!")
        except Exception as e:
            st.error(f"Error saving meal options: {e}")

# Streamlit layout
def main():
    menu = ["Today's Suggestion", "Customize Meal Lists"]
    choice = st.sidebar.selectbox("Select a page", menu)

    if choice == "Today's Suggestion":
        # Call your function for today's suggestion
        pass  # Replace with your function
    elif choice == "Customize Meal Lists":
        customize_meal_page()  # Call the customize page function

if __name__ == "__main__":
    main()
