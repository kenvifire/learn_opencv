import cv2
import numpy as np

cap = cv2.VideoCapture(0)


if not cap.isOpened():
    print("Unable to read camera feed")

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv2.VideoWriter('out.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

while True:
    ret, frame = cap.read()

    if ret:
        out.write(frame)
        cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    else:
        break


cap.release()
out.release()
cv2.destroyAllWindows()
