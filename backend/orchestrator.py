# backend/orchestrator.py
from backend.agents.research_agent import ResearchAgents
from backend.agents.critical_agent import CriticalAgents
from backend.agents.architect_agent import SolutionArchitectAgents
from backend.agents.pitch_agent import PitchAgents
from backend.tasks import ResearchTasks, CriticalTasks, SolutionArchitectTasks, PitchTasks
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
        self.llm = ChatLiteLLM(model="ollama/gemma:2b", base_url="http://localhost:8080")
        
        # Setup Groq for architect and pitch agents
        self.groq_api_key = os.getenv("GROQ_API_KEY")
        if self.groq_api_key:
            # Create Groq LLM specifically for architect and pitch agents
            self.groq_llm = ChatLiteLLM(
                model="groq/gemma2-9b-it",
                api_key=self.groq_api_key,
                base_url="https://api.groq.com/openai/v1"
            )
            print("✅ Groq API configured for architect & pitch agents")
        else:
            self.groq_llm = self.llm
            print("⚠️ GROQ_API_KEY not found, using local LLM for all agents")

    def validate_inputs(self, team_strength: str, hackathon_duration: int) -> tuple:
        """Validate and normalize inputs"""
        valid_strengths = ["Frontend", "Backend", "AI/ML", "Full-Stack"]
        team_strength = team_strength.strip().title()
        
        if team_strength == "Ai/Ml":
            team_strength = "AI/ML"
        elif team_strength in ["Full Stack", "Fullstack"]:
            team_strength = "Full-Stack"
            
        if team_strength not in valid_strengths:
            print(f"⚠️ Invalid team strength '{team_strength}'. Defaulting to 'Full-Stack'")
            team_strength = "Full-Stack"
        
        if hackathon_duration < 1 or hackathon_duration > 168:
            hackathon_duration = 24
            print(f"⚠️ Invalid duration. Defaulting to 24 hours")
            
        return team_strength, hackathon_duration

    def log_progress(self, step: int, total: int, description: str, elapsed: float = None):
        """Enhanced progress logging"""
        progress = int((step / total) * 100)
        status = "✅" if step == total else "🔄"
        time_info = f" ({elapsed:.1f}s)" if elapsed else ""
        print(f"{status} [{progress:3d}%] {description}{time_info}")

    def extract_clean_output(self, crew_result, agent_type: str = "unknown") -> str:
        """Extract clean string output from crew result with enhanced debugging"""
        try:
            print(f"🔍 Extracting output for {agent_type} agent")
            print(f"🔍 Crew result type: {type(crew_result)}")
            
            # Log all available attributes for debugging
            if hasattr(crew_result, '__dict__'):
                attrs = [attr for attr in dir(crew_result) if not attr.startswith('_')]
                print(f"🔍 Available attributes: {attrs}")
            
            output = None
            
            # Try multiple extraction methods in order of preference
            extraction_methods = [
                ('raw', lambda x: getattr(x, 'raw', None)),
                ('output', lambda x: getattr(x, 'output', None)),
                ('result', lambda x: getattr(x, 'result', None)),
                ('tasks_output', lambda x: str(x.tasks_output[0].output) if hasattr(x, 'tasks_output') and len(x.tasks_output) > 0 else None),
                ('tasks_output_raw', lambda x: str(x.tasks_output[0].raw) if hasattr(x, 'tasks_output') and len(x.tasks_output) > 0 else None),
                ('str_conversion', lambda x: str(x))
            ]
            
            for method_name, extractor in extraction_methods:
                try:
                    extracted = extractor(crew_result)
                    if extracted and str(extracted).strip():
                        output = str(extracted).strip()
                        print(f"✅ Successfully extracted using method: {method_name}")
                        print(f"✅ Output preview: {output[:200]}...")
                        break
                except Exception as e:
                    print(f"❌ Method {method_name} failed: {str(e)}")
                    continue
            
            if not output:
                print(f"❌ All extraction methods failed for {agent_type}")
                print(f"❌ Raw crew_result: {str(crew_result)[:500]}")
                return f"No output extracted for {agent_type} agent. Result: {str(crew_result)[:200]}..."
            
            # Clean up common formatting issues
            if output.startswith('```') and output.endswith('```'):
                output = output[3:-3].strip()
            
            # Remove common prefixes
            prefixes_to_remove = [
                "Agent:", "Output:", "Result:", "Response:", 
                f"{agent_type}:", f"{agent_type} Agent:", 
                "Final Answer:", "Conclusion:"
            ]
            for prefix in prefixes_to_remove:
                if output.lower().startswith(prefix.lower()):
                    output = output[len(prefix):].strip()
            
            # Ensure we have substantive content
            if len(output) < 50:
                print(f"⚠️ Short output detected for {agent_type} ({len(output)} chars): {output}")
                
            print(f"✅ Final output length for {agent_type}: {len(output)} chars")
            return output
            
        except Exception as e:
            error_msg = f"Output extraction failed for {agent_type}: {str(e)}"
            print(f"❌ {error_msg}")
            return error_msg

    def run_strategy_workflow(self, theme: str, idea: str, team_strength: str, hackathon_duration: int) -> Dict[str, Any]:
        """Execute complete AI Strategist workflow with proper task chaining"""
        
        workflow_start = time.time()
        team_strength, hackathon_duration = self.validate_inputs(team_strength, hackathon_duration)
        
        try:
            self.log_progress(0, 4, f"Initializing {team_strength} workflow ({hackathon_duration}h hackathon)")
            
            # Initialize task creators
            research_tasks = ResearchTasks()
            critical_tasks = CriticalTasks()
            architect_tasks = SolutionArchitectTasks()
            pitch_tasks = PitchTasks()

            # STEP 1: Research Agent (Local LLM)
            step_start = time.time()
            self.log_progress(1, 4, "Market Research & Competitor Analysis")
            
            research_agent = ResearchAgents().enhanced_research_agent_with_team_focus(
                self.llm, team_strength, hackathon_duration
            )
            research_task = research_tasks.research_task(
                research_agent, theme, idea, team_strength, hackathon_duration
            )
            
            research_crew = Crew(
                agents=[research_agent],
                tasks=[research_task],
                process=Process.sequential,
                verbose=False
            )
            research_result = research_crew.kickoff()
            research_output = self.extract_clean_output(research_result, "research")
            
            step_time = time.time() - step_start
            self.log_progress(1, 4, f"Research Complete", step_time)
            print(f"📊 Research output length: {len(research_output)} chars")

            # STEP 2: Critical Analysis Agent (Local LLM)
            step_start = time.time()
            self.log_progress(2, 4, "Critical Risk Analysis")
            
            critical_agent = CriticalAgents().enhanced_critical_agent_with_team_focus(
                self.llm, team_strength, hackathon_duration
            )
            critical_task = critical_tasks.critical_task(
                critical_agent, research_output, idea, team_strength, hackathon_duration
            )
            
            critical_crew = Crew(
                agents=[critical_agent],
                tasks=[critical_task],
                process=Process.sequential,
                verbose=False
            )
            critical_result = critical_crew.kickoff()
            critical_output = self.extract_clean_output(critical_result, "critical")
            
            step_time = time.time() - step_start
            self.log_progress(2, 4, f"Critical Analysis Complete", step_time)
            print(f"⚠️ Critical analysis output length: {len(critical_output)} chars")

            # STEP 3: Solution Architect Agent (GROQ LLM for speed)
            step_start = time.time()
            self.log_progress(3, 4, "MVP Architecture Design (Groq)")
            
            architect_agent = SolutionArchitectAgents().enhanced_solution_architect_with_team_focus(
                self.groq_llm, team_strength, hackathon_duration
            )
            architect_task = architect_tasks.solution_architect_task(
                architect_agent, idea, research_output, critical_output, team_strength, hackathon_duration
            )
            
            architect_crew = Crew(
                agents=[architect_agent],
                tasks=[architect_task],
                process=Process.sequential,
                verbose=False
            )
            architect_result = architect_crew.kickoff()
            architect_output = self.extract_clean_output(architect_result, "architect")
            
            step_time = time.time() - step_start
            self.log_progress(3, 4, f"Architecture Complete (Groq)", step_time)
            print(f"🏗️ Architecture output length: {len(architect_output)} chars")

            # STEP 4: Pitch Strategy Agent (GROQ LLM for speed)
            step_start = time.time()
            self.log_progress(4, 4, "Pitch Strategy Generation (Groq)")
            
            pitch_agent = PitchAgents().enhanced_pitch_agent_with_team_focus(
                self.groq_llm, team_strength, hackathon_duration
            )
            pitch_task = pitch_tasks.pitch_task(
                pitch_agent, architect_output, team_strength, theme, hackathon_duration
            )
            
            pitch_crew = Crew(
                agents=[pitch_agent],
                tasks=[pitch_task],
                process=Process.sequential,
                verbose=False
            )
            pitch_result = pitch_crew.kickoff()
            pitch_output = self.extract_clean_output(pitch_result, "pitch")
            
            # Special handling for pitch agent - often has different result structure
            if not pitch_output or len(pitch_output.strip()) < 100:
                print(f"🔧 Attempting alternative pitch extraction methods...")
                
                # Try alternative extraction for pitch
                alternative_methods = [
                    lambda x: x.tasks_output[0].output if hasattr(x, 'tasks_output') and x.tasks_output else None,
                    lambda x: x.tasks_output[0].raw if hasattr(x, 'tasks_output') and x.tasks_output else None,
                    lambda x: getattr(x.tasks_output[0], 'result', None) if hasattr(x, 'tasks_output') and x.tasks_output else None,
                    lambda x: str(x).split('\n')[-1] if '\n' in str(x) else None,  # Sometimes output is at the end
                ]
                
                for i, method in enumerate(alternative_methods):
                    try:
                        alt_output = method(pitch_result)
                        if alt_output and len(str(alt_output).strip()) > 100:
                            pitch_output = str(alt_output).strip()
                            print(f"✅ Pitch output recovered using alternative method {i+1}")
                            break
                    except Exception as e:
                        print(f"❌ Alternative method {i+1} failed: {str(e)}")
                        continue
                
                # Last resort: provide debugging info
                if not pitch_output or len(pitch_output.strip()) < 100:
                    print(f"🚨 PITCH AGENT DEBUG INFO:")
                    print(f"🚨 Result type: {type(pitch_result)}")
                    print(f"🚨 Result str: {str(pitch_result)[:500]}")
                    if hasattr(pitch_result, '__dict__'):
                        print(f"🚨 Result dict: {pitch_result.__dict__}")
                    
                    pitch_output = f"Pitch generation completed but output extraction needs debugging. Raw result: {str(pitch_result)[:300]}..."
            
            step_time = time.time() - step_start
            total_time = time.time() - workflow_start
            self.log_progress(4, 4, f"Workflow Complete", total_time)
            print(f"🎯 Pitch output length: {len(pitch_output)} chars")

            # Validate all outputs before returning
            outputs = {
                "research": research_output,
                "critical_analysis": critical_output, 
                "mvp_plan": architect_output,
                "pitch_strategy": pitch_output
            }
            
            # Check for empty outputs
            empty_outputs = [key for key, value in outputs.items() if not value or len(value.strip()) < 20]
            if empty_outputs:
                print(f"⚠️ Warning: Empty/short outputs detected: {empty_outputs}")

            # Structure clean response for Streamlit
            response = {
                "success": True,
                "team_strength": team_strength,
                "hackathon_duration": hackathon_duration,
                "theme": theme,
                "original_idea": idea,
                
                # Core outputs (clean strings for Streamlit display)
                **outputs,
                
                # Quick summary for UI
                "summary": {
                    "feasibility": self._assess_feasibility(team_strength, hackathon_duration),
                    "competitive_edge": self._get_team_advantage(team_strength),
                    "execution_time": f"{total_time:.1f} seconds",
                    "workflow_status": "Completed Successfully",
                    "groq_used": bool(self.groq_api_key),
                    "output_lengths": {k: len(v) for k, v in outputs.items()}
                },
                
                # Metadata
                "execution_time": total_time,
                "timestamp": time.time(),
                "workflow_version": "3.2_groq_fixed",
                "llm_config": {
                    "research_critical": "Ollama Gemma:2b",
                    "architect_pitch": "Groq Gemma2-9b-it" if self.groq_api_key else "Ollama Gemma:2b"
                }
            }
            
            print(f"✅ All 4 agents completed successfully for {team_strength} team!")
            print(f"🚀 Architect & Pitch used {'Groq' if self.groq_api_key else 'Local'} LLM")
            return response
            
        except Exception as e:
            error_time = time.time() - workflow_start
            print(f"❌ Workflow failed after {error_time:.1f}s: {str(e)}")
            
            return {
                "success": False,
                "error": str(e),
                "error_type": type(e).__name__,
                "team_strength": team_strength,
                "hackathon_duration": hackathon_duration,
                "theme": theme,
                "original_idea": idea,
                "execution_time": error_time,
                "workflow_version": "3.2_groq_fixed",
                "groq_available": bool(self.groq_api_key)
            }

    def _assess_feasibility(self, team_strength: str, duration: int) -> str:
        """Quick feasibility assessment"""
        if duration >= 24:
            return "High - Sufficient time for polished MVP"
        elif duration >= 12:
            return "Medium - Focus on core features"
        else:
            return "Challenging - Minimal viable demo only"

    def _get_team_advantage(self, team_strength: str) -> str:
        """Get team-specific competitive advantages"""
        advantages = {
            "Frontend": "Superior user experience and visual design",
            "Backend": "High-performance APIs and data processing", 
            "AI/ML": "Intelligent automation and predictive capabilities",
            "Full-Stack": "Complete end-to-end system integration"
        }
        return advantages.get(team_strength, "Balanced development capabilities")

    def get_workflow_preview(self, theme: str, idea: str, team_strength: str, hackathon_duration: int) -> Dict[str, Any]:
        """Get workflow preview without execution"""
        team_strength, hackathon_duration = self.validate_inputs(team_strength, hackathon_duration)
        
        return {
            "workflow_preview": True,
            "team_strength": team_strength,
            "hackathon_duration": hackathon_duration,
            "estimated_time": "1-3 minutes (with Groq acceleration)",
            "workflow_steps": [
                "Market Research & Competitor Analysis (Ollama)",
                "Critical Risk Analysis & Failure Prevention (Ollama)", 
                "MVP Architecture Design - 6 Key Areas (Groq ⚡)",
                "Winning Pitch Strategy Generation (Groq ⚡)"
            ],
            "focus_areas": {
                "research": f"Competitor analysis for {team_strength} solutions",
                "critical": f"Risk assessment for {hackathon_duration}h timeline",
                "architecture": f"MVP design with problem/innovation/audience/feasibility/wow-factor/differentiation", 
                "pitch": f"3-minute demo strategy showcasing {team_strength} expertise"
            },
            "feasibility": self._assess_feasibility(team_strength, hackathon_duration),
            "competitive_edge": self._get_team_advantage(team_strength),
            "groq_acceleration": bool(self.groq_api_key),
            "ready": True
        }

    def get_system_status(self) -> Dict[str, Any]:
        """Get system status and capabilities"""
        return {
            "version": "3.2_groq_fixed",
            "agents": ["Research", "Critical Analysis", "Solution Architect", "Pitch Strategy"],
            "supported_teams": ["Frontend", "Backend", "AI/ML", "Full-Stack"],
            "hackathon_duration_range": "1-168 hours",
            "architect_features": [
                "Real-world problem analysis",
                "Innovation identification", 
                "Target audience specification",
                "Feasibility validation",
                "Wow factor engineering",
                "Competitive differentiation"
            ],
            "llm_status": "Connected" if self.llm else "Disconnected",
            "groq_available": bool(self.groq_api_key),
            "groq_model": "gemma2-9b-it",
            "workflow_fixed": True,
            "speed_optimization": "Architect & Pitch use Groq for 3-5x speedup",
            "ready": True
        }

    def test_llm_connections(self) -> Dict[str, Any]:
        """Test both LLM connections"""
        results = {
            "ollama_status": "unknown",
            "groq_status": "unknown",
            "timestamp": time.time()
        }
        
        # Test Ollama
        try:
            test_response = self.llm.invoke("Test message")
            results["ollama_status"] = "connected"
        except Exception as e:
            results["ollama_status"] = f"failed: {str(e)[:100]}"
        
        # Test Groq (if available)
        if self.groq_api_key:
            try:
                test_response = self.groq_llm.invoke("Test message")
                results["groq_status"] = "connected"
            except Exception as e:
                results["groq_status"] = f"failed: {str(e)[:100]}"
        else:
            results["groq_status"] = "no_api_key"
            
        return results

# Export for easy import
__all__ = ['AIStrategistOrchestrator']