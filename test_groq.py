import os
from crewai import Agent, Task, Crew, Process
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()
os.environ["OPENAI_API_KEY"] = "dummy-key"
# --- 1. CONFIGURATION ---
# Get Groq API key from environment variable
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables.")


# --- NEW IMPORT ---
from langchain_groq import ChatGroq
# Initialize the Groq client
client = ChatGroq(api_key=api_key,model_name="mixtral-8x7b-32768")

# --- 2. AGENT DEFINITION ---
# A simple agent with a clear role and goal.
groq_agent = Agent(
    role='Expert Researcher',
    goal='Provide a concise summary of a given topic using Groq.',
    backstory='You are a highly efficient AI assistant specialized in fast-paced research.',
    verbose=True,
    llm=client # Assign the Groq client here
)

# --- 3. TASK DEFINITION ---
# A task for the agent to perform.
research_task = Task(
    description='Summarize the key features of FastAPI and its main benefits.',
    agent=groq_agent,
    expected_output='A one-paragraph summary about FastAPI.'
)

# --- 4. CREW EXECUTION ---
# Create the crew and run the process
project_crew = Crew(
    agents=[groq_agent],
    tasks=[research_task],
    process=Process.sequential,
    verbose=True
)

# Kick off the crew's work
print("### Running Groq with CrewAI...")
result = project_crew.kickoff()

print("\n\n### Crew's Final Output:")
print(result)