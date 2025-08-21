# backend/agents/research_agent.py
from crewai import Agent
from crewai_tools import SerperDevTool
from typing import Dict, List
import json

# Enhanced search tool with better configuration
search_tool = SerperDevTool(
    n_results=8,  # More results for better analysis
    country="us",
    locale="en",
    timeout=10
)

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

    def research_agent(self, llm):
        return Agent(
            role='Hackathon Market Intelligence Specialist',
            goal='''Execute comprehensive market research that provides actionable intelligence 
                   for hackathon teams. Find specific competitors, identify market gaps, and 
                   recommend exact technical solutions that can be implemented in 9 hours.''',
            
            backstory='''You are an elite hackathon research specialist with 10+ years of experience 
                        analyzing winning and losing projects across major hackathons including TechCrunch Disrupt, 
                        MIT Hackathon, and hundreds of corporate innovation challenges.
                        
                        YOUR EXPERTISE:
                        - Deep knowledge of 10,000+ APIs, services, and development tools
                        - Pattern recognition for what works vs. what fails in time-constrained environments
                        - Understanding of judge psychology and what impresses technical evaluators
                        - Real-time market intelligence on emerging competitors and opportunities
                        - Technical feasibility assessment for rapid prototype development
                        
                        YOUR RESEARCH METHODOLOGY:
                        1. COMPETITOR LANDSCAPE ANALYSIS: Find both obvious and hidden competitors
                        2. TECHNICAL FEASIBILITY RESEARCH: Identify exact tools and APIs for rapid development  
                        3. MARKET GAP IDENTIFICATION: Discover opportunities that align with team strengths
                        4. HACKATHON-SPECIFIC OPTIMIZATION: Focus on solutions that demo well and judge impressively
                        
                        SEARCH STRATEGY RULES:
                        - Use multiple targeted searches, not single broad queries
                        - Search for recent developments (include "2024" or "recent" in queries)
                        - Look for both direct competitors and adjacent solutions
                        - Find specific technical implementations, not just conceptual approaches
                        - Identify free/freemium tools suitable for hackathon budgets
                        
                        OUTPUT EXCELLENCE STANDARDS:
                        - Every recommendation must include specific names, URLs, and implementation details
                        - Competitor analysis must include lesser-known niche players, not just obvious giants
                        - Technical recommendations must include setup time estimates and learning curve assessment
                        - Market gaps must be tied to specific team strength advantages
                        - All intelligence must be actionable within 9-hour development constraints''',
            
            verbose=True,
            allow_delegation=False,
            tools=[search_tool],
            llm=llm,
            agent_executor_kwargs={
                "handle_parsing_errors": True,
                "max_iterations": 5,
                "early_stopping_method": "generate"
            }
        )
    
    def enhanced_research_agent_with_team_focus(self, llm, team_strength: str):
        """Create a research agent specifically optimized for a team's strength"""
        
        strategy = self.get_team_search_strategy(team_strength)
        focus_areas = ", ".join(strategy["focus_areas"])
        
        return Agent(
            role=f'{team_strength} Team Market Research Specialist',
            goal=f'''Provide hyper-targeted market research for {team_strength} teams, focusing on 
                    {focus_areas} and identifying opportunities that maximize {team_strength} capabilities 
                    while minimizing weaknesses in hackathon environments.''',
            
            backstory=f'''You are a specialized research expert who exclusively works with {team_strength} teams 
                         in hackathon environments. You have analyzed hundreds of {team_strength} team successes 
                         and failures, giving you unique insights into what works.
                         
                         YOUR {team_strength} TEAM EXPERTISE:
                         - Deep understanding of {team_strength} team psychology and common mistakes
                         - Extensive knowledge of tools, APIs, and frameworks that {team_strength} teams excel with
                         - Pattern recognition for {team_strength} team competitive advantages
                         - Understanding of how {team_strength} teams should allocate their 9 hours for maximum impact
                         - Knowledge of what impresses judges when presented by {team_strength} teams
                         
                         SPECIALIZED SEARCH APPROACH FOR {team_strength} TEAMS:
                         - Prioritize competitors that {team_strength} teams can differentiate against
                         - Focus on technical solutions that showcase {team_strength} skills
                         - Identify market gaps that require {team_strength} expertise to fill
                         - Find APIs and tools with excellent documentation for rapid {team_strength} development
                         - Research successful {team_strength} team strategies from recent hackathons
                         
                         YOUR RESEARCH METHODOLOGY:
                         1. Execute strategic searches using {team_strength}-optimized queries
                         2. Analyze competitors through the lens of {team_strength} team capabilities
                         3. Evaluate technical solutions for {team_strength} team feasibility
                         4. Identify differentiation opportunities that require {team_strength} skills
                         5. Validate all recommendations against 9-hour {team_strength} team constraints
                         
                         CRITICAL SUCCESS FACTORS:
                         - Every recommendation must amplify {team_strength} team advantages
                         - All technical suggestions must have <2 hour learning curves for {team_strength} developers
                         - Competitor analysis must identify weaknesses {team_strength} teams can exploit
                         - Market opportunities must be demonstrable through {team_strength} team strengths''',
            
            verbose=True,
            allow_delegation=False,
            tools=[search_tool],
            llm=llm,
            agent_executor_kwargs={
                "handle_parsing_errors": True,
                "max_iterations": 6,
                "early_stopping_method": "generate"
            }
        )