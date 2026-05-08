from langgraph.graph import StateGraph, END

from state.agent_state import AgentState

from agents.coordinator_agent import coordinator_agent
from agents.research_agent import research_agent
from agents.news_agent import news_agent
from agents.report_agent import report_agent

print("\n========== CREATING GRAPH ==========")
workflow = StateGraph(AgentState)


workflow.add_node("coordinator", coordinator_agent)
workflow.add_node("research", research_agent)
workflow.add_node("news", news_agent)
workflow.add_node("report", report_agent)


workflow.set_entry_point("coordinator")


workflow.add_edge("coordinator", "research")
workflow.add_edge("research", "news")
workflow.add_edge("news", "report")
workflow.add_edge("report", END)


app = workflow.compile()

print("\n========== GRAPH CREATED ==========")
