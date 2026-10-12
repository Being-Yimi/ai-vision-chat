"""
AI Vision Chat - 大模型服务模块
作用：封装与 Ollama 本地大模型的交互逻辑
"""
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def ask_llm(prompt: str) -> str:
    resp = requests.post(OLLAMA_URL, json={
        "model": "qwen2.5:1.5b",
        "prompt": prompt,
        "stream": False
    })
    return resp.json().get("response", "")