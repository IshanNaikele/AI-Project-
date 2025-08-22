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

# MODIFICATION: Added hackathon_duration to the request model
class StrategyRequest(BaseModel):
    theme: str
    idea: str
    team_strength: str
    hackathon_duration: int # <-- NEW FIELD

# MODIFICATION: Added hackathon_duration to the response model for completeness
class StrategyResponse(BaseModel):
    success: bool
    research: str = ""
    critical_analysis: str = ""
    mvp_plan: str = ""
    pitch: str = ""
    team_strength: str = ""
    hackathon_duration: int = 0 # <-- NEW FIELD
    error: str = ""

# Initialize orchestrator globally
orchestrator = AIStrategistOrchestrator()

@app.get("/")
async def root():
    return {"message": "AI Strategist API is running!"}

# MODIFICATION: Updated endpoint to accept the new request model
@app.post("/generate-strategy", response_model=StrategyResponse)
async def generate_strategy(request: StrategyRequest):
    """
    Generate a personalized strategy based on team strength and hackathon duration.
    """
    try:
        # Validate team strength
        valid_strengths = ["Frontend", "Backend", "AI/ML", "Full-Stack"]
        if request.team_strength not in valid_strengths:
            raise HTTPException(
                status_code=400, 
                detail=f"Invalid team_strength. Must be one of: {valid_strengths}"
            )
        
        # MODIFICATION: Add validation for hackathon duration
        if request.hackathon_duration <= 0:
            raise HTTPException(
                status_code=400,
                detail="Hackathon duration must be a positive number."
            )

        print(f"🎯 Generating strategy for {request.team_strength} team for {request.hackathon_duration} hours")
        print(f"Theme: {request.theme}")
        print(f"Idea: {request.idea}")

        # MODIFICATION: Pass hackathon_duration to the orchestrator
        result = orchestrator.run_strategy_workflow(
            theme=request.theme,
            idea=request.idea,
            team_strength=request.team_strength,
            hackathon_duration=request.hackathon_duration # <-- NEW PARAMETER
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
    
    # MODIFICATION: Added hackathon_duration to test cases
    test_cases = [
        {"team": "Frontend", "expected": "UI/UX", "duration": 24},
        {"team": "AI/ML", "expected": "algorithm", "duration": 48},
        {"team": "Backend", "expected": "API", "duration": 9}
    ]
    
    for test in test_cases:
        print(f"\n{'='*50}")
        print(f"Testing {test['team']} team for a {test['duration']}-hour hackathon")
        print(f"{'='*50}")
        
        # MODIFICATION: Passed duration to run_strategy_workflow
        result = orchestrator.run_strategy_workflow(
            theme="AI in Education",
            idea="Language learning app",
            team_strength=test["team"],
            hackathon_duration=test["duration"]
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
