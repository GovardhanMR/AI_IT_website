import streamlit as st

def ai_this_week():
    st.title("AI This Week")
    st.markdown("## Main News")
    st.write("1. OpenAI releases a new version of ChatGPT with enhanced language capabilities.")
    st.write("2. Google's DeepMind achieves a major breakthrough in protein folding predictions.")
    st.markdown("## Headlines")
    st.write("- Facebook announces AI-powered content moderation tools.")
    st.write("- Tesla incorporates advanced AI algorithms in its autonomous driving system.")
    st.write("- Research team develops AI model to detect early signs of diseases from medical images.")

def it_this_week():
    st.title("IT This Week")
    st.markdown("## Main News")
    st.write("1. Microsoft launches Windows 11 with redesigned interface and enhanced performance.")
    st.write("2. Amazon Web Services (AWS) introduces new cloud services for AI and machine learning.")
    st.markdown("## Headlines")
    st.write("- Apple unveils the latest iPhone model with advanced camera technology.")
    st.write("- IBM develops quantum computer prototype with improved qubit stability.")
    st.write("- Cisco releases new network security solutions to combat cyber threats.")

def user_questions():
    st.title("User Questions")
    # Add your code to handle user questions here

# Create navigation menu
pages = {
    "AI This Week": ai_this_week,
    "IT This Week": it_this_week,
    "User Questions": user_questions
}

# Streamlit app
st.sidebar.title("Weekly Updates")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Display selected page
pages[selection]()
