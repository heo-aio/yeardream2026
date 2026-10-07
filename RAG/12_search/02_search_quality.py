# k 값에 따라서 다양한 답변을 낼 수 있으며, k=1 이라 하더라도 점수가 낮을 수 있다.
# 여기에는 언어특성에 따른 경우가 많다.

questions = [
    "RAG와 파인튜닝의 차이는?",
    "한국어 문서엔 어떤 임베딩을 써야 하나?",
    "환각을 줄이려면 프롬프트를 어떻게 써야 하나?",
    "벡터 데이터베이스에는 어떤 종류가 있나?",
]

EMB_KO = "intfloat/multilingual-e5-small" # ~470MB, 다국어(한국어양호)
EMB_EN = "sentence-transformers/all-MiniLM-L6-v2" # ~90MB, 영어위주(한국어약함)

# index 함수 - 특정 임베딩 모델을 이용해 데이터를 청킹/저장

