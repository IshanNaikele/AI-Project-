# backend/orchestrator.py
from backend.agents.research_agent import ResearchAgents
from backend.agents.critical_agent import CriticalAgents
from backend.agents.architect_agent import SolutionArchitectAgents
from backend.agents.pitch_agent import PitchAgents
from langchain_groq import ChatGroq
from backend.tasks import ResearchTasks, CriticalTasks, SolutionArchitectTasks, PitchTasks, TaskValidator
from crewai import Crew, Process
from langchain_community.chat_models import ChatLiteLLM
from dotenv import load_dotenv
import os
import time
from typing import Dict, Any

load_dotenv()
os.environ["OPENAI_API_KEY"] = "dummy-key"

class AIStrategistOrchestrator:
    def __init__(self):
        self.llm = ChatLiteLLM(
            model="ollama/gemma:2b", 
            base_url="http://localhost:8080"
        )
        groq_api_key = os.getenv("GROQ_API_KEY")
        if groq_api_key:
            # Set up Groq environment variables
            os.environ["OPENAI_API_KEY"] = groq_api_key
            os.environ["OPENAI_API_BASE"] = "https://api.groq.com/openai/v1"
            # Groq LLM string (not an object)
            self.groq_llm = "groq/llama3-8b-8192"  # or "groq/mixtral-8x7b-32768"
        else:
            print("⚠️ GROQ_API_KEY not found, falling back to local LLM for all agents")
            self.groq_llm = self.llm
        self.task_validator = TaskValidator()

    def validate_team_strength(self, team_strength: str) -> str:
        """Validate and normalize team strength input"""
        valid_strengths = ["Frontend", "Backend", "AI/ML", "Full-Stack"]
        
        # Normalize input
        team_strength = team_strength.strip().title()
        if team_strength == "Ai/Ml":
            team_strength = "AI/ML"
        elif team_strength == "Full Stack" or team_strength == "Fullstack":
            team_strength = "Full-Stack"
        
        if team_strength not in valid_strengths:
            print(f"⚠️ Invalid team strength '{team_strength}'. Defaulting to 'Full-Stack'")
            return "Full-Stack"
        
        return team_strength

    def log_step_progress(self, step: int, total: int, description: str, status: str = "running"):
        """Enhanced logging with progress tracking"""
        progress = int((step / total) * 100)
        status_emoji = {
            "running": "🔄",
            "complete": "✅",
            "error": "❌",
            "warning": "⚠️"
        }
        
        print(f"{status_emoji.get(status, '🔄')} [{progress:3d}%] Step {step}/{total}: {description}")

    def validate_task_output(self, output: str, team_strength: str, task_name: str) -> Dict[str, Any]:
        """Validate task output quality and team-specificity"""
        validation_results = self.task_validator.validate_task_specificity(output, team_strength)
        quality_score = self.task_validator.get_task_quality_score(validation_results)
        
        if quality_score < 0.5:
            print(f"⚠️ Low quality score ({quality_score:.2f}) for {task_name}")
            print(f"   Issues: {[k for k, v in validation_results.items() if not v]}")
        
        return {
            "quality_score": quality_score,
            "validation_results": validation_results,
            "output_length": len(output),
            "team_specific": validation_results.get("mentions_team_strength", False)
        }

    # MODIFICATION: Added `hackathon_duration` parameter
    def run_strategy_workflow(self, theme: str, idea: str, team_strength: str, hackathon_duration: int) -> Dict[str, Any]:
        """Execute the enhanced workflow with time and team-specific optimizations"""
        
        # Validate inputs
        team_strength = self.validate_team_strength(team_strength)
        
        workflow_start = time.time()
        
        try:
            # The total number of steps is 4, as you requested to skip the Consistency Agent
            self.log_step_progress(0, 4, f"Initializing workflow for {team_strength} team and {hackathon_duration}-hour hackathon", "running")
            
            # Initialize agents and tasks
            research_agents = ResearchAgents()
            critical_agents = CriticalAgents()
            solution_architect_agents = SolutionArchitectAgents()
            pitch_agents = PitchAgents()
            
            research_tasks = ResearchTasks()
            critical_tasks = CriticalTasks()
            solution_architect_tasks = SolutionArchitectTasks()
            pitch_tasks = PitchTasks()

            # STEP 1: Enhanced Market Research
            step_start = time.time()
            self.log_step_progress(1, 4, "Market Research & Competitor Analysis")
            
            # MODIFICATION: Passed `hackathon_duration` to the agent and task
            researcher = research_agents.enhanced_research_agent_with_team_focus(llm=self.llm, team_strength=team_strength, hackathon_duration=hackathon_duration)
            research_task = research_tasks.research_task(researcher, theme, idea, team_strength, hackathon_duration)
            
            research_crew = Crew(
                agents=[researcher],
                tasks=[research_task],
                process=Process.sequential,
                verbose=False
            )
            research_result = research_crew.kickoff()
            
            research_validation = self.validate_task_output(str(research_result), team_strength, "Research")
            step_time = time.time() - step_start
            self.log_step_progress(1, 4, f"Research complete ({step_time:.1f}s) - Quality: {research_validation['quality_score']:.2f}", "complete")

            # STEP 2: Enhanced Critical Analysis  
            step_start = time.time()
            self.log_step_progress(2, 4, "Critical Risk Analysis & Failure Prevention")
            
            # MODIFICATION: Passed `hackathon_duration` to the agent and task
            critic = critical_agents.enhanced_critical_agent_with_team_focus(llm=self.llm, team_strength=team_strength, hackathon_duration=hackathon_duration)
            critical_task = critical_tasks.critical_task(
                critic, str(research_result), idea, team_strength, hackathon_duration
            )
            
            critical_crew = Crew(
                agents=[critic],
                tasks=[critical_task], 
                process=Process.sequential,
                verbose=False
            )
            critical_result = critical_crew.kickoff()
            
            critical_validation = self.validate_task_output(str(critical_result), team_strength, "Critical Analysis")
            step_time = time.time() - step_start
            self.log_step_progress(2, 4, f"Critical analysis complete ({step_time:.1f}s) - Quality: {critical_validation['quality_score']:.2f}", "complete")

            # STEP 3: Enhanced Solution Architecture
            step_start = time.time()
            self.log_step_progress(3, 4, f"MVP Architecture for {team_strength} team")
            
            # MODIFICATION: Passed `hackathon_duration` to the agent and task
            architect = solution_architect_agents.enhanced_solution_architect_with_team_focus(llm=self.llm, team_strength=team_strength, hackathon_duration=hackathon_duration)
            architect_task = solution_architect_tasks.solution_architect_task(
                architect, idea, str(research_result), str(critical_result), team_strength, hackathon_duration
            )
            
            architect_crew = Crew(
                agents=[architect],
                tasks=[architect_task],
                process=Process.sequential,
                verbose=False
            )
            architect_result = architect_crew.kickoff()
            
            architect_validation = self.validate_task_output(str(architect_result), team_strength, "Solution Architecture")
            step_time = time.time() - step_start
            self.log_step_progress(3, 4, f"Architecture complete ({step_time:.1f}s) - Quality: {architect_validation['quality_score']:.2f}", "complete")

            # STEP 4: Enhanced Pitch Generation
            step_start = time.time()
            self.log_step_progress(4, 4, "Winning Pitch Strategy Generation")
            
            # MODIFICATION: Passed `hackathon_duration` to the agent and task
            pitch_gen = pitch_agents.enhanced_pitch_agent_with_team_focus(llm=self.llm, team_strength=team_strength, hackathon_duration=hackathon_duration)
            pitch_task = pitch_tasks.pitch_task(
                pitch_gen, str(architect_result), team_strength, theme, hackathon_duration
            )
            
            pitch_crew = Crew(
                agents=[pitch_gen],
                tasks=[pitch_task],
                process=Process.sequential,
                verbose=False
            )
            pitch_result = pitch_crew.kickoff()
            
            pitch_validation = self.validate_task_output(str(pitch_result), team_strength, "Pitch Strategy")
            step_time = time.time() - step_start
            total_time = time.time() - workflow_start
            
            self.log_step_progress(4, 4, f"Pitch complete ({step_time:.1f}s) - Quality: {pitch_validation['quality_score']:.2f}", "complete")
            
            print(f"🎉 Workflow completed in {total_time:.1f}s for {team_strength} team!")

            # Calculate overall quality metrics
            overall_quality = (
                research_validation['quality_score'] + 
                critical_validation['quality_score'] + 
                architect_validation['quality_score'] + 
                pitch_validation['quality_score']
            ) / 4

            # Prepare enhanced response
            response = {
                "success": True,
                "team_strength": team_strength,
                "theme": theme,
                "original_idea": idea,
                "hackathon_duration": hackathon_duration,
                
                # Core outputs
                "research": str(research_result),
                "critical_analysis": str(critical_result), 
                "mvp_plan": str(architect_result),
                "pitch": str(pitch_result),
                
                # Quality metrics
                "quality_metrics": {
                    "overall_quality_score": overall_quality,
                    "research_quality": research_validation['quality_score'],
                    "critical_quality": critical_validation['quality_score'], 
                    "architect_quality": architect_validation['quality_score'],
                    "pitch_quality": pitch_validation['quality_score'],
                    "team_specific_optimization": all([
                        research_validation['team_specific'],
                        critical_validation['team_specific'],
                        architect_validation['team_specific'],
                        pitch_validation['team_specific']
                    ])
                },
                
                # Performance metrics
                "performance_metrics": {
                    "total_execution_time": total_time,
                    "workflow_efficiency": "high" if total_time < 120 else "medium" if total_time < 300 else "low"
                },
                
                # Workflow metadata
                "workflow_metadata": {
                    "workflow_version": "2.0_enhanced",
                    "timestamp": time.time(),
                    "team_strength_validated": team_strength,
                    "all_validations_passed": overall_quality > 0.6
                }
            }

            # Add warnings if quality is low
            if overall_quality < 0.5:
                response["warnings"] = [
                    "Low overall quality score detected",
                    "Outputs may not be sufficiently team-specific",
                    "Consider re-running workflow with clearer inputs"
                ]
                self.log_step_progress(0, 0, "Quality warnings detected", "warning")

            return response

        except Exception as e:
            error_time = time.time() - workflow_start
            self.log_step_progress(0, 0, f"Workflow failed after {error_time:.1f}s", "error")
            
            return {
                "success": False,
                "error": str(e),
                "error_type": type(e).__name__,
                "team_strength": team_strength,
                "theme": theme,
                "original_idea": idea,
                "execution_time": error_time,
                "workflow_metadata": {
                    "workflow_version": "2.0_enhanced",
                    "timestamp": time.time(),
                    "error_occurred": True
                }
            }

    def get_workflow_status(self) -> Dict[str, Any]:
        """Get current workflow capabilities and status"""
        return {
            "orchestrator_version": "2.0_enhanced",
            "supported_team_strengths": ["Frontend", "Backend", "AI/ML", "Full-Stack"],
            "features": [
                "Team-specific task optimization",
                "Quality validation and scoring", 
                "Enhanced progress tracking",
                "Detailed performance metrics",
                "Input validation and normalization",
                "Failure recovery and error handling"
            ],
            "llm_config": {
                "research_critical_model": "ollama/gemma:2b",
                "research_critical_base_url": "http://localhost:8080",
                "architect_pitch_model": self.llm if isinstance(self.llm, str) else "groq/llama3-8b-8192"
            },
            "validation_enabled": True,
            "quality_threshold": 0.6
        }

    def run_quick_validation(self, theme: str, idea: str, team_strength: str) -> Dict[str, Any]:
        """Run quick validation without full workflow execution"""
        team_strength = self.validate_team_strength(team_strength)
        
        # Get team-specific constraints and templates
        research_constraints = ResearchTasks.get_team_research_constraints(team_strength)
        risk_profile = CriticalTasks.get_team_risk_profile(team_strength)
        arch_template = SolutionArchitectTasks.get_architecture_templates(team_strength)
        pitch_template = PitchTasks.get_pitch_templates(team_strength)
        
        return {
            "input_validation": "passed",
            "team_strength": team_strength,
            "optimization_preview": {
                "research_focus": research_constraints['competitor_type'],
                "tech_priority": research_constraints['tech_priority'],
                "main_risk": risk_profile['scope_creep'],
                "architecture_pattern": arch_template['core_pattern'],
                "demo_emphasis": pitch_template['demo_emphasis']
            },
            "estimated_execution_time": "2-5 minutes",
            "ready_for_execution": True
        }