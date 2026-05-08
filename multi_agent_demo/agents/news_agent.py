from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

from tools.news_api_tool import get_company_news


llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)


def news_agent(state):
    print("\n========== NEWS AGENT ==========")

    query = state["user_query"]

    company_name = query.strip()

    news_data = get_company_news.invoke(company_name)

    prompt = f"""
You are a news analyst.

Analyze these recent company news updates and summarize key business implications.

News:
{news_data}
"""

    response = llm.invoke([
        HumanMessage(content=prompt)
    ])

    summary = response.content

    print("\n[News Agent Output]")
    print(summary)

    return {
        "news_data": summary,
        "messages": state.get("messages", []) + ["News analysis completed"]
    }
