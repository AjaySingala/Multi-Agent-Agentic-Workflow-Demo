from fastapi import FastAPI
from pydantic import BaseModel

from langchain_core.messages import HumanMessage

from agent import report_llm


app = FastAPI()


class ReportRequest(BaseModel):
    company: str
    research: str
    news: str


@app.post("/report")
def report(request: ReportRequest):

    prompt = f"""
    Create an executive business report.

    Company:
    {request.company}

    Research:
    {request.research}

    News:
    {request.news}

    Include:
    1. Executive Summary
    2. Business Strengths
    3. Strategic Risks
    4. AI Opportunities
    5. Recommendation
    """

    response = report_llm.invoke([
        HumanMessage(content=prompt)
    ])

    return {
        "final_report": response.content
    }
