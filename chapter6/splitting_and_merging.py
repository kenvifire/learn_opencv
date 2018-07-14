import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args['image'])

(B, G, R) = cv2.split(image)

cv2.imshow("B", B)
cv2.imshow("G", G)
cv2.imshow("R", R)

cv2.waitKey(0)

merged = cv2.merge([B, R, G])

cv2.imshow("merged",merged)
cv2.waitKey(0)
cv2.destroyAllWindows()