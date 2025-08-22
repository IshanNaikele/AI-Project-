# backend/tasks.py
from crewai import Task
from textwrap import dedent
from typing import Dict, Any

class ResearchTasks:
    """Personalized research tasks optimized for team strengths and hackathon constraints"""
    
    @staticmethod
    def get_team_constraints(team_strength: str) -> Dict[str, str]:
        """Team-specific research focus and constraints"""
        constraints = {
            "Frontend": {
                "focus": "UI-friendly APIs, component libraries, design systems",
                "avoid": "complex ML models, backend infrastructure",
                "priority": "visual appeal, user experience, responsive design"
            },
            "Backend": {
                "focus": "data APIs, cloud services, database solutions",
                "avoid": "complex frontend frameworks, UI/UX design",
                "priority": "API performance, data processing, scalability"
            },
            "AI/ML": {
                "focus": "pre-trained models, ML APIs, data processing tools",
                "avoid": "complex UI frameworks, extensive backend setup",
                "priority": "model accuracy, data insights, intelligent features"
            },
            "Full-Stack": {
                "focus": "integrated solutions, complete frameworks",
                "avoid": "over-specialization in single domain",
                "priority": "end-to-end functionality, system integration"
            }
        }
        return constraints.get(team_strength, constraints["Full-Stack"])

    def research_task(self, agent, theme, idea, team_strength, hackathon_duration):
        constraints = self.get_team_constraints(team_strength)
        
        return Task(
            description=dedent(f"""
                HACKATHON MARKET RESEARCH - {team_strength} Team Optimization
                
                Theme: '{theme}'
                Idea: '{idea}'
                Duration: {hackathon_duration} hours
                Team Focus: {constraints['priority']}
                
                **RESEARCH OBJECTIVES:**
                
                1. **COMPETITOR ANALYSIS**:
                   - 2 major competitors (established solutions)
                   - 3-4 niche/emerging solutions 
                   - Identify specific gaps a {team_strength} team can exploit
                   - Focus on: {constraints['focus']}
                
                2. **TECHNICAL RECOMMENDATIONS**:
                   - APIs/tools matching team strength: {constraints['priority']}
                   - Setup time under 1 hour total
                   - Free/freemium tiers available
                   - Backup options if primary fails
                   - Avoid: {constraints['avoid']}
                
                3. **HACKATHON OPPORTUNITIES**:
                   - 2-3 missing features across ALL competitors
                   - Quick wins demonstrable in 3-minute pitch
                   - Features showcasing {team_strength} expertise
                   - Demo-safe implementations
                
                **OUTPUT FORMAT:**
                ```
                **COMPETITOR LANDSCAPE:**
                Major Players: [Names + core features + gaps]
                Niche Solutions: [Specialized tools + focus areas]
                Market Gap for {team_strength}: [Specific opportunity]
                
                **TECH STACK RECOMMENDATIONS:**
                Primary Stack: [Specific tools/APIs with URLs]
                Setup Time: [Under 1 hour breakdown]
                Backup Plan: [Alternative if primary fails]
                Demo Considerations: [Rate limits, costs, reliability]
                
                **HACKATHON ADVANTAGE:**
                Unique Features: [2-3 differentiators]
                {team_strength} Edge: [How team strength creates advantage]
                Pitch-Ready Elements: [Demo-worthy capabilities]
                ```
            """),
            expected_output=f"Detailed research report with competitor analysis and technical recommendations optimized for {team_strength} team in {hackathon_duration}-hour hackathon",
            agent=agent,
        )

class CriticalTasks:
    """Risk analysis and failure prediction for hackathon teams"""
    
    @staticmethod
    def get_team_risks(team_strength: str) -> Dict[str, str]:
        """Team-specific risk profiles and failure modes"""
        risks = {
            "Frontend": {
                "scope_trap": "building custom backend logic or complex algorithms",
                "demo_risk": "backend failures, API outages during presentation",
                "time_sink": "perfect pixel designs, complex animations"
            },
            "Backend": {
                "scope_trap": "complex UI design, mobile responsiveness",  
                "demo_risk": "no visual interface, hard to show functionality",
                "time_sink": "database optimization, deployment complexity"
            },
            "AI/ML": {
                "scope_trap": "production deployment, scalable infrastructure",
                "demo_risk": "model not performing consistently live",
                "time_sink": "model training, data preprocessing"
            },
            "Full-Stack": {
                "scope_trap": "perfecting both frontend and backend equally",
                "demo_risk": "integration failures between components", 
                "time_sink": "attempting enterprise-level features"
            }
        }
        return risks.get(team_strength, risks["Full-Stack"])

    def critical_task(self, agent, research_report, idea, team_strength, hackathon_duration):
        risks = self.get_team_risks(team_strength)
        
        return Task(
            description=dedent(f"""
                HACKATHON REALITY CHECK - {team_strength} Team Risk Analysis
                
                Research Context: {research_report}
                Original Idea: {idea}
                Duration: {hackathon_duration} hours
                
                **CRITICAL FAILURE ANALYSIS:**
                
                1. **SCOPE CREEP RISKS**:
                   - Features consuming >{hackathon_duration//4} hours each
                   - {team_strength} trap: {risks['scope_trap']}
                   - Features to CUT immediately
                   - Time sinks: {risks['time_sink']}
                
                2. **TECHNICAL & DEMO RISKS**:
                   - API reliability during demo
                   - Integration failure points
                   - Demo risk: {risks['demo_risk']}
                   - Backup plans for technical failures
                
                3. **COMPETITIVE DIFFERENTIATION**:
                   - Why existing solutions might already win
                   - "How is this different?" - judge question prep
                   - Value proposition clarity
                
                4. **MARKET VIABILITY CONCERNS**:
                   - User switching costs from current solutions
                   - "Nice to have" vs "must have" problem
                   - Commercial adoption barriers
                
                **OUTPUT FORMAT:**
                ```
                **🚨 SCOPE KILLERS:**
                Cut These Features: [Specific time-wasters for {team_strength}]
                Team Trap: [What {team_strength} teams always over-build]
                
                **⚡ TECHNICAL RISKS:**
                API Vulnerabilities: [Unreliable services + backups]
                Demo Disasters: [What breaks under pressure]
                
                **🎯 DIFFERENTIATION GAPS:**
                Judge Concerns: [Why they might say "this exists"]
                Value Prop Issues: [Unclear unique benefits]
                
                **🔧 MITIGATION PLAN:**
                Minimum Viable Demo: [Guaranteed working version]
                Technical Backup: [When main approach fails]
                Pitch Recovery: [Presenting when demo breaks]
                ```
                
                BE BRUTALLY HONEST - identify every failure mode and force backup planning.
            """),
            expected_output=f"Honest risk assessment with failure scenarios and mitigation strategies for {team_strength} team",
            agent=agent,
        )

class SolutionArchitectTasks:
    """MVP architect that creates viable, differentiated solutions"""
    
    @staticmethod
    def get_architecture_patterns(team_strength: str) -> Dict[str, str]:
        """Architecture patterns optimized for each team type"""
        patterns = {
            "Frontend": {
                "pattern": "Component-Based UI with Mock Backend",
                "focus": "responsive design and smooth interactions",
                "stack": "React/Vue + Tailwind + Mock APIs + JSON Server",
                "innovation_angle": "superior UX/UI design and user engagement",
                "wow_factor": "stunning visual design with smooth animations"
            },
            "Backend": {
                "pattern": "API-First Architecture with Simple Frontend",
                "focus": "robust APIs and data processing",
                "stack": "FastAPI + PostgreSQL + Redis + Basic Templates",
                "innovation_angle": "high-performance data processing and scalable architecture",
                "wow_factor": "lightning-fast API responses and real-time data handling"
            },
            "AI/ML": {
                "pattern": "Model-as-Service with Streamlit Interface",
                "focus": "AI capabilities and data insights",
                "stack": "Python ML + Hugging Face + FastAPI + Streamlit",
                "innovation_angle": "intelligent automation and predictive capabilities",
                "wow_factor": "AI making smart decisions visible in real-time"
            },
            "Full-Stack": {
                "pattern": "Layered Full-Stack with Balanced Components",
                "focus": "complete user journey and integration",
                "stack": "MERN/MEAN + Database + Authentication + Cloud Deploy",
                "innovation_angle": "seamless end-to-end integration and user experience",
                "wow_factor": "complete working system that handles entire user flow"
            }
        }
        return patterns.get(team_strength, patterns["Full-Stack"])

    @staticmethod
    def get_feasibility_framework(hackathon_duration: int, team_strength: str) -> Dict[str, Any]:
        """Feasibility assessment framework based on time and team"""
        frameworks = {
            "time_allocation": {
                8: {"core": 4, "features": 2, "polish": 2},
                24: {"core": 12, "features": 8, "polish": 4}, 
                48: {"core": 20, "features": 18, "polish": 10}
            },
            "complexity_limits": {
                "Frontend": {"avoid": "custom backend logic", "max_apis": 3},
                "Backend": {"avoid": "complex UI frameworks", "max_endpoints": 8},
                "AI/ML": {"avoid": "custom training", "max_models": 2},
                "Full-Stack": {"avoid": "enterprise features", "max_components": 6}
            }
        }
        
        # Get closest time allocation
        closest_time = min(frameworks["time_allocation"].keys(), 
                          key=lambda x: abs(x - hackathon_duration))
        
        return {
            "time_budget": frameworks["time_allocation"][closest_time],
            "constraints": frameworks["complexity_limits"].get(team_strength, 
                          frameworks["complexity_limits"]["Full-Stack"])
        }

    def solution_architect_task(self, agent, idea, research_result, critical_result, team_strength, hackathon_duration):
        arch = self.get_architecture_patterns(team_strength)
        feasibility = self.get_feasibility_framework(hackathon_duration, team_strength)
        
        return Task(
            description=dedent(f"""
                COMPREHENSIVE MVP SOLUTION ARCHITECTURE
                
                Original Idea: "{idea}"
                Research Context: {research_result}
                Critical Analysis: {critical_result}
                Team Strength: {team_strength}
                Hackathon Duration: {hackathon_duration} hours
                
                **CORE ARCHITECT RESPONSIBILITIES:**
                
                1. **REAL-WORLD PROBLEM DEFINITION:**
                   - Clearly articulate the specific problem being solved
                   - Quantify the problem impact (who, how many, how often)
                   - Connect to hackathon theme meaningfully
                   - Ensure problem is significant enough to matter
                
                2. **INNOVATION ANALYSIS:**
                   - Identify the core innovation beyond existing solutions
                   - Leverage {team_strength} strengths for unique approach: {arch['innovation_angle']}
                   - Define technical or methodological breakthrough
                   - Explain why this approach hasn't been done before
                
                3. **TARGET AUDIENCE SPECIFICATION:**
                   - Primary users (demographics, needs, pain points)
                   - Secondary markets and expansion opportunities
                   - Market size and accessibility for {team_strength} team
                   - User acquisition strategy within team capabilities
                
                4. **FEASIBILITY VALIDATION:**
                   - Time budget: Core ({feasibility['time_budget']['core']}h), Features ({feasibility['time_budget']['features']}h), Polish ({feasibility['time_budget']['polish']}h)
                   - Technical constraints: {feasibility['constraints']}
                   - Resource requirements vs team skills
                   - Risk mitigation for time/scope overruns
                   - Clear go/no-go decision framework
                
                5. **WOW FACTOR ENGINEERING:**
                   - Define the "holy shit" moment for judges/users
                   - {team_strength} team advantage: {arch['wow_factor']}
                   - Demo-ready features that showcase innovation
                   - Emotional impact and memorable experience design
                
                6. **COMPETITIVE DIFFERENTIATION:**
                   - Specific advantages over existing solutions from research
                   - Unique value proposition only {team_strength} team can deliver
                   - Defensible moats (technical, user experience, market positioning)
                   - Clear answer to "why can't competitors copy this?"
                
                **ARCHITECTURE CONSTRAINTS:**
                - Must use {team_strength} strengths prominently
                - Recommended pattern: {arch['pattern']}
                - Tech stack: {arch['stack']}
                - Avoid: {feasibility['constraints']['avoid']}
                - Maximum complexity limits applied
                
                **DELIVERABLE REQUIREMENTS:**
                Create a complete MVP specification that addresses all 6 core questions while ensuring the solution is:
                - Buildable by {team_strength} team in {hackathon_duration} hours
                - Clearly differentiated from competitors
                - Demo-ready with high wow factor
                - Commercially viable with clear target market
                - Technically feasible with specific implementation plan
            """),
            expected_output=dedent(f"""
                # MVP SOLUTION ARCHITECTURE - {team_strength} Team
                
                ## 🎯 REAL-WORLD PROBLEM
                **Problem Statement**: [Specific, quantified problem]
                **Impact Scale**: [Who affected, frequency, severity]
                **Current Pain Points**: [What users struggle with today]
                **Market Validation**: [Evidence problem matters]
                
                ## 💡 CORE INNOVATION
                **Innovation Thesis**: [What's genuinely new/different]
                **Technical Breakthrough**: [Leveraging {arch['innovation_angle']}]
                **Unique Approach**: [Why {team_strength} team can do this]
                **Competitive Moat**: [Why competitors can't easily copy]
                
                ## 🎯 TARGET AUDIENCE
                **Primary Users**: [Demographics, needs, behaviors]
                **Market Size**: [Addressable market scope]
                **User Acquisition**: [How to reach them with {team_strength} skills]
                **Expansion Path**: [Secondary markets and growth]
                
                ## ⚡ FEASIBILITY ASSESSMENT
                **Time Breakdown**:
                - Core Features ({feasibility['time_budget']['core']}h): [Essential functionality]
                - Additional Features ({feasibility['time_budget']['features']}h): [Nice-to-have]
                - Polish & Demo Prep ({feasibility['time_budget']['polish']}h): [Final touches]
                
                **Technical Feasibility**: 
                - Stack: {arch['stack']}
                - Constraints: {feasibility['constraints']}
                - Risk Factors: [What could go wrong + mitigation]
                
                **GO/NO-GO Decision**: ✅ FEASIBLE / ❌ NEEDS SCOPE REDUCTION
                
                ## 🚀 WOW FACTOR DESIGN
                **The Magic Moment**: [Specific feature that amazes users]
                **{team_strength} Showcase**: {arch['wow_factor']}
                **Demo Hook**: [First 30 seconds that grab attention]
                **Emotional Impact**: [How users will feel using this]
                
                ## 🏆 COMPETITIVE DIFFERENTIATION
                **Unique Value Prop**: [What only we can deliver]
                **Advantages Over Competitors**:
                - vs Major Players: [How we're different from big solutions]
                - vs Niche Solutions: [Our advantage over smaller competitors]
                **{team_strength} Edge**: [Why our team type wins here]
                **Defensibility**: [Why this advantage is sustainable]
                
                ## 🏗️ TECHNICAL ARCHITECTURE
                **System Design**: {arch['pattern']}
                **Core Components**: [3-4 main system parts]
                **Data Flow**: [How information moves through system]
                **API Strategy**: [External integrations and interfaces]
                
                ## 📋 IMPLEMENTATION ROADMAP
                **Phase 1 - Foundation**: [Hours 0-{feasibility['time_budget']['core']}]
                **Phase 2 - Features**: [Hours {feasibility['time_budget']['core']}-{feasibility['time_budget']['core'] + feasibility['time_budget']['features']}]
                **Phase 3 - Polish**: [Final {feasibility['time_budget']['polish']} hours]
                
                **Team Task Distribution**: [Specific roles for {team_strength} team]
                **Demo Preparation**: [What to build for maximum judge impact]
            """),
            agent=agent
        )

class PitchTasks:
    """Winning pitch strategy optimized for team strengths"""
    
    @staticmethod
    def get_pitch_strategies(team_strength: str) -> Dict[str, str]:
        """Pitch templates showcasing team strengths"""
        strategies = {
            "Frontend": {
                "demo_focus": "visual interface, smooth interactions, design quality",
                "wow_factor": "beautiful, intuitive interface working flawlessly",
                "credibility": "responsive design, API integration skills"
            },
            "Backend": {
                "demo_focus": "API performance, data processing, system reliability",
                "wow_factor": "fast, robust system handling complex operations", 
                "credibility": "architecture decisions, scalability planning"
            },
            "AI/ML": {
                "demo_focus": "model intelligence, real-time predictions, data insights",
                "wow_factor": "AI making visibly smart decisions live",
                "credibility": "model selection, evaluation metrics, data pipeline"
            },
            "Full-Stack": {
                "demo_focus": "complete user journey, seamless integration",
                "wow_factor": "end-to-end application that just works",
                "credibility": "system integration, full-stack architecture"
            }
        }
        return strategies.get(team_strength, strategies["Full-Stack"])

    def pitch_task(self, agent, mvp_plan, team_strength, theme, hackathon_duration):
        strategy = self.get_pitch_strategies(team_strength)
        
        return Task(
            description=dedent(f"""
                WINNING PITCH STRATEGY - {team_strength} Team Showcase
                
                MVP Plan: {mvp_plan}
                Theme: {theme}
                Duration: {hackathon_duration} hours
                
                **PITCH OPTIMIZATION:**
                - Demo Focus: {strategy['demo_focus']}
                - Wow Factor: {strategy['wow_factor']}
                - Credibility: {strategy['credibility']}
                
                **3-MINUTE STRUCTURE:**
                
                **HOOK (0:00-0:25)**: Problem tied to {theme}
                **SOLUTION (0:25-0:45)**: Core concept + {team_strength} advantage  
                **LIVE DEMO (0:45-2:00)**: Showcase {strategy['demo_focus']}
                **CREDIBILITY (2:00-2:30)**: Technical depth + {strategy['credibility']}
                **CLOSE (2:30-3:00)**: Impact + memorable ending
                
                Create exact script with timing, demo choreography, and backup plans.
            """),
            expected_output=dedent(f"""
                # 3-Minute Pitch Script - {team_strength} Team
                
                ## 🎯 HOOK (0:00-0:25)
                [Problem question tied to {theme}]
                [Demo setup and expectation]
                
                ## 💡 SOLUTION (0:25-0:45) 
                [One-sentence concept]
                [{team_strength} advantage highlight]
                
                ## 🚀 LIVE DEMO (0:45-2:00)
                [Step-by-step user actions → system responses]
                [Narration emphasizing {strategy['demo_focus']}]
                [Wow moment showcasing {team_strength}]
                
                ## 🛠️ CREDIBILITY (2:00-2:30)
                [Tech stack mention: {strategy['credibility']}]
                [Challenge overcome]
                [Market opportunity]
                
                ## 🏆 CLOSE (2:30-3:00)
                [Impact statement]
                [Commercial viability]
                [Memorable closing line]
                
                ## 🔧 BACKUP PLAN
                [Demo failure recovery]
                [Simplified fallback version]
                
                ## 📋 Q&A PREP
                [Top 3 judge questions + answers]
            """),
            agent=agent,
        )

# Task factory for easy instantiation
class TaskFactory:
    """Factory for creating all task types with consistent parameters"""
    
    def __init__(self):
        self.research = ResearchTasks()
        self.critical = CriticalTasks()
        self.architect = SolutionArchitectTasks()
        self.pitch = PitchTasks()
    
    def create_all_tasks(self, agents_dict, theme, idea, team_strength, hackathon_duration):
        """Create complete task chain for the AI Strategist workflow"""
        
        # Research task
        research_task = self.research.research_task(
            agents_dict['research'], theme, idea, team_strength, hackathon_duration
        )
        
        # Critical analysis task  
        critical_task = self.critical.critical_task(
            agents_dict['critical'], "{research_output}", idea, team_strength, hackathon_duration
        )
        
        # Solution architect task
        architect_task = self.architect.solution_architect_task(
            agents_dict['architect'], idea, "{research_output}", 
            "{critical_output}", team_strength, hackathon_duration
        )
        
        # Pitch strategy task
        pitch_task = self.pitch.pitch_task(
            agents_dict['pitch'], "{architect_output}", team_strength, theme, hackathon_duration
        )
        
        return [research_task, critical_task, architect_task, pitch_task]

# Export all classes
__all__ = [
    'ResearchTasks', 'CriticalTasks', 'SolutionArchitectTasks', 
    'PitchTasks', 'TaskFactory'
]