import bcrypt

# Hash 암호화
def encode_pass(plain:str) -> str:
    # 1. 문자열을 byte 형태로 변환
    plain_bytes = plain.encode('utf-8')
    # 2. 해시 암호화 진행
    # salt 값 : 같은 입력을 하여도 결과값이 다르게 나오게 하는 하나의 값
    enc_bytes = bcrypt.hashpw(plain_bytes,bcrypt.gensalt())
    # 3. 문자형태로 변경(DB 에 저장하기 위해)
    return enc_bytes.decode('utf-8')

# 암호화 확인
def matches(plain:str,hash:str) -> bool:
    # byte 형태로 넣어줘야 한다.
    return bcrypt.checkpw(plain.encode("utf-8"),hash.encode("utf-8"))
"""
plain_text = input('암호화 하려는 문자열을 입력 하세요')
hash_text = encode_pass(plain_text)
print(hash_text)

confirm_text = input('방금 입력한 암호를 다시 입력해 보세요')
yn = matches(confirm_text, hash_text)
print(f'일치 여부 : {yn}')
"""
