from fastapi import FastAPI
from pydantic import BaseModel

from workflow import graph


app = FastAPI()


class UserRequest(BaseModel):
    company: str


@app.post("/analyze")
def analyze(request: UserRequest):

    result = graph.invoke({
        "company": request.company,
        "research": "",
        "news": "",
        "final_report": ""
    })

    return {
        "company": request.company,
        "final_report":
            result["final_report"]
    }
