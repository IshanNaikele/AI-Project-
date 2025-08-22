import os
from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# --- 1. CONFIGURATION ---
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables.")

os.environ["OPENAI_API_KEY"] = api_key
os.environ["OPENAI_API_BASE"] = "https://api.groq.com/openai/v1"

# --- 2. AGENT DEFINITION ---
# Assign the LLM with the provider prefix and a working model name
groq_agent = Agent(
    role='Expert Researcher',
    goal='Provide a concise summary of a given topic using Groq.',
    backstory='You are a highly efficient AI assistant...',
    verbose=True,
    llm="groq/llama3-8b-8192" # <-- The fix is here
)

# --- 3. TASK DEFINITION ---
research_task = Task(
    description='Summarize the key features of FastAPI and its main benefits.',
    agent=groq_agent,
    expected_output='A one-paragraph summary about FastAPI.'
)

# --- 4. CREW EXECUTION ---
project_crew = Crew(
    agents=[groq_agent],
    tasks=[research_task],
    process=Process.sequential,
    verbose=True
)

print("### Running Groq with CrewAI...")
result = project_crew.kickoff()

print("\n\n### Crew's Final Output:")
print(result)