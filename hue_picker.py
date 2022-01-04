import cv2
import numpy as np

def nothing(x):
    pass

# Trackbar


cv2.namedWindow("Hue Picker")
cv2.createTrackbar("H", "Hue Picker", 0, 360, nothing)
cv2.createTrackbar("S", "Hue Picker", 255, 255, nothing)
cv2.createTrackbar("V", "Hue Picker", 255, 255, nothing)

img_hsv = np.zeros((250, 500, 3), np.uint8)

while True:
    h = cv2.getTrackbarPos("H", "Hue Picker")
    s = cv2.getTrackbarPos("S", "Hue Picker")
    v = cv2.getTrackbarPos("V", "Hue Picker")

    img_hsv[:] = (h, s, v)
    img_bgr = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

    cv2.imshow("Hue Picker", img_bgr)
    key = cv2.waitKey(1)
    if key == 27:
        break


cv2.destroyAllWindows()
