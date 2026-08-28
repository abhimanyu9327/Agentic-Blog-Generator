import uvicorn
from fastapi import FastAPI, Request
from src.llms.groqllm import GroqLLM

import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

print(os.getenv("LANGCHAIN_API_KEY"))

os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

## API's

@app.post("/blogs")
async def create_blogs(request: Request):
    data = await request.json()
    topic = data.get("topic", "")

    ## get the llm object
    groqllm = GroqLLM()
    llm = groqllm.get_llm()

    return {"topic": topic}
