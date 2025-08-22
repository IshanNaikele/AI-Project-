import streamlit as st
import requests
import json
import time

# FIXED: Updated endpoint to match your FastAPI backend
FASTAPI_URL = "http://127.0.0.1:8000/generate-strategy"

st.set_page_config(
    page_title="The AI Strategist",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced CSS for better UX
st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
            padding: 2rem;
        }
        .stButton>button {
            width: 100%;
            border-radius: 0.5rem;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            color: white;
            font-size: 1.2rem;
            font-weight: 600;
            height: 3rem;
            border: none;
            transition: all 0.3s;
        }
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        .stTextInput>div>div>input, .stTextArea>div>div>textarea, .stSelectbox>div>div>div, .stNumberInput>div>div>input {
            border-radius: 0.5rem;
            border: 2px solid #e9ecef;
        }
        .agent-step {
            background: white;
            padding: 1rem;
            border-radius: 0.5rem;
            border-left: 4px solid #667eea;
            margin: 1rem 0;
        }
        .success-box {
            background: #d4edda;
            border: 1px solid #c3e6cb;
            border-radius: 0.5rem;
            padding: 1rem;
            margin: 1rem 0;
        }
        .debug-info {
            background: #f8f9fa;
            border: 1px solid #dee2e6;
            border-radius: 0.5rem;
            padding: 1rem;
            margin: 1rem 0;
            font-size: 0.9rem;
        }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("""
# 🚀 The AI Strategist
### A Multi-Agent System for Personalized Strategic Planning
*Transform your raw ideas into tailored, executable strategies*
""")

st.markdown("---")

# Input Section
col1, col2 = st.columns([2, 1])

with col1:
    st.header("📝 Project Details")
    hackathon_theme = st.text_input(
        "Hackathon Theme", 
        value="AI in Education",
        help="What's the main theme or focus area?"
    )
    raw_idea = st.text_area(
        "Your Raw Idea", 
        value="An AI-powered app to help students learn new languages.",
        height=100,
        help="Describe your initial concept or idea"
    )

with col2:
    st.header("👥 Team Setup")
    team_strength = st.selectbox(
        "Team's Core Strength",
        ("Frontend", "Backend", "AI/ML", "Full-Stack"),
        help="What is your team best at? This will tailor the strategy."
    )
    # NEW: Add hackathon duration input
    hackathon_duration = st.number_input(
        "Hackathon Duration (in hours)",
        min_value=1,
        max_value=168,  # A week-long hackathon
        value=24,
        help="The total time available for the hackathon."
    )
    
    # Show what each strength means
    strength_info = {
        "Frontend": "🎨 UI/UX focused, responsive design, user experience",
        "Backend": "⚙️ Server logic, APIs, databases, data processing", 
        "AI/ML": "🤖 Algorithms, models, data science, machine learning",
        "Full-Stack": "🔧 Balanced frontend and backend capabilities"
    }
    st.info(strength_info[team_strength])

# Debug toggle (optional - can be removed in production)
show_debug = st.sidebar.checkbox("Show Debug Info", value=True)  # Default to True for troubleshooting

# Generate Strategy Button
if st.button("🎯 Generate Personalized Strategy", type="primary"):
    # MODIFICATION: Updated payload structure to include hackathon_duration
    payload = {
        "theme": hackathon_theme,
        "idea": raw_idea, 
        "team_strength": team_strength,
        "hackathon_duration": hackathon_duration # <-- NEW FIELD
    }

    st.markdown("---")
    
    # Progress tracking
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Agent workflow visualization
    agents = [
        ("🔍 Research Agent", "Analyzing market and competitors..."),
        ("🎯 Critical Agent", "Identifying risks and challenges..."),
        ("🏗️ Solution Architect", f"Designing MVP for {team_strength} team..."),
        ("📢 Pitch Agent", "Creating compelling presentation...")
    ]
    
    agent_containers = []
    for i, (agent_name, description) in enumerate(agents):
        container = st.empty()
        agent_containers.append(container)
    
    try:
        # Show workflow progress
        for i, (agent_name, description) in enumerate(agents):
            progress_bar.progress((i) / len(agents))
            status_text.text(f"Step {i+1}/4: {description}")
            
            agent_containers[i].markdown(f"""
                <div class="agent-step">
                    <strong>{agent_name}</strong><br>
                    <em>{description}</em>
                </div>
            """, unsafe_allow_html=True)
            
            time.sleep(0.5)  # Visual delay
        
        progress_bar.progress(1.0)
        status_text.text("🚀 Sending request to AI Strategist...")
        
        # Send request to FastAPI backend
        response = requests.post(FASTAPI_URL, json=payload, timeout=600)
        
        if response.status_code == 200:
            data = response.json()
            
            # Debug info display
            if show_debug:
                st.markdown('<div class="debug-info">', unsafe_allow_html=True)
                st.subheader("🔍 Debug Information")
                st.write("**Response Keys:**", list(data.keys()) if isinstance(data, dict) else "Not a dict")
                st.write("**Success Status:**", data.get("success", "Key not found"))
                
                # Check what pitch-related keys exist
                pitch_keys = [key for key in data.keys() if 'pitch' in key.lower()]
                st.write("**Pitch-related Keys:**", pitch_keys)
                
                # Show lengths of all text outputs
                text_outputs = {}
                for key in ['research', 'critical_analysis', 'mvp_plan', 'pitch', 'pitch_strategy']:
                    if key in data:
                        text_outputs[key] = len(str(data[key])) if data[key] else 0
                st.write("**Output Lengths:**", text_outputs)
                st.markdown('</div>', unsafe_allow_html=True)
            
            if data.get("success"):
                progress_bar.progress(1.0)
                status_text.text("✅ Strategy generated successfully!")
                
                # Display results in organized sections
                st.markdown("---")
                st.markdown('<div class="success-box"><h2>🎉 Your Personalized Strategy is Ready!</h2></div>', unsafe_allow_html=True)
                
                # FIXED: Check for both possible pitch keys and use the correct one
                pitch_content = data.get("pitch_strategy") or data.get("pitch") or "No pitch content available"
                
                # Create tabs for different outputs
                tab1, tab2, tab3, tab4 = st.tabs(["📊 Market Research", "⚠️ Risk Analysis", "🏗️ MVP Plan", "🎯 Pitch Deck"])
                
                with tab1:
                    st.subheader("Market Research")
                    research_content = data.get("research", "No research data available")
                    if research_content and len(research_content.strip()) > 10:
                        st.markdown(research_content)
                    else:
                        st.warning("Research content appears to be empty or very short.")
                        if show_debug:
                            st.code(f"Raw content: {repr(research_content)}")
                
                with tab2:
                    st.subheader("Critical Risk Analysis")
                    critical_content = data.get("critical_analysis", "No critical analysis available")
                    if critical_content and len(critical_content.strip()) > 10:
                        st.markdown(critical_content)
                    else:
                        st.warning("Critical analysis content appears to be empty or very short.")
                        if show_debug:
                            st.code(f"Raw content: {repr(critical_content)}")
                
                with tab3:
                    st.subheader(f"MVP Plan (Optimized for {team_strength} Team)")
                    mvp_content = data.get("mvp_plan", "No MVP plan available")
                    if mvp_content and len(mvp_content.strip()) > 10:
                        st.markdown(mvp_content)
                    else:
                        st.warning("MVP plan content appears to be empty or very short.")
                        if show_debug:
                            st.code(f"Raw content: {repr(mvp_content)}")
                
                with tab4:
                    st.subheader("Pitch Presentation")
                    # FIXED: Use the correct pitch content
                    if pitch_content and len(str(pitch_content).strip()) > 10:
                        st.markdown(str(pitch_content))
                    else:
                        st.error("⚠️ Pitch agent produced empty content. This is a backend extraction issue.")
                        
                        # Provide a fallback pitch template based on available data
                        st.info("📝 **Generating Fallback Pitch Strategy:**")
                        
                        fallback_pitch = f"""
## 🎯 Pitch Strategy for {team_strength} Team

### The Problem
Based on the theme "{hackathon_theme}", there's a clear need for innovative solutions.

### Our Solution
**{raw_idea}**

### Why Our {team_strength} Team Will Win

**Team Advantage:** {strength_info[team_strength]}

### 3-Minute Demo Structure
1. **Hook (30s):** Start with the core problem demonstration
2. **Solution (90s):** Live demo of key features showcasing {team_strength.lower()} expertise  
3. **Impact (45s):** Market potential and next steps
4. **Q&A (15s):** Handle technical questions

### Key Talking Points
- Emphasize technical execution quality (your {team_strength.lower()} strength)
- Show measurable impact/metrics if possible
- Demonstrate scalability and market fit
- Address feasibility within {hackathon_duration} hours

### Presentation Tips
- Start with a compelling story/problem statement
- Use visuals and live demo (avoid slides-heavy presentations)
- Practice smooth transitions between team members
- Prepare for technical deep-dive questions
- End with clear next steps and vision

*Note: This is a fallback strategy. The AI pitch agent needs debugging in the backend.*
"""
                        
                        st.markdown(fallback_pitch)
                        
                        if show_debug:
                            st.markdown("---")
                            st.subheader("🔧 Debug Information")
                            st.code(f"Raw pitch content: {repr(pitch_content)}")
                            st.code(f"Available keys: {list(data.keys())}")
                            # Show all keys containing 'pitch'
                            pitch_debug = {k: v for k, v in data.items() if 'pitch' in k.lower()}
                            st.json(pitch_debug)
                            
                            st.warning("""
                            **Backend Issue Identified:**
                            - Pitch agent runs successfully (no errors)
                            - But `extract_clean_output()` returns empty string for pitch agent
                            - Likely issue: Pitch agent result structure differs from other agents
                            - Check orchestrator logs for pitch agent extraction methods
                            """)
                        
                        # Update pitch_content for download to use fallback
                        pitch_content = fallback_pitch
                
                # Show execution summary
                if data.get("summary"):
                    st.markdown("---")
                    st.subheader("📈 Execution Summary")
                    summary = data["summary"]
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Feasibility", summary.get("feasibility", "Unknown"))
                    with col2:
                        st.metric("Execution Time", summary.get("execution_time", "Unknown"))
                    with col3:
                        st.metric("LLM Used", "Groq + Ollama" if summary.get("groq_used") else "Ollama Only")
                    
                    st.info(f"**Competitive Edge:** {summary.get('competitive_edge', 'Unknown')}")
                
                # Download option
                if st.button("📥 Download Complete Strategy"):
                    strategy_text = f"""
# AI Strategist Output

**Theme:** {hackathon_theme}
**Idea:** {raw_idea}
**Team Strength:** {team_strength}
**Hackathon Duration:** {hackathon_duration} hours

## Market Research
{data.get("research", "N/A")}

## Risk Analysis  
{data.get("critical_analysis", "N/A")}

## MVP Plan
{data.get("mvp_plan", "N/A")}

## Pitch Strategy
{pitch_content}

## Execution Summary
- **Feasibility:** {data.get("summary", {}).get("feasibility", "Unknown")}
- **Competitive Edge:** {data.get("summary", {}).get("competitive_edge", "Unknown")}
- **Execution Time:** {data.get("summary", {}).get("execution_time", "Unknown")}
- **LLM Configuration:** {data.get("llm_config", {})}
"""
                    st.download_button(
                        label="Download Strategy.md",
                        data=strategy_text,
                        file_name=f"ai_strategist_{team_strength}_{int(time.time())}.md",
                        mime="text/markdown"
                    )
                    
            else:
                st.error(f"❌ Strategy generation failed: {data.get('error', 'Unknown error')}")
                if show_debug:
                    st.code(str(data))
                    
        else:
            st.error(f"❌ Backend error (Status {response.status_code})")
            if show_debug:
                try:
                    error_data = response.json()
                    st.code(str(error_data))
                except:
                    st.code(response.text)
            st.error("Make sure FastAPI server is running on http://127.0.0.1:8000")

    except requests.exceptions.ConnectionError:
        st.error("❌ Connection failed. Please start your FastAPI server:")
        st.code("python backend/api.py", language="bash")
        
    except requests.exceptions.Timeout:
        st.error("⏱️ Request timed out. The AI agents might be taking too long.")
        st.info("Try with a simpler idea or check your Ollama server.")
        
    except Exception as e:
        st.error(f"❌ Unexpected error: {str(e)}")
        if show_debug:
            st.exception(e)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6c757d; font-size: 0.9rem;">
    <p>🤖 Powered by Multi-Agent AI • Built for Hackathon Success</p>
</div>
""", unsafe_allow_html=True)