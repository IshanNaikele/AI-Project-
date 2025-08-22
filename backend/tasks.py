# backend/tasks.py
from crewai import Task
import json
from typing import Dict, Any
from textwrap import dedent
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

    # MODIFICATION: Added `hackathon_duration` parameter
    def research_task(self, agent, theme, idea, team_strength, hackathon_duration):
        constraints = self.get_team_research_constraints(team_strength)
        
        return Task(
            description=f"""HACKATHON MARKET RESEARCH for {team_strength} team
            
            Theme: '{theme}'
            Idea: '{idea}'
            Team Strength: {team_strength}
            Hackathon Duration: {hackathon_duration} hours
            
            **CRITICAL RESEARCH REQUIREMENTS:**
            
            1. **NICHE COMPETITOR ANALYSIS** (Focus: {constraints['competitor_type']}):
                - Find 2 major competitors (obvious ones everyone knows)
                - Find 3-4 smaller/niche solutions that solve PARTS of this problem
                - For each competitor, note: Name, core feature, what they DON'T do
                - Identify specific gaps that a {team_strength} team can fill in {hackathon_duration} hours
            
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
            - All recommendations must be buildable by {team_strength} team in {hackathon_duration - 6} hours, leaving 6 hours for bugs, polish, and demo prep.
            - Every API must have a free tier or reasonable demo costs
            - Focus on solutions that can be live-demo'd confidently
            - Avoid generic advice - be specific to {team_strength} capabilities
            """,
            expected_output=f"Detailed research report with competitor analysis, technical recommendations, and hackathon-specific opportunities optimized for {team_strength} team for a {hackathon_duration}-hour hackathon",
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

    # MODIFICATION: Added `hackathon_duration` parameter
    def critical_task(self, agent, research_report, idea, team_strength, hackathon_duration):
        risk_profile = self.get_team_risk_profile(team_strength)
        
        return Task(
            description=f"""BRUTAL HACKATHON REALITY CHECK for a {hackathon_duration}-hour hackathon
            
            Research Context: {research_report}
            Original Idea: {idea}
            Team Profile: {team_strength}
            
            **CRITICAL RISK ANALYSIS REQUIREMENTS:**
            
            As a hackathon mentor who has seen teams fail repeatedly, analyze these specific failure modes:
            
            1. **SCOPE CREEP RISKS for {team_strength} teams**:
                - Identify features that will consume >{hackathon_duration / 4} hours each
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
            expected_output=f"Brutally honest risk assessment with specific failure scenarios and mitigation strategies for {team_strength} team, considering a {hackathon_duration}-hour time limit",
            agent=agent,
        )

class SolutionArchitectTasks:
    """Simplified Solution Architect Tasks"""
    
    def solution_architect_task(self, agent, idea: str, research_result: str, critical_result: str, team_strength: str, hackathon_duration: int):
        """Create a simplified solution architect task with team focus"""
        
        # Get team-specific templates and time constraints
        arch_template = self.get_architecture_templates(team_strength)
        time_strategy = self._get_time_strategy(hackathon_duration)
        
        return Task(
            description=dedent(f"""
                Create a practical MVP architecture plan for the idea: "{idea}"
                
                Team Strength: {team_strength}
                Hackathon Duration: {hackathon_duration} hours
                
                Use this research context: {research_result}
                Consider these critical insights: {critical_result}
                
                Focus on {arch_template['core_pattern']} architecture pattern.
                Prioritize {arch_template['priority_focus']} for maximum impact.
                
                Time Strategy: {time_strategy}
                
                Provide a clear, actionable architecture plan that this {team_strength} team can execute successfully.
            """),
            expected_output=dedent(f"""
                ## MVP Architecture Plan for {team_strength} Team
                
                ### 🎯 Core Architecture
                **Pattern**: {arch_template['core_pattern']}
                **Primary Focus**: {arch_template['priority_focus']}
                
                ### ⚡ Quick Start Stack
                [Recommended technologies and tools]
                
                ### 🏗️ System Components
                [3-5 main components with clear responsibilities]
                
                ### 📊 Data Flow
                [Simple data flow diagram or description]
                
                ### ⏰ Implementation Timeline
                **Phase 1 (First {hackathon_duration//3} hours)**: Core functionality
                **Phase 2 (Next {hackathon_duration//3} hours)**: Key features
                **Phase 3 (Final {hackathon_duration//3} hours)**: Polish and integration
                
                ### 🚀 Demo Strategy
                [What to build for maximum demo impact]
                
                ### ⚠️ Risk Mitigation
                [Top 3 technical risks and quick solutions]
                
                ### 📋 Team Task Distribution
                [How to divide work based on {team_strength} strengths]
                
                Team Strength Optimization: {team_strength}
                Hackathon Duration: {hackathon_duration} hours
            """),
            agent=agent
        )
    
    @staticmethod
    def get_architecture_templates(team_strength: str) -> dict:
        """Get simplified architecture templates for each team type"""
        templates = {
            "Frontend": {
                "core_pattern": "Component-Based UI Architecture",
                "priority_focus": "responsive design and user experience",
                "tech_stack": "React/Vue + CSS Framework + Mock APIs",
                "demo_emphasis": "Visual appeal and smooth interactions"
            },
            "Backend": {
                "core_pattern": "RESTful API Architecture", 
                "priority_focus": "robust APIs and data management",
                "tech_stack": "Express/FastAPI + Database + Authentication",
                "demo_emphasis": "API functionality and data processing"
            },
            "AI/ML": {
                "core_pattern": "Model-as-a-Service Architecture",
                "priority_focus": "AI model integration and data pipeline",
                "tech_stack": "Python ML Stack + API Layer + Data Processing",
                "demo_emphasis": "AI capabilities and intelligent features"
            },
            "Full-Stack": {
                "core_pattern": "Layered Full-Stack Architecture",
                "priority_focus": "end-to-end integration and user flow",
                "tech_stack": "Full-Stack Framework + Database + Deployment",
                "demo_emphasis": "Complete working application"
            }
        }
        return templates.get(team_strength, templates["Full-Stack"])
    
    def _get_time_strategy(self, hackathon_duration: int) -> str:
        """Get time-specific development strategy"""
        if hackathon_duration <= 8:
            return "MVP-only approach: Build one core feature extremely well"
        elif hackathon_duration <= 24:
            return "Feature-focused: 2-3 key features with basic integration"
        elif hackathon_duration <= 48:
            return "Polish-enabled: Complete features with testing and refinement"
        else:
            return "Comprehensive: Full feature set with quality assurance"
    
    @staticmethod 
    def get_team_constraints(team_strength: str) -> dict:
        """Get team-specific development constraints"""
        constraints = {
            "Frontend": {
                "avoid": "Complex backend logic",
                "leverage": "Visual design and user interaction",
                "shortcuts": "Use mock APIs and static data initially"
            },
            "Backend": {
                "avoid": "Complex frontend frameworks", 
                "leverage": "Data processing and API design",
                "shortcuts": "Use simple frontend templates"
            },
            "AI/ML": {
                "avoid": "Complex UI development",
                "leverage": "Data analysis and model building", 
                "shortcuts": "Use pre-trained models and simple interfaces"
            },
            "Full-Stack": {
                "avoid": "Over-engineering any single component",
                "leverage": "System integration and end-to-end flow",
                "shortcuts": "Use proven technology stacks"
            }
        }
        return constraints.get(team_strength, constraints["Full-Stack"])
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

    # MODIFICATION: Added `hackathon_duration` parameter
    def pitch_task(self, agent, mvp_plan, team_strength, theme, hackathon_duration):
        pitch_template = self.get_pitch_templates(team_strength)
        
        return Task(
            description=f"""WINNING HACKATHON PITCH STRATEGY for a {hackathon_duration}-hour hackathon
            
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
            expected_output=f"Complete 3-minute pitch script with exact timing, live demo choreography, and backup plans optimized for {team_strength} team presentation for a {hackathon_duration}-hour hackathon",
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
                "hour", "time", "quick", "rapid", "fast", "9 hours", "24 hours", "48 hours"
            ]) # MODIFICATION: Added specific hackathon durations to check for
        }
        
        return validation_results
    
    
    @staticmethod
    def get_task_quality_score(validation_results: Dict[str, bool]) -> float:
        print(f"DEBUG: Data being passed to get_task_quality_score: {validation_results}")
        print(f"DEBUG: Data type: {type(validation_results)}")
        
        # Fix: Handle empty dictionary case
        if not validation_results or len(validation_results) == 0:
            return 0.0
            
        return sum(validation_results.values()) / len(validation_results)

# Usage example with validation
# MODIFICATION: Added hackathon_duration parameter
def create_validated_research_task(agent, theme, idea, team_strength, hackathon_duration):
    """Create research task with built-in validation"""
    task_creator = ResearchTasks()
    task = task_creator.research_task(agent, theme, idea, team_strength, hackathon_duration)
    
    # Add validation metadata
    task.metadata = {
        "team_strength": team_strength,
        "hackathon_duration": hackathon_duration,
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