import time


def get_news(company: str):
    print("\n========== [TOOL]: get_news() ==========")

    print(f"[News Tool] Fetching news for {company}")

    time.sleep(2)

    fake_news = {
        "Walmart": [
            "Walmart expands AI supply chain automation.",
            "Walmart increases ecommerce investments.",
            "Walmart improves delivery optimization."
        ],
        "Microsoft": [
            "Microsoft expands Copilot adoption.",
            "Azure growth accelerates.",
            "Microsoft invests heavily in AI."
        ]
    }

    return fake_news.get(company, [
        "No recent news found."
    ])
