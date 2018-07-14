import argparse
import numpy as np
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",
                help="Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args['image'])
cv2.imshow("Original", image)

cropped = image[30:400, 240:600]
cv2.imshow("T-Rex Face", cropped)

cv2.waitKey(0)
