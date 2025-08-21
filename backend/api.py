# ===================================
# backend/api.py - FastAPI Integration
# ===================================

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from backend.orchestrator import AIStrategistOrchestrator
import uvicorn

app = FastAPI(title="AI Strategist API", version="1.0.0")

# Add CORS middleware for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class StrategyRequest(BaseModel):
    theme: str
    idea: str
    team_strength: str

# Response model  
class StrategyResponse(BaseModel):
    success: bool
    research: str = ""
    critical_analysis: str = ""
    mvp_plan: str = ""
    pitch: str = ""
    team_strength: str = ""
    error: str = ""

# Initialize orchestrator globally
orchestrator = AIStrategistOrchestrator()

@app.get("/")
async def root():
    return {"message": "AI Strategist API is running!"}

@app.post("/generate-strategy", response_model=StrategyResponse)
async def generate_strategy(request: StrategyRequest):
    """
    Generate a personalized strategy based on team strength
    """
    try:
        # Validate team strength
        valid_strengths = ["Frontend", "Backend", "AI/ML", "Full-Stack"]
        if request.team_strength not in valid_strengths:
            raise HTTPException(
                status_code=400, 
                detail=f"Invalid team_strength. Must be one of: {valid_strengths}"
            )

        print(f"🎯 Generating strategy for {request.team_strength} team")
        print(f"Theme: {request.theme}")
        print(f"Idea: {request.idea}")

        # Run the workflow
        result = orchestrator.run_strategy_workflow(
            theme=request.theme,
            idea=request.idea,
            team_strength=request.team_strength
        )

        return StrategyResponse(**result)

    except Exception as e:
        print(f"❌ API Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "AI Strategist"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

# ===================================
# TESTING SCRIPT - test_workflow.py  
# ===================================

"""
# Create this file to test your workflow
from backend.orchestrator import AIStrategistOrchestrator

def test_personalization():
    orchestrator = AIStrategistOrchestrator()
    
    test_cases = [
        {"team": "Frontend", "expected": "UI/UX"},
        {"team": "AI/ML", "expected": "algorithm"},
        {"team": "Backend", "expected": "API"}
    ]
    
    for test in test_cases:
        print(f"\n{'='*50}")
        print(f"Testing {test['team']} team")
        print(f"{'='*50}")
        
        result = orchestrator.run_strategy_workflow(
            theme="AI in Education",
            idea="Language learning app",
            team_strength=test["team"]
        )
        
        if result["success"]:
            mvp = result["mvp_plan"]
            print(f"MVP: {mvp[:200]}...")
            
            if test["expected"].lower() in mvp.lower():
                print(f"✅ PASS: Found '{test['expected']}' in output")
            else:
                print(f"❌ FAIL: Missing '{test['expected']}' in output")
        else:
            print(f"❌ ERROR: {result['error']}")

if __name__ == "__main__":
    test_personalization()
"""