from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
import os

load_dotenv()

report_llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)
