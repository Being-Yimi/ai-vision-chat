# AI Vision Chat 工程日志

## 项目背景
本项目为 AI 协会创智部二面实战题目，基于自身设备（GTX 1650 Ti 4G显存 + 8G内存）完成本地大模型部署与 YOLO 视觉识别的综合应用。
技术栈：Ollama (Qwen2.5:1.5b) + FastAPI + WebSocket + Ultralytics YOLOv8 + 原生 HTML/JS。

---

## Day 1：大模型部署与 Web 骨架搭建

### 🎯 目标
完成本地大模型部署，搭建 FastAPI 后端 + 前端网页骨架，成功通过 API 调用本地大模型。

### ✅ 完成情况
1. 下载并安装 Ollama，成功拉取并运行轻量级本地模型 `qwen2.5:1.5b`。
2. 建立 `ai-vision-chat` 项目目录，初始化 Git，配置 Python 虚拟环境 `.venv`。
3. 安装 FastAPI、Uvicorn、Requests 等依赖。
4. 编写后端接口 `/api/chat`，前端页面 `index.html`，成功实现网页对话。
5. 配置 `.gitignore`，清理 Git 缓存，完成第一次代码提交。

### 🚧 遇到的卡点与解决
1. **下载卡顿**：Ollama 官网下载速度极慢甚至超时。
   * **解决**：放弃浏览器下载，改用 Windows 自带的 `winget install Ollama.Ollama` 命令行下载，从微软 CDN 源顺利拉取 1.47GB 安装包。
2. **内存危机**：8G 物理内存在运行大模型时极易卡死。
   * **解决**：调整 Windows 系统设置，手动将 D 盘（软件盘）的虚拟内存设置为 8000 - 16000 MB，给系统兜底。
3. **Git 仓库污染**：首次 `git add .` 时，把几千个 `.venv` 里的第三方库文件和 `__pycache__` 缓存全加进去了。
   * **解决**：编写 `.gitignore` 文件（`__pycache__/`、`*.pyc`、`*.db`、`.venv/`），并执行 `git rm -r --cached .venv` 清理索引，保持仓库干净。
4. **PowerShell 权限报错**：激活虚拟环境时提示“禁止运行脚本”。
   * **解决**：以管理员身份运行 PowerShell，执行 `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` 修改权限。

---

## Day 2：YOLO 跑通与 AI 联动应用

### 🎯 目标
跑通 Ultralytics YOLO 训练，实现“上传图片 -> YOLO 画框检测 -> 传标签给大模型生成描述”的完整链路。

### ✅ 完成情况
1. 安装 `ultralytics` 库（自动安装 PyTorch 2.14.1 及 CUDA 环境）。
2. 成功运行一次 YOLO 微型数据集训练，验证显卡（GTX 1650 Ti）可用，推理速度达到 81.5ms/张。
3. 修改后端，新增 `/api/analyze` 接口，集成 YOLOv8n 模型推理。
4. 修改前端，增加文件上传功能，并展示画框图片与 AI 描述。
5. 本地测试大获成功：上传猫咪照片，YOLO 打上 `cat 0.82` 标签，大模型输出“这是一只猫。”

### 🚧 遇到的卡点与解决
1. **GitHub 连接超时**：执行 `yolo detect train` 时，试图从 GitHub 自动下载 `yolov8n.pt` 权重文件，反复重试 3 次均报 `ConnectionTimeout`。
   * **解决**：利用 ghproxy 镜像手动下载 6MB 的权重文件，放到项目根目录，将训练命令改为 `model=./yolov8n.pt` 加载本地文件，成功绕开网络封锁。
2. **端口占用错误**：手动启动 `ollama serve` 时提示 `bind: Only one usage of each socket address...`
   * **解决**：意识到 Ollama 安装后已作为后台服务自动运行，无需手动再次启动，直接关掉多余的 CMD 窗口即可。
3. **资源极限**：同时跑 Ollama 大模型 + YOLO 推理 + Web 服务，系统资源极度吃紧。
   * **解决**：测试期间强制关闭 Steam、微信、QQ 及多余浏览器标签，并选用最轻量级的 `yolov8n` 模型和 `coco8` 微型数据集，遵循“做减法”的原则。

### 💡 目前的想法与改进方向
作为零基础开发者，我深刻体会到了 AI 时代“工程整合能力”比“手写底层代码”更重要。本次项目利用 AI 辅助生成了基础接口代码，但我亲力亲为解决了环境配置、网络超时、内存瓶颈和 Git 版本控制等所有实际工程问题。
后续如果能继续优化，我会尝试：
1. 将前端封装成桌面应用（如 Electron）。
2. 增加对视频流的实时检测，而不仅限于图片上传。
3. 优化大模型 Prompt，让其生成的描述更加丰富细致。

---

## 📌 AI 使用说明
本项目如实说明 AI 使用情况：项目中的 FastAPI 后端基础框架、HTML/JS 前端代码由 AI 生成，本人全程参与需求定义、环境搭建、代码调试、报错排查与最终的功能验证。在开发过程中，本人深入理解了数据流转与接口调用逻辑，并自行完成了所有排错与文档撰写。