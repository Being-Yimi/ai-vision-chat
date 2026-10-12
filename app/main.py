"""
AI Vision Chat - 主程序入口
作用：组装 FastAPI 应用，挂载静态资源，注册路由
"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.api.routes import router

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# 注册 API 路由
app.include_router(router)

@app.get("/")
def index():
    return FileResponse("static/index.html")