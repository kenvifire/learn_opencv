import cv2
import math

center = []
circumference = []


def drawCircle(action, x, y, flags, userdata):
    global center, circumference

    if action == cv2.EVENT_LBUTTONDOWN:
        center = [(x, y)]

        cv2.circle(source, center[0], 1, (255, 255, 0), 2, cv2.LINE_AA)

    elif action == cv2.EVENT_LBUTTONUP:
        circumference=[(x, y)]
        radius = math.sqrt(math.pow(center[0][0] - circumference[0][0], 2)
            + math.pow(center[0][1]-circumference[0][1], 2))
        cv2.circle(source, center[0], int(radius), (0, 255, 0), cv2.LINE_AA)
        cv2.imshow("window", source)


source = cv2.imread('IMG_1278.JPG')

dummy = source.copy()

cv2.namedWindow("Window")

cv2.setMouseCallback("Window", drawCircle)

k = 0

while k != 27:
    cv2.imshow("Window", source)
    cv2.putText(source, "Choose center, and drag, Press Esc to exit and c to clear", (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (255, 255, 255), 2)
    k = cv2.waitKey(20) & 0xff

    if k == 99:
        source = dummy.copy()

cv2.destroyAllWindows()
