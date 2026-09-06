from pydantic import BaseModel, Field
from typing import List, Dict, Any
import statistics

class AnalyticsInput(BaseModel):
    numbers: List[float] = Field(description="List of numbers to analyze.")
def simple_analytics_tool(numbers: List[float], operation: str = "all") -> Dict[str, Any]:
    """Computes specific or all analytics metrics for a list of numbers."""
    if not numbers:
        return {"error": "Input list is empty or invalid."}
    
    try:
        op = operation.lower().strip()

        if op == "average":
            return {"average": statistics.mean(numbers)}
        elif op in ["max", "maximum"]:
            return {"maximum": max(numbers)}
        elif op in ["min", "minimum"]:
            return {"minimum": min(numbers)}
        elif op == "count":
            return {"count": len(numbers)}
        

        return {
            "count": len(numbers),
            "average": statistics.mean(numbers),
            "maximum": max(numbers),
            "minimum": min(numbers)
        }
    except Exception as e:
        return {"error": str(e)}