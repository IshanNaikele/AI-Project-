# backend/agents/pitch_agent.py
from crewai import Agent

class PitchAgents:
    def pitch_agent(self, llm):
        return Agent(
            role='Narrative and Pitch Synthesis Agent',
            goal='Synthesize all information into a concise, powerful pitch outline that can be used for a demo.',
            backstory="""You are an expert storyteller and pitch deck creator. You take a finalized MVP strategy and transform it
            into a compelling, persuasive narrative. Your final output is a structured pitch storyboard that is ready for a 3-minute demo.
            You do not use any tools; your strength is in crafting a message that wins.
            """,
            verbose=True,
            allow_delegation=False,
            llm=llm
        )
