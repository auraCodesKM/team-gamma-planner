# TripPlanner (Team Gamma)

**Problem.** Planning a short trip means juggling distances, budgets and day plans across many tabs.

**Solution.** A multi-agent planner: a **researcher** agent gathers facts with tools, then a **writer** agent turns them into a day-by-day itinerary.

## Architecture
```
graph.py (LangGraph StateGraph)
  research  -- ReAct agent with tools: distance(a, b), budget(total, days)
     |
  write     -- ReAct agent, no tools: writes the itinerary
     |
   END       checkpointer: MemorySaver, recursion_limit 12
tools.py: deterministic tools (great-circle distance, budget split)
```

## Claims
- Two agents with a clear hand-off: the researcher delegates to the writer through the graph.
- Agent tools are deterministic and **unit-tested in CI** (`tests/test_tools.py`, GitHub Actions on every push).
- Bounded agents: a recursion limit and a memory checkpointer.
- Running the agents needs `OPENAI_API_KEY`; the tool tests do not.

## Run locally
```bash
pip install -r requirements.txt
pytest -q                                # tool tests, no key needed
OPENAI_API_KEY=... python graph.py       # full plan: 3 days Delhi -> Jaipur on 15000 INR
```

---
*Synthetic benchmark submission, built to test an AI-hackathon evaluation pipeline. Not a real team's project.*
