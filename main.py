import cv2
import pyaudio
import platform
import sys
from bs4 import BeautifulSoup
from gtts import gTTS
import pyglet
import os
import time

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    cx = int(width/2)
    cy = int(height/2)

    pixel_center = frame[cy, cx]
    hue_value = pixel_center[0]
    sat_value = pixel_center[1]
    val_value = pixel_center[2]

    color = "Undefined"
    if hue_value == 0:
        color = "BLACK"
    elif hue_value < 5 and hue_value > 0:
        color = "RED"
    elif hue_value > 5 and hue_value <= 17:
        color = "ORANGE"
    elif hue_value > 17 and hue_value <= 30:
        color = "YELLOW"
    elif hue_value > 30 and hue_value <= 45:
        color = "LIME GREEN"
    elif hue_value > 45 and hue_value < 77:
        color = "GREEN"
    elif hue_value > 77 and hue_value < 98:
        color = "SKY BLUE"
    elif hue_value > 98 and hue_value < 102:
        color = "LIGHT BLUE"
    elif hue_value > 102 and hue_value < 126:
        color = "DARK BLUE"
    elif hue_value > 126 and hue_value < 138:
        color = "VIOLET"
    elif hue_value > 138 and hue_value < 170:
        color = "PINK"

    pixel_center_bgr = frame[cy,cx]
    cv2.putText(frame, color, (10,50), 0, 1, (255, 0, 0), 2)
    cv2.circle(frame, (cx, cy), 5, (255, 0, 0), 3)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
