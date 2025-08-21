# backend/agents/critical_agent.py
from crewai import Agent
from crewai_tools import SerperDevTool

# Instantiate the tool. This agent will also need a search tool to verify claims.
search_tool = SerperDevTool(num_results=3)

class CriticalAgents:
    def critical_agent(self, llm):
        return Agent(
            role='Idea Validation and Critical Analysis Agent',
            goal='Analyze and stress-test a hackathon idea by identifying weaknesses, potential scope creep, and lack of novelty.',
            backstory="""You are a cynical but brilliant startup consultant. Your job is to poke holes in ideas,
            not to be mean, but to make sure they are strong enough to succeed. You scrutinize the market analysis
            from the research agent, verify its claims, and present a clear, data-driven critique.
            You MUST use the 'Search the internet with Serper' tool to verify information and validate your critiques.
            """,
            verbose=True,
            allow_delegation=False,
            tools=[search_tool],
            llm=llm
        )
