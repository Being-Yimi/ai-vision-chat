"""
AI Vision Chat - 视觉识别服务模块
作用：封装 YOLO 模型的加载与图像推理逻辑
"""
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def analyze_image(image_path: str, output_path: str):
    results = model(image_path)
    r = results[0]
    names = r.names
    dets = []

    for box in r.boxes:
        cls = int(box.cls[0])
        conf = float(box.conf[0])
        dets.append({"class": names[cls], "conf": round(conf, 2)})

    r.save(filename=output_path)
    return dets













