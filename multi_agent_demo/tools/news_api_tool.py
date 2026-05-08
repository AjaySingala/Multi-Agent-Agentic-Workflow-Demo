import time
from langchain.tools import tool


@tool
def get_company_news(company_name: str) -> str:
    """
    Simulates fetching recent news articles.
    """

    print(f"\n[Tool] Calling News API for: {company_name}")

    time.sleep(2)

    fake_news = {
        "Microsoft": [
            "Microsoft expands AI investments.",
            "Azure revenue continues strong growth.",
            "Copilot adoption increases in enterprises."
        ],
        "Tesla": [
            "Tesla launches new robotics initiative.",
            "EV sales rise globally.",
            "Tesla invests in AI-driven manufacturing."
        ],
        "Walmart": [
            "Walmart enhances supply chain automation.",
            "Walmart expands digital commerce.",
            "Retail AI initiatives improve customer experience."
        ]
    }

    news_items = fake_news.get(company_name, [
        "No recent news available."
    ])

    return "\n".join(news_items)
