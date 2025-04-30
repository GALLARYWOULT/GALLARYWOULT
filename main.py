from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import io
from ai_tools.text_ai import summarize_text
from ai_tools.image_ai import blur_image

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/ai-tools", response_class=HTMLResponse)
async def ai_tools(request: Request):
    return templates.TemplateResponse("ai_tools.html", {"request": request})

@app.post("/ai/summarize")
async def ai_summarize(text: str):
    summary = summarize_text(text)
    return {"summary": summary}

@app.post("/ai/blur-image")
async def blur_uploaded_image(file: UploadFile = File(...)):
    image_data = blur_image(file.file.read())
    return StreamingResponse(io.BytesIO(image_data), media_type="image/png")
