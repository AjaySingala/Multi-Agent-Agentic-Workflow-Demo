from fastapi import FastAPI
from pydantic import BaseModel

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

app = FastAPI()

import os
from dotenv import load_dotenv
load_dotenv()

# print(f"OPENAI_API_KEY: {os.getenv('OPENAI_API_KEY')}")

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


class ReportRequest(BaseModel):
    company: str
    research: str
    news: str


@app.post("/report")
def generate_report(request: ReportRequest):
    print("\n========== /report ==========")

    prompt = f"""
    Create an executive business report for {request.company}.

    Research:
    {request.research}

    News:
    {request.news}

    Include:
    1. Executive Summary
    2. Opportunities
    3. Risks
    4. AI Strategy
    5. Recommendation
    """

    response = llm.invoke([
        HumanMessage(content=prompt)
    ])

    return {
        "final_report": response.content
    }
