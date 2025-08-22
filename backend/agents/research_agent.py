# backend/agents/research_agent.py
from crewai import Agent
from crewai_tools import SerperDevTool
from typing import Dict, List
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize search tool with proper configuration
search_tool = SerperDevTool()

class ResearchAgents:
    """Enhanced research agents with hackathon-specific intelligence"""
    
    @staticmethod
    def get_team_search_strategy(team_strength: str) -> Dict[str, List[str]]:
        """Get search queries optimized for different team strengths"""
        strategies = {
            "Frontend": {
                "competitor_queries": [
                    "{idea} UI design competitors",
                    "{idea} user interface examples", 
                    "best UX for {idea} apps",
                    "{idea} frontend frameworks comparison"
                ],
                "tech_queries": [
                    "{idea} React components libraries",
                    "{idea} API integration frontend",
                    "free APIs for {idea} development",
                    "{idea} CSS frameworks responsive"
                ],
                "focus_areas": ["user experience", "visual design", "API integration", "responsive design"]
            },
            "Backend": {
                "competitor_queries": [
                    "{idea} API competitors",
                    "{idea} backend architecture examples",
                    "{idea} database design patterns",
                    "{idea} server infrastructure"
                ],
                "tech_queries": [
                    "{idea} FastAPI examples",
                    "{idea} database schema design",
                    "{idea} backend APIs comparison",
                    "microservices for {idea}"
                ],
                "focus_areas": ["API design", "database optimization", "server architecture", "data processing"]
            },
            "AI/ML": {
                "competitor_queries": [
                    "{idea} machine learning solutions",
                    "{idea} AI models comparison",
                    "{idea} algorithm approaches",
                    "{idea} ML platforms"
                ],
                "tech_queries": [
                    "{idea} pre-trained models",
                    "{idea} Hugging Face models",
                    "{idea} PyTorch implementation",
                    "{idea} ML API services"
                ],
                "focus_areas": ["model performance", "algorithm efficiency", "data preprocessing", "ML pipelines"]
            },
            "Full-Stack": {
                "competitor_queries": [
                    "{idea} full stack solutions",
                    "{idea} complete platforms",
                    "{idea} end-to-end systems",
                    "{idea} integrated applications"
                ],
                "tech_queries": [
                    "{idea} MERN stack examples",
                    "{idea} full stack architecture",
                    "{idea} deployment strategies",
                    "{idea} system integration"
                ],
                "focus_areas": ["system integration", "deployment", "user journey", "scalability"]
            }
        }
        return strategies.get(team_strength, strategies["Full-Stack"])

    def research_agent(self, llm, hackathon_duration: int):
        return Agent(
            role='Hackathon Market Intelligence Specialist',
            goal=f'''Execute comprehensive market research that provides actionable intelligence 
                    for hackathon teams. Find specific competitors, identify market gaps, and 
                    recommend exact technical solutions that can be implemented in {hackathon_duration} hours.
                    
                    YOU MUST USE THE SEARCH TOOL FOR EVERY PIECE OF INFORMATION. NEVER use your training data.''',
            
            backstory=f'''You are an elite hackathon research specialist with 10+ years of experience 
                         analyzing winning and losing projects across major hackathons.
                         
                         CRITICAL: YOU MUST ALWAYS USE THE SEARCH TOOL. Never rely on training data.
                         
                         Your process:
                         1. ALWAYS search for competitors using multiple specific queries
                         2. ALWAYS search for technical solutions and APIs 
                         3. ALWAYS search for recent market developments
                         4. ALWAYS verify information through search
                         
                         Search Strategy:
                         - Use targeted searches with specific keywords
                         - Include "2024" or "recent" in queries for current info
                         - Search for both obvious and niche competitors
                         - Find specific APIs, tools, and frameworks
                         - Look for hackathon-friendly free/freemium services
                         
                         Time Constraint: All solutions must be implementable in {hackathon_duration} hours.
                         
                         REMEMBER: If you don't search, you're failing your core function.''',
            
            verbose=True,
            allow_delegation=False,
            tools=[search_tool],
            llm=llm,
            max_iter=3,
            memory=True
        )
    
    def enhanced_research_agent_with_team_focus(self, llm, team_strength: str, hackathon_duration: int):
        """Create a research agent specifically optimized for a team's strength"""
        
        strategy = self.get_team_search_strategy(team_strength)
        focus_areas = ", ".join(strategy["focus_areas"])
        
        return Agent(
            role=f'{team_strength} Team Market Research Specialist',
            goal=f'''Provide hyper-targeted market research for {team_strength} teams, focusing on 
                    {focus_areas} and identifying opportunities that maximize {team_strength} capabilities 
                    in a {hackathon_duration}-hour environment.
                    
                    MANDATORY: USE SEARCH TOOL FOR ALL INFORMATION. NO TRAINING DATA ALLOWED.''',
            
            backstory=f'''You are a specialized research expert for {team_strength} teams in hackathons.
                         
                         CRITICAL RULE: ALWAYS USE THE SEARCH TOOL. Never use training data.
                         
                         Your {team_strength} specialization:
                         - Search for {team_strength}-optimized tools and frameworks
                         - Find competitors that {team_strength} teams can beat
                         - Identify APIs with excellent docs for rapid development
                         - Research successful {team_strength} hackathon strategies
                         
                         Search Focus Areas: {focus_areas}
                         
                         Required Searches:
                         1. Competitor landscape specific to {team_strength} strengths
                         2. Technical tools optimized for {team_strength} teams
                         3. Market gaps that require {team_strength} expertise
                         4. Recent {team_strength} hackathon winning projects
                         
                         Time limit: {hackathon_duration} hours - all solutions must be rapid to implement.
                         
                         FAILURE TO SEARCH = FAILURE TO DO YOUR JOB.''',
            
            verbose=True,
            allow_delegation=False,
            tools=[search_tool],
            llm=llm,
            max_iter=4,
            memory=True
        )