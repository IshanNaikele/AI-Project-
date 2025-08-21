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
        .stTextInput>div>div>input, .stTextArea>div>div>textarea, .stSelectbox>div>div>div {
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
    
    # Show what each strength means
    strength_info = {
        "Frontend": "🎨 UI/UX focused, responsive design, user experience",
        "Backend": "⚙️ Server logic, APIs, databases, data processing", 
        "AI/ML": "🤖 Algorithms, models, data science, machine learning",
        "Full-Stack": "🔧 Balanced frontend and backend capabilities"
    }
    st.info(strength_info[team_strength])

# Generate Strategy Button
if st.button("🎯 Generate Personalized Strategy", type="primary"):
    # FIXED: Updated payload structure to match FastAPI backend
    payload = {
        "theme": hackathon_theme,
        "idea": raw_idea, 
        "team_strength": team_strength
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
        response = requests.post(FASTAPI_URL, json=payload, timeout=300)
        
        if response.status_code == 200:
            data = response.json()
            
            if data.get("success"):
                progress_bar.progress(1.0)
                status_text.text("✅ Strategy generated successfully!")
                
                # Display results in organized sections
                st.markdown("---")
                st.markdown('<div class="success-box"><h2>🎉 Your Personalized Strategy is Ready!</h2></div>', unsafe_allow_html=True)
                
                # Create tabs for different outputs
                tab1, tab2, tab3, tab4 = st.tabs(["📊 Market Research", "⚠️ Risk Analysis", "🏗️ MVP Plan", "🎯 Pitch Deck"])
                
                with tab1:
                    st.subheader("Market Research")
                    st.markdown(data.get("research", "No research data available"))
                
                with tab2:
                    st.subheader("Critical Risk Analysis")
                    st.markdown(data.get("critical_analysis", "No critical analysis available"))
                
                with tab3:
                    st.subheader(f"MVP Plan (Optimized for {team_strength} Team)")
                    st.markdown(data.get("mvp_plan", "No MVP plan available"))
                
                with tab4:
                    st.subheader("Pitch Presentation")
                    st.markdown(data.get("pitch", "No pitch available"))
                
                # Download option
                if st.button("📥 Download Complete Strategy"):
                    strategy_text = f"""
# AI Strategist Output

**Theme:** {hackathon_theme}
**Idea:** {raw_idea}
**Team Strength:** {team_strength}

## Market Research
{data.get("research", "N/A")}

## Risk Analysis  
{data.get("critical_analysis", "N/A")}

## MVP Plan
{data.get("mvp_plan", "N/A")}

## Pitch Deck
{data.get("pitch", "N/A")}
"""
                    st.download_button(
                        label="Download Strategy.md",
                        data=strategy_text,
                        file_name=f"ai_strategist_{team_strength}_{int(time.time())}.md",
                        mime="text/markdown"
                    )
                    
            else:
                st.error(f"❌ Strategy generation failed: {data.get('error', 'Unknown error')}")
        else:
            st.error(f"❌ Backend error (Status {response.status_code})")
            st.error("Make sure FastAPI server is running on http://127.0.0.1:8000")

    except requests.exceptions.ConnectionError:
        st.error("❌ Connection failed. Please start your FastAPI server:")
        st.code("python backend/api.py", language="bash")
        
    except requests.exceptions.Timeout:
        st.error("⏱️ Request timed out. The AI agents might be taking too long.")
        st.info("Try with a simpler idea or check your Ollama server.")
        
    except Exception as e:
        st.error(f"❌ Unexpected error: {str(e)}")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6c757d; font-size: 0.9rem;">
    <p>🤖 Powered by Multi-Agent AI • Built for Hackathon Success</p>
</div>
""", unsafe_allow_html=True)