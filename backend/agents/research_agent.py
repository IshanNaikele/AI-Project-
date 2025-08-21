# backend/agents/research_agent.py
from crewai import Agent
from crewai_tools import SerperDevTool

# Instantiate the tool
search_tool = SerperDevTool()


class ResearchAgents:
    def research_agent(self, llm):
        return Agent(
            role='Expert Market Research Analyst',
            goal='Execute a research plan by conducting internet searches and returning concise, factual information. Your goal is to provide a comprehensive, fact-based summary for the next agent.',
            backstory="""You are a seasoned market research analyst. Your primary and ONLY function is to use the internet search tool to find information.
            For every search, you MUST generate a simple, single-line search query.
            NEVER provide tool inputs in JSON format, a dictionary, or any complex object.
            For example, a valid tool input is 'market demand for AI language learning apps', NOT {'search_query': 'market demand for AI language learning apps'}.
            Your entire output must be based on the facts you find, and you must adhere strictly to the format below.""",
            verbose=True,
            allow_delegation=False,
            tools=[search_tool],
            llm=llm,
            agent_executor_kwargs={"handle_parsing_errors": True}
        )