"""
Principal Software Engineer Agent Demo
"""
import os
import sys
from pathlib import Path

# Add the parent directory to the path so we can import the principal_se package
sys.path.append(str(Path(__file__).parent.parent))

from principal_se.agent import PrincipalSE, ArchitecturePattern, Technology, CodeReviewFinding

def main():
    # Initialize the Principal Software Engineer agent
    print("Initializing Principal Software Engineer agent...")
    principal = PrincipalSE(
        name="Alex Johnson",
        expertise=["Cloud Architecture", "Distributed Systems", "DevOps"],
        experience_years=15
    )
    
    # Add some technologies to evaluate
    print("\n=== Evaluating Technologies ===")
    rust_tech = Technology(
        name="Rust",
        category="Programming Language",
        maturity="growth",
        adoption_level="pilot",
        description="A language empowering everyone to build reliable and efficient software.",
        pros=["Memory safety without garbage collection", "Performance", "Concurrency"],
        cons=["Steep learning curve", "Longer compile times"],
        use_cases=["System programming", "Performance-critical applications", "WebAssembly"]
    )
    
    # Evaluate a technology
    evaluation = principal.evaluate_technology("Rust", {
        "requirements": ["performance-critical", "memory safety", "concurrency"]
    })
    
    print(f"Evaluation for {evaluation['technology']}:")
    print(f"- Maturity: {evaluation['maturity']}")
    print(f"- Fit Score: {evaluation['fit_score']}/10")
    print(f"- Recommendation: {evaluation['recommendation']}")
    print(f"- Rationale: {evaluation['rationale']}")
    
    # Generate a system design
    print("\n=== Generating System Design ===")
    requirements = {
        "name": "E-commerce Platform",
        "scale": "large",
        "availability": "99.99%",
        "features": ["product catalog", "shopping cart", "payment processing", "recommendations"]
    }
    
    design = principal.design_system(requirements)
    print(f"Designed system: {design.name}")
    print(f"Architecture patterns: {[p.value for p in design.patterns]}")
    
    # Code review example
    print("\n=== Code Review Example ===")
    sample_code = """
    def process_payment(user_id, payment_details):
        # Process payment
        if payment_details['amount'] > 1000:
            # Hardcoded API key - security issue
            api_key = "sk_test_1234567890abcdef"
            result = payment_gateway.charge(api_key, payment_details)
            return result
        return None
    """
    
    findings = principal.review_code(sample_code, "python")
    print(f"Found {len(findings)} issues in the code:")
    for i, finding in enumerate(findings, 1):
        print(f"{i}. [{finding.severity.upper()}] {finding.description}")
        print(f"   Recommendation: {finding.recommendation}")
    
    # Mentor a junior engineer
    print("\n=== Mentoring Example ===")
    question = "How should I approach designing a scalable notification service?"
    print(f"Question: {question}")
    print(f"Mentor's Response: {principal.mentor_junior_engineer(question)}")
    
    # Generate a technology radar
    print("\n=== Technology Radar ===")
    radar = principal.generate_tech_radar()
    for category, techs in radar.items():
        if category != "last_updated":
            print(f"\n{category.upper()}:")
            for tech in techs:
                print(f"- {tech}")
    
    # Save the agent's state
    os.makedirs("data", exist_ok=True)
    principal.save_state("data/principal_se_state.json")
    print("\nAgent state saved to 'data/principal_se_state.json'")

if __name__ == "__main__":
    main()
