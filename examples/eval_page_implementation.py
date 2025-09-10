from principal_se.agent import PrincipalSE
from pathlib import Path

def evaluate_page_implementation():
    # Initialize the PrincipalSE agent
    principal = PrincipalSE(
        name="Frontend Architecture Expert",
        expertise=["Next.js", "TypeScript", "React", "Three.js", "Performance Optimization"]
    )
    
    # Files to evaluate
    files_to_review = [
        "app/page.tsx",
        "app/layout.tsx",
        "components/ThreeDBackground.tsx",
        "components/ErrorBoundary.tsx",
        "components/LoadingSpinner.tsx",
        "app/globals.css"
    ]
    
    # Read file contents
    file_contents = {}
    base_path = Path(__file__).parent.parent
    
    for file_path in files_to_review:
        try:
            with open(base_path / file_path, 'r') as f:
                file_contents[file_path] = f.read()
        except Exception as e:
            print(f"Error reading {file_path}: {str(e)}")
    
    # Prepare the evaluation request
    request = {
        "files": file_contents,
        "requirements": [
            "Code quality and best practices",
            "Performance optimizations",
            "Accessibility compliance",
            "Responsive design implementation",
            "Error handling and edge cases",
            "TypeScript type safety",
            "CSS architecture",
            "Component reusability"
        ]
    }
    
    # Get the evaluation
    evaluation = principal.evaluate_implementation(
        request=request,
        context={
            "framework": "Next.js 14",
            "typescript": True,
            "tailwind_css": True,
            "three_js": True
        }
    )
    
    return evaluation

if __name__ == "__main__":
    result = evaluate_page_implementation()
    print("\n" + "="*80)
    print("PRINCIPAL SOFTWARE ENGINEER EVALUATION")
    print("="*80)
    
    # Print overall assessment
    print("\nOVERALL ASSESSMENT:")
    print("-" * 40)
    print(result.get("overall_assessment", "No overall assessment provided"))
    
    # Print strengths
    print("\nSTRENGTHS:")
    print("-" * 40)
    for i, strength in enumerate(result.get("strengths", []), 1):
        print(f"{i}. {strength}")
    
    # Print recommendations
    print("\nRECOMMENDATIONS:")
    print("-" * 40)
    for i, rec in enumerate(result.get("recommendations", []), 1):
        print(f"{i}. {rec}")
    
    # Print critical issues
    if result.get("critical_issues"):
        print("\nCRITICAL ISSUES:")
        print("-" * 40)
        for i, issue in enumerate(result.get("critical_issues", []), 1):
            print(f"{i}. {issue}")
    
    # Print performance metrics if available
    if result.get("performance_metrics"):
        print("\nPERFORMANCE METRICS:")
        print("-" * 40)
        for metric, value in result.get("performance_metrics", {}).items():
            print(f"- {metric}: {value}")
