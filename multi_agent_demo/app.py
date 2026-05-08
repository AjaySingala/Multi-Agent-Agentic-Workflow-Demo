# Set env vars from config.py.
import sys
import os

# Add the folder path (use absolute or relative path)
folder_path = os.path.join(os.path.dirname(__file__), '../')
sys.path.insert(0, folder_path)

import config

# Start.

from graph.workflow import app


def main():
    print("\n==============================")
    print(" MULTI-AGENT BUSINESS SYSTEM ")
    print("==============================\n")

    company_name = input("Enter company name: ")

    result = app.invoke({
        "user_query": company_name,
        "company_data": "",
        "news_data": "",
        "final_report": "",
        "messages": []
    })

    print("\n================ FINAL REPORT ================\n")

    print(result["final_report"])

    print("\n================ EXECUTION TRACE ================\n")

    for msg in result["messages"]:
        print(f"- {msg}")


if __name__ == "__main__":
    main()
