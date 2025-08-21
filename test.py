import os
from dotenv import load_dotenv
load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
GROQ_API_KEY=os.getenv("GROQ_API_KEY")

if GROQ_API_KEY:
    print("GROQ_API_KEY loaded successfully!")
    print(f"Your key starts with: {GROQ_API_KEY[:4]}...") 
else:
    print("Error: GROQ_API_KEY not found.")

from langchain_groq import ChatGroq
model=ChatGroq(model="openai/gpt-oss-120b",groq_api_key=GROQ_API_KEY
)
# from langchain_core.messages import HumanMessage,SystemMessage
print(model.invoke("What's Going on ?"))
