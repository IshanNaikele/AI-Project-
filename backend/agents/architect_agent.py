# backend/agents/architect_agent.py
from crewai import Agent
from textwrap import dedent

class SolutionArchitectAgents:
    """Simplified Solution Architect Agents"""
    
    def enhanced_solution_architect_with_team_focus(self, llm, team_strength: str, hackathon_duration: int):
        """Create a simplified team-focused solution architect agent"""
        
        # Define team-specific focus areas
        team_focus = self._get_team_focus(team_strength)
        time_constraint = self._get_time_constraint(hackathon_duration)
        
        return Agent(
            role=f'{team_strength} Solution Architect',
            goal=dedent(f"""
                Design a practical MVP architecture that maximizes {team_strength} team strengths 
                within {hackathon_duration} hours, focusing on {team_focus['priority']} and ensuring 
                {team_focus['delivery']}.
            """),
            backstory=dedent(f"""
                You are an experienced solution architect specializing in {team_strength} development 
                with extensive hackathon experience. You understand the critical balance between 
                ambition and deliverability in time-constrained environments.
                
                Your expertise includes:
                - {team_focus['expertise']}
                - Rapid prototyping and MVP development
                - Time-efficient architecture patterns
                - Team workflow optimization
                
                You always consider: {time_constraint}
            """),
            verbose=False,
            allow_delegation=False,
            llm=llm
        )
    
    def _get_team_focus(self, team_strength: str) -> dict:
        """Get simplified team-specific focus areas"""
        focus_map = {
            "Frontend": {
                "priority": "user experience and visual appeal",
                "delivery": "polished UI/UX with responsive design",
                "expertise": "Modern frontend frameworks, UI/UX design, responsive development"
            },
            "Backend": {
                "priority": "robust APIs and data architecture", 
                "delivery": "scalable backend services with proper data flow",
                "expertise": "API development, database design, server architecture"
            },
            "AI/ML": {
                "priority": "intelligent features and data processing",
                "delivery": "working AI/ML models with clear value demonstration",
                "expertise": "Machine learning algorithms, data preprocessing, model deployment"
            },
            "Full-Stack": {
                "priority": "complete end-to-end solution",
                "delivery": "integrated full-stack application with balanced features",
                "expertise": "Full-stack development, system integration, balanced architecture"
            }
        }
        return focus_map.get(team_strength, focus_map["Full-Stack"])
    
    def _get_time_constraint(self, hackathon_duration: int) -> str:
        """Get time-specific architectural constraints"""
        if hackathon_duration <= 8:
            return "Ultra-tight timeline - focus on core MVP with minimal complexity"
        elif hackathon_duration <= 24:
            return "Standard hackathon timeline - balanced features with smart shortcuts"
        elif hackathon_duration <= 48:
            return "Extended timeline - opportunity for polished features and testing"
        else:
            return "Marathon timeline - comprehensive solution with quality focus"