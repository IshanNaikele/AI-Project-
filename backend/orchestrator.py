from backend.agents.research_agent import ResearchAgents
from backend.agents.critical_agent import CriticalAgents
from backend.agents.architect_agent import SolutionArchitectAgents
from backend.agents.pitch_agent import PitchAgents

from backend.tasks import ResearchTasks, CriticalTasks, SolutionArchitectTasks, PitchTasks
from crewai import Crew, Process
from langchain_community.chat_models import ChatLiteLLM
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["OPENAI_API_KEY"] = "dummy-key"

class AIStrategistOrchestrator:
    def __init__(self):
        self.llm = ChatLiteLLM(
            model="ollama/gemma:2b", 
            base_url="http://localhost:8080"
        )

    def run_strategy_workflow(self, theme, idea, team_strength):
        """Execute the workflow step by step to ensure proper data flow"""
        try:
            print(f"🚀 Starting workflow: {team_strength} team")
            
            # Initialize agents
            research_agents = ResearchAgents()
            critical_agents = CriticalAgents()
            solution_architect_agents = SolutionArchitectAgents()
            pitch_agents = PitchAgents()
            
            research_tasks = ResearchTasks()
            critical_tasks = CriticalTasks()
            solution_architect_tasks = SolutionArchitectTasks()
            pitch_tasks = PitchTasks()

            # STEP 1: Research
            print("📊 Step 1: Market Research...")
            researcher = research_agents.research_agent(llm=self.llm)
            research_task = research_tasks.research_task(researcher, theme, idea)
            
            research_crew = Crew(
                agents=[researcher],
                tasks=[research_task],
                process=Process.sequential,
                verbose=False
            )
            research_result = research_crew.kickoff()
            print(f"✅ Research complete: {str(research_result)[:100]}...")

            # STEP 2: Critical Analysis
            print("🔍 Step 2: Critical Analysis...")
            critic = critical_agents.critical_agent(llm=self.llm)
            critical_task = critical_tasks.critical_task(critic, str(research_result))
            
            critical_crew = Crew(
                agents=[critic],
                tasks=[critical_task], 
                process=Process.sequential,
                verbose=False
            )
            critical_result = critical_crew.kickoff()
            print(f"✅ Critical analysis complete: {str(critical_result)[:100]}...")

            # STEP 3: Solution Architecture
            print(f"🏗️ Step 3: Solution Architecture for {team_strength} team...")
            architect = solution_architect_agents.solution_architect_agent(llm=self.llm)
            architect_task = solution_architect_tasks.solution_architect_task(
                architect, idea, str(research_result), str(critical_result), team_strength
            )
            
            architect_crew = Crew(
                agents=[architect],
                tasks=[architect_task],
                process=Process.sequential,
                verbose=False
            )
            architect_result = architect_crew.kickoff()
            print(f"✅ Architecture complete: {str(architect_result)[:100]}...")

            # STEP 4: Pitch Generation
            print("🎯 Step 4: Pitch Generation...")
            pitch_gen = pitch_agents.pitch_agent(llm=self.llm)
            pitch_task = pitch_tasks.pitch_task(pitch_gen, str(architect_result))
            
            pitch_crew = Crew(
                agents=[pitch_gen],
                tasks=[pitch_task],
                process=Process.sequential,
                verbose=False
            )
            pitch_result = pitch_crew.kickoff()
            print("✅ Pitch complete!")

            return {
                "success": True,
                "research": str(research_result),
                "critical_analysis": str(critical_result), 
                "mvp_plan": str(architect_result),
                "pitch": str(pitch_result),
                "team_strength": team_strength
            }

        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return {
                "success": False,
                "error": str(e),
                "team_strength": team_strength
            }
