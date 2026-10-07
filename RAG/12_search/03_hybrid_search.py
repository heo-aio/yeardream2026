SCENARIOS = [
    {
        "query": "키워드 검색의 한국어 처리",
        "target": "doc02",
        "expect": "BM25 우위 — 정답 doc02에 'BM25'가 직접 등장. Vector는 '한국어'에 끌려 다국어(doc05)로 샘"
     },
    {
        "query": "검색 결과를 좁은 후보에서 한 번 더 정렬하는 모델",
        "target": "doc04",
        "expect": "Vector 우위 — 정답 doc04의 단어가 질의와 거의 안 겹쳐 BM25는 놓침"
    },
]