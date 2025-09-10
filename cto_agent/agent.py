"""
CTO Agent - Core implementation of the Chief Technology Officer AI agent.
"""
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from datetime import datetime
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class TechnologyTrend:
    """Represents an emerging technology trend relevant to the organization."""
    name: str
    category: str
    maturity: str  # e.g., 'emerging', 'growth', 'mature', 'declining'
    potential_impact: str  # High, Medium, Low
    description: str
    relevant_use_cases: List[str]
    last_updated: str = field(default_factory=lambda: datetime.utcnow().isoformat())

class CTOAgent:
    """
    An AI-powered Chief Technology Officer agent that provides strategic technical
    leadership and decision-making capabilities.
    """
    
    def __init__(self, company_name: str, industry: str, tech_stack: Optional[Dict] = None):
        """
        Initialize the CTO Agent.
        
        Args:
            company_name: Name of the company
            industry: Industry the company operates in
            tech_stack: Current technology stack (optional)
        """
        self.company_name = company_name
        self.industry = industry
        self.tech_stack = tech_stack or {}
        self.technology_portfolio: Dict[str, TechnologyTrend] = {}
        self.strategic_goals: List[Dict] = []
        self.team_structure: Dict = {}
        self.budget_allocation: Dict = {}
        self._init_default_technologies()
        
    def _init_default_technologies(self):
        """Initialize with some default technology trends."""
        default_techs = [
            TechnologyTrend(
                name="AI/ML",
                category="Artificial Intelligence",
                maturity="growth",
                potential_impact="High",
                description="Advancements in machine learning and AI are transforming business operations.",
                relevant_use_cases=["automation", "predictive analytics", "personalization"]
            ),
            TechnologyTrend(
                name="Cloud Native",
                category="Cloud Computing",
                maturity="mature",
                potential_impact="High",
                description="Cloud-native technologies enable scalable and resilient applications.",
                relevant_use_cases=["microservices", "containers", "serverless"]
            )
        ]
        
        for tech in default_techs:
            self.technology_portfolio[tech.name] = tech
    
    def set_strategic_goals(self, goals: List[Dict]):
        """
        Set the strategic goals for the organization.
        
        Args:
            goals: List of goal dictionaries with 'name', 'description', 'timeframe', 'priority'
        """
        self.strategic_goals = goals
        logger.info(f"Updated strategic goals: {[g['name'] for g in goals]}")
    
    def assess_technology(self, technology_name: str, business_context: Dict) -> Dict:
        """
        Assess a technology's fit for the organization.
        
        Args:
            technology_name: Name of the technology to assess
            business_context: Business context for the assessment
            
        Returns:
            Dict containing assessment results
        """
        tech = self.technology_portfolio.get(technology_name)
        if not tech:
            return {"status": "unknown", "message": f"No data on {technology_name}"}
            
        assessment = {
            "technology": tech.name,
            "maturity": tech.maturity,
            "potential_impact": tech.potential_impact,
            "recommendation": "",
            "rationale": ""
        }
        
        # Simple assessment logic - can be enhanced
        if tech.maturity == "emerging" and tech.potential_impact == "High":
            assessment["recommendation"] = "Monitor and consider pilot projects"
            assessment["rationale"] = "High potential impact warrants monitoring despite emerging status"
        elif tech.maturity == "mature" and tech.potential_impact in ["High", "Medium"]:
            assessment["recommendation"] = "Strong candidate for adoption"
            assessment["rationale"] = "Mature technology with significant potential impact"
        else:
            assessment["recommendation"] = "Evaluate case-by-case"
            assessment["rationale"] = "Needs further evaluation based on specific use cases"
            
        return assessment
    
    def make_decision(self, decision_context: Dict) -> Dict:
        """
        Make a strategic technology decision.
        
        Args:
            decision_context: Context for the decision including options and criteria
            
        Returns:
            Dict containing the decision and rationale
        """
        # This is a simplified decision-making framework
        options = decision_context.get("options", [])
        criteria = decision_context.get("criteria", ["strategic_alignment", "cost", "risk"])
        
        if not options:
            return {"decision": None, "rationale": "No options provided for decision"}
            
        # Simple scoring mechanism - can be enhanced
        scored_options = []
        for option in options:
            score = 0
            if "strategic_alignment" in criteria:
                score += option.get("strategic_alignment_score", 0) * 0.5
            if "cost" in criteria:
                score += (1 - min(option.get("cost_score", 0.5), 1)) * 0.3
            if "risk" in criteria:
                score += (1 - min(option.get("risk_score", 0.5), 1)) * 0.2
                
            scored_options.append({
                "option": option,
                "score": score
            })
        
        # Sort by score descending
        scored_options.sort(key=lambda x: x["score"], reverse=True)
        
        best_option = scored_options[0]
        return {
            "decision": best_option["option"],
            "score": best_option["score"],
            "rationale": f"Selected option based on criteria: {', '.join(criteria)}",
            "all_options": scored_options
        }
    
    def generate_roadmap(self, timeframe: str = "1y") -> Dict:
        """
        Generate a technology roadmap.
        
        Args:
            timeframe: Timeframe for the roadmap (e.g., '6m', '1y', '3y')
            
        Returns:
            Dict containing the technology roadmap
        """
        # This is a simplified roadmap generation
        roadmap = {
            "timeframe": timeframe,
            "initiatives": [
                {
                    "name": "Cloud Migration",
                    "description": "Migrate on-premises infrastructure to cloud",
                    "timeline": "Q1-Q2",
                    "priority": "High"
                },
                {
                    "name": "AI/ML Integration",
                    "description": "Implement AI/ML capabilities for business processes",
                    "timeline": "Q2-Q3",
                    "priority": "High"
                },
                {
                    "name": "DevOps Maturity",
                    "description": "Enhance CI/CD pipelines and automation",
                    "timeline": "Q3-Q4",
                    "priority": "Medium"
                }
            ],
            "key_technologies": ["Cloud Services", "AI/ML Platforms", "Containerization", "IaC"],
            "budget_allocation": {
                "cloud_infrastructure": 40,
                "talent_acquisition": 30,
                "training_development": 15,
                "rnd": 15
            }
        }
        
        return roadmap
    
    def communicate_strategy(self, audience: str = "executive") -> str:
        """
        Generate a communication about the technology strategy.
        
        Args:
            audience: Target audience ('executive', 'technical', 'board')
            
        Returns:
            Formatted strategy communication
        """
        if audience == "executive":
            return (
                f"As the CTO of {self.company_name}, our technology strategy is focused on "
                f"driving business value through innovation in the {self.industry} sector. "
                "Our key priorities include digital transformation, cloud adoption, and "
                "leveraging AI/ML for competitive advantage."
            )
        elif audience == "technical":
            return (
                "Our technical strategy emphasizes scalable architecture, developer "
                "productivity, and operational excellence. We're investing in modern "
                "practices like DevOps, cloud-native development, and continuous "
                "learning to build a future-ready technology organization."
            )
        else:  # board
            return (
                f"The technology strategy for {self.company_name} is designed to support "
                f"our business objectives in the {self.industry} market. Through strategic "
                "investments in digital capabilities, we aim to drive innovation, "
                "operational efficiency, and sustainable growth."
            )

    def to_dict(self) -> Dict[str, Any]:
        """Convert the CTO agent's state to a dictionary."""
        return {
            "company_name": self.company_name,
            "industry": self.industry,
            "tech_stack": self.tech_stack,
            "strategic_goals": self.strategic_goals,
            "technology_portfolio": {
                name: {
                    "category": tech.category,
                    "maturity": tech.maturity,
                    "potential_impact": tech.potential_impact,
                    "description": tech.description,
                    "relevant_use_cases": tech.relevant_use_cases,
                    "last_updated": tech.last_updated
                } for name, tech in self.technology_portfolio.items()
            },
            "team_structure": self.team_structure,
            "budget_allocation": self.budget_allocation
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CTOAgent':
        """Create a CTOAgent instance from a dictionary."""
        agent = cls(
            company_name=data["company_name"],
            industry=data["industry"],
            tech_stack=data.get("tech_stack", {})
        )
        
        agent.strategic_goals = data.get("strategic_goals", [])
        agent.team_structure = data.get("team_structure", {})
        agent.budget_allocation = data.get("budget_allocation", {})
        
        # Rebuild technology portfolio
        agent.technology_portfolio = {}
        for name, tech_data in data.get("technology_portfolio", {}).items():
            agent.technology_portfolio[name] = TechnologyTrend(
                name=name,
                category=tech_data["category"],
                maturity=tech_data["maturity"],
                potential_impact=tech_data["potential_impact"],
                description=tech_data["description"],
                relevant_use_cases=tech_data["relevant_use_cases"],
                last_updated=tech_data.get("last_updated", datetime.utcnow().isoformat())
            )
            
        return agent
    
    def save_state(self, filepath: str):
        """Save the agent's state to a JSON file."""
        with open(filepath, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)
        logger.info(f"Agent state saved to {filepath}")
    
    @classmethod
    def load_state(cls, filepath: str) -> 'CTOAgent':
        """Load an agent's state from a JSON file."""
        with open(filepath, 'r') as f:
            data = json.load(f)
        return cls.from_dict(data)
