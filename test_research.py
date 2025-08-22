import os
from crewai_tools import SerperDevTool
from crewai import Agent, Task, Crew
import json

def diagnose_search_issues():
    """Comprehensive diagnostic for search functionality issues"""
    
    print("🔍 SEARCH FUNCTIONALITY DIAGNOSTIC")
    print("=" * 50)
    
    # 1. Check environment variables
    print("1. Environment Variables Check:")
    serper_api_key = os.getenv('SERPER_API_KEY')
    if serper_api_key:
        print(f"   ✅ SERPER_API_KEY found (ending with: ...{serper_api_key[-4:]})")
    else:
        print("   ❌ SERPER_API_KEY not found in environment variables")
        print("   💡 Set it with: export SERPER_API_KEY='your_key_here'")
        return False
    
    # 2. Test SerperDevTool initialization
    print("\n2. SerperDevTool Initialization:")
    try:
        search_tool = SerperDevTool()
        print("   ✅ SerperDevTool initialized successfully")
    except Exception as e:
        print(f"   ❌ SerperDevTool initialization failed: {e}")
        return False
    
    # 3. Test direct search
    print("\n3. Direct Search Test:")
    try:
        result = search_tool.run("Python programming tutorial")
        if result and len(str(result)) > 10:
            print("   ✅ Direct search successful")
            print(f"   📊 Result length: {len(str(result))} characters")
            print(f"   📝 Sample: {str(result)[:100]}...")
        else:
            print("   ❌ Direct search returned empty or invalid result")
            print(f"   📝 Result: {result}")
            return False
    except Exception as e:
        print(f"   ❌ Direct search failed: {e}")
        return False
    
    # 4. Test agent search integration
    print("\n4. Agent Search Integration Test:")
    try:
        # Create a simple test agent
        from your_llm_config import get_llm  # You'll need to import your LLM
        
        # If you don't have LLM setup, skip this test
        print("   ⚠️  Skipping agent test - need LLM configuration")
        print("   💡 To test agent integration, ensure your LLM is properly configured")
        
    except ImportError:
        print("   ⚠️  Skipping agent test - LLM not configured")
    
    print("\n5. Common Issues & Solutions:")
    print("   🔧 If searches return asterisks (**):")
    print("      - Agent prompts may be too vague")
    print("      - Agent may not be using the search tool")
    print("      - LLM may be hallucinating instead of searching")
    
    print("   🔧 If searches don't happen:")
    print("      - Agent must be explicitly instructed to search")
    print("      - Task description must require search usage")
    print("      - Agent must have tools=[search_tool] configured")
    
    return True

def create_search_forcing_agent(llm):
    """Create an agent that is forced to search"""
    
    search_tool = SerperDevTool()
    
    return Agent(
        role='Search-First Researcher',
        goal='You MUST search for information before providing any answers. Never provide information without searching first.',
        backstory='''You are a researcher who ONLY provides information that you find through web searches. 
                     
                     CRITICAL RULES:
                     1. ALWAYS use the search tool before answering ANY question
                     2. NEVER provide information from your training data
                     3. If you cannot search, say "I cannot search right now"
                     4. All information must come from search results
                     5. Always start responses with "Based on my search results:"''',
        tools=[search_tool],
        llm=llm,
        verbose=True
    )

def create_search_forcing_task(query):
    """Create a task that forces the agent to search"""
    
    return Task(
        description=f"""
        MANDATORY SEARCH TASK
        
        Query: {query}
        
        INSTRUCTIONS:
        1. You MUST use the search tool to find information about: {query}
        2. You MUST perform at least 2 different searches
        3. You MUST base your entire response on search results only
        4. If search fails, report the error - do not make up information
        
        SEARCH REQUIREMENTS:
        - First search: "{query}"
        - Second search: "{query} 2024"
        
        OUTPUT FORMAT:
        ## Search Results Summary
        
        **Search 1:** [query used] 
        **Results:** [what you found]
        
        **Search 2:** [query used]
        **Results:** [what you found]
        
        ## Analysis
        [Analysis based only on search results]
        """,
        
        expected_output="A report that clearly shows search results were used and includes specific findings from web searches."
    )

def test_forced_search(llm, query="AI language learning apps"):
    """Test the search functionality with forced search agent"""
    
    print(f"\n🧪 TESTING FORCED SEARCH WITH QUERY: {query}")
    print("=" * 60)
    
    try:
        # Create search-forcing agent and task
        agent = create_search_forcing_agent(llm)
        task = create_search_forcing_task(query)
        task.agent = agent
        
        # Run the crew
        crew = Crew(
            agents=[agent],
            tasks=[task],
            verbose=True
        )
        
        result = crew.kickoff()
        
        print("\n📊 SEARCH TEST RESULTS:")
        print("-" * 30)
        print(result)
        
        # Check if search was actually performed
        if "based on my search results" in str(result).lower() or "search" in str(result).lower():
            print("\n✅ Search appears to have been performed!")
        else:
            print("\n❌ Search may not have been performed - check agent behavior")
            
    except Exception as e:
        print(f"\n❌ Forced search test failed: {e}")

# Main diagnostic function
def run_full_diagnostic(llm=None):
    """Run complete diagnostic"""
    
    # Basic diagnostic
    basic_ok = diagnose_search_issues()
    
    if basic_ok and llm:
        # Advanced test with LLM
        test_forced_search(llm)
    elif basic_ok:
        print("\n💡 Basic search functionality works!")
        print("   To test agent integration, provide your LLM configuration")
    
    print("\n🎯 TROUBLESHOOTING CHECKLIST:")
    print("   □ SERPER_API_KEY environment variable set")
    print("   □ SerperDevTool can be imported")
    print("   □ Direct search returns results")
    print("   □ Agent has tools=[search_tool] configured")
    print("   □ Task explicitly requires searching")
    print("   □ Agent backstory emphasizes search usage")

if __name__ == "__main__":
    # Run basic diagnostic
    run_full_diagnostic()
    
    print("\n" + "="*60)
    print("🔧 QUICK FIXES FOR COMMON ISSUES:")
    print("="*60)
    print("1. Agent not searching:")
    print("   - Add 'You MUST use the search tool' to agent backstory")
    print("   - Make task description require specific searches")
    print("   - Use verbose=True to see what agent is doing")
    
    print("\n2. Search returning asterisks:")
    print("   - Agent is hallucinating instead of using tools")
    print("   - Strengthen the 'must search' instructions")
    print("   - Reduce max_iterations to force faster tool usage")
    
    print("\n3. Generic/wrong information:")
    print("   - Agent using training data instead of search")
    print("   - Add 'NEVER use training data' to backstory")
    print("   - Require search results to be cited in output")