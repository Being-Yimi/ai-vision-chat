# AI Vision Chat 工程日志

## Day 1：大模型部署与 Web 骨架
- 目标：完成本地大模型部署，搭建 FastAPI 后端 + 前端网页。
- 完成：使用 winget 安装 Ollama，拉取 qwen2.5:1.5b 模型。使用 FastAPI 搭建接口，前端 HTML 接入聊天功能。
- 卡点：8G 内存紧张，手动调整 Windows 虚拟内存至 16GB；Git 第一次提交时误将 .venv 加入，用 git rm -r --cached 清理。

## Day 2：YOLO 跑通与 AI 联动
- 目标：跑通 YOLO 训练，实现图片上传 -> YOLO 画框 -> 大模型写描述。
- 完成：安装 ultralytics，成功跑通 coco8 微型数据集。新增 /api/analyze 接口，前端增加图片上传与结果展示。
- 卡点：YOLO 官方权重下载超时，手动用 ghproxy 镜像下载 yolov8n.pt 放在根目录解决。

## Day 3：工程化重构与云端部署
- 目标：按工程规范进行模块化重构，前后端解耦，补齐文档并推送到 GitHub。
- 完成：将后端拆分为 api/routes.py 和 services/llm_service.py、vision_service.py；前端拆分为 index.html、css/style.css、js/app.js。补齐各文件夹 README，代码成功推送到 GitHub。
- 卡点：拆分后出现 ModuleNotFoundError，排查发现是文件名"11m"被误写为字母"llm"，重命名后修复。

## AI 使用说明

本项目基础框架代码由 AI 辅助生成，本人负责环境搭建、网络排错、模块拆分、功能验证与文档撰写。
