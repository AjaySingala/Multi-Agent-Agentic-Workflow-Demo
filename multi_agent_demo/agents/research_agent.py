from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

from tools.company_api_tool import get_company_info


llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)


def research_agent(state):
    print("\n========== RESEARCH AGENT ==========")

    query = state["user_query"]

    company_name = query.strip()

    company_data = get_company_info.invoke(company_name)

    prompt = f"""
You are a business research analyst.

Summarize the following company information.

{company_data}
"""

    response = llm.invoke([
        HumanMessage(content=prompt)
    ])

    summary = response.content

    print("\n[Research Agent Output]")
    print(summary)

    return {
        "company_data": summary,
        "messages": state.get("messages", []) + ["Research completed"]
    }
