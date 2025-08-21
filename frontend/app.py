import streamlit as st
import requests
import json

# Define the FastAPI endpoint
FASTAPI_URL = "http://127.0.0.1:8000/run-strategist"

st.set_page_config(
    page_title="The AI Strategist",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for a clean look
st.markdown("""
    <style>
        .main {
            background-color: #f0f2f6;
            padding: 2rem;
        }
        .stButton>button {
            width: 100%;
            border-radius: 0.5rem;
            background-color: #4CAF50;
            color: white;
            font-size: 1.2rem;
            height: 3rem;
            border: none;
            transition: background-color 0.3s;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .stTextInput>div>div>input {
            border-radius: 0.5rem;
        }
        .stTextArea>div>div>textarea {
            border-radius: 0.5rem;
        }
    </style>
""", unsafe_allow_html=True)


st.title("💡 The AI Strategist")
st.markdown("A multi-agent system for rapid idea validation and strategic planning.")
st.markdown("---")

# User Inputs
st.header("Project Details")
hackathon_theme = st.text_input("Hackathon Theme", "AI in Education")
raw_idea = st.text_area("Your Raw Idea", "An AI-powered app to help students learn new languages.")
team_strength = st.selectbox(
    "Team's Core Strength",
    ("Frontend", "Backend", "AI/ML", "Full-Stack")
)

if st.button("Generate Strategy"):
    # Create the payload from user inputs
    payload = {
        "hackathon_theme": hackathon_theme,
        "raw_idea": raw_idea,
        "team_strength": team_strength
    }

    st.markdown("---")
    st.info("🚀 Your AI strategist team is at work. This may take a moment...")

    # Display a spinner while waiting for the response
    with st.spinner("Generating strategic plan..."):
        try:
            # Send the request to the FastAPI endpoint
            response = requests.post(FASTAPI_URL, json=payload, timeout=300) # 5-minute timeout
            
            # Check for a successful response
            if response.status_code == 200:
                data = response.json()
                if data.get("success"):
                    st.success("✅ Strategic plan generated successfully!")
                    st.subheader("Final Pitch Outline")
                    st.markdown(data["result"])
                else:
                    st.error(f"An error occurred: {data.get('error')}")
            else:
                st.error(f"Failed to connect to the backend. Status code: {response.status_code}")
                st.error("Please ensure your FastAPI server is running on http://127.0.0.1:8000.")

        except requests.exceptions.ConnectionError:
            st.error("Connection failed. Please ensure the FastAPI server is running.")
        except requests.exceptions.Timeout:
            st.error("The request timed out. The agent crew may be taking too long to run. Please try again.")

