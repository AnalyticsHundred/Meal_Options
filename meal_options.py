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
        </st
