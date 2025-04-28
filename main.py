from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

fake_ai_responses = [
    "Yeh AI response hai aapke prompt ke liye. 🚀",
    "Aapka idea bahut zabardast hai! 🎯",
    "AI kehta hai: Mehnat jaari rakho. 🔥",
    "Gallary Woult AI bolta hai: Success pakka hai! 🌟",
]

@app.get("/")
def read_root():
    return {"message": "Gallary Woult Free App with AI is Live! 🚀"}

@app.post("/ai/generate")
def generate_ai_response(request: PromptRequest):
    response = random.choice(fake_ai_responses)
    return {
        "prompt": request.prompt,
        "ai_response": response
    }
