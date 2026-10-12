import os

import cv2

cap = cv2.VideoCapture("data/mouse.mp4")
save_dir = "dataset/source"

if not os.path.exists(save_dir):
    os.makedirs(save_dir)
    print('폴더 생성')

while True:
    success,frame = cap.read()

    if not success:
        break

    resize_frame = cv2.resize(frame,(480,640))

    cv2.imshow('mouse',resize_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()