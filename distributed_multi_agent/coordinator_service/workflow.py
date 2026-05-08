from typing import TypedDict
import requests

from langgraph.graph import StateGraph, END


class AgentState(TypedDict):
    company: str
    research: str
    news: str
    final_report: str


def research_node(state):
    print("\n========== [NODE]: research_node() ==========")

    response = requests.post(
        "http://research-agent:8001/research",
        json={
            "company": state["company"]
        }
    )

    return {
        "research": response.json()["research_summary"]
    }


def news_node(state):
    print("\n========== [NODE]: news_node() ==========")

    response = requests.post(
        "http://news-agent:8002/news",
        json={
            "company": state["company"]
        }
    )

    return {
        "news": response.json()["news_summary"]
    }


def report_node(state):
    print("\n========== [NODE]: report_node() ==========")

    response = requests.post(
        "http://report-agent:8003/report",
        json={
            "company": state["company"],
            "research": state["research"],
            "news": state["news"]
        }
    )

    return {
        "final_report": response.json()["final_report"]
    }

print("\n========== CREATING GRAPH ==========")

workflow = StateGraph(AgentState)

workflow.add_node("research", research_node)
workflow.add_node("news", news_node)
workflow.add_node("report", report_node)

workflow.set_entry_point("research")

workflow.add_edge("research", "news")
workflow.add_edge("news", "report")
workflow.add_edge("report", END)

graph = workflow.compile()

print("\n========== GRAPH CREATED ==========")
