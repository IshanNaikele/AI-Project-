# backend/orchestrator.py

# Import the necessary components
from backend.agents.research_agent import ResearchAgents
from backend.tasks import ResearchTasks
from crewai import Crew, Process
from langchain_community.chat_models import ChatLiteLLM
from dotenv import load_dotenv
import os

# Load all environment variables from the .env file
load_dotenv()

# Set a dummy OPENAI_API_KEY to prevent internal CrewAI checks from failing.
os.environ["OPENAI_API_KEY"] = "dummy-key"

if __name__ == '__main__':
    # Initialize the classes
    agents = ResearchAgents()
    tasks = ResearchTasks()

    # Define the LLM for the crew, pointing to your local Ollama instance
    # Use the smaller 'gemma:2b' model
    llm = ChatLiteLLM(
        model="ollama/gemma:2b", # <-- This is the correct model name
        base_url="http://localhost:8080" 
    )

    # Get the agent and task objects
    research_agent = agents.research_agent(llm=llm)
    research_task = tasks.research_task(
        agent=research_agent,
        theme="AI in Education",
        idea="An AI-powered app to help students learn new languages."
    )

    # Create and configure the Crew
    crew = Crew(
        agents=[research_agent],
        tasks=[research_task],
        process=Process.sequential,
        verbose=True,
        llm=llm
    )

    # Kick off the crew's work
    print("🚀 Crew kicking off...")
    result = crew.kickoff()

    print("\n\n✅ Crew execution finished!")
    print("Final Result:")
    print(result)
