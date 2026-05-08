from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from tools.company_tools import get_company_info

from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

research_agent = create_react_agent(
    model=llm,
    tools=[get_company_info]
)
