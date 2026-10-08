from pathlib import Path

from ultralytics import YOLO

curr_dir = Path(__file__).resolve().parent
run_dir = f"{curr_dir}/runs/MyProject"
print(run_dir)
model = YOLO('yolo26n.pt')
results = model.predict(
    source="bus.jpg",
    conf=0.5,
    project=run_dir,
    name="result",
    exist_ok=True
)
print(f'이미지 경로 : {results[0].path}')
print(f'걸린시간 : {results[0].speed}')
print(f'이미지 크기 : {results[0].orig_img.shape}') # orig_img : 원본 이미지 배열
print(f'분류사전 : {results[0].names}')