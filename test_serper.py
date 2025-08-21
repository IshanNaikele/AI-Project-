import os
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment
api_key = os.getenv("SERPER_API_KEY")

if not api_key:
    print("Error: SERPER_API_KEY not found in environment variables.")
else:
    try:
        # Instantiate the tool
        search_tool = SerperDevTool()

        # Run a simple search query using the correct method signature
        print("Testing Serper API...")
        search_results = search_tool.run(search_query="what is a large language model?")

        # Print the results to confirm a successful response
        print("\n✅ Serper API call successful!")
        print("Search Results:")
        print(search_results)

    except Exception as e:
        print(f"\n❌ Serper API call failed with an error: {e}")