# AI Vision Chat

基于 FastAPI + Ollama + YOLO 的本地视觉对话应用。
实现了“上传图片 -> YOLO 目标检测 -> 大模型生成描述”的完整链路。

## 环境依赖
- Python 3.10+
- Ollama（需提前 pull qwen2.5:1.5b）
- 安装依赖：
  ```bash
  pip install fastapi uvicorn requests ultralytics python-multipart
  ```
## 启动命令
1.确保 Ollama 服务在后台运行（默认会自动启动，或手动运行 ollama serve）。

2.在项目根目录下启动后端：
uvicorn app.main:app --reload

3.浏览器访问 http://127.0.0.1:8000 即可使用。
## 项目结构
ai-vision-chat/
├── app/                # 后端核心代码
│   ├── api/            # 路由接口
│   └── services/       # 业务逻辑（大模型与YOLO）
├── static/             # 前端静态资源（HTML/CSS/JS）
├── docs/               # 工程日志
├── yolov8n.pt          # YOLO 预训练权重
└── README.md           # 项目说明

## AI使用说明
本项目在开发过程中使用了 AI 辅助：FastAPI 基础框架和前端 HTML/JS 代码由 AI 生成，本人负责环境搭建、代码调试、报错排查与最终功能验证。