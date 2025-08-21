# backend/tasks.py
from crewai import Task

class ResearchTasks:
    def research_task(self, agent, theme, idea):
        return Task(
            description=f"""Research the idea: '{idea}' for theme: '{theme}'.
            
            Provide ONLY these 3 sections:
            1. **Market Demand**: One sentence on immediate need + target users
            2. **Top 2 Competitors**: Name + brief description each
            3. **MVP Tech Stack**: 2-3 specific technologies/APIs needed
            
            Keep total response under 150 words. Be factual and direct.""",
            expected_output="Structured report with exactly 3 sections: Market Demand, Top 2 Competitors, MVP Tech Stack. Concise bullet points only.",
            agent=agent,
        )

class CriticalTasks:
    def critical_task(self, agent, research_report):
        return Task(
            description=f"""Analyze this research: {research_report}
            
            Identify exactly 3 critical risks:
            1. **Competitive Risk**: Why existing solutions might be better
            2. **Technical Risk**: Biggest implementation challenge  
            3. **Market Risk**: Why users might not adopt this
            
            Each risk = 1-2 sentences max. Total under 100 words.""",
            expected_output="3 numbered risks with brief explanations. Direct and critical tone.",
            agent=agent,
        )

class SolutionArchitectTasks:
    def solution_architect_task(self, agent, idea, research_report, critical_analysis, team_strength):
        # Critical personalization logic
        strength_focus = {
            "Frontend": "UI/UX-heavy solution. Use existing APIs. Focus: responsive design, user experience, minimal backend.",
            "Backend": "API-first architecture. Focus: server logic, databases, data processing. Keep frontend basic.",
            "AI/ML": "Algorithm-centric solution. Focus: model performance, data pipelines. Simple UI (Streamlit/basic HTML).",
            "Full-Stack": "Balanced approach with clear frontend/backend separation."
        }
        
        focus_instruction = strength_focus.get(team_strength, "Balanced full-stack approach")
        
        return Task(
            description=f"""Design an MVP for: {idea}
            
            Research Context: {research_report}
            Risks to Address: {critical_analysis}
            
            **CRITICAL CONSTRAINT**: Team strength is {team_strength}. 
            {focus_instruction}
            
            Output format:
            1. **MVP Title** (5-8 words)
            2. **Core Features** (3 features max, each 1 line)
            3. **Tech Architecture** (Stack optimized for {team_strength} team)
            4. **Why Perfect for {team_strength}** (2-3 sentences explaining fit)
            
            Make it buildable in 6-8 hours by a {team_strength} team.""",
            expected_output=f"Structured MVP plan specifically optimized for {team_strength} team strengths. Clear technical decisions that play to team capabilities.",
            agent=agent,
        )

class PitchTasks:
    def pitch_task(self, agent, mvp_plan):
        return Task(
            description=f"""Create a 3-minute pitch from: {mvp_plan}
            
            Structure (with exact timing):
            
            **Hook (0:00-0:20)**: Start with problem question
            **Solution (0:20-0:50)**: Introduce AI Strategist concept  
            **Demo (0:50-2:00)**: Narrate the live workflow
            **Reveal (2:00-2:30)**: Show personalized output
            **Close (2:30-3:00)**: Vision + "AI co-founder" line
            
            Emphasize how the solution is TAILORED to team skills (not generic).
            Use conversational, confident tone.""",
            expected_output="Complete pitch script with 5 timed sections. Conversational language, emphasizes personalization as key innovation.",
            agent=agent,
        )