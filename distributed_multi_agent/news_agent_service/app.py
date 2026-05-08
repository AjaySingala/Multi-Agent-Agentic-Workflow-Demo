from fastapi import FastAPI
from pydantic import BaseModel

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

from tools.news_tool import get_news

app = FastAPI()

import os
from dotenv import load_dotenv
load_dotenv()

# print(f"OPENAI_API_KEY: {os.getenv('OPENAI_API_KEY')}")

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


class NewsRequest(BaseModel):
    company: str


@app.post("/news")
def news(request: NewsRequest):
    print("\n========== /news ==========")

    news_data = get_news(request.company)

    prompt = f"""
    You are a business news analyst.

    Analyze these news updates:

    {news_data}

    Explain business implications.
    """

    response = llm.invoke([
        HumanMessage(content=prompt)
    ])

    return {
        "news_summary": response.content
    }
