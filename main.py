from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Gallary Woult Free App is Live! 🚀"}
