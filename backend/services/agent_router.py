from backend.tools.calculator import calculate
from backend.tools.web_search import web_search


def route_query(query: str):
    """
    Decide which tool should handle the user's question.
    """

    query_lower = query.lower()

    # Calculator
    math_keywords = [
        "+", "-", "*", "/", "%",
        "calculate",
        "what is",
        "how much is"
    ]

    if any(keyword in query_lower for keyword in math_keywords):
        # Only route to calculator when the query looks mathematical
        if any(char.isdigit() for char in query):
            return {
                "tool": "calculator",
                "result": calculate(query)
            }

    # Web Search
    web_keywords = [
        "latest",
        "today",
        "current",
        "recent",
        "news",
        "search the web",
        "search online"
    ]

    if any(keyword in query_lower for keyword in web_keywords):
        return {
            "tool": "web_search",
            "result": web_search(query, 5)
        }

    # Default
    return {
        "tool": "rag",
        "result": None
    }  