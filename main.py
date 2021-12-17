import cv2
from gtts import gTTS
import pyglet
import os
import time

# To get continuous stream of frames of Live Image and create a Window

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    _, frame = capture.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    cx = int(width/2)
    cy = int(height/2)

# Setting the pixel center

    pixel_center = frame[cy, cx]

# Picking up Hue value, saturation value and Variation value from pixel matrix

    hue_value = pixel_center[0]
    sat_value = pixel_center[1]
    val_value = pixel_center[2]

    color = "Undefined"       # Default Value
    if (val_value == 0) and (sat_value <= 255) and (hue_value <= 255):
        color = "BLACK"
        s = gTTS(text="Black", lang='en')  # Text to Speech Conversion to Speak out the Color
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (hue_value <= 255) and (sat_value <= 50) and (210 <= val_value <= 255):
        color = "WHITE"
        s = gTTS(text="White", lang='en')   # Text to Speech Conversion to Speak out the Color
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (hue_value <= 5) and (sat_value <= 100) and (180 <= val_value <= 255):
        color = "RED"
        s = gTTS(text="Red", lang='en')  # Text to Speech Conversion to Speak out the Color
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (5 < hue_value <= 17) and (150 <= sat_value <= 255) and (
            200 <= val_value <= 255):
        color = "ORANGE"
        s = gTTS(text="Orange", lang='en')   # Text to Speech Conversion to Speak out the Color
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (17 < hue_value <= 37) and (110 <= sat_value <= 180) and (
            220 <= val_value <= 255):
        color = "YELLOW"
        s = gTTS(text="Yellow", lang='en')   # Text to Speech Conversion to Speak out the Color
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (38 < hue_value <= 48) and (140 <= sat_value <= 190) and (
            230 <= val_value <= 255):
        color = "LIME GREEN"
        s = gTTS(text="Lime Green", lang='en')   # Text to Speech Conversion to Speak out the Color
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (48 < hue_value < 70) and (225 <= sat_value <= 255) and (
            220 <= val_value <= 255):
        color = "GREEN"
        s = gTTS(text="Green", lang='en')   # Text to Speech Conversion to Speak out the Color
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif 77 < hue_value < 98:
        color = "SKY BLUE"
        s = gTTS(text="Sky Blue", lang='en')   # Text to Speech Conversion to Speak out the Color
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (80 < hue_value < 100) and (70 <= sat_value <= 200) and (
            245 <= val_value <= 255):
        color = "LIGHT BLUE"
        s = gTTS(text="Light Blue", lang='en')  # Text to Speech Conversion to Speak out the Color
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (102 < hue_value < 126) and (225 <= sat_value <= 255) and (
            35 <= val_value <= 255):
        color = "DARK BLUE"
        s = gTTS(text="Dark Blue", lang='en')    # Text to Speech Conversion to Speak out the Color
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (140 < hue_value < 150) and (80 <= sat_value <= 255) and (
            150 <= val_value <= 210):
        color = "VIOLET"
        s = gTTS(text="Violet", lang='en')   # Text to Speech Conversion to Speak out the Color
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (155 < hue_value < 172) and (100 <= sat_value <= 255) and (
            220 <= val_value <= 255):
        color = "PINK"
        s = gTTS(text="Pink", lang='en')   # Text to Speech Conversion to Speak out the Color
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)

    pixel_center_bgr = frame[cy, cx]
    cv2.putText(frame, color, (10, 50), 0, 1, (255, 0, 0), 2)
    cv2.circle(frame, (cx, cy), 5, (255, 0, 0), 3)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

capture.release()
cv2.destroyAllWindows()
