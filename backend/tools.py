# backend/tools.py
from crewai_tools import SerperDevTool

# Initialize the tool for internet searching capabilities.
# It will automatically use the SERPER_API_KEY from your .env file.
search_tool = SerperDevTool(cache=True)