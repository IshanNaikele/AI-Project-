# backend/orchestrator.py

# Import all necessary agents and tasks
from backend.agents.research_agent import ResearchAgents
from backend.agents.critical_agent import CriticalAgents
from backend.agents.architect_agent import SolutionArchitectAgents
from backend.agents.pitch_agent import PitchAgents

from backend.tasks import ResearchTasks, CriticalTasks, SolutionArchitectTasks, PitchTasks
from crewai import Crew, Process
from langchain_community.chat_models import ChatLiteLLM
from dotenv import load_dotenv
import os

# Load all environment variables from the .env file
load_dotenv()

# Set a dummy OPENAI_API_KEY to prevent internal CrewAI checks from failing.
os.environ["OPENAI_API_KEY"] = "dummy-key"

if __name__ == '__main__':
    # Initialize all agent and task classes
    llm = ChatLiteLLM(
        model="ollama/gemma:2b", 
        base_url="http://localhost:8080"
    )

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
    
    # Define a variable for the team's core strength
    # You can get this from user input later in your frontend
    team_strength = "AI/ML Focused"
    
    # Get the task objects
    # Pass the theme and idea as inputs
    research_task = research_tasks.research_task(
        agent=researcher,
        theme="AI in Education",
        idea="An AI-powered app to help students learn new languages."
    )
    
    # The output of research_task becomes the input for critical_task
    critical_task = critical_tasks.critical_task(
        agent=critic,
        research_report=research_task.output
    )
    
    # The output of both previous tasks become inputs for architect_task
    architect_task = solution_architect_tasks.solution_architect_task(
        agent=architect,
        idea="An AI-powered app to help students learn new languages.",
        research_report=research_task.output,
        critical_analysis=critical_task.output,
        team_strength=team_strength
    )
    
    # The output of architect_task becomes the input for pitch_task
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

    # Kick off the crew's work
    print("🚀 Crew kicking off...")
    result = crew.kickoff()

    print("\n\n✅ Crew execution finished!")
    print("Final Result:")
    print(result)
