import time


def get_company_info(company: str):
    print("\n========== [TOOL]: get_company_info() ==========")
    
    print(f"[Research Tool] Fetching data for {company}")

    time.sleep(2)

    fake_db = {
        "Walmart": {
            "industry": "Retail",
            "revenue": "$648 Billion",
            "employees": "2.1 Million",
            "focus": "Retail, AI Supply Chain"
        },
        "Microsoft": {
            "industry": "Technology",
            "revenue": "$245 Billion",
            "employees": "220,000",
            "focus": "Cloud, AI"
        }
    }

    return fake_db.get(company, {
        "industry": "Unknown",
        "revenue": "Unknown",
        "employees": "Unknown",
        "focus": "Unknown"
    })
