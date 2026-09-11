import logging

from langchain_core.tracers import langchain
from langchain_ollama import ChatOllama

logging.basicConfig(level=logging.INFO)
langchain.debug=True

# ollama 모델 생성
llm = ChatOllama(model="gemma4:e4b")

def start_agent(query:str):
    # 프롬프트 생성 + 대답 듣기
    for chunk in llm.stream(query):
        print(chunk.content,end="",flush=True)