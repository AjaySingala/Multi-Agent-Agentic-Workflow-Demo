from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage


llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)


def report_agent(state):
    print("\n========== REPORT AGENT ==========")

    company_data = state["company_data"]
    news_data = state["news_data"]
    company_name = state["user_query"]

    prompt = f"""
Create an executive business report for {company_name}.

Company Research:
{company_data}

Recent News Analysis:
{news_data}

Provide:
1. Executive Summary
2. Business Strengths
3. Strategic Risks
4. AI/Technology Opportunities
5. Final Recommendation
"""

    response = llm.invoke([
        HumanMessage(content=prompt)
    ])

    report = response.content

    print("\n[Final Report Generated]")
    print(report)

    return {
        "final_report": report,
        "messages": state.get("messages", []) + ["Report generated"]
    }