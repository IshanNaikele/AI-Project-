# backend/tasks.py
from crewai import Task

class ResearchTasks:
    def research_task(self, agent, theme, idea):
        return Task(
            description=f"""Analyze the hackathon idea: '{idea}' within the theme: '{theme}'.
            Your goal is to provide a brief, high-level summary. Focus on these key areas, using a simple search query string for each:
            1. Market Demand: Is there a clear, immediate need for this? Summarize in 1-2 sentences.
            2. Key Competitors: List the top 2-3 existing competitors.
            3. Tech Stack: Suggest 1-2 core technologies or APIs that would be essential for an MVP.
            
            Keep your entire report concise and to the point, focusing only on the most critical information.
            """,
            expected_output="A concise report with clear headings for Market Demand, Key Competitors, and Tech Stack, providing a structured, concise answer to the task.",
            agent=agent,
        )

class CriticalTasks:
    def critical_task(self, agent, research_report):
        return Task(
            description=f"""Critically analyze the following research report:
            {research_report}
            Your goal is to poke holes in the idea. Stress-test it for weaknesses, scope creep, and lack of novelty.
            You must use the search tool to verify any claims made in the research.
            Your final output must be a concise, critical analysis that highlights the main risks and challenges of the idea.
            """,
            expected_output="A brief, critical analysis in markdown format that outlines the risks, competitive challenges, and potential flaws of the initial idea.",
            agent=agent,
        )

class SolutionArchitectTasks:
    def solution_architect_task(self, agent, idea, research_report, critical_analysis, team_strength):
        return Task(
            description=f"""Based on the following inputs, define a concrete and feasible MVP.
            - Initial Idea: {idea}
            - Research Report: {research_report}
            - Critical Analysis: {critical_analysis}
            - Team's Core Strength: {team_strength}
            
            Your goal is to create a solution that maximizes the team's strengths and minimizes their weaknesses.
            Your final output must be a detailed, actionable plan for the MVP, including a high-level technical breakdown.
            """,
            expected_output="A structured MVP plan with a title, a brief summary, a list of core features, a suggested technical architecture, and a rationale for why this plan is ideal for the team's strengths.",
            agent=agent,
        )

# backend/tasks.py
from crewai import Task

# ... (other task classes)

class PitchTasks:
    def pitch_task(self, agent, mvp_plan):
        return Task(
            description=f"""Synthesize the following MVP plan into a powerful, concise pitch outline for a 3-minute demo.
            - MVP Plan: {mvp_plan}

            Your goal is to create a compelling narrative that hooks the audience and clearly explains the problem, solution, and innovation.
            The pitch should be persuasive and ready for presentation.
            """,
            expected_output="A pitch storyboard in markdown format, with clear sections for the hook, solution, live demo, reveal, and close, as outlined in the project brief. The output MUST contain ONLY the final markdown text and nothing else, such as internal thoughts, tool descriptions, or any JSON objects.",
            agent=agent,
        )