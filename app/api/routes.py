"""
AI Vision Chat - 路由模块
作用：定义前端可访问的所有 API 接口
"""
from fastapi import APIRouter, UploadFile, File
from app.services.llm_service import ask_llm
from app.services.vision_service import analyze_image
import uuid, shutil, os

router = APIRouter(prefix="/api")
os.makedirs("static/results", exist_ok=True)

@router.post("/chat")
def chat(prompt: str):
    return {"reply": ask_llm(prompt)}

@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    uid = str(uuid.uuid4())
    in_path = f"static/results/{uid}_in.jpg"
    out_path = f"static/results/{uid}_out.jpg"

    with open(in_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    dets = analyze_image(in_path, out_path)
    labels = list({d["class"] for d in dets})
    prompt = f"图片目标检测结果：{labels}。请用中文写一句自然、简短的图片描述。"
    desc = ask_llm(prompt)

    return {
        "detections": dets,
        "image_url": f"/static/results/{uid}_out.jpg",
        "description": desc
    }