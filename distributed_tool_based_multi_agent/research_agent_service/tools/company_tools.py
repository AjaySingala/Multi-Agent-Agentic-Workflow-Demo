import time

from langchain_core.tools import tool


@tool
def get_company_info(company: str) -> str:
    """
    Fetch company information from an external source.
    """

    print(f"[Tool] Fetching company data for {company}")

    time.sleep(2)

    fake_db = {
        "Walmart": {
            "industry": "Retail",
            "revenue": "$648 Billion",
            "employees": "2.1 Million",
            "focus": "AI Supply Chain"
        },
        "Microsoft": {
            "industry": "Technology",
            "revenue": "$245 Billion",
            "employees": "220,000",
            "focus": "Cloud and AI"
        }
    }

    result = fake_db.get(company)

    if not result:
        return "No company information found."

    return str(result)
