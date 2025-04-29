from fastapi import FastAPI, UploadFile, File
from ai_tools.text_ai import summarize_text
from ai_tools.image_ai import blur_image
from fastapi.responses import StreamingResponse
import io

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "GALLARY WOULT AI TOOLS LIVE 🔥"}

@app.post("/ai/summarize")
def ai_summarize(text: str):
    summary = summarize_text(text)
    return {"summary": summary}

@app.post("/ai/blur-image")
def blur_uploaded_image(file: UploadFile = File(...)):
    image_data = blur_image(file.file.read())
    return StreamingResponse(io.BytesIO(image_data), media_type="image/png")
