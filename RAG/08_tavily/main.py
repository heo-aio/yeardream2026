"""
LLM 활용하는 정보
1. 자체 모델 - 모델이 학습한 내용들(ollama)
2. RAG - 저장소에서 담고있는 고유의 지식(chromadb)
3. 인터넷 검색 - 최식정보, 실시간 정보(tavily)
tavily search API - AI 에이젼트 및 LLM 을 위해 최적화된 AI 전용 검색엔진 서비스 API
"""
import os

from langchain_tavily import TavilySearch

os.environ["TAVILY_API_KEY"] = ""

def basic_search(query:str):
    search = TavilySearch(max_results=3, search_depth='basic', topic='general')
    result = search.invoke({'query':query})
    print(result['results'])

basic_search('2026년 langchain 최신버전 주요 변경사항')