# backend/llm_config.py
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Provide the API key directly
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables!")

# print(groq_api_key)