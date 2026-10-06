import os
from typing import TypedDict

from dotenv import load_dotenv

# 1. API 키 환경변수 등록
load_dotenv()
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

class State(TypedDict):
    question:str    # 질문
    generation:str  # 생성된 답변
    data:str        # 참고데이터