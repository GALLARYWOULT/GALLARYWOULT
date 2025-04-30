from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    return "<h1>🎉 Gallary Woult FastAPI App is Live on Hugging Face!</h1>"
