def coordinator_agent(state):
    print("\n========== COORDINATOR AGENT ==========")

    query = state["user_query"]

    print(f"Received request: {query}")
    print("Delegating work to specialist agents...")

    return {
        "messages": state.get("messages", []) + [
            "Coordinator delegated tasks"
        ]
    }
