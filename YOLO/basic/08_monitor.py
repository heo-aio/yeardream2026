# 카메라 또는 영상 에서 '사람' 이 탐지되면
# 콘솔로 '사람 탐지' 라고 출력해 보기
import cv2
from ultralytics import YOLO

# 1. 카메라 연결
cap = cv2.VideoCapture(0) # 'data/sample.mp4'
# 2. 모델 준비
model = YOLO('yolo26n.pt')

if not cap.isOpened():
    print('비디오에 문제가 있습니다.')
    exit()

while True:
    success,frame = cap.read() # 카메라에서 프레임을 읽어오기(성공여부,이미지프레임)

    if not success: # 못 읽어올 경우 나간다.
        break

    # 3. 탐지
    # 4. 탐지시 출력

    if cv2.waitKey(1) & 0xFF == ord("q"):   # 1/1000초 마다 q가 눌렸는지 확인
        break


cap.release()
cv2.destroyAllWindows()