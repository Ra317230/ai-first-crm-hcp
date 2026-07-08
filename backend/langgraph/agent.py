from langgraph.graph import StateGraph

class AgentState(dict):
    pass

def log_interaction(state):
    state["result"] = "Interaction logged successfully."
    return state

def edit_interaction(state):
    state["result"] = "Interaction updated successfully."
    return state

graph = StateGraph(AgentState)

graph.add_node("log_interaction", log_interaction)
graph.add_node("edit_interaction", edit_interaction)

graph.set_entry_point("log_interaction")

app = graph.compile()