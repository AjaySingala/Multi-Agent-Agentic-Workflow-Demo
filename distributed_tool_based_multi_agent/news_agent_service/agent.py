from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from tools.news_tools import get_company_news

from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

news_agent = create_react_agent(
    model=llm,
    tools=[get_company_news]
)
