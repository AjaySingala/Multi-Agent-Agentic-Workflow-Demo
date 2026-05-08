from fastapi import FastAPI
from pydantic import BaseModel

from agent import research_agent


app = FastAPI()


class ResearchRequest(BaseModel):
    company: str


@app.post("/research")
def research(request: ResearchRequest):

    response = research_agent.invoke({
        "messages": [
            (
                "user",
                f"""
                Research the company: {request.company}

                Use available tools if needed.

                Provide:
                - company overview
                - strengths
                - strategic risks
                """
            )
        ]
    })

    return {
        "research_summary":
            response["messages"][-1].content
    }
