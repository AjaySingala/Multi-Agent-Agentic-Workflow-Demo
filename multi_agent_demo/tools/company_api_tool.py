import time
from langchain.tools import tool


@tool
def get_company_info(company_name: str) -> str:
    """
    Simulates fetching company information from an external API.
    """

    print(f"\n[Tool] Calling Company API for: {company_name}")

    time.sleep(2)

    fake_database = {
        "Microsoft": {
            "industry": "Technology",
            "employees": "220,000",
            "revenue": "$245 Billion",
            "focus": "Cloud Computing, AI, Enterprise Software"
        },
        "Tesla": {
            "industry": "Automotive & Energy",
            "employees": "140,000",
            "revenue": "$97 Billion",
            "focus": "Electric Vehicles, Robotics, AI"
        },
        "Walmart": {
            "industry": "Retail",
            "employees": "2.1 Million",
            "revenue": "$648 Billion",
            "focus": "Retail, Supply Chain, E-Commerce"
        }
    }

    data = fake_database.get(company_name, {
        "industry": "Unknown",
        "employees": "Unknown",
        "revenue": "Unknown",
        "focus": "Unknown"
    })

    return f"""
Company: {company_name}
Industry: {data['industry']}
Employees: {data['employees']}
Revenue: {data['revenue']}
Focus Areas: {data['focus']}
"""
