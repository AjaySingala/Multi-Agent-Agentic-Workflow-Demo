from typing import TypedDict, List


class AgentState(TypedDict):
    user_query: str
    company_data: str
    news_data: str
    final_report: str
    messages: List[str]
