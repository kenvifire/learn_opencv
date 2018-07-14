import cv2
import numpy as np

cap = cv2.VideoCapture('movie.mp4')

if not cap.isOpened():
    print("Error opening video stream or file")


while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow("Frame", frame)

        if cv2.waitKey(25) & 0xFF == 27:
            break

    else:
        break

cap.release()

cv2.destroyAllWindows()
