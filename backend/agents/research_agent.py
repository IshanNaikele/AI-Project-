# backend/agents/research_agent.py
from crewai import Agent
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

class ResearchAgents:
    def research_agent(self, llm):
        return Agent(
            role='Market Research Specialist',
            goal='Find factual data about market demand, competitors, and tech requirements. Provide structured, concise summaries only.',
            backstory="""You are a data-focused market analyst. You search the internet for facts and organize them into exactly 3 sections:
            Market Demand, Top 2 Competitors, and MVP Tech Stack.
            
            SEARCH RULES:
            - Use simple search queries like 'market demand healthcare apps' or 'competitors patient monitoring'
            - Never use JSON format or complex objects
            - Make 2-3 targeted searches maximum
            
            OUTPUT RULES:
            - Keep each section under 50 words
            - Use bullet points, not paragraphs
            - Focus on actionable facts, not opinions""",
            verbose=True,
            allow_delegation=False,
            tools=[search_tool],
            llm=llm,
            agent_executor_kwargs={"handle_parsing_errors": True}
        )