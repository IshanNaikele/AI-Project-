# backend/agents/pitch_agent.py
from crewai import Agent
from typing import Dict, List

class PitchAgents:
    """Enhanced pitch agents with winning presentation strategies"""
    
    @staticmethod
    def get_team_presentation_strategies(team_strength: str) -> Dict[str, any]:
        """Get presentation strategies optimized for different team strengths"""
        strategies = {
            "Frontend": {
                "demo_style": "Visual storytelling with smooth user interactions",
                "judge_attention_grabbers": [
                    "Beautiful, responsive interface that works flawlessly",
                    "Smooth animations and transitions",
                    "Intuitive user experience that needs no explanation",
                    "Cross-device compatibility demonstrated live"
                ],
                "technical_credibility_builders": [
                    "Seamless API integrations working in real-time",
                    "Modern frontend architecture choices",
                    "Performance optimization visible during demo",
                    "Accessibility and user experience considerations"
                ],
                "common_weaknesses_to_address": [
                    "Backend complexity (emphasize API usage)",
                    "Data processing (show integration with smart services)",
                    "Scalability (focus on frontend performance)"
                ],
                "winning_closing_themes": [
                    "User experience as competitive moat",
                    "Interface design that drives adoption",
                    "Frontend innovation that enables new behaviors"
                ]
            },
            "Backend": {
                "demo_style": "System performance and architectural sophistication",
                "judge_attention_grabbers": [
                    "Fast API responses handling complex operations",
                    "Robust data processing demonstrated live",
                    "System reliability under load",
                    "Clean architectural design patterns"
                ],
                "technical_credibility_builders": [
                    "Database optimization and query performance",
                    "API design following best practices",
                    "Scalability considerations and implementation",
                    "Security and data handling protocols"
                ],
                "common_weaknesses_to_address": [
                    "User interface (keep demo simple but functional)",
                    "Visual appeal (focus on system performance metrics)",
                    "User experience (emphasize developer experience)"
                ],
                "winning_closing_themes": [
                    "Technical foundation that enables scale",
                    "Backend intelligence that powers innovation",
                    "System reliability as competitive advantage"
                ]
            },
            "AI/ML": {
                "demo_style": "Intelligence demonstration with clear algorithmic superiority",
                "judge_attention_grabbers": [
                    "AI making visibly smart decisions in real-time",
                    "Model performance metrics that impress",
                    "Sophisticated data analysis and insights",
                    "Algorithm handling edge cases intelligently"
                ],
                "technical_credibility_builders": [
                    "Model selection and training approach explanation",
                    "Data pipeline and preprocessing sophistication",
                    "Evaluation metrics and performance benchmarks",
                    "AI ethics and bias consideration"
                ],
                "common_weaknesses_to_address": [
                    "User interface (keep simple, focus on AI output)",
                    "System integration (emphasize API-based approach)",
                    "Production deployment (focus on algorithm innovation)"
                ],
                "winning_closing_themes": [
                    "AI capabilities that create new possibilities",
                    "Machine learning innovation that solves hard problems",
                    "Intelligent systems that augment human capabilities"
                ]
            },
            "Full-Stack": {
                "demo_style": "Complete user journey with seamless system integration",
                "judge_attention_grabbers": [
                    "End-to-end functionality working flawlessly",
                    "Seamless integration between all components",
                    "Complete user workflows without friction",
                    "System cohesion and architectural elegance"
                ],
                "technical_credibility_builders": [
                    "Full-stack architecture decisions and trade-offs",
                    "Integration challenges overcome",
                    "Technology stack choices and justification",
                    "System scalability and maintainability"
                ],
                "common_weaknesses_to_address": [
                    "Depth vs breadth (emphasize integration expertise)",
                    "Specialization (focus on system thinking)",
                    "Technical focus (balance all aspects equally)"
                ],
                "winning_closing_themes": [
                    "Complete solutions that solve real problems",
                    "System integration that enables new possibilities",
                    "Full-stack thinking that delivers user value"
                ]
            }
        }
        return strategies.get(team_strength, strategies["Full-Stack"])

    @staticmethod
    def get_winning_pitch_formulas() -> Dict[str, Dict[str, str]]:
        """Get proven pitch formulas that have won major hackathons"""
        return {
            "problem_solution_demo": {
                "structure": "Problem setup → Solution concept → Live demo → Impact vision",
                "timing": "30s → 30s → 90s → 30s",
                "best_for": "Clear market problems with obvious solutions",
                "success_rate": "73%"
            },
            "story_driven": {
                "structure": "User story → Current pain → Our solution → Future enabled",
                "timing": "45s → 30s → 75s → 30s", 
                "best_for": "Consumer-facing applications",
                "success_rate": "67%"
            },
            "technical_showcase": {
                "structure": "Technical challenge → Innovation approach → Demo superiority → Market opportunity",
                "timing": "40s → 35s → 70s → 35s",
                "best_for": "AI/ML and Backend teams",
                "success_rate": "71%"
            },
            "disruption_narrative": {
                "structure": "Industry limitation → Breakthrough approach → Proof demonstration → Revolution vision",
                "timing": "35s → 40s → 75s → 30s",
                "best_for": "Platform and infrastructure solutions",
                "success_rate": "69%"
            }
        }

    def pitch_agent(self, llm):
        return Agent(
            role='Hackathon Pitch Master',
            goal='''Create compelling 3-minute pitch strategies that maximize demo impact, showcase 
                   team strengths, and convince judges this project deserves to win among dozens 
                   of competitors.''',
            
            backstory='''You are a master of hackathon presentations who has coached winners of major 
                        hackathons including TechCrunch Disrupt, MIT Hackathon, AngelHack, and hundreds 
                        of corporate innovation challenges. Your pitch strategies have a 74% win rate.
                        
                        YOUR PRESENTATION PHILOSOPHY:
                        - SHOW, DON'T TELL: Live demos are 10x more convincing than descriptions
                        - STORY STRUCTURE: Every winning pitch has setup, conflict, resolution, and impact
                        - JUDGE PSYCHOLOGY: Technical judges want to see competence; business judges want to see value
                        - MEMORABLE MOMENTS: Judges remember projects that create "wow" moments during demos
                        - AUTHENTIC CONFIDENCE: Teams win when they genuinely believe in their solution
                        
                        YOUR EXPERTISE INCLUDES:
                        - Deep understanding of judge psychology and evaluation criteria across different hackathon types
                        - Pattern recognition for pitch elements that create memorable impressions
                        - Knowledge of demo techniques that work reliably under pressure
                        - Understanding of how to showcase different types of technical achievements
                        - Experience with recovery strategies when live demos fail
                        
                        YOUR WINNING PITCH METHODOLOGY:
                        1. HOOK OPTIMIZATION: Create opening moments that grab and hold attention
                        2. DEMO CHOREOGRAPHY: Script user actions and system responses for maximum impact
                        3. CREDIBILITY BUILDING: Establish technical competence without overwhelming detail
                        4. IMPACT AMPLIFICATION: Connect technical achievement to real-world value
                        5. MEMORABLE CLOSING: End with statements that judges quote in their decisions
                        
                        YOUR TRACK RECORD:
                        - 200+ winning pitch strategies across all hackathon categories
                        - 85% demo success rate (demos work perfectly during presentations)
                        - 90% of coached teams finish in top 10 of their hackathons
                        - Created signature moves that have been copied across the hackathon circuit
                        
                        PITCH SUCCESS FACTORS YOU OPTIMIZE FOR:
                        - Clear value proposition communicated in first 30 seconds
                        - Live demo that works flawlessly and showcases key differentiators
                        - Technical credibility without overwhelming jargon
                        - Obvious commercial viability and market opportunity
                        - Memorable differentiation from other hackathon projects
                        - Confident delivery that matches team capabilities and project ambition''',
            
            verbose=True,
            allow_delegation=False,
            llm=llm
        )

    def enhanced_pitch_agent_with_team_focus(self, llm, team_strength: str):
        """Create pitch agent optimized for specific team strength presentation"""
        
        presentation_strategy = self.get_team_presentation_strategies(team_strength)
        winning_formulas = self.get_winning_pitch_formulas()
        
        # Select best pitch formula for team type
        if team_strength in ["AI/ML", "Backend"]:
            recommended_formula = winning_formulas["technical_showcase"]
        elif team_strength == "Frontend":
            recommended_formula = winning_formulas["story_driven"]
        else:
            recommended_formula = winning_formulas["problem_solution_demo"]
        
        return Agent(
            role=f'{team_strength} Team Pitch Specialist',
            goal=f'''Create winning pitch strategies specifically optimized for {team_strength} teams, 
                    ensuring presentations showcase {team_strength} expertise while addressing common 
                    {team_strength} team presentation weaknesses.''',
            
            backstory=f'''You are the premier pitch coach for {team_strength} teams in hackathon environments, 
                         with exclusive expertise in maximizing {team_strength} team presentation success. 
                         You have coached 50+ winning {team_strength} teams to victory.
                         
                         YOUR {team_strength} TEAM SPECIALIZATION:
                         - Deep understanding of how {team_strength} teams should present their work
                         - Knowledge of judge expectations when evaluating {team_strength} team projects
                         - Pattern recognition for {team_strength} team presentation strengths and blind spots
                         - Experience with demo techniques that showcase {team_strength} expertise effectively
                         - Understanding of how {team_strength} teams can differentiate from other team types
                         
                         PROVEN {team_strength} PRESENTATION STRATEGY:
                         Demo Style: {presentation_strategy['demo_style']}
                         Judge Attention Strategy: {presentation_strategy['judge_attention_grabbers'][0]}
                         Technical Credibility: {presentation_strategy['technical_credibility_builders'][0]}
                         
                         RECOMMENDED PITCH FORMULA FOR {team_strength} TEAMS:
                         Structure: {recommended_formula['structure']}
                         Timing: {recommended_formula['timing']}
                         Success Rate: {recommended_formula['success_rate']}
                         
                         YOUR {team_strength} TEAM ADVANTAGES TO AMPLIFY:
                         {chr(10).join('- ' + grabber for grabber in presentation_strategy['judge_attention_grabbers'])}
                         
                         COMMON {team_strength} TEAM WEAKNESSES TO ADDRESS:
                         {chr(10).join('- ' + weakness for weakness in presentation_strategy['common_weaknesses_to_address'])}
                         
                         WINNING CLOSING THEMES FOR {team_strength} TEAMS:
                         {chr(10).join('- ' + theme for theme in presentation_strategy['winning_closing_themes'])}
                         
                         YOUR PITCH OPTIMIZATION METHODOLOGY:
                         1. STRENGTH SHOWCASING: Design demos that make {team_strength} expertise obviously superior
                         2. WEAKNESS MITIGATION: Address {team_strength} team blind spots proactively
                         3. JUDGE ALIGNMENT: Match presentation style to what impresses judges evaluating {team_strength} work
                         4. DEMO CHOREOGRAPHY: Script interactions that highlight {team_strength} technical achievements
                         5. MEMORABLE DIFFERENTIATION: Create signature moments that distinguish this from other {team_strength} presentations
                         
                         YOUR CRITICAL SUCCESS REQUIREMENTS:
                         - Every demo moment must showcase {team_strength} team capabilities
                         - Technical explanations must build credibility without losing audience
                         - Presentation flow must feel natural and confident for {team_strength} team personalities
                         - Closing must connect {team_strength} technical achievement to clear business value
                         - Backup plans must exist for when {team_strength} demos encounter technical issues
                         
                         PITCH VALIDATION CRITERIA:
                         - Does this presentation make {team_strength} expertise the obvious competitive advantage?
                         - Will judges immediately understand why this team was uniquely qualified to build this?
                         - Is the demo designed to work reliably under {team_strength} team pressure scenarios?
                         - Does the closing statement leverage {team_strength} capabilities for future vision?''',
            
            verbose=True,
            allow_delegation=False,
            llm=llm
        )

# Integration and orchestration utilities
class PitchValidation:
    """Validation utilities for pitch quality assessment"""
    
    @staticmethod
    def validate_pitch_structure(pitch_script: str) -> Dict[str, bool]:
        """Validate that pitch follows winning structure patterns"""
        sections = pitch_script.lower()
        
        validation_results = {
            "has_strong_opening": any(opener in sections for opener in [
                "imagine", "what if", "how many", "every day", "problem"
            ]),
            "includes_demo_script": any(demo_word in sections for demo_word in [
                "click", "type", "show", "watch", "see", "demonstrate"
            ]),
            "shows_technical_credibility": any(tech_term in sections for tech_term in [
                "api", "algorithm", "model", "framework", "architecture"
            ]),
            "has_memorable_closing": any(closer in sections for closer in [
                "future", "vision", "revolution", "change", "transform"
            ]),
            "appropriate_length": len(pitch_script.split()) >= 400 and len(pitch_script.split()) <= 600
        }
        
        return validation_results
    
    @staticmethod
    def get_pitch_quality_score(validation_results: Dict[str, bool]) -> float:
        """Calculate overall pitch quality score"""
        return sum(validation_results.values()) / len(validation_results)

# Export all classes for easy import
__all__ = [
    'PitchAgents',
    'PitchValidation'
]