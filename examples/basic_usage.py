"""
Basic usage example for the CTO Agent.
"""
import os
import sys
from pathlib import Path

# Add the parent directory to the path so we can import the cto_agent package
sys.path.append(str(Path(__file__).parent.parent))

from cto_agent.agent import CTOAgent, TechnologyTrend

def main():
    # Initialize the CTO Agent for a fintech company
    print("Initializing CTO Agent for FinTech Innovations Inc...")
    cto = CTOAgent(
        company_name="FinTech Innovations Inc",
        industry="Financial Technology",
        tech_stack={
            "frontend": ["React", "TypeScript"],
            "backend": ["Python", "Node.js"],
            "database": ["PostgreSQL", "MongoDB"],
            "infrastructure": ["AWS", "Docker", "Kubernetes"]
        }
    )
    
    # Set strategic goals
    strategic_goals = [
        {
            "name": "Cloud-First Strategy",
            "description": "Migrate 100% of infrastructure to cloud-native solutions",
            "timeframe": "18 months",
            "priority": "High"
        },
        {
            "name": "AI/ML Integration",
            "description": "Implement AI/ML capabilities across all product lines",
            "timeframe": "24 months",
            "priority": "High"
        },
        {
            "name": "Developer Experience",
            "description": "Improve developer productivity and satisfaction",
            "timeframe": "12 months",
            "priority": "Medium"
        }
    ]
    cto.set_strategic_goals(strategic_goals)
    
    # Add a new technology trend
    blockchain = TechnologyTrend(
        name="Blockchain",
        category="Distributed Ledger",
        maturity="growth",
        potential_impact="High",
        description="Blockchain technology for secure and transparent financial transactions",
        relevant_use_cases=["smart contracts", "cross-border payments", "identity verification"]
    )
    cto.technology_portfolio[blockchain.name] = blockchain
    
    # Assess a technology
    print("\nAssessing Blockchain technology...")
    assessment = cto.assess_technology("Blockchain", {"business_unit": "Payments"})
    print(f"Assessment: {assessment['recommendation']}")
    print(f"Rationale: {assessment['rationale']}")
    
    # Make a strategic decision
    print("\nMaking a strategic decision about cloud providers...")
    decision = cto.make_decision({
        "options": [
            {
                "name": "AWS",
                "description": "Amazon Web Services",
                "strategic_alignment_score": 0.9,
                "cost_score": 0.7,
                "risk_score": 0.2
            },
            {
                "name": "Azure",
                "description": "Microsoft Azure",
                "strategic_alignment_score": 0.8,
                "cost_score": 0.6,
                "risk_score": 0.3
            },
            {
                "name": "GCP",
                "description": "Google Cloud Platform",
                "strategic_alignment_score": 0.7,
                "cost_score": 0.8,
                "risk_score": 0.4
            }
        ],
        "criteria": ["strategic_alignment", "cost", "risk"]
    })
    
    print(f"\nDecision: {decision['decision']['name']} (Score: {decision['score']:.2f})")
    print(f"Rationale: {decision['rationale']}")
    
    # Generate a technology roadmap
    print("\nGenerating a 1-year technology roadmap...")
    roadmap = cto.generate_roadmap("1y")
    print(f"Key initiatives:")
    for initiative in roadmap["initiatives"]:
        print(f"- {initiative['name']} ({initiative['priority']}): {initiative['description']}")
    
    # Communicate strategy to different audiences
    print("\nExecutive Summary:")
    print(cto.communicate_strategy("executive"))
    
    # Save the agent's state
    os.makedirs("data", exist_ok=True)
    cto.save_state("data/cto_agent_state.json")
    print("\nAgent state saved to 'data/cto_agent_state.json'")

if __name__ == "__main__":
    main()
