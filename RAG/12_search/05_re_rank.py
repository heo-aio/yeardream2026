# 2단계 검색 구조(retriever -> re rank)
# 1. 검색결과를 폭넓게 가져와 추려낸다.
# 2. 그 안에서 (질문,답변) 연관관계를 추론해 다시 정렬한다.
from common import rag_tech_documents

# 데이터 호출
docs = rag_tech_documents()
RERANK = "BAAI/bge-reranker-v2-m3"
# 질문 준비
SCENARIOS = [
    # 1차 벡터는 doc02(BM25)에 끌려 정답 doc03(하이브리드)을 2위로 → 리랭커가 1위로
    {"query": "BM25와 벡터를 합쳐 약점을 보완하는 검색", "target": "doc03"},
    # 1차 벡터는 doc04(리랭킹, '1차로 추린')에 끌려 정답 doc07(압축)을 2위로 → 리랭커가 1위로
    {"query": "1차로 추린 문서에서 핵심 문장만 추출", "target": "doc07"},
]