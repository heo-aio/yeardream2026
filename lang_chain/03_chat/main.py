from typing import Dict

from fastapi import FastAPI
from starlette.responses import RedirectResponse, StreamingResponse
from starlette.staticfiles import StaticFiles

from ollama_service import chat_answer

app = FastAPI()
app.mount("/view",StaticFiles(directory="view"))

@app.get("/")
def main():
    return RedirectResponse("/view/chat.html")

@app.post("/ask/chat")
def ask_chat(info:Dict[str,str]):
    print(f'input : {info['q']}')
    return StreamingResponse(chat_answer(info['q']), media_type="text/plain")