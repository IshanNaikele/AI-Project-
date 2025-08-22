# backend/agents/solution_architect_agent.py
from crewai import Agent
from typing import Dict, List

class SolutionArchitectAgents:
    """Enhanced solution architect agents with team-specific optimization"""
    
    @staticmethod
    def get_team_architecture_patterns(team_strength: str) -> Dict[str, any]:
        """Get proven architecture patterns for different team strengths"""
        patterns = {
            "Frontend": {
                "core_pattern": "API-Consumer Architecture",
                "time_allocation": "75% UI/UX Development, 15% API Integration, 10% Setup",
                "technology_constraints": {
                    "required": ["React/Vue.js", "CSS Framework", "HTTP Client"],
                    "forbidden": ["Custom backends", "Database design", "Server deployment"],
                    "preferred_apis": ["Stripe", "OpenAI", "Google Cloud", "Firebase"],
                    "ui_frameworks": ["Tailwind CSS", "Material-UI", "Bootstrap", "Chakra UI"]
                },
                "demo_optimization": {
                    "focus": "Visual storytelling and user interaction flows",
                    "wow_factors": ["Smooth animations", "Responsive design", "Intuitive UX"],
                    "judge_appeal": "Beautiful interfaces that work flawlessly"
                },
                "success_criteria": [
                    "Interface works perfectly across devices",
                    "User flow is intuitive and demonstrates value clearly",
                    "Visual design impresses judges immediately",
                    "All interactions are smooth and responsive"
                ]
            },
            "Backend": {
                "core_pattern": "API-First Architecture", 
                "time_allocation": "80% Backend Logic, 15% API Design, 5% Basic Frontend",
                "technology_constraints": {
                    "required": ["FastAPI/Flask", "Database", "API Documentation"],
                    "forbidden": ["Complex frontends", "Mobile apps", "Advanced UI frameworks"],
                    "preferred_databases": ["PostgreSQL", "SQLite", "Redis"],
                    "api_frameworks": ["FastAPI", "Flask-RESTful", "Django REST"]
                },
                "demo_optimization": {
                    "focus": "Data processing speed and system reliability",
                    "wow_factors": ["Fast API responses", "Complex data handling", "System scalability"],
                    "judge_appeal": "Robust systems that handle complex operations efficiently"
                },
                "success_criteria": [
                    "APIs respond quickly and reliably", 
                    "Data processing demonstrates technical sophistication",
                    "System architecture is clean and scalable",
                    "Backend logic solves complex problems elegantly"
                ]
            },
            "AI/ML": {
                "core_pattern": "Model-Centric Architecture",
                "time_allocation": "60% Model Development, 25% Data Pipeline, 15% Simple Interface",
                "technology_constraints": {
                    "required": ["PyTorch/TensorFlow", "Jupyter Notebooks", "Data Processing"],
                    "forbidden": ["Complex web frameworks", "Advanced UI design", "Mobile development"],
                    "preferred_models": ["Hugging Face Transformers", "OpenAI API", "Pre-trained models"],
                    "interfaces": ["Streamlit", "Gradio", "Jupyter Widgets", "Simple Flask"]
                },
                "demo_optimization": {
                    "focus": "Algorithm intelligence and model performance",
                    "wow_factors": ["Smart predictions", "Real-time analysis", "Data insights"],
                    "judge_appeal": "AI making visibly intelligent decisions"
                },
                "success_criteria": [
                    "Model performs accurately on live data",
                    "AI decision-making is transparent and impressive",
                    "Data processing demonstrates sophisticated understanding",
                    "Algorithm provides clear competitive advantage"
                ]
            },
            "Full-Stack": {
                "core_pattern": "Integrated Full-Application Architecture",
                "time_allocation": "45% Frontend, 45% Backend, 10% Integration",
                "technology_constraints": {
                    "required": ["Full-stack framework", "Database", "Frontend framework"],
                    "forbidden": ["Experimental technologies", "Multiple unrelated services"],
                    "preferred_stacks": ["MERN", "MEAN", "Django+React", "FastAPI+Vue"],
                    "integration_tools": ["Docker", "Vercel", "Heroku", "Netlify"]
                },
                "demo_optimization": {
                    "focus": "Complete user journey and system integration",
                    "wow_factors": ["Seamless user experience", "End-to-end functionality", "System cohesion"],
                    "judge_appeal": "Complete, working applications that solve problems end-to-end"
                },
                "success_criteria": [
                    "All system components work together seamlessly",
                    "User can complete full workflows without issues",
                    "Application demonstrates clear business value",
                    "Technical architecture supports future scaling"
                ]
            }
        }
        return patterns.get(team_strength, patterns["Full-Stack"])

    @staticmethod
    def get_winning_mvp_templates(team_strength: str) -> List[Dict[str, str]]:
        """Get proven MVP templates that have won hackathons for each team type"""
        templates = {
            "Frontend": [
                {
                    "template": "API Mashup Dashboard",
                    "description": "Beautiful interface combining multiple APIs into unified experience",
                    "example": "Personal finance dashboard using Plaid + OpenAI for insights",
                    "winning_factor": "Superior UX on existing data sources"
                },
                {
                    "template": "Interactive Data Visualization",
                    "description": "Compelling visual stories from complex datasets",
                    "example": "Climate data visualization with predictive modeling display",
                    "winning_factor": "Makes complex data accessible and beautiful"
                }
            ],
            "Backend": [
                {
                    "template": "Smart API Gateway",
                    "description": "Intelligent routing and processing layer for existing services",
                    "example": "Multi-vendor payment processing with fraud detection",
                    "winning_factor": "Sophisticated business logic and reliability"
                },
                {
                    "template": "Real-time Data Pipeline",
                    "description": "High-performance data processing and analytics engine",
                    "example": "Social media sentiment analysis with trend prediction",
                    "winning_factor": "Technical complexity and processing speed"
                }
            ],
            "AI/ML": [
                {
                    "template": "Intelligent Classification System",
                    "description": "AI model that categorizes and makes predictions on real data",
                    "example": "Medical image analysis for early disease detection",
                    "winning_factor": "AI expertise solving real problems"
                },
                {
                    "template": "Personalization Engine",
                    "description": "ML system that adapts to user behavior and preferences",
                    "example": "Learning assistant that adapts to individual study patterns",
                    "winning_factor": "Sophisticated personalization algorithms"
                }
            ],
            "Full-Stack": [
                {
                    "template": "Complete Platform Solution",
                    "description": "End-to-end application solving a specific market need",
                    "example": "Freelancer matching platform with integrated payments",
                    "winning_factor": "Complete solution ready for real users"
                }
            ]
        }
        return templates.get(team_strength, templates["Full-Stack"])

    def solution_architect_agent(self, llm):
        # NOTE: This method is not used in your current setup with team_strength
        # but is kept for reference as it was in the original code.
        return Agent(
            role='Hackathon MVP Strategist',
            goal='''Design ruthlessly scoped MVPs that maximize team strengths, ensure demo success, 
                    and create obvious competitive advantages within hackathon time constraints.''',
            
            backstory='''You are a legendary hackathon strategist with an unmatched track record of turning 
                         good ideas into winning implementations. Over 12 years, you have architected 
                         200+ winning hackathon projects across every major event.
                         
                         YOUR CORE PHILOSOPHY:
                         - SCOPE IS EVERYTHING: One perfect feature beats three mediocre ones
                         - PLAY TO STRENGTHS: Frontend teams showcase UI, Backend teams showcase logic, AI teams showcase intelligence
                         - API-FIRST MINDSET: Use existing services for non-differentiating functionality 
                         - DEMO-DRIVEN DESIGN: Every architectural decision optimizes for 3-minute live presentations
                         - TECHNICAL PRAGMATISM: Boring, reliable technology beats exciting, experimental technology
                         
                         YOUR WINNING FORMULA:
                         1. TEAM STRENGTH AMPLIFICATION: Identify what the team does better than anyone
                         2. RUTHLESS SCOPE REDUCTION: Cut everything that doesn't showcase core strength
                         3. API LEVERAGE STRATEGY: Use existing solutions for everything except differentiation
                         4. DEMO OPTIMIZATION: Design features that create "wow moments" in presentations
                         5. FALLBACK PLANNING: Always have Plan B when Plan A fails
                         
                         YOUR ARCHITECTURAL EXPERTISE:
                         - Deep knowledge of which technology combinations work reliably under pressure
                         - Understanding of setup times, learning curves, and integration complexity for all major frameworks
                         - Pattern recognition for architecture decisions that lead to demo day disasters
                         - Insight into judge psychology and what impresses technical evaluators
                         - Experience with rapid prototyping techniques that maximize development speed
                         
                         YOUR TRACK RECORD INCLUDES:
                         - 73% win rate for teams following your architectural recommendations
                         - Zero demo failures in 200+ architected projects
                         - Average development time reduction of 40% through smart technology choices
                         - Consistent pattern of turning good ideas into obviously superior implementations
                         
                         ARCHITECTURAL DECISION FRAMEWORK:
                         - Every technology choice must have <2 hour learning curve for the team
                         - Every feature must be demonstrable in <30 seconds during pitch
                         - Every integration point must have documented examples and community support
                         - Every architectural decision must amplify team strengths while minimizing weaknesses
                         - Every MVP must have obvious commercial value beyond the hackathon environment''',
            
            verbose=True,
            allow_delegation=False,
            llm=llm
        )
    
    # <-- MODIFICATION: ADDED `hackathon_duration` PARAMETER
    def enhanced_solution_architect_with_team_focus(self, llm, team_strength: str, hackathon_duration: int):
        """Create solution architect specifically optimized for team strength"""
        
        architecture_pattern = self.get_team_architecture_patterns(team_strength)
        mvp_templates = self.get_winning_mvp_templates(team_strength)
        
        return Agent(
            role=f'{team_strength} Team MVP Architecture Specialist',
            # <-- MODIFICATION: GOAL NOW INCLUDES TIME CONSTRAINT
            goal=f'''Design MVPs that are perfectly optimized for {team_strength} teams, can be completed
                    within a strict {hackathon_duration}-hour time limit, and use proven architectural patterns 
                    that showcase {team_strength} expertise while ensuring reliable demo performance and 
                    obvious competitive advantages.''',
            
            # <-- MODIFICATION: BACKSTORY NOW INCLUDES TIME-BASED RULES AND PHILOSOPHY
            backstory=f'''You are the world's leading expert in {team_strength} team hackathon architecture, 
                         with exclusive focus on maximizing {team_strength} team success rates. You have 
                         architected 100+ winning projects specifically for {team_strength} teams.
                         
                         YOUR {team_strength} TEAM SPECIALIZATION:
                         - Deep understanding of {team_strength} team psychology, strengths, and blind spots
                         - Extensive experience with technology stacks that {team_strength} teams excel with
                         - Pattern recognition for architectural decisions that amplify {team_strength} advantages
                         - Knowledge of common {team_strength} team mistakes and how to prevent them
                         - Insight into how judges evaluate projects presented by {team_strength} teams
                         
                         PROVEN {team_strength} ARCHITECTURE PATTERN:
                         Core Pattern: {architecture_pattern['core_pattern']}
                         Time Allocation: {architecture_pattern['time_allocation']}
                         Demo Focus: {architecture_pattern['demo_optimization']['focus']}
                         Success Metric: {architecture_pattern['success_criteria'][0]}
                         
                         YOUR {team_strength} TEAM METHODOLOGY:
                         1. STRENGTH AMPLIFICATION: Design architecture that makes {team_strength} skills the obvious differentiator
                         2. WEAKNESS MITIGATION: Use APIs and services to handle areas where {team_strength} teams struggle
                         3. TECHNOLOGY SELECTION: Choose from proven {team_strength} team technology stacks
                         4. DEMO OPTIMIZATION: Ensure architecture creates impressive {team_strength} team presentations
                         5. RISK MANAGEMENT: Plan for common {team_strength} team failure scenarios
                         
                         WINNING MVP TEMPLATES FOR {team_strength} TEAMS:
                         {[template['template'] + ': ' + template['winning_factor'] for template in mvp_templates[:2]]}
                         
                         YOUR ARCHITECTURAL CONSTRAINTS:
                         Required Technologies: {architecture_pattern['technology_constraints']['required']}
                         Forbidden Approaches: {architecture_pattern['technology_constraints']['forbidden']}
                         
                         # <-- MODIFICATION: NEW SECTION FOR TIME-BASED PRIORITIZATION
                         TIME-BASED PRIORITIZATION RULES FOR {hackathon_duration} HOURS:
                         - Any plan must be realistically completed and deployed for demo within the {hackathon_duration} hour deadline.
                         - Allocate at least 25% of the total time for unexpected bugs, deployment issues, and final demo prep.
                         - If {hackathon_duration} is less than 12 hours, **FORBID** any technology with a non-trivial setup or learning curve (e.g., complex frameworks like Django or Spring).
                         - Prioritize using technologies that can be deployed in under 15 minutes (e.g., Vercel, Netlify, simple Docker containers).
                         - If a feature takes more than {hackathon_duration / 2} hours to build, it must be scoped down or cut entirely.
                         
                         DEMO SUCCESS OPTIMIZATION:
                         - Focus on showcasing: {architecture_pattern['demo_optimization']['focus']}
                         - Create wow factors: {', '.join(architecture_pattern['demo_optimization']['wow_factors'])}
                         - Judge appeal strategy: {architecture_pattern['demo_optimization']['judge_appeal']}
                         
                         YOUR RUTHLESS PRIORITIZATION MANDATE:
                         - Cut any feature that doesn't showcase {team_strength} team excellence within {hackathon_duration} hours.
                         - Eliminate any technology choice that has a learning curve that will consume a significant portion of the {hackathon_duration} hours.
                         - Remove any integration that hasn't been proven reliable by {team_strength} teams and can't be implemented quickly.
                         - Discard any architectural complexity that doesn't directly contribute to winning.
                         
                         SUCCESS MEASUREMENT:
                         Your architecture succeeds when:
                         {chr(10).join('- ' + criterion for criterion in architecture_pattern['success_criteria'])}
                         
                         Your final output MUST be a plan that is provably feasible within the {hackathon_duration}-hour time limit.''', # <-- MODIFICATION: FINAL OUTPUT REQUIREMENT
            
            verbose=True,
            allow_delegation=False,
            llm=llm
        )