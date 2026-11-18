from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, StateGraph
from langgraph.prebuilt import create_react_agent

import tools as t

model = ChatOpenAI(model="gpt-4o-mini")


@tool
def distance(a: str, b: str) -> float:
    """Great-circle distance between two cities in km."""
    return t.distance_km(a, b)


@tool
def budget(total: float, days: int) -> dict:
    """Split a trip budget per day."""
    return t.split_budget(total, days)


researcher = create_react_agent(model, tools=[distance, budget])
writer = create_react_agent(model, tools=[])

g = StateGraph(dict)
g.add_node("research", researcher)
g.add_node("write", writer)
g.set_entry_point("research")
g.add_edge("research", "write")
g.add_edge("write", END)
app = g.compile(checkpointer=MemorySaver())

if __name__ == "__main__":
    print(app.invoke({"messages": [("user", "Plan 3 days Delhi -> Jaipur on 15000 INR")]},
                     config={"recursion_limit": 12, "configurable": {"thread_id": "1"}}))
