from fastapi import FastAPI
from pydantic import BaseModel

from agent import news_agent


app = FastAPI()


class NewsRequest(BaseModel):
    company: str


@app.post("/news")
def news(request: NewsRequest):

    response = news_agent.invoke({
        "messages": [
            (
                "user",
                f"""
                Analyze recent news for {request.company}.

                Use available tools if needed.

                Explain:
                - important developments
                - business impact
                - strategic implications
                """
            )
        ]
    })

    return {
        "news_summary":
            response["messages"][-1].content
    }
