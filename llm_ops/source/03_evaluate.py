from opik import Opik

client = Opik()
dataset = client.get_or_create_dataset(name="haksa-qa")
dataset.insert([
    {"input": "수강 신청은 어디서 하나요?", "expected_output": "학사서비스 > 수강신청 메뉴"},
    {"input": "수강 정정 기간은 언제인가요?", "expected_output": "개강 후 첫째 주 월~금"},
    {"input": "최대 신청 학점은?", "expected_output": "18학점, 평점 4.0 이상이면 21학점"},
    {"input": "기숙사 신청은 어떻게 하나요?", "expected_output": "문서에 없는 내용"},
])