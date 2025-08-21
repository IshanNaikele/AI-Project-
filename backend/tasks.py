# backend/tasks.py
from crewai import Task
import json
from typing import Dict, Any

class ResearchTasks:
    """Enhanced Research Tasks with hackathon-specific intelligence gathering"""
    
    @staticmethod
    def get_team_research_constraints(team_strength: str) -> Dict[str, Any]:
        """Get research constraints specific to team strengths"""
        constraints = {
            "Frontend": {
                "api_focus": "UI-friendly APIs, third-party services for complex logic",
                "competitor_type": "consumer-facing apps with great UX",
                "tech_priority": "React/Vue components, CSS frameworks, API integrations",
                "avoid_research": "custom ML models, complex backend infrastructure"
            },
            "Backend": {
                "api_focus": "data APIs, database services, server-side technologies",
                "competitor_type": "API-first companies, data processing platforms",
                "tech_priority": "FastAPI, databases, cloud services, data pipelines",
                "avoid_research": "complex frontend frameworks, UI/UX tools"
            },
            "AI/ML": {
                "api_focus": "ML APIs, model serving, data science tools",
                "competitor_type": "AI-powered solutions, ML platforms",
                "tech_priority": "Hugging Face, PyTorch, scikit-learn, Jupyter",
                "avoid_research": "complex UI frameworks, extensive backend architecture"
            },
            "Full-Stack": {
                "api_focus": "balanced API usage, end-to-end services",
                "competitor_type": "complete platforms, integrated solutions",
                "tech_priority": "MERN/MEAN stacks, integrated frameworks",
                "avoid_research": "highly specialized tools in single domain"
            }
        }
        return constraints.get(team_strength, constraints["Full-Stack"])

    def research_task(self, agent, theme, idea, team_strength):
        constraints = self.get_team_research_constraints(team_strength)
        
        return Task(
            description=f"""HACKATHON MARKET RESEARCH for {team_strength} team
            
            Theme: '{theme}'
            Idea: '{idea}'
            Team Strength: {team_strength}
            
            **CRITICAL RESEARCH REQUIREMENTS:**
            
            1. **NICHE COMPETITOR ANALYSIS** (Focus: {constraints['competitor_type']}):
               - Find 2 major competitors (obvious ones everyone knows)
               - Find 3-4 smaller/niche solutions that solve PARTS of this problem
               - For each competitor, note: Name, core feature, what they DON'T do
               - Identify specific gaps that a {team_strength} team can fill in 9 hours
            
            2. **TECHNICAL STACK RESEARCH** (Priority: {constraints['tech_priority']}):
               - Recommend specific APIs for: {constraints['api_focus']}
               - Avoid suggesting: {constraints['avoid_research']}
               - Include setup time estimates (under 1 hour total)
               - Provide fallback options if primary APIs fail
               - Focus on free/freemium tiers for hackathon use
            
            3. **HACKATHON-SPECIFIC MARKET INTELLIGENCE**:
               - Identify 2-3 features missing from ALL existing solutions
               - Focus on features that showcase {team_strength} team strengths
               - Highlight quick wins that can be demo'd in 3 minutes
               - Note any API rate limits or costs for demo day
            
            **OUTPUT FORMAT REQUIREMENTS:**
            ```
            **COMPETITOR LANDSCAPE:**
            Major: [2 big names + what they do]
            Niche: [3-4 smaller solutions + their specific focus]
            Gap for {team_strength}: [Specific opportunity]
            
            **RECOMMENDED TECH STACK FOR {team_strength}:**
            Primary APIs: [Specific services with URLs]
            Framework: [Best fit for team strength]
            Setup Time: [Realistic estimate under 1 hour]
            Backup Plan: [If primary APIs fail]
            
            **HACKATHON ADVANTAGE:**
            Missing Features: [2-3 specific gaps]
            {team_strength} Opportunity: [How team strength creates advantage]
            Demo-Ready Elements: [Features that will impress judges]
            ```
            
            **CRITICAL CONSTRAINTS:**
            - All recommendations must be buildable by {team_strength} team in 6-8 hours
            - Every API must have a free tier or reasonable demo costs
            - Focus on solutions that can be live-demo'd confidently
            - Avoid generic advice - be specific to {team_strength} capabilities
            """,
            expected_output=f"Detailed research report with competitor analysis, technical recommendations, and hackathon-specific opportunities optimized for {team_strength} team",
            agent=agent,
        )

class CriticalTasks:
    """Enhanced Critical Analysis with hackathon failure prediction"""
    
    @staticmethod
    def get_team_risk_profile(team_strength: str) -> Dict[str, str]:
        """Get risk profiles specific to team strengths"""
        profiles = {
            "Frontend": {
                "scope_creep": "Building custom backend logic, complex algorithms",
                "technical_debt": "API rate limits during demo, third-party service failures",
                "demo_risk": "Backend not working, APIs failing during presentation"
            },
            "Backend": {
                "scope_creep": "Complex UI design, mobile responsiveness",
                "technical_debt": "Database setup time, deployment complexity", 
                "demo_risk": "No visual interface for judges to see"
            },
            "AI/ML": {
                "scope_creep": "Production-ready deployment, scalable UI",
                "technical_debt": "Model training time, integration complexity",
                "demo_risk": "Model not performing as expected live"
            },
            "Full-Stack": {
                "scope_creep": "Trying to perfect both frontend and backend",
                "technical_debt": "Integration complexity between components",
                "demo_risk": "System components not working together"
            }
        }
        return profiles.get(team_strength, profiles["Full-Stack"])

    def critical_task(self, agent, research_report, idea, team_strength):
        risk_profile = self.get_team_risk_profile(team_strength)
        
        return Task(
            description=f"""BRUTAL HACKATHON REALITY CHECK
            
            Research Context: {research_report}
            Original Idea: {idea}
            Team Profile: {team_strength}
            
            **CRITICAL RISK ANALYSIS REQUIREMENTS:**
            
            As a hackathon mentor who has seen teams fail repeatedly, analyze these specific failure modes:
            
            1. **SCOPE CREEP RISKS for {team_strength} teams**:
               - Identify features that will consume >2 hours each
               - Flag anything that doesn't match {team_strength} core strength
               - Specific risk: {risk_profile['scope_creep']}
               - List features to CUT immediately to stay in scope
            
            2. **TECHNICAL DEBT & DEMO RISKS**:
               - API failures during demo: which APIs are most unreliable?
               - Integration hell: where will components not work together?
               - Specific risk: {risk_profile['technical_debt']}
               - What's the backup plan if main tech fails?
            
            3. **COMPETITIVE REALITY CHECK**:
               - Based on research, why might existing solutions already win?
               - What makes this NOT just "another wrapper around existing APIs"?
               - If judges ask "how is this different?", what's the answer?
            
            4. **DEMO FAILURE SCENARIOS for {team_strength} teams**:
               - What will go wrong during the 3-minute presentation?
               - Specific risk: {risk_profile['demo_risk']}
               - What happens if the main feature doesn't work live?
               - How do you recover if internet/APIs fail?
            
            5. **MARKET ADOPTION RISKS**:
               - Why might users stick with existing solutions?
               - What's the switching cost from current solutions?
               - Is this solving a "nice to have" or "must have" problem?
            
            **OUTPUT FORMAT:**
            ```
            **🚨 SCOPE CREEP KILLERS:**
            Features to CUT: [Specific features that will kill timeline]
            {team_strength} Trap: [What your team type always over-builds]
            Time Wasters: [Tasks that don't showcase team strength]
            
            **⚡ TECHNICAL RISKS:**
            API Failure Points: [Which APIs are unreliable + backup plan]
            Integration Nightmares: [Where components won't connect]
            Demo Day Disasters: [What breaks under pressure]
            
            **🎯 COMPETITIVE WEAKNESSES:**
            Differentiation Gap: [Why judges might say "this already exists"]
            Switching Cost Problem: [Why users won't switch]
            Value Prop Clarity: [Is the unique value obvious?]
            
            **🔧 MITIGATION STRATEGIES:**
            Scope Safety Net: [Minimum viable demo that works]
            Technical Backup: [What to do when main approach fails]
            Pitch Pivot: [How to present if demo breaks]
            ```
            
            **BE BRUTALLY HONEST**: This team needs reality, not encouragement. 
            Point out every way this could fail and force them to have backup plans.
            """,
            expected_output=f"Brutally honest risk assessment with specific failure scenarios and mitigation strategies for {team_strength} team",
            agent=agent,
        )

class SolutionArchitectTasks:
    """Enhanced Solution Architecture with ruthless hackathon pragmatism"""
    
    @staticmethod
    def get_architecture_templates(team_strength: str) -> Dict[str, Any]:
        """Get architecture patterns optimized for each team type"""
        templates = {
            "Frontend": {
                "core_pattern": "API-First UI with third-party backend services",
                "time_allocation": "70% UI/UX, 20% API integration, 10% setup",
                "demo_focus": "User experience, visual design, interaction flows",
                "tech_constraints": "Use existing APIs for ALL complex logic",
                "success_metric": "Judges can see and interact with beautiful interface"
            },
            "Backend": {
                "core_pattern": "API-centric with minimal frontend",
                "time_allocation": "80% backend logic, 15% API design, 5% basic UI",
                "demo_focus": "API performance, data processing, system architecture", 
                "tech_constraints": "Build robust APIs, use basic frontend (Streamlit/simple HTML)",
                "success_metric": "Judges can see data flowing and processing happening"
            },
            "AI/ML": {
                "core_pattern": "Model-centric with simple interface",
                "time_allocation": "60% model work, 25% data pipeline, 15% basic UI",
                "demo_focus": "Algorithm performance, model accuracy, intelligent features",
                "tech_constraints": "Use pre-trained models or fine-tune existing ones",
                "success_metric": "Judges can see AI making smart decisions in real-time"
            },
            "Full-Stack": {
                "core_pattern": "Balanced frontend-backend with clear separation",
                "time_allocation": "40% frontend, 40% backend, 20% integration",
                "demo_focus": "Complete user journey, end-to-end functionality",
                "tech_constraints": "Choose mature, integrated frameworks",
                "success_metric": "Judges can see complete, working application"
            }
        }
        return templates.get(team_strength, templates["Full-Stack"])

    def solution_architect_task(self, agent, idea, research_report, critical_analysis, team_strength):
        arch_template = self.get_architecture_templates(team_strength)
        
        return Task(
            description=f"""HACKATHON MVP ARCHITECT - WINNING STRATEGY DESIGN
            
            Original Idea: {idea}
            Research Intelligence: {research_report}
            Critical Risks: {critical_analysis}
            Team Type: {team_strength}
            
            **ARCHITECTURE MANDATE for {team_strength} teams:**
            Pattern: {arch_template['core_pattern']}
            Time Budget: {arch_template['time_allocation']}
            Demo Focus: {arch_template['demo_focus']}
            Success Metric: {arch_template['success_metric']}
            
            **SOLUTION ARCHITECTURE REQUIREMENTS:**
            
            1. **RUTHLESS SCOPE DEFINITION** (The ONE Thing):
               - Define exactly ONE core feature that can be built in 6 hours
               - This feature must showcase {team_strength} team strength
               - Everything else gets CUT or simplified to basic functionality
               - Feature must be demo-able in 30 seconds of the pitch
            
            2. **API-FIRST ARCHITECTURE** (Especially for Frontend/Full-Stack):
               - Specify exact APIs to replace custom development
               - Include backup APIs in case primary fails
               - Estimate costs for demo day (must be under $20)
               - {arch_template['tech_constraints']}
            
            3. **TECH STACK SPECIFICATION** (Battle-tested only):
               - Choose technologies with <1 hour setup time
               - Every choice must have extensive documentation/tutorials
               - Include specific version numbers and compatibility notes
               - Prioritize technologies team already knows
            
            4. **DEMO-OPTIMIZED FEATURE DESIGN**:
               - Design features that work well in 3-minute live demos
               - Plan for "wow moments" that showcase {team_strength} skills
               - Include fallback demos if main feature fails
               - Ensure features work without perfect internet connectivity
            
            5. **DIFFERENTIATION THROUGH {team_strength} EXCELLENCE**:
               - Identify the ONE thing competitors can't do as well
               - Ensure differentiation is immediately visible/demonstrable
               - Make sure advantage comes from team skills, not just technology
               - Create sustainable competitive advantage in the demo
            
            **OUTPUT FORMAT:**
            ```
            **🎯 THE ONE CORE FEATURE:**
            Feature Name: [Compelling 3-4 word name]
            What it does: [One sentence description]
            Why {team_strength} teams excel: [Specific skill alignment]
            Demo script (30 seconds): [Exact user actions → system responses]
            
            **✂️ WHAT'S EXPLICITLY CUT:**
            Excluded Features: [List of features that would cause scope creep]
            Simplified Elements: [Complex features reduced to basics]
            Future Phase: [What gets built after hackathon IF this wins]
            
            **🛠️ EXACT TECH ARCHITECTURE:**
            Primary Stack: [Specific technologies with version numbers]
            APIs Used: [Exact services with free tier limits]
            Setup Sequence: [Step-by-step with time estimates]
            Fallback Options: [What to use if primary tech fails]
            Total Setup Time: [Must be under 90 minutes]
            
            **🚀 DEMO STRATEGY:**
            Wow Moment: [The 10-second clip that wins judges]
            User Journey: [Step-by-step demo flow]
            {team_strength} Showcase: [How demo highlights team strengths]
            Backup Demo: [Simplified version if main feature fails]
            
            **💡 DIFFERENTIATION STATEMENT:**
            One-liner: "Unlike [competitor], our solution [unique value] because [team strength advantage]"
            Competitive Moat: [Why others can't easily copy this]
            Judge Appeal: [Why this wins over other hackathon projects]
            ```
            
            **CRITICAL SUCCESS CRITERIA:**
            - Buildable by {team_strength} team in 6-8 hours maximum
            - Demonstrates clear competitive advantage
            - Works reliably during live 3-minute demo
            - Showcases team's core strengths visibly
            - Has obvious commercial/practical value beyond hackathon
            """,
            expected_output=f"Complete, executable MVP strategy optimized for {team_strength} team success with detailed technical architecture and demo plan",
            agent=agent,
        )

class PitchTasks:
    """Enhanced Pitch Strategy with winning presentation tactics"""
    
    @staticmethod
    def get_pitch_templates(team_strength: str) -> Dict[str, str]:
        """Get pitch strategies optimized for showcasing team strengths"""
        templates = {
            "Frontend": {
                "demo_emphasis": "Visual interface, user interaction, design quality",
                "technical_credibility": "API integration skills, responsive design",
                "wow_factor": "Beautiful, intuitive interface that works flawlessly"
            },
            "Backend": {
                "demo_emphasis": "Data processing speed, API performance, system reliability",
                "technical_credibility": "Architecture decisions, scalability planning",
                "wow_factor": "Fast, robust system handling complex operations"
            },
            "AI/ML": {
                "demo_emphasis": "Model intelligence, algorithm performance, data insights",
                "technical_credibility": "Model selection, training approach, evaluation metrics",
                "wow_factor": "AI making visibly smart decisions in real-time"
            },
            "Full-Stack": {
                "demo_emphasis": "Complete user journey, end-to-end functionality",
                "technical_credibility": "System integration, architecture design",
                "wow_factor": "Seamless, complete application that just works"
            }
        }
        return templates.get(team_strength, templates["Full-Stack"])

    def pitch_task(self, agent, mvp_plan, team_strength, theme):
        pitch_template = self.get_pitch_templates(team_strength)
        
        return Task(
            description=f"""WINNING HACKATHON PITCH STRATEGY
            
            MVP Strategy: {mvp_plan}
            Team Strength: {team_strength}
            Hackathon Theme: {theme}
            
            **PITCH OPTIMIZATION for {team_strength} teams:**
            Demo Focus: {pitch_template['demo_emphasis']}
            Technical Credibility: {pitch_template['technical_credibility']}
            Wow Factor: {pitch_template['wow_factor']}
            
            **3-MINUTE PITCH STRUCTURE (Timed exactly):**
            
            Create a pitch script that follows this winning formula:
            
            **HOOK (0:00-0:25) - Problem Setup:**
            - Start with a specific, relatable problem question
            - Reference the hackathon theme: {theme}
            - Set up the demo with clear expectation
            - Transition: "Let me show you our solution..."
            
            **SOLUTION INTRO (0:25-0:45) - Concept Overview:**
            - Introduce the core concept in one sentence
            - Highlight what makes it different (not just better)
            - Emphasize {team_strength} team advantage
            - Transition: "Here's how it works..."
            
            **LIVE DEMO (0:45-2:00) - The Core Experience:**
            - Script exact user actions: "I click here, type this, press enter"
            - Narrate system responses with enthusiasm
            - Highlight {pitch_template['demo_emphasis']} visibly
            - Include the "wow moment" that showcases {team_strength} skills
            - Show the differentiation factor working live
            - Transition: "What you just saw demonstrates..."
            
            **TECHNICAL CREDIBILITY (2:00-2:30) - Why It Works:**
            - Mention specific technologies/APIs used (shows competence)
            - Address one major challenge overcome (shows depth)
            - Reference {pitch_template['technical_credibility']}
            - Connect to hackathon theme and market opportunity
            - Transition: "This is more than just a hackathon project..."
            
            **VISION CLOSE (2:30-3:00) - Impact Statement:**
            - Broader impact beyond hackathon
            - Clear commercial/practical application
            - Why judges should remember this project
            - Strong closing line that reinforces {team_strength} advantage
            - End with confidence and eye contact
            
            **OUTPUT FORMAT:**
            ```
            **🎯 HOOK (0:00-0:25):**
            [Specific opening question tied to {theme}]
            [Problem setup that resonates with judges]
            [Clear demo setup and expectation]
            
            **💡 SOLUTION INTRO (0:25-0:45):**
            [One-sentence concept explanation]
            [Differentiation statement]
            [{team_strength} advantage highlight]
            
            **🚀 LIVE DEMO SCRIPT (0:45-2:00):**
            [Step 1: Exact user action → Expected system response]
            [Step 2: Next action → Response that shows {pitch_template['demo_emphasis']}]
            [Step 3: Wow moment → Response that proves differentiation]
            [Narration emphasizing {team_strength} excellence]
            
            **🛠️ TECHNICAL CREDIBILITY (2:00-2:30):**
            [Specific tech stack mention]
            [One challenge overcome]
            [Market opportunity connection]
            
            **🏆 VISION CLOSE (2:30-3:00):**
            [Broader impact statement]
            [Commercial application]
            [Memorable closing line]
            
            **🔧 BACKUP PLAN:**
            [What to do if demo fails]
            [Simplified version to show]
            [How to recover gracefully]
            
            **📋 JUDGE Q&A PREP:**
            [Top 3 questions judges will ask]
            [Prepared answers that reinforce strengths]
            [How to handle technical challenges]
            ```
            
            **PITCH SUCCESS CRITERIA:**
            - Demonstrates clear value proposition in first 30 seconds
            - Live demo works flawlessly and showcases {team_strength}
            - Technical credibility without overwhelming jargon
            - Commercial viability is obvious
            - Memorable and differentiated from other pitches
            - Confident delivery that matches team capabilities
            """,
            expected_output=f"Complete 3-minute pitch script with exact timing, live demo choreography, and backup plans optimized for {team_strength} team presentation",
            agent=agent,
        )

# Integration validation and testing
class TaskValidator:
    """Validates that tasks produce non-generic, team-specific outputs"""
    
    @staticmethod
    def validate_task_specificity(task_output: str, team_strength: str) -> Dict[str, bool]:
        """Check if task output is properly customized for team strength"""
        validation_results = {
            "mentions_team_strength": team_strength.lower() in task_output.lower(),
            "avoids_generic_language": not any(phrase in task_output.lower() for phrase in [
                "consider using", "you might want", "could potentially", "various options"
            ]),
            "includes_specific_tech": any(tech in task_output.lower() for tech in [
                "react", "vue", "fastapi", "pytorch", "streamlit", "api", "database"
            ]),
            "has_time_constraints": any(time_ref in task_output.lower() for time_ref in [
                "hour", "time", "quick", "rapid", "fast"
            ])
        }
        
        return validation_results
    
    @staticmethod
    def get_task_quality_score(validation_results: Dict[str, bool]) -> float:
        """Calculate quality score for task output"""
        return sum(validation_results.values()) / len(validation_results)

# Usage example with validation
def create_validated_research_task(agent, theme, idea, team_strength):
    """Create research task with built-in validation"""
    task_creator = ResearchTasks()
    task = task_creator.research_task(agent, theme, idea, team_strength)
    
    # Add validation metadata
    task.metadata = {
        "team_strength": team_strength,
        "expected_specificity": ["competitor analysis", "tech stack", "api recommendations"],
        "validation_required": True
    }
    
    return task

# Export all task classes for easy import
__all__ = [
    'ResearchTasks',
    'CriticalTasks', 
    'SolutionArchitectTasks',
    'PitchTasks',
    'TaskValidator',
    'create_validated_research_task'
]