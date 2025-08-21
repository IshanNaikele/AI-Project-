# backend/agents/critical_agent.py
from crewai import Agent
from crewai_tools import SerperDevTool
from typing import Dict, List

# Enhanced search tool for risk analysis
search_tool = SerperDevTool(
    n_results=6,
    country="us",
    locale="en", 
    timeout=10
)

class CriticalAgents:
    """Enhanced critical analysis agents with hackathon failure prediction"""
    
    @staticmethod
    def get_team_risk_patterns(team_strength: str) -> Dict[str, List[str]]:
        """Get common failure patterns for different team types"""
        patterns = {
            "Frontend": {
                "scope_creep_risks": [
                    "Building custom backend APIs instead of using existing services",
                    "Implementing complex algorithms in JavaScript",
                    "Creating custom authentication systems",
                    "Building mobile-responsive design from scratch"
                ],
                "technical_risks": [
                    "API rate limiting during demo",
                    "Third-party service outages",
                    "Browser compatibility issues",
                    "Network connectivity problems"
                ],
                "demo_risks": [
                    "Backend services not working during presentation",
                    "UI breaking on different screen sizes",
                    "Slow API responses making demo lag",
                    "JavaScript errors in front of judges"
                ],
                "search_queries": [
                    "frontend development common failures",
                    "API integration challenges hackathon",
                    "JavaScript demo failures",
                    "UI/UX presentation problems"
                ]
            },
            "Backend": {
                "scope_creep_risks": [
                    "Building complex UI instead of focusing on API excellence",
                    "Implementing advanced security features",
                    "Creating scalable infrastructure for hackathon demo",
                    "Building custom deployment pipelines"
                ],
                "technical_risks": [
                    "Database connection issues",
                    "Server deployment complications", 
                    "API endpoint reliability problems",
                    "Data processing bottlenecks"
                ],
                "demo_risks": [
                    "Server crashing during demo",
                    "Database queries being too slow",
                    "API endpoints returning errors",
                    "No visual interface for judges to understand"
                ],
                "search_queries": [
                    "backend development hackathon pitfalls",
                    "API demo presentation challenges",
                    "database setup time hackathon",
                    "server deployment issues"
                ]
            },
            "AI/ML": {
                "scope_creep_risks": [
                    "Training models from scratch instead of fine-tuning",
                    "Building production-grade ML pipelines",
                    "Implementing complex data preprocessing",
                    "Creating sophisticated model evaluation systems"
                ],
                "technical_risks": [
                    "Model training taking longer than expected",
                    "Insufficient training data quality",
                    "Model performance being inconsistent",
                    "Integration between model and interface failing"
                ],
                "demo_risks": [
                    "Model giving poor results during live demo",
                    "Training data being inappropriate or biased",
                    "Model inference being too slow for real-time demo",
                    "Technical complexity being too hard to explain"
                ],
                "search_queries": [
                    "machine learning hackathon common mistakes",
                    "AI model demo failures",
                    "ML project time estimation errors",
                    "AI hackathon presentation challenges"
                ]
            },
            "Full-Stack": {
                "scope_creep_risks": [
                    "Trying to perfect both frontend and backend",
                    "Implementing too many features across the stack",
                    "Building complex integrations between components",
                    "Adding unnecessary third-party services"
                ],
                "technical_risks": [
                    "Integration complexity between frontend and backend",
                    "Time management across multiple technology areas",
                    "Debugging issues across the entire stack",
                    "Deployment complications for full applications"
                ],
                "demo_risks": [
                    "One part of the stack failing and breaking everything",
                    "Integration issues appearing only during demo",
                    "Complex demo flow being hard to follow",
                    "Technical debt making the system unreliable"
                ],
                "search_queries": [
                    "full stack development hackathon challenges",
                    "integration problems rapid development",
                    "full stack demo presentation issues",
                    "hackathon time management full stack"
                ]
            }
        }
        return patterns.get(team_strength, patterns["Full-Stack"])

    def critical_agent(self, llm):
        return Agent(
            role='Hackathon Risk Assessment Expert',
            goal='''Identify critical risks that could derail hackathon project success and provide 
                   specific, actionable mitigation strategies. Focus on scope creep, technical debt, 
                   and demo failure scenarios with brutal honesty.''',
            
            backstory='''You are a veteran hackathon mentor with 15+ years of experience watching teams fail 
                        due to predictable, preventable mistakes. You have personally witnessed over 1,000 
                        hackathon presentations and have developed an uncanny ability to predict failure modes.
                        
                        YOUR TRACK RECORD:
                        - Mentored 500+ hackathon teams with 73% success rate improvement
                        - Identified patterns in why technically strong teams lose to simpler, well-executed projects
                        - Developed frameworks for risk assessment in time-constrained development environments
                        - Expert in the psychology of hackathon teams and their common blind spots
                        
                        YOUR ANALYTICAL APPROACH:
                        1. SCOPE CREEP DETECTION: Identify features that consume disproportionate time
                        2. TECHNICAL DEBT PREDICTION: Find integration points that will cause problems
                        3. DEMO FAILURE ANALYSIS: Predict what will go wrong during live presentations
                        4. MARKET REALITY CHECK: Assess whether the value proposition actually holds up
                        5. COMPETITIVE THREAT EVALUATION: Determine if existing solutions make this obsolete
                        
                        YOUR PHILOSOPHY:
                        - "Perfect is the enemy of good" in hackathon environments
                        - Better to build something simple that works than something complex that doesn't
                        - Demo day failures are usually predictable and preventable
                        - Teams consistently underestimate integration time and overestimate development speed
                        - The best hackathon projects solve real problems with obvious solutions
                        
                        RISK ASSESSMENT METHODOLOGY:
                        - Search for similar project failures and success stories
                        - Analyze technical complexity vs. available time constraints
                        - Evaluate market adoption barriers and competitive responses
                        - Predict specific demo failure scenarios and probability
                        - Assess team capability vs. project requirements mismatch
                        
                        OUTPUT STANDARDS:
                        - Every risk must be specific, not generic (e.g., "API rate limits during demo" not "technical issues")
                        - Each risk must include probability assessment and specific mitigation strategy
                        - Focus on risks that have high impact and reasonable probability of occurring
                        - Provide backup plans for when primary approaches fail
                        - Be brutally honest - teams need reality, not encouragement''',
            
            verbose=True,
            allow_delegation=False,
            tools=[search_tool],
            llm=llm,
            agent_executor_kwargs={
                "handle_parsing_errors": True,
                "max_iterations": 4,
                "early_stopping_method": "generate"
            }
        )
    
    def enhanced_critical_agent_with_team_focus(self, llm, team_strength: str):
        """Create a critical agent specifically tuned to team strength failure patterns"""
        
        risk_patterns = self.get_team_risk_patterns(team_strength)
        common_failures = ", ".join(risk_patterns["scope_creep_risks"][:2])
        
        return Agent(
            role=f'{team_strength} Team Risk Assessment Specialist',
            goal=f'''Identify and prevent the most common failure modes that specifically plague 
                    {team_strength} teams in hackathon environments. Provide team-specific risk 
                    mitigation strategies based on {team_strength} team behavioral patterns.''',
            
            backstory=f'''You are the world's leading expert on {team_strength} team failures in hackathon 
                         environments. You have analyzed hundreds of {team_strength} team projects and 
                         identified the specific patterns that lead to their success or failure.
                         
                         YOUR {team_strength} TEAM EXPERTISE:
                         - Documented failure patterns across 200+ {team_strength} hackathon teams
                         - Deep understanding of {team_strength} team psychology and common blind spots
                         - Specialized knowledge of technical risks that {team_strength} teams underestimate
                         - Expertise in {team_strength} team time management and scope estimation errors
                         - Pattern recognition for {team_strength} team demo failure scenarios
                         
                         COMMON {team_strength} TEAM FAILURE PATTERNS YOU'VE OBSERVED:
                         {common_failures}
                         
                         YOUR SPECIALIZED RISK ASSESSMENT APPROACH:
                         - Focus on risks that {team_strength} teams consistently underestimate
                         - Identify scope creep patterns specific to {team_strength} team strengths
                         - Predict technical integration issues common to {team_strength} projects
                         - Analyze demo failure scenarios that {team_strength} teams experience
                         - Evaluate market risks through the lens of {team_strength} team capabilities
                         
                         RISK PREDICTION METHODOLOGY:
                         1. Search for recent {team_strength} team hackathon failures and lessons learned
                         2. Analyze technical complexity vs. {team_strength} team typical capabilities
                         3. Evaluate scope realism based on {team_strength} team time allocation patterns
                         4. Predict demo risks specific to {team_strength} team presentation styles
                         5. Assess competitive threats that {team_strength} teams often miss
                         
                         YOUR BRUTAL HONESTY MANDATE:
                         - Call out unrealistic expectations that {team_strength} teams commonly have
                         - Identify the "easy" tasks that actually consume enormous time for {team_strength} teams
                         - Predict the specific moment in development when {team_strength} teams usually hit walls
                         - Force consideration of backup plans for when {team_strength} team strengths aren't enough
                         - Challenge assumptions that {team_strength} teams make about market adoption''',
            
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