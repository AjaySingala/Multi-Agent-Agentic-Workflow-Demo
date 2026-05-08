import time

from langchain_core.tools import tool


@tool
def get_company_news(company: str) -> str:
    """
    Fetch recent company news.
    """

    print(f"[Tool] Fetching news for {company}")

    time.sleep(2)

    fake_news = {
        "Walmart": [
            "Walmart expands AI supply chain automation.",
            "Walmart improves ecommerce logistics.",
            "Walmart increases digital transformation investments."
        ],
        "Microsoft": [
            "Microsoft expands Copilot globally.",
            "Azure AI revenue grows significantly.",
            "Microsoft invests in enterprise AI."
        ]
    }

    result = fake_news.get(company)

    if not result:
        return "No news found."

    return "\\n".join(result)
