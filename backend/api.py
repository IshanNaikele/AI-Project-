# backend/api.py

from fastapi import FastAPI
from pydantic import BaseModel, Field
from crewai import Crew, Process
from langchain_community.chat_models import ChatLiteLLM
from dotenv import load_dotenv
import os
import uvicorn

# Import all agents and tasks
from backend.agents.research_agent import ResearchAgents
from backend.agents.critical_agent import CriticalAgents
from backend.agents.architect_agent import SolutionArchitectAgents
from backend.agents.pitch_agent import PitchAgents
from backend.tasks import ResearchTasks, CriticalTasks, SolutionArchitectTasks, PitchTasks

# Load environment variables for API keys and other configurations
load_dotenv()

# Set a dummy OPENAI_API_KEY for CrewAI's internal checks
os.environ["OPENAI_API_KEY"] = "dummy-key"

# Define a Pydantic model for the request body
class CrewInput(BaseModel):
    """
    Input schema for the crew's kickoff method.
    """
    hackathon_theme: str = Field(..., description="The theme of the hackathon.")
    raw_idea: str = Field(..., description="The raw idea to be validated.")
    team_strength: str = Field(..., description="The core strength of the team (e.g., 'Frontend', 'Backend', 'AI/ML', 'Full-Stack').")

# Initialize the FastAPI app
app = FastAPI(
    title="The AI Strategist",
    description="A multi-agent system for personalized, rapid idea validation and strategic planning.",
    version="1.0.0",
)

# Main endpoint to run the crew
@app.post("/run-strategist", tags=["main"])
def run_strategist(input: CrewInput):
    """
    This endpoint takes a hackathon idea and team strength as input and
    returns a complete, tailored strategic plan and pitch outline.
    """
    # Initialize the LLM
    try:
        llm = ChatLiteLLM(
            model="ollama/gemma:2b",
            base_url="http://localhost:8080"
        )
    except Exception as e:
        return {"error": f"Failed to initialize LLM: {e}"}

    # Initialize all agent and task classes
    research_agents = ResearchAgents()
    research_tasks = ResearchTasks()
    critical_agents = CriticalAgents()
    critical_tasks = CriticalTasks()
    solution_architect_agents = SolutionArchitectAgents()
    solution_architect_tasks = SolutionArchitectTasks()
    pitch_agents = PitchAgents()
    pitch_tasks = PitchTasks()

    # Get the agent objects
    researcher = research_agents.research_agent(llm=llm)
    critic = critical_agents.critical_agent(llm=llm)
    architect = solution_architect_agents.solution_architect_agent(llm=llm)
    pitch_gen = pitch_agents.pitch_agent(llm=llm)
    
    # Define the tasks. The output of one task is passed as context to the next.
    research_task = research_tasks.research_task(
        agent=researcher,
        theme=input.hackathon_theme,
        idea=input.raw_idea
    )
    
    critical_task = critical_tasks.critical_task(
        agent=critic,
        research_report=research_task.output
    )
    
    architect_task = solution_architect_tasks.solution_architect_task(
        agent=architect,
        idea=input.raw_idea,
        research_report=research_task.output,
        critical_analysis=critical_task.output,
        team_strength=input.team_strength
    )
    
    pitch_task = pitch_tasks.pitch_task(
        agent=pitch_gen,
        mvp_plan=architect_task.output
    )

    # Create and configure the Crew
    crew = Crew(
        agents=[researcher, critic, architect, pitch_gen],
        tasks=[research_task, critical_task, architect_task, pitch_task],
        process=Process.sequential,
        verbose=True,
        llm=llm
    )

    try:
        # Kick off the crew's work
        result = crew.kickoff()
        return {"success": True, "result": result}
    except Exception as e:
        return {"success": False, "error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
 