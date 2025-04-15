from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Gallery-Woult™ AI Server Running Successfully!"}