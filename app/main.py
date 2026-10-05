from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import requests

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

OLLAMA_URL = "http://localhost:11434/api/generate"

@app.get("/")
def index():
    return FileResponse("static/index.html")

@app.post("/api/chat")
def chat(prompt: str):
    resp = requests.post(OLLAMA_URL, json={
        "model": "qwen2.5:1.5b",
        "prompt": prompt,
        "stream": False
    })
    return {"reply": resp.json().get("response", "")}