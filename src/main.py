from transformers import pipeline
from fastapi import FastAPI
from pydantic import BaseModel


class RequestBody(BaseModel):
    text: str


app = FastAPI()
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


@app.get("/")
async def root():
    return {"message": "hello world"}


@app.post("/get-summary/")
async def get_summary(request_body: RequestBody):
    summary = summarizer(request_body.text, max_length=130, min_length=30, do_sample=False)
    return summary
