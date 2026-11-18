# TripPlanner (Team Gamma)

A multi-agent travel planner: a **researcher** agent gathers options with tools, and a **writer** agent turns them into an itinerary. Built with LangGraph.

- `graph.py`: two ReAct agents connected in a `StateGraph`, with a memory checkpointer and a recursion limit
- `tools.py`: deterministic tools (distance, budget split), unit-tested in CI
- Needs `OPENAI_API_KEY` to run the agents. The tool tests do not.


---
*Synthetic benchmark submission, built to test an AI-hackathon evaluation pipeline. Not a real team's project.*
