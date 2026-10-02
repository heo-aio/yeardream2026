from typing import TypedDict

from langgraph.graph import StateGraph


class State(TypedDict):
    question:str    # 질문 내용
    generation:str  # 생성된 답변
    data:str        # 참고자료

def get_state():
    return StateGraph(State)

def init_answer(state:State):
    q = state['question']
    print(f'최초질문 : {q}')
    return state

def router(state:State):
    print('router 도착')
    return "rag"

def plain(state:State):
    return state

def web_search(state:State):
    return state

def last_answer(state:State):
    print('최종답변')
    return state


