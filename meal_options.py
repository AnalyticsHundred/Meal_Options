import streamlit as st
import json
import random
from datetime import datetime

# Meal options stored as a JSON file for persistence
meal_options_file = "data/meal_options.json"

# Function to load the meal options from the JSON file
def load_meal_options():
    try:
        with open(meal_options_file, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            "breakfast": ["Pancakes", "Omelette", "Smoothie"],
            "lunch": ["Salad", "Sandwich", "Pizza"],
            "dinner": ["Pasta", "Steak", "Soup"]
        }

# Function to get today's meal suggestions
def get_today_meal_suggestions(meal_options):
    today = datetime.today().strftime('%Y-%m-%d')
    breakfast = random.choice(meal_options["breakfast"])
    lunch = random.choice(meal_options["lunch"])
    dinner = random.choice(meal_options["dinner"])
    return today, breakfast, lunch, dinner

# Function to apply custom CSS for the user interface
def apply_custom_css():
    st.markdown(
        """
        <style>
        body {
            background-color: #F4F1E1; /* Light Cream Background */
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; /* Clean Font */
        }
        .stApp {
            color: #3E4A51; /* Dark Gray text color for better readability */
        }
        .stTitle {
            color: #00704A; /* Starbucks Green for titles */
            font-size: 32px;
            font-weight: bold;
        }
        .stSubheader {
            color: #00704A; /* Starbucks Green for subheaders */
        }
        .stButton>button {
            background-color: #00704A; /* Green background for buttons */
            color: white; /* White text color for buttons */
            border-radius: 8px;
            padding: 12px 24px;
            font-size: 18px;
        }
        .stButton>button:hover {
            background-color: #4A3C31; /* Dark Brown hover for buttons */
        }
        .stTextInput>div>input {
            background-color: #FFFFFF; /* White background for input fields */
            color: #3E4A51; /* Dark Gray text for inputs */
            font-size: 16px;
        }
        .stSelectbox>div>div>input {
            background-color: #FFFFFF; /* White background for dropdowns */
            color: #3E4A51; /* Dark Gray text for dropdowns */
        }
        .stForm>div>div>input {
            background-color: #FFFFFF;
            color: #3E4A51;
        }
        /* Styling for the Change Suggestion button */
        .change-suggestion-btn {
            background-color: #4A3C31; /* Dark Brown background */
            color: white; /* White text */
            padding: 8px 16px;
            font-size: 14px;
            border-radius: 5px;
            border: none;
            cursor: pointer;
            transition: all 0.3s ease;
            margin-top: 10px;
        }
        .change-suggestion-btn:hover {
            background-color: #00704A; /* Starbucks Green on hover */
            transform: scale(1.1); /* Slight zoom on hover */
        }
        /* Styling for meal options */
        .meal-option-container {
            padding: 15px;
            border-radius: 8px;
            margin: 10px;
            background-color: #FFFFFF;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .meal-option-header {
            font-size: 24px;
            font-weight: bold;
            color: #00704A;
        }
        .meal-option {
            padding: 15px;
            font-size: 18px;
            background-color: #f1f1f1;
            border-radius: 8px;
            margin: 5px 0;
        }
        .meal-option.breakfast {
            background-color: #FFEB3B;
        }
        .meal-option.lunch {
            background-color: #8BC34A;
        }
        .meal-option.dinner {
            background-color: #FF5722;
        }
        </style>
        """, unsafe_allow_html=True
    )

# Display meal options for today's suggestion page
def todays_suggestion():
    meal_options = load_meal_options()
    today, breakfast, lunch, dinner = get_today_meal_suggestions(meal_options)

    st.title("Today's Meal Suggestions")
    st.write(f"Today's Date: {today}")

    # Initialize session state for suggestions if not already initialized
    if "breakfast" not in st.session_state:
        st.session_state.breakfast = breakfast
    if "lunch" not in st.session_state:
        st.session_state.lunch = lunch
    if "dinner" not in st.session_state:
        st.session_state.dinner = dinner

    col1, col2, col3 = st.columns(3)

    # Breakfast Section
    with col1:
        st.markdown(f"<div class='meal-option-container'>", unsafe_allow_html=True)
        st.markdown("<div class='meal-option-header'>Breakfast</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='meal-option breakfast'>{st.session_state.breakfast}</div>", unsafe_allow_html=True)
        if st.button("Change Breakfast Suggestion", key="breakfast_btn"):
            st.session_state.breakfast = random.choice(meal_options["breakfast"])
        st.markdown("</div>", unsafe_allow_html=True)

    # Lunch Section
    with col2:
        st.markdown(f"<div class='meal-option-container'>", unsafe_allow_html=True)
        st.markdown("<div class='meal-option-header'>Lunch</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='meal-option lunch'>{st.session_state.lunch}</div>", unsafe_allow_html=True)
        if st.button("Change Lunch Suggestion", key="lunch_btn"):
            st.session_state.lunch = random.choice(meal_options["lunch"])
        st.markdown("</div>", unsafe_allow_html=True)

    # Dinner Section
    with col3:
        st.markdown(f"<div class='meal-option-container'>", unsafe_allow_html=True)
        st.markdown("<div class='meal-option-header'>Dinner</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='meal-option dinner'>{st.session_state.dinner}</div>", unsafe_allow_html=True)
        if st.button("Change Dinner Suggestion", key="dinner_btn"):
            st.session_state.dinner = random.choice(meal_options["dinner"])
        st.markdown("</div>", unsafe_allow_html=True)

# Streamlit layout
def main():
    apply_custom_css()  # Apply custom styling

    menu = ["Today's Suggestion", "Customize Meal Lists"]
    choice = st.sidebar.selectbox("Select a page", menu)

    if choice == "Today's Suggestion":
        todays_suggestion()  # Show today's meal suggestions
    elif choice == "Customize Meal Lists":
        customize_meal_page()  # Customize meal options

if __name__ == "__main__":
    main()
