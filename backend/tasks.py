# backend/tasks.py
from crewai import Task
from datetime import datetime

class ResearchTasks():
    def research_task(self, agent, theme, idea):
        return Task(
            description=f"""
                Analyze the hackathon idea: '{idea}' within the theme: '{theme}'.
                Your goal is to provide a brief, high-level summary. Focus on these key areas:
                1. Market Demand: Is there a clear, immediate need for this? Summarize in 1-2 sentences.
                2. Key Competitors: List the top 2-3 existing competitors.
                3. Tech Stack: Suggest 1-2 core technologies or APIs that would be essential for an MVP.
                
                Keep your entire report concise and to the point, focusing only on the most critical information.
            """,
            expected_output="""A short, summarized report with three sections:
            - Market Demand (1-2 sentences)
            - Key Competitors (A list of 2-3 names)
            - Tech Stack (A list of 1-2 technologies)
            """,
            agent=agent,
            # Adding a timestamp to the output file name
            output_file=f'outputs/research_report_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.md'
        )