from fastapi import FastAPI
from pydantic import BaseModel

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

from tools.company_tool import get_company_info

app = FastAPI()

import os
from dotenv import load_dotenv
load_dotenv()

# print(f"OPENAI_API_KEY: {os.getenv('OPENAI_API_KEY')}")

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


class ResearchRequest(BaseModel):
    company: str


@app.post("/research")
def research(request: ResearchRequest):
    print("\n========== /research ==========")

    company_data = get_company_info(request.company)

    prompt = f"""
    You are a business research analyst.

    Analyze this company information.

    {company_data}

    Give:
    - company overview
    - strengths
    - risks
    """

    response = llm.invoke([
        HumanMessage(content=prompt)
    ])

    return {
        "research_summary": response.content
    }
