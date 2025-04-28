import os
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Gallary Woult Free App is Live! 🚀"}

if __name__ == "__main__":
    # Environment variable se port read karo, default port 10000 hai
    port = int(os.environ.get("PORT", 10000))  # Render will set the PORT automatically
    uvicorn.run(app, host="0.0.0.0", port=port)  # Bind to the correct port
