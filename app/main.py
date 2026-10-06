from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from ultralytics import YOLO
import requests
import uuid
import shutil
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

OLLAMA_URL = "http://localhost:11434/api/generate"
os.makedirs("static/results", exist_ok=True)

# 加载 YOLO 模型
model = YOLO("yolov8n.pt")

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

@app.post("/api/analyze")
async def analyze(file: UploadFile = File(...)):
    uid = str(uuid.uuid4())
    in_path = f"static/results/{uid}_in.jpg"
    out_path = f"static/results/{uid}_out.jpg"

    with open(in_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    # YOLO 推理
    results = model(in_path)
    r = results[0]
    names = r.names
    dets = []

    for box in r.boxes:
        cls = int(box.cls[0])
        conf = float(box.conf[0])
        dets.append({"class": names[cls], "conf": round(conf, 2)})

    r.save(filename=out_path) # 保存画了框的图片

    # 把识别到的类别交给大模型写描述
    labels = list({d["class"] for d in dets})
    prompt = f"图片目标检测结果：{labels}。请用中文写一句自然、简短的图片描述。"
    resp = requests.post(OLLAMA_URL, json={
        "model": "qwen2.5:1.5b",
        "prompt": prompt,
        "stream": False
    })
    desc = resp.json().get("response", "")

    return {
        "detections": dets,
        "image_url": f"/static/results/{uid}_out.jpg",
        "description": desc
    }