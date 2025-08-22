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
    """Enhanced Solution Architecture with comprehensive MVP planning and team-first approach"""
    
    @staticmethod
    def get_architecture_templates(team_strength: str) -> Dict[str, Any]:
        """Get comprehensive architecture patterns optimized for each team type"""
        templates = {
            "Frontend": {
                "core_pattern": "API-First UI with stunning visual experience",
                "time_allocation": "70% UI/UX development, 20% API integration, 10% setup/deployment",
                "demo_focus": "User experience excellence, visual design impact, seamless interactions",
                "tech_constraints": "Leverage existing APIs for ALL complex logic, focus on presentation layer",
                "success_metric": "Judges are visually impressed and can interact intuitively",
                "primary_skills": ["React/Vue mastery", "CSS/Animation expertise", "API integration", "Responsive design"],
                "innovation_areas": ["UI/UX patterns", "Interactive visualizations", "User journey optimization"],
                "wow_opportunities": ["Micro-interactions", "Real-time UI updates", "Beautiful data presentation"]
            },
            "Backend": {
                "core_pattern": "Robust API architecture with performance optimization",
                "time_allocation": "75% backend logic/APIs, 15% data management, 10% basic frontend",
                "demo_focus": "System performance, data processing capabilities, API reliability", 
                "tech_constraints": "Build scalable APIs, use simple frontend (Streamlit/basic HTML)",
                "success_metric": "Judges can see fast, reliable data processing and system architecture",
                "primary_skills": ["API design", "Database optimization", "System architecture", "Performance tuning"],
                "innovation_areas": ["Data processing algorithms", "System efficiency", "API design patterns"],
                "wow_opportunities": ["Real-time data processing", "High-performance APIs", "Smart caching systems"]
            },
            "AI/ML": {
                "core_pattern": "Intelligence-first architecture with model showcase",
                "time_allocation": "65% model/algorithm work, 20% data pipeline, 15% interface",
                "demo_focus": "AI decision-making, model accuracy, intelligent insights generation",
                "tech_constraints": "Leverage pre-trained models and fine-tune, minimize infrastructure complexity",
                "success_metric": "Judges witness AI making visibly intelligent decisions in real-time",
                "primary_skills": ["Model selection/fine-tuning", "Data preprocessing", "Algorithm optimization", "ML pipelines"],
                "innovation_areas": ["Novel ML applications", "Model combination strategies", "AI-driven insights"],
                "wow_opportunities": ["Real-time AI predictions", "Intelligent automation", "Smart data analysis"]
            },
            "Full-Stack": {
                "core_pattern": "Balanced end-to-end solution with seamless integration",
                "time_allocation": "40% frontend experience, 40% backend logic, 20% system integration",
                "demo_focus": "Complete user journey, system cohesion, end-to-end functionality",
                "tech_constraints": "Choose proven, integrated frameworks that work well together",
                "success_metric": "Judges see a polished, complete application that works seamlessly",
                "primary_skills": ["Full-stack frameworks", "System integration", "Database design", "User experience"],
                "innovation_areas": ["System architecture", "Integration patterns", "User experience flows"],
                "wow_opportunities": ["Seamless user journeys", "Real-time synchronization", "Intelligent system behavior"]
            }
        }
        return templates.get(team_strength, templates["Full-Stack"])

    @staticmethod
    def get_team_specific_tech_stack(team_strength: str, hackathon_duration: int) -> Dict[str, Any]:
        """Get detailed tech recommendations based on team strength and time constraints"""
        stacks = {
            "Frontend": {
                "primary_framework": "React with Vite (fastest setup)" if hackathon_duration >= 24 else "Vanilla JS with modern CSS",
                "styling": "Tailwind CSS (rapid styling) + Framer Motion (animations)",
                "api_integration": "Axios + React Query (data fetching)",
                "deployment": "Vercel (instant deployment)",
                "backup_stack": "Vue.js + Bootstrap if React fails",
                "setup_time": "45 minutes maximum",
                "key_libraries": ["react-router-dom", "lucide-react", "react-hook-form"]
            },
            "Backend": {
                "primary_framework": "FastAPI (Python) - fastest API development",
                "database": "SQLite (local) or Supabase (cloud) for quick setup",
                "api_docs": "Auto-generated with FastAPI Swagger",
                "deployment": "Railway or Render (simple deployment)",
                "backup_stack": "Express.js + MongoDB if Python fails",
                "setup_time": "30 minutes maximum",
                "key_libraries": ["pydantic", "sqlalchemy", "python-multipart"]
            },
            "AI/ML": {
                "primary_framework": "Python + Streamlit (ML-friendly UI)",
                "ml_stack": "Hugging Face Transformers + scikit-learn",
                "data_processing": "Pandas + NumPy",
                "deployment": "Streamlit Community Cloud",
                "backup_stack": "Gradio + Google Colab if Streamlit fails",
                "setup_time": "20 minutes maximum",
                "key_libraries": ["transformers", "torch", "streamlit", "plotly"]
            },
            "Full-Stack": {
                "primary_framework": "Next.js (React + API routes) or MEAN stack",
                "database": "MongoDB Atlas (cloud) or PostgreSQL",
                "styling": "Tailwind CSS",
                "deployment": "Vercel (frontend) + Railway (backend)",
                "backup_stack": "Create React App + Express.js",
                "setup_time": "60 minutes maximum",
                "key_libraries": ["prisma", "next-auth", "react-query", "socket.io"]
            }
        }
        return stacks.get(team_strength, stacks["Full-Stack"])

    # ENHANCED SOLUTION ARCHITECT TASK
    def solution_architect_task(self, agent, idea, research_report, critical_analysis, team_strength, hackathon_duration):
        arch_template = self.get_architecture_templates(team_strength)
        tech_stack = self.get_team_specific_tech_stack(team_strength, hackathon_duration)
        
        return Task(
            description=f"""COMPREHENSIVE MVP ARCHITECT - WINNING STRATEGY BLUEPRINT
            
            **CONTEXT ANALYSIS:**
            Original Idea: {idea}
            Research Intelligence: {research_report}
            Critical Risk Assessment: {critical_analysis}
            Team Strength: {team_strength}
            Hackathon Duration: {hackathon_duration} hours
            Available Development Time: {hackathon_duration * 0.75} hours (25% buffer for issues)
            
            **TEAM-FIRST ARCHITECTURE MANDATE:**
            Core Pattern: {arch_template['core_pattern']}
            Time Allocation: {arch_template['time_allocation']}
            Primary Skills to Leverage: {arch_template['primary_skills']}
            Innovation Focus Areas: {arch_template['innovation_areas']}
            Success Definition: {arch_template['success_metric']}
            
            **COMPREHENSIVE MVP PLANNING REQUIREMENTS:**
            
            1. **CORE PROBLEM & SOLUTION DEFINITION:**
                - Identify the ONE specific problem this MVP solves better than existing solutions
                - Define the unique value proposition that leverages {team_strength} expertise
                - Ensure the solution is demonstrable within {hackathon_duration} hours
                - Connect directly to hackathon theme and judges' evaluation criteria
            
            2. **FEATURE PRIORITIZATION & SCOPE MANAGEMENT:**
                - Define exactly THREE tiers of features:
                  * MUST-HAVE (Core Demo): Buildable in {hackathon_duration * 0.4} hours
                  * SHOULD-HAVE (Polish): Additional {hackathon_duration * 0.2} hours if time permits
                  * COULD-HAVE (Future): Post-hackathon expansion features
                - Each feature must showcase {team_strength} capabilities visibly
                - Ensure MUST-HAVE features alone create a winning demo
            
            3. **TECHNICAL ARCHITECTURE DEEP-DIVE:**
                - Specify exact technology choices from: {tech_stack}
                - Include version numbers, setup commands, and configuration details
                - Design system architecture that plays to {team_strength} strengths
                - Plan data flow, API endpoints, and component structure
                - Ensure all choices support rapid development and reliable demos
            
            4. **INNOVATION & DIFFERENTIATION STRATEGY:**
                - Identify the specific innovation that makes this unique
                - Focus on innovations within {arch_template['innovation_areas']}
                - Plan for {arch_template['wow_opportunities']} that showcase team expertise
                - Ensure differentiation is immediately visible to judges
                - Design competitive moats that leverage team's core competencies
            
            5. **IMPLEMENTATION ROADMAP:**
                - Break down development into hourly milestones
                - Prioritize {team_strength} showcase features early in timeline
                - Include integration points, testing phases, and demo preparation
                - Plan parallel development streams where possible
                - Account for deployment, bug fixes, and polish time
            
            6. **RISK MITIGATION & BACKUP PLANS:**
                - Address every risk identified in critical analysis
                - Provide fallback solutions for each major component
                - Ensure minimum viable demo works even if advanced features fail
                - Plan offline demo capabilities for internet/API failures
            
            7. **DEMO OPTIMIZATION & JUDGE APPEAL:**
                - Design features specifically for 3-minute live demonstrations
                - Plan "wow moments" that highlight {team_strength} expertise
                - Ensure demo showcases innovation, technical competence, and market value
                - Include interactive elements that engage judges directly
            
            **COMPREHENSIVE OUTPUT FORMAT:**
            ```
            **🎯 PROBLEM & SOLUTION FRAMEWORK:**
            Core Problem Solved: [Specific, measurable problem statement]
            Unique Value Proposition: [What competitors can't offer]
            {team_strength} Advantage: [How team skills create competitive edge]
            Target User Persona: [Specific user type who needs this most]
            Success Metrics: [How to measure MVP success]
            
            **✨ INNOVATION & WOW FACTOR:**
            Primary Innovation: [The ONE thing that makes this special]
            Technical Innovation: [Specific {team_strength} technical achievement]
            User Experience Innovation: [How users benefit uniquely]
            Market Innovation: [Why this approach beats existing solutions]
            Judge Appeal Factor: [What will make judges remember this]
            
            **🏗️ COMPREHENSIVE FEATURE ARCHITECTURE:**
            
            TIER 1 - MUST HAVE (Core Demo - {hackathon_duration * 0.4} hours):
            Feature 1: [Name] - [Exact functionality] - [Why it showcases {team_strength}] - [Time: X hours]
            Feature 2: [Name] - [Exact functionality] - [Demo impact] - [Time: X hours]
            Feature 3: [Name] - [Exact functionality] - [Competitive advantage] - [Time: X hours]
            
            TIER 2 - SHOULD HAVE (Polish - {hackathon_duration * 0.2} hours):
            Enhancement 1: [Feature improvement that adds wow factor]
            Enhancement 2: [User experience polish that impresses judges]
            
            TIER 3 - COULD HAVE (Future Expansion):
            Future 1: [Post-hackathon feature for commercial viability]
            Future 2: [Scalability feature for real-world deployment]
            
            **🛠️ DETAILED TECHNICAL IMPLEMENTATION:**
            
            Primary Tech Stack:
            Framework: {tech_stack['primary_framework']}
            Database: {tech_stack['database']}
            Key Libraries: {tech_stack['key_libraries']}
            Deployment: {tech_stack['deployment']}
            Setup Time: {tech_stack['setup_time']}
            
            System Architecture:
            Frontend Components: [List of UI components needed]
            Backend APIs: [Specific endpoints and their purposes]
            Data Models: [Database schema or data structures]
            External Integrations: [Third-party APIs and their roles]
            
            File Structure: [Organized project layout]
            Development Environment: [Setup requirements and commands]
            
            **📋 HOURLY IMPLEMENTATION ROADMAP:**
            Hour 1-2: [Project setup + core architecture]
            Hour 3-5: [Core Feature 1 development - {team_strength} focus]
            Hour 6-8: [Core Feature 2 + basic integration]
            Hour 9-11: [Core Feature 3 + system integration]
            Hour 12-14: [Testing, bug fixes, deployment setup]
            Hour 15-17: [Polish, demo preparation, backup plans]
            Hour 18+: [Final testing, demo rehearsal, presentation prep]
            
            **🚀 DEMO STRATEGY & JUDGE ENGAGEMENT:**
            Opening Hook: [Specific demo opening that showcases {team_strength}]
            Core Demo Flow: [Step-by-step user journey highlighting innovation]
            Wow Moment: [The 15-second sequence that wins judges over]
            Technical Showcase: [How to display {team_strength} competence]
            Interaction Elements: [Ways judges can engage with the demo]
            Closing Impact: [Memorable ending that reinforces value]
            
            **🔧 COMPREHENSIVE BACKUP PLANS:**
            Technical Backup: {tech_stack['backup_stack']}
            Feature Fallbacks: [Simplified versions of each core feature]
            Demo Alternatives: [What to show if main demo fails]
            Offline Capabilities: [How demo works without internet]
            Recovery Scripts: [Quick fixes for common failures]
            
            **💰 COMMERCIAL VIABILITY & MARKET FIT:**
            Revenue Model: [How this makes money post-hackathon]
            Market Size: [Target addressable market]
            Go-to-Market Strategy: [How to reach first users]
            Competitive Positioning: [Market differentiation strategy]
            Scalability Plan: [How to grow beyond MVP]
            
            **🏆 WINNING FACTORS SUMMARY:**
            Technical Excellence: [How {team_strength} creates superior solution]
            Innovation Impact: [Why this advances the field]
            User Value: [Immediate benefit users will experience]
            Market Opportunity: [Commercial potential beyond hackathon]
            Team Advantage: [Why this team can execute this vision]
            ```
            
            **CRITICAL ARCHITECTURE PRINCIPLES:**
            1. Every decision prioritizes {team_strength} expertise showcase
            2. All features must be demo-ready and judge-impressing
            3. Innovation is specific and measurable, not generic
            4. Technical choices optimize for rapid development + reliability
            5. Backup plans exist for every critical component
            6. Commercial viability is clear and compelling
            7. The MVP creates genuine competitive advantage through team skills
            
            **VALIDATION CRITERIA:**
            - Can this be built by a {team_strength} team in {hackathon_duration * 0.75} hours?
            - Does this showcase what the team does better than anyone else?
            - Will judges immediately understand the innovation and value?
            - Is this differentiated enough to win against other hackathon projects?
            - Does this solve a real problem people will pay for?
            """,
            expected_output=f"Complete MVP strategy blueprint with detailed technical architecture, implementation roadmap, and winning demo plan optimized for {team_strength} team excellence within {hackathon_duration} hours",
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