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
    if 0 <= val_value <= 50:
        color = "BLACK"
        s = gTTS(text="Black", lang='en')    # Text to Speech Conversion to Speak out the Color
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif sat_value < 30 and val_value > 180:
        color = "WHITE"
        s = gTTS(text="White", lang='en')    # Text to Speech Conversion to Speak out the Color
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif 5 > hue_value > 0:
        color = "RED"
        s = gTTS(text="Red", lang='en')    # Text to Speech Conversion to Speak out the Color
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif 5 < hue_value <= 17:
        color = "ORANGE"
        s = gTTS(text="Orange", lang='en')    # Text to Speech Conversion to Speak out the Color
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif 17 < hue_value <= 30:
        color = "YELLOW"
        s = gTTS(text="Yellow", lang='en')        # Text to Speech Conversion to Speak out the Color
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif 30 < hue_value <= 45:
        color = "LIME GREEN"
        s = gTTS(text="Lime Green", lang='en')      # Text to Speech Conversion to Speak out the Color
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif 45 < hue_value < 77:
        color = "GREEN"
        s = gTTS(text="Green", lang='en')    # Text to Speech Conversion to Speak out the Color
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif 77 < hue_value < 98:
        color = "SKY BLUE"
        s = gTTS(text="Sky Blue", lang='en')      # Text to Speech Conversion to Speak out the Color
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif 98 < hue_value < 102:
        color = "LIGHT BLUE"
        s = gTTS(text="Light Blue", lang='en')    # Text to Speech Conversion to Speak out the Color
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif 102 < hue_value < 126:
        color = "DARK BLUE"
        s = gTTS(text="Dark Blue", lang='en')     # Text to Speech Conversion to Speak out the Color
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif 126 < hue_value < 138:
        color = "VIOLET"
        s = gTTS(text="Violet", lang='en')   # Text to Speech Conversion to Speak out the Color
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif 138 < hue_value < 170:
        color = "PINK"
        s = gTTS(text="Pink", lang='en')    # Text to Speech Conversion to Speak out the Color
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
