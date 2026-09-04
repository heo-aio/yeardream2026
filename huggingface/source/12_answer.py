import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = 'LGAI-EXAONE/EXAONE-3.0-7.8B-Instruct'
# 1. 토크나이저
tokenizer = AutoTokenizer.from_pretrained(model_id)
# 2. 모델
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    trust_remote_code=True,
    dtype=torch.bfloat16,
    device_map="auto"
)

prompt = input('AI 에게 질문하고 싶은 내용은?\n')
print(prompt)
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

print("생각 하는 중...")
with torch.no_grad():
    output = model.generate(
        **inputs,
        max_new_tokens=246,
        do_sample=True,
        temperature=0.7,
        eos_token_id=tokenizer.eos_token_id
    )
    print(tokenizer.decode(output[0]))

# 3. 토큰화
# 4. 추론