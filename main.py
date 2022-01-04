import cv2
from gtts import gTTS
import pyglet
import os
import time

# Creating the frame to display our Application
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# To take a series of frame
while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Converting the Image Pixel from BGR to HSV format
    height, width, _ = frame.shape

    # To find the center of the frame
    cx = int(width / 2)
    cy = int(height / 2)
    pixel_center = frame[cy, cx]

    # print(pixel_center) to Print each pixel

    hue_value = pixel_center[0]
    sat_value = pixel_center[1]
    val_value = pixel_center[2]

    color = "Undefined"
    if (200 <= hue_value <= 208) and (20 <= sat_value <= 40) and (41 <= val_value <= 61):
        color = "Air Force Blue"
        s = gTTS(text="Air Force Blue", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (204 <= hue_value <= 212) and (90 <= sat_value <= 110) and (87 <= val_value <= 107):
        color = "Alice Blue"
        s = gTTS(text="Alice Blue", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (351 <= hue_value <= 359) and (67 <= sat_value <= 87) and (42 <= val_value <= 62):
        color = "Alizarin"
        s = gTTS(text="Alizarin", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (344 <= hue_value <= 352) and (68 <= sat_value <= 88) and (43 <= val_value <= 63):
        color = "Amaranth"
        s = gTTS(text="Amaranth", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (44 <= hue_value <= 46) and (90 <= sat_value <= 110) and (40 <= val_value <= 60):
        color = "Amber"
        s = gTTS(text="Amber", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (69 <= hue_value <= 78) and (45 <= sat_value <= 65) and (40 <= val_value <= 60):
        color = "Android Green"
        s = gTTS(text="Android Green", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (69 <= hue_value <= 78) and (90 <= sat_value <= 110) and (26 <= val_value <= 46):
        color = "Apple Green"
        s = gTTS(text="Apple Green", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (22 <= hue_value <= 25) and (80 <= sat_value <= 100) and (74 <= val_value <= 94):
        color = "Apricot"
        s = gTTS(text="Apricot", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (156 <= hue_value <= 164) and (90 <= sat_value <= 110) and (65 <= val_value <= 85):
        color = "Aquamarine"
        s = gTTS(text="Aquamarine", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (65 <= hue_value <= 73) and (34 <= sat_value <= 54) and (13 <= val_value <= 33):
        color = "Army Green"
        s = gTTS(text="Army Green", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (202 <= hue_value <= 210) and (2 <= sat_value <= 22) and (16 <= val_value <= 36):
        color = "Arsenic"
        s = gTTS(text="Arsenic", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (47 <= hue_value <= 55) and (64 <= sat_value <= 84) and (57 <= val_value <= 77):
        color = "Arylide Yellow"
        s = gTTS(text="Arylide Yellow", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (128 <= hue_value <= 139) and (0 <= sat_value <= 18) and (62 <= val_value <= 82):
        color = "Ash Grey"
        s = gTTS(text="Ash Grey", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (87 <= hue_value <= 97) and (17 <= sat_value <= 37) and (44 <= val_value <= 64):
        color = "Asparagus"
        s = gTTS(text="Asparagus", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (16 <= hue_value <= 24) and (90 <= sat_value <= 110) and (60 <= val_value <= 80):
        color = "Atomic Tangerine"
        s = gTTS(text="Atomic Tangerine", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (16 <= hue_value <= 24) and (51 <= sat_value <= 71) and (16 <= val_value <= 36):
        color = "Auburn"
        s = gTTS(text="Auburn", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (206 <= hue_value <= 214) and (0 <= sat_value <= 20) and (40 <= val_value <= 60):
        color = "Azure"

        s = gTTS(text="Azure", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (195 <= hue_value <= 203) and (67 <= sat_value <= 87) and (64 <= val_value <= 84):
        color = "Baby Blue"
        s = gTTS(text="Baby Blue", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (208 <= hue_value <= 210) and (64 <= sat_value <= 84) and (69 <= val_value <= 89):
        color = "Baby Blue Eyes"
        s = gTTS(text="Baby Blue Eyes", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (hue_value <= 5) and (59 <= sat_value <= 79) and (76 <= val_value <= 96):
        color = "Baby pink"
        s = gTTS(text="Baby Pink", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (43 <= hue_value <= 51) and (90 <= sat_value <= 110) and (48 <= val_value <= 68):
        color = "Banana Yellow"
        s = gTTS(text="Banana Yellow", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (56 <= hue_value <= 64) and (0 <= sat_value <= 11) and (41 <= val_value <= 61):
        color = "Battleship Grey"
        s = gTTS(text="Battleship Grey", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (349 <= hue_value <= 357) and (4 <= sat_value <= 24) and (43 <= val_value <= 63):
        color = "Bazaar"
        s = gTTS(text="Bazaar", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (56 <= hue_value <= 64) and (46 <= sat_value <= 66) and (81 <= val_value <= 101):
        color = "Beige"
        s = gTTS(text="Beige", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (20 <= hue_value <= 28) and (23 <= sat_value <= 23) and (8 <= val_value <= 28):
        color = "Bistre"
        s = gTTS(text="Bistre", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (hue_value <= 5) and (0 <= sat_value <= 10) and (0 <= val_value <= 10):
        color = "Black"
        s = gTTS(text="Black", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (205 <= hue_value <= 214) and (69 <= sat_value <= 89) and (45 <= val_value <= 65):
        color = "Bleu De France"
        s = gTTS(text="Bleu De France", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (46 <= hue_value <= 54) and (76 <= sat_value <= 96) and (76 <= val_value <= 96):
        color = "Blond"
        s = gTTS(text="Blond", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (234 <= hue_value <= 246) and (90 <= sat_value <= 110) and (40 <= val_value <= 60):
        color = "Blue"
        s = gTTS(text="Blue", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (338 <= hue_value <= 346) and (56 <= sat_value <= 76) and (52 <= val_value <= 72):
        color = "Blush"
        s = gTTS(text="Blush", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (6 <= hue_value <= 12) and (24 <= sat_value <= 44) and (25 <= val_value <= 45):
        color = "Bole"
        s = gTTS(text="Bole", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (0 <= hue_value <= 5) and (90 <= sat_value <= 110) and (30 <= val_value <= 50):
        color = "Boston University Red"
        s = gTTS(text="Boston University Red", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (48 <= hue_value <= 56) and (37 <= sat_value <= 57) and (38 <= val_value <= 58):
        color = "Brass"
        s = gTTS(text="Brass", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (92 <= hue_value <= 100) and (90 <= sat_value <= 110) and (40 <= val_value <= 60):
        color = "Bright Green"
        s = gTTS(text="Bright Green", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (268 <= hue_value <= 276) and (50 <= sat_value <= 70) and (64 <= val_value <= 84):
        color = "Bright Lavender"
        s = gTTS(text="Bright Lavender", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (342 <= hue_value <= 350) and (61 <= sat_value <= 81) and (35 <= val_value <= 55):
        color = "Bright Maroon"
        s = gTTS(text="Bright Maroon", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (326 <= hue_value <= 334) and (90 <= sat_value <= 110) and (40 <= val_value <= 60):
        color = "Bright Pink"
        s = gTTS(text="Bright Pink", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (173 <= hue_value <= 181) and (83 <= sat_value <= 103) and (37 <= val_value <= 57):
        color = "Bright Turquoise"
        s = gTTS(text="Bright Turquoise", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (277 <= hue_value <= 286) and (51 <= sat_value <= 71) and (67 <= val_value <= 87):
        color = "Bright Ube"
        s = gTTS(text="Bright Ube", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (150 <= hue_value <= 158) and (90 <= sat_value <= 110) and (3 <= val_value <= 23):
        color = "British Racing Green"
        s = gTTS(text="British Racing Green", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (26 <= hue_value <= 34) and (51 <= sat_value <= 71) and (40 <= val_value <= 60):
        color = "Bronze"
        s = gTTS(text="Bronze", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (26 <= hue_value <= 34) and (90 <= sat_value <= 110) and (19 <= val_value <= 39):
        color = "Brown"
        s = gTTS(text="Brown", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (345 <= hue_value <= 353) and (90 <= sat_value <= 110) and (78 <= val_value <= 98):
        color = "Bubble Gum"
        s = gTTS(text="Bubble Gum", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (178 <= hue_value <= 190) and (90 <= sat_value <= 110) and (85 <= val_value <= 105):
        color = "Bubbles"
        s = gTTS(text="Bubbles", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (45 <= hue_value <= 53) and (69 <= sat_value <= 89) and (63 <= val_value <= 83):
        color = "Buff"
        s = gTTS(text="Buff", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (341 <= hue_value <= 349) and (90 <= sat_value <= 110) and (15 <= val_value <= 35):
        color = "Burgundy"
        s = gTTS(text="Burgundy", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (30 <= hue_value <= 38) and (47 <= sat_value <= 67) and (60 <= val_value <= 80):
        color = "Burlywood"
        s = gTTS(text="Burlywood", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (21 <= hue_value <= 29) and (90 <= sat_value <= 110) and (30 <= val_value <= 50):
        color = "Burnt Orange"
        s = gTTS(text="Burnt Orange", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (10 <= hue_value <= 18) and (68 <= sat_value <= 88) and (52 <= val_value <= 72):
        color = "Burnt Sienna"
        s = gTTS(text="Burnt Sienna", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (6 <= hue_value <= 12) and (49 <= sat_value <= 69) and (24 <= val_value <= 44):
        color = "Burnt Umber"
        s = gTTS(text="Burnt Umber", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (306 <= hue_value <= 315) and (48 <= sat_value <= 68) and (37 <= val_value <= 57):
        color = "Byzantine"
        s = gTTS(text="Byzantine", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (306 <= hue_value <= 315) and (36 <= sat_value <= 56) and (20 <= val_value <= 40):
        color = "Byzantium"
        s = gTTS(text="Byzantium", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (202 <= hue_value <= 210) and (8 <= sat_value <= 28) and (30 <= val_value <= 50):
        color = "Cadet"
        s = gTTS(text="Cadet", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (150 <= hue_value <= 158) and (90 <= sat_value <= 110) and (11 <= val_value <= 31):
        color = "Cadmium Green"
        s = gTTS(text="Cadium Green", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (24 <= hue_value <= 32) and (74 <= sat_value <= 94) and (45 <= val_value <= 65):
        color = "Cadmium Orange"
        s = gTTS(text="Cadium Orange", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (347 <= hue_value <= 355) and (90 <= sat_value <= 110) and (35 <= val_value <= 55):
        color = "Cadmium Red"
        s = gTTS(text="Cadium Red", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (136 <= hue_value <= 144) and (9 <= sat_value <= 29) and (60 <= val_value <= 80):
        color = "Cambridge Blue"
        s = gTTS(text="Cadium Blue", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (87 <= hue_value <= 95) and (1 <= sat_value <= 21) and (37 <= val_value <= 57):
        color = "Camouflage Green"
        s = gTTS(text="Camouflage Green", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (52 <= hue_value <= 60) and (90 <= sat_value <= 110) and (40 <= val_value <= 60):
        color = "Canary Yellow"
        s = gTTS(text="Canary Yellow", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (0 <= hue_value <= 5) and (90 <= sat_value <= 110) and (40 <= val_value <= 60):
        color = "Candy Apple Red"
        s = gTTS(text="Candy Apple Red", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (346 <= hue_value <= 354) and (63 <= sat_value <= 83) and (34 <= val_value <= 54):
        color = "Cardinal"
        s = gTTS(text="Cardinal", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (160 <= hue_value <= 171) and (90 <= sat_value <= 110) and (30 <= val_value <= 50):
        color = "Caribbean Green"
        s = gTTS(text="Caribbean Green", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (346 <= hue_value <= 354) and (90 <= sat_value <= 110) and (19 <= val_value <= 39):
        color = "Carmine"
        s = gTTS(text="Carmine", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (207 <= hue_value <= 215) and (40 <= sat_value <= 60) and (63 <= val_value <= 83):
        color = "Carolina Blue"
        s = gTTS(text="Carolina Blue", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (29 <= hue_value <= 37) and (75 <= sat_value <= 95) and (43 <= val_value <= 63):
        color = "Carrot Orange"
        s = gTTS(text="Carrot Orange", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (221 <= hue_value <= 229) and (29 <= sat_value <= 49) and (59 <= val_value <= 79):
        color = "Ceil"
        s = gTTS(text="Ceil", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (119 <= hue_value <= 130) and (37 <= sat_value <= 57) and (68 <= val_value <= 88):
        color = "Celadon"
        s = gTTS(text="Celadon", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (190 <= hue_value <= 200) and (90 <= sat_value <= 110) and (23 <= val_value <= 43):
        color = "Cerulean"
        s = gTTS(text="Cerulean", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (220 <= hue_value <= 228) and (54 <= sat_value <= 74) and (35 <= val_value <= 55):
        color = "Cerulean Blue"
        s = gTTS(text="Cerulean Blue", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (22 <= hue_value <= 30) and (18 <= sat_value <= 38) and (39 <= val_value <= 59):
        color = "Chamoisee"
        s = gTTS(text="Chamoisee", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (33 <= hue_value <= 41) and (62 <= sat_value <= 82) and (79 <= val_value <= 99):
        color = "Champagne"
        s = gTTS(text="Champagne", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (200 <= hue_value <= 208) and (9 <= sat_value <= 29) and (16 <= val_value <= 36):
        color = "Charcoal"
        s = gTTS(text="Charcoal", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (64 <= hue_value <= 72) and (90 <= sat_value <= 110) and (40 <= val_value <= 60):
        color = "Chartreuse"
        s = gTTS(text="Chartreuse", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (339 <= hue_value <= 347) and (62 <= sat_value <= 82) and (43 <= val_value <= 63):
        color = "Cherry"
        s = gTTS(text="Cherry", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (344 <= hue_value <= 352) and (90 <= sat_value <= 110) and (76 <= val_value <= 96):
        color = "Cherry Blossom Pink"
        s = gTTS(text="Cherry Blossom Pink", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (hue_value <= 5) and (43 <= sat_value <= 63) and (48 <= val_value <= 68):
        color = "Chestnut"
        s = gTTS(text="Chestnut", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (27 <= hue_value <= 35) and (90 <= sat_value <= 110) and (14 <= val_value <= 34):
        color = "Chocolate"
        s = gTTS(text="Chocolate", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (35 <= hue_value <= 43) and (90 <= sat_value <= 110) and (40 <= val_value <= 60):
        color = "Chrome Yellow"
        s = gTTS(text="Chrome Yellow", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (8 <= hue_value <= 16) and (2 <= sat_value <= 22) and (44 <= val_value <= 64):
        color = "Cinereous"
        s = gTTS(text="Cinereous", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (0 <= hue_value <= 6) and (66 <= sat_value <= 86) and (45 <= val_value <= 65):
        color = "Cinnabar"
        s = gTTS(text="Cinnabar", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (21 <= hue_value <= 29) and (65 <= sat_value <= 85) and (67 <= val_value <= 57):
        color = "Cinnamon"
        s = gTTS(text="Cinnamon", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (51 <= hue_value <= 59) and (82 <= sat_value <= 102) and (67 <= val_value <= 57):
        color = "Citrine"
        s = gTTS(text="Citrine", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (322 <= hue_value <= 330) and (75 <= sat_value <= 95) and (79 <= val_value <= 99):
        color = "Classic Rose"
        s = gTTS(text="Classic Rose", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (142 <= hue_value <= 150) and (90 <= sat_value <= 110) and (40 <= val_value <= 60):
        color = "Clover"
        s = gTTS(text="Clover", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (211 <= hue_value <= 219) and (90 <= sat_value <= 110) and (24 <= val_value <= 44):
        color = "Cobalt"
        s = gTTS(text="Cobalt", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (196 <= hue_value <= 204) and (90 <= sat_value <= 110) and (70 <= val_value <= 90):
        color = "Columbia Blue"
        s = gTTS(text="Columbia Blue", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (208 <= hue_value <= 216) and (90 <= sat_value <= 110) and (9 <= val_value <= 29):
        color = "Cool Black"
        s = gTTS(text="Cool Black", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (225 <= hue_value <= 236) and (6 <= sat_value <= 26) and (51 <= val_value <= 71):
        color = "Cool Grey"
        s = gTTS(text="Cool Grey", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (25 <= hue_value <= 33) and (47 <= sat_value <= 67) and (36 <= val_value <= 56):
        color = "Copper"
        s = gTTS(text="Copper", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (9 <= hue_value <= 17) and (90 <= sat_value <= 110) and (40 <= val_value <= 60):
        color = "Coquelicot"
        s = gTTS(text="Coquelicot", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (14 <= hue_value <= 20) and (90 <= sat_value <= 110) and (56 <= val_value <= 76):
        color = "Coral"
        s = gTTS(text="Coral", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (351 <= hue_value <= 359) and (27 <= sat_value <= 47) and (29 <= val_value <= 49):
        color = "Cordovan"
        s = gTTS(text="Cordovan", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (50 <= hue_value <= 58) and (85 <= sat_value <= 105) and (57 <= val_value <= 77):
        color = "Corn"
        s = gTTS(text="Corn", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (0 <= hue_value <= 5) and (64 <= sat_value <= 84) and (30 <= val_value <= 50):
        color = "Cornell Red"
        s = gTTS(text="Cornell Red", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (215 <= hue_value <= 223) and (69 <= sat_value <= 89) and (56 <= val_value <= 76):
        color = "Cornflower Blue"
        s = gTTS(text="Cornflower Blue", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (44 <= hue_value <= 52) and (90 <= sat_value <= 110) and (83 <= val_value <= 103):
        color = "Cornsilk"
        s = gTTS(text="Cornsilk", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (53 <= hue_value <= 61) and (90 <= sat_value <= 110) and (81 <= val_value <= 101):
        color = "Cream"
        s = gTTS(text="Cream", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (344 <= hue_value <= 352) and (73 <= sat_value <= 93) and (67 <= val_value <= 57):
        color = "Crimson"
        s = gTTS(text="Crimson", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (176 <= hue_value <= 184) and (90 <= sat_value <= 110) and (40 <= val_value <= 60):
        color = "Cyan"
        s = gTTS(text="Cyan", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (56 <= hue_value <= 64) and (90 <= sat_value <= 110) and (50 <= val_value <= 70):
        color = "Daffodil"
        s = gTTS(text="Daffodil", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (51 <= hue_value <= 59) and (76 <= sat_value <= 96) and (46 <= val_value <= 66):
        color = "Dandelion"
        s = gTTS(text="Dandelion", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (234 <= hue_value <= 246) and (90 <= sat_value <= 110) and (17 <= val_value <= 37):
        color = "Dark Blue"
        s = gTTS(text="Dark Blue", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (26 <= hue_value <= 34) and (41 <= sat_value <= 61) and (16 <= val_value <= 36):
        color = "Dark Brown"
        s = gTTS(text="Dark Brown", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (306 <= hue_value <= 320) and (14 <= sat_value <= 34) and (19 <= val_value <= 39):
        color = "Dark Byzantium"
        s = gTTS(text="Dark Byzantium", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (0 <= hue_value <= 5) and (90 <= sat_value <= 110) and (22 <= val_value <= 42):
        color = "Dark Candy Apple Red"
        s = gTTS(text="Dark Candy Apple Red", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (205 <= hue_value <= 213) and (78 <= sat_value <= 98) and (16 <= val_value <= 36):
        color = "Dark Cerulean"
        s = gTTS(text="Dark Cerulean", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (6 <= hue_value <= 14) and (13 <= sat_value <= 33) and (39 <= val_value <= 59):
        color = "Dark Chestnut"
        s = gTTS(text="Dark Chestnut", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (6 <= hue_value <= 14) and (48 <= sat_value <= 68) and (44 <= val_value <= 64):
        color = "Dark Coral"
        s = gTTS(text="Dark Coral", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (176 <= hue_value <= 184) and (90 <= sat_value <= 110) and (17 <= val_value <= 37):
        color = "Dark Cyan"
        s = gTTS(text="Dark Cyan", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (39 <= hue_value <= 47) and (79 <= sat_value <= 99) and (28 <= val_value <= 48):
        color = "Dark Goldenrod"
        s = gTTS(text="Dark Goldenrod", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (154 <= hue_value <= 162) and (86 <= sat_value <= 106) and (0 <= val_value <= 20):
        color = "Dark Green"
        s = gTTS(text="Dark Green", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (158 <= hue_value <= 166) and (6 <= sat_value <= 26) and (2 <= val_value <= 22):
        color = "Dark Jungle Green"
        s = gTTS(text="Dark Jungle Green", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (52 <= hue_value <= 60) and (28 <= sat_value <= 48) and (48 <= val_value <= 68):
        color = "Dark Khaki"
        s = gTTS(text="Dark Khaki", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (23 <= hue_value <= 31) and (8 <= sat_value <= 28) and (14 <= val_value <= 34):
        color = "Dark Lava"
        s = gTTS(text="Dark Lava", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (266 <= hue_value <= 274) and (21 <= sat_value <= 41) and (35 <= val_value <= 55):
        color = "Dark Lavender"
        s = gTTS(text="Dark Lavender", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (296 <= hue_value <= 304) and (90 <= sat_value <= 110) and (17 <= val_value <= 37):
        color = "Dark Magenta"
        s = gTTS(text="Dark Magenta", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (205 <= hue_value <= 214) and (90 <= sat_value <= 110) and (10 <= val_value <= 30):
        color = "Dark Midnight Blue"
        s = gTTS(text="Dark Midnight Blue", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (78 <= hue_value <= 86) and (29 <= sat_value <= 49) and (20 <= val_value <= 40):
        color = "Dark Olive Green"
        s = gTTS(text="Dark Olive Green", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (29 <= hue_value <= 37) and (90 <= sat_value <= 110) and (40 <= val_value <= 60):
        color = "Dark Orange"
        s = gTTS(text="Dark Orange", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (208 <= hue_value <= 216) and (35 <= sat_value <= 55) and (53 <= val_value <= 73):
        color = "Dark Pastel Blue"
        s = gTTS(text="Dark Pastel Blue", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (134 <= hue_value <= 142) and (87 <= sat_value <= 107) and (28 <= val_value <= 48):
        color = "Dark Pastel Green"
        s = gTTS(text="Dark Pastel Green", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (253 <= hue_value <= 267) and (46 <= sat_value <= 66) and (54 <= val_value <= 74):
        color = "Dark Pastel Purple"
        s = gTTS(text="Dark Pastel Purple", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (6 <= hue_value <= 12) and (60 <= sat_value <= 80) and (35 <= val_value <= 55):
        color = "Dark Pastel Red"
        s = gTTS(text="Dark Pastel Red", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (338 <= hue_value <= 346) and (65 <= sat_value <= 85) and (52 <= val_value <= 72):
        color = "Dark Pink"
        s = gTTS(text="Dark Pink", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (216 <= hue_value <= 224) and (90 <= sat_value <= 110) and (20 <= val_value <= 40):
        color = "Dark Powder Blue"
        s = gTTS(text="Dark Powder Blue", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (326 <= hue_value <= 334) and (46 <= sat_value <= 66) and (24 <= val_value <= 44):
        color = "Dark Raspberry"
        s = gTTS(text="Dark Raspberry", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (11 <= hue_value <= 19) and (62 <= sat_value <= 82) and (60 <= val_value <= 80):
        color = "Dark Salmon"
        s = gTTS(text="Dark Salmon", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (340 <= hue_value <= 348) and (83 <= sat_value <= 103) and (7 <= val_value <= 27):
        color = "Dark Scarlet"
        s = gTTS(text="Dark Scarlet", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (0 <= hue_value <= 5) and (5 <= sat_value <= 25) and (6 <= val_value <= 26):
        color = "Dark Sienna"
        s = gTTS(text="Dark Sienna", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (176 <= hue_value <= 184) and (15 <= sat_value <= 35) and (15 <= val_value <= 35):
        color = "Dark Slate Gray"
        s = gTTS(text="Dark Slate Gray", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (146 <= hue_value <= 154) and (56 <= sat_value <= 76) and (17 <= val_value <= 37):
        color = "Dark Spring Green"
        s = gTTS(text="Dark Spring Green", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (41 <= hue_value <= 49) and (18 <= sat_value <= 38) and (34 <= val_value <= 54):
        color = "Dark Tan"
        s = gTTS(text="Dark Tan", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (34 <= hue_value <= 42) and (90 <= sat_value <= 110) and (44 <= val_value <= 64):
        color = "Dark Tangerine"
        s = gTTS(text="Dark Tangerine", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (349 <= hue_value <= 357) and (45 <= sat_value <= 65) and (45 <= val_value <= 65):
        color = "Dark Terra Cotta"
        s = gTTS(text="Dark Terra Cotta", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (277 <= hue_value <= 290) and (90 <= sat_value <= 110) and (31 <= val_value <= 51):
        color = "Dark Violet"
        s = gTTS(text="Dark Violet", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (0 <= hue_value <= 5) and (0 <= sat_value <= 10) and (23 <= val_value <= 43):
        color = "Davy'S Grey"
        s = gTTS(text="Davy's Grey", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (209 <= hue_value <= 217) and (70 <= sat_value <= 90) and (31 <= val_value <= 51):
        color = "Denim"
        s = gTTS(text="Denim", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (29 <= hue_value <= 37) and (31 <= sat_value <= 51) and (49 <= val_value <= 69):
        color = "Desert"
        s = gTTS(text="Desert", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (21 <= hue_value <= 29) and (53 <= sat_value <= 73) and (71 <= val_value <= 91):
        color = "Desert Sand"
        s = gTTS(text="Desert Sand", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (0 <= hue_value <= 5) and (0 <= sat_value <= 10) and (31 <= val_value <= 51):
        color = "Dim Gray"
        s = gTTS(text="Dim Gray", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (94 <= hue_value <= 107) and (29 <= sat_value <= 49) and (46 <= val_value <= 66):
        color = "Dollar Bill"
        s = gTTS(text="Dollar Bill", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (234 <= hue_value <= 246) and (90 <= sat_value <= 110) and (21 <= val_value <= 41):
        color = "Duke Blue"
        s = gTTS(text="Duke Blue", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (30 <= hue_value <= 38) and (58 <= sat_value <= 78) and (53 <= val_value <= 73):
        color = "Earth Yellow"
        s = gTTS(text="Earth Yellow", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (325 <= hue_value <= 333) and (11 <= sat_value <= 31) and (22 <= val_value <= 42):
        color = "Eggplant"
        s = gTTS(text="Eggplant", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (136 <= hue_value <= 144) and (42 <= sat_value <= 62) and (45 <= val_value <= 65):
        color = "Emerald"
        s = gTTS(text="Emerald", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (26 <= hue_value <= 34) and (59 <= sat_value <= 79) and (57 <= val_value <= 77):
        color = "Fawn"
        s = gTTS(text="Fawn", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (6 <= hue_value <= 8) and (90 <= sat_value <= 110) and (40 <= val_value <= 60):
        color = "Ferrari Red"
        s = gTTS(text="Ferrari Red", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (352 <= hue_value <= 360) and (71 <= sat_value <= 91) and (35 <= val_value <= 55):
        color = "Fire Engine Red"
        s = gTTS(text="Fire Engine Red", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (0 <= hue_value <= 5) and (58 <= sat_value <= 78) and (32 <= val_value <= 52):
        color = "Firebrick"
        s = gTTS(text="Firebrick", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (13 <= hue_value <= 21) and (67 <= sat_value <= 87) and (41 <= val_value <= 61):
        color = "Flame"
        s = gTTS(text="Flame", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (340 <= hue_value <= 348) and (85 <= sat_value <= 105) and (67 <= val_value <= 87):
        color = "Flamingo Pink"
        s = gTTS(text="Flamingo Pink", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (48 <= hue_value <= 56) and (77 <= sat_value <= 97) and (66 <= val_value <= 86):
        color = "Flavescent"
        s = gTTS(text="Flavescent", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (145 <= hue_value <= 153) and (87 <= sat_value <= 107) and (4 <= val_value <= 24):
        color = "Forest Green"
        s = gTTS(text="Forest Green", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (35 <= hue_value <= 43) and (78 <= sat_value <= 98) and (38 <= val_value <= 58):
        color = "Gamboge"
        s = gTTS(text="Gamboge", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (234 <= hue_value <= 246) and (90 <= sat_value <= 110) and (89 <= val_value <= 109):
        color = "Ghost White"
        s = gTTS(text="Ghost White", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (212 <= hue_value <= 220) and (27 <= sat_value <= 47) and (45 <= val_value <= 65):
        color = "Glaucous"
        s = gTTS(text="Glaucous", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (32 <= hue_value <= 40) and (66 <= sat_value <= 86) and (24 <= val_value <= 44):
        color = "Golden Brown"
        s = gTTS(text="Golden Brown", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (48 <= hue_value <= 56) and (90 <= sat_value <= 110) and (40 <= val_value <= 60):
        color = "Golden Yellow"
        s = gTTS(text="Golden Yellow", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (39 <= hue_value <= 47) and (64 <= sat_value <= 84) and (39 <= val_value <= 59):
        color = "Goldenrod"
        s = gTTS(text="Goldenrod", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (0 <= hue_value <= 5) and (0 <= sat_value <= 10) and (40 <= val_value <= 60):
        color = "Gray"
        s = gTTS(text="Gray", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (116 <= hue_value <= 124) and (90 <= sat_value <= 110) and (15 <= val_value <= 35):
        color = "Green"
        s = gTTS(text="Green", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (203 <= hue_value <= 211) and (42 <= sat_value <= 62) and (53 <= val_value <= 73):
        color = "Iceberg"
        s = gTTS(text="Iceberg", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (54 <= hue_value <= 62) and (86 <= sat_value <= 106) and (58 <= val_value <= 78):
        color = "Icterine"
        s = gTTS(text="Icterine", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (80 <= hue_value <= 88) and (69 <= sat_value <= 89) and (55 <= val_value <= 75):
        color = "Inchworm"
        s = gTTS(text="Inchworm", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (107 <= hue_value <= 120) and (79 <= sat_value <= 99) and (18 <= val_value <= 38):
        color = "India Green"
        s = gTTS(text="India Green", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (hue_value <= 5) and (90 <= sat_value <= 110) and (58 <= val_value <= 78):
        color = "Indian Red"
        s = gTTS(text="Indian Red", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (31 <= hue_value <= 39) and (61 <= sat_value <= 81) and (52 <= val_value <= 72):
        color = "Indian Yellow"
        s = gTTS(text="Indian Yellow", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (219 <= hue_value <= 227) and (90 <= sat_value <= 110) and (23 <= val_value <= 43):
        color = "International Klein Blue"
        s = gTTS(text="International Klein Blue", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (56 <= hue_value <= 64) and (90 <= sat_value <= 110) and (87 <= val_value <= 107):
        color = "Ivory"
        s = gTTS(text="Ivory", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (154 <= hue_value <= 162) and (90 <= sat_value <= 110) and (23 <= val_value <= 43):
        color = "Jade"
        s = gTTS(text="Jade", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (352 <= hue_value <= 360) and (56 <= sat_value <= 76) and (44 <= val_value <= 64):
        color = "Jasper"
        s = gTTS(text="Jasper", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (33 <= hue_value <= 41) and (19 <= sat_value <= 39) and (57 <= val_value <= 77):
        color = "Khaki"
        s = gTTS(text="Khaki", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (271 <= hue_value <= 279) and (47 <= sat_value <= 67) and (58 <= val_value <= 78):
        color = "Lavender"
        s = gTTS(text="Lavender", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (234 <= hue_value <= 246) and (90 <= sat_value <= 110) and (80 <= val_value <= 100):
        color = "Lavender Blue"
        s = gTTS(text="Lavender Blue", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (336 <= hue_value <= 344) and (90 <= sat_value <= 110) and (87 <= val_value <= 107):
        color = "Lavender Blush"
        s = gTTS(text="Lavender Blush", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (240 <= hue_value <= 255) and (2 <= sat_value <= 22) and (69 <= val_value <= 89):
        color = "Lavender Gray"
        s = gTTS(text="Lavender Gray", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (86 <= hue_value <= 94) and (90 <= sat_value <= 110) and (39 <= val_value <= 59):
        color = "Lawn Green"
        s = gTTS(text="Lawn Green", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (54 <= hue_value <= 62) and (90 <= sat_value <= 110) and (40 <= val_value <= 60):
        color = "Lemon"
        s = gTTS(text="Lemon", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (71 <= hue_value <= 79) and (90 <= sat_value <= 110) and (40 <= val_value <= 60):
        color = "Lime"
        s = gTTS(text="Lime", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (296 <= hue_value <= 304) and (90 <= sat_value <= 110) and (40 <= val_value <= 60):
        color = "Magenta"
        s = gTTS(text="Magenta", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (16 <= hue_value <= 24) and (90 <= sat_value <= 110) and (28 <= val_value <= 48):
        color = "Mahogany"
        s = gTTS(text="Mahogany", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (hue_value <= 5) and (90 <= sat_value <= 110) and (15 <= val_value <= 35):
        color = "Maroon"
        s = gTTS(text="Maroon", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (234 <= hue_value <= 246) and (54 <= sat_value <= 74) and (17 <= val_value <= 37):
        color = "Midnight Blue"
        s = gTTS(text="Midnight Blue", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (154 <= hue_value <= 162) and (39 <= sat_value <= 59) and (67 <= val_value <= 57):
        color = "Mint"
        s = gTTS(text="Mint", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (43 <= hue_value <= 51) and (90 <= sat_value <= 110) and (57 <= val_value <= 77):
        color = "Mustard"
        s = gTTS(text="Mustard", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (234 <= hue_value <= 246) and (90 <= sat_value <= 110) and (15 <= val_value <= 35):
        color = "Navy Blue"
        s = gTTS(text="Navy Blue", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (26 <= hue_value <= 34) and (61 <= sat_value <= 81) and (67 <= val_value <= 57):
        color = "Ochre"
        s = gTTS(text="Ochre", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (56 <= hue_value <= 64) and (90 <= sat_value <= 110) and (15 <= val_value <= 35):
        color = "Olive"
        s = gTTS(text="Olive", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (26 <= hue_value <= 34) and (90 <= sat_value <= 110) and (40 <= val_value <= 60):
        color = "Orange"
        s = gTTS(text="Orange", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (208 <= hue_value <= 216) and (90 <= sat_value <= 110) and (4 <= val_value <= 24):
        color = "Oxford Blue"
        s = gTTS(text="Oxford Blue", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (190 <= hue_value <= 200) and (16 <= sat_value <= 36) and (65 <= val_value <= 85):
        color = "Pastel Blue"
        s = gTTS(text="Pastel Blue", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (24 <= hue_value <= 32) and (12 <= sat_value <= 32) and (32 <= val_value <= 52):
        color = "Pastel Brown"
        s = gTTS(text="Pastel Brown", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (56 <= hue_value <= 64) and (0 <= sat_value <= 20) and (69 <= val_value <= 89):
        color = "Pastel Gray"
        s = gTTS(text="Pastel Gray", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (116 <= hue_value <= 124) and (50 <= sat_value <= 70) and (57 <= val_value <= 77):
        color = "Pastel Green"
        s = gTTS(text="Pastel Green", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (329 <= hue_value <= 337) and (70 <= sat_value <= 90) and (68 <= val_value <= 88):
        color = "Pastel Magenta"
        s = gTTS(text="Pastel Magenta", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (hue_value == 35) and (90 <= sat_value <= 110) and (54 <= val_value <= 74):
        color = "Pastel Orange"
        s = gTTS(text="Pastel Orange", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (342 <= hue_value <= 350) and (90 <= sat_value <= 110) and (81 <= val_value <= 101):
        color = "Pastel Pink"
        s = gTTS(text="Pastel Pink", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (287 <= hue_value <= 299) and (3 <= sat_value <= 23) and (56 <= val_value <= 76):
        color = "Pastel Purple"
        s = gTTS(text="Pastel Purple", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (0 <= hue_value <= 5) and (90 <= sat_value <= 110) and (59 <= val_value <= 79):
        color = "Pastel Red"
        s = gTTS(text="Pastel Red", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (298 <= hue_value <= 306) and (22 <= sat_value <= 42) and (60 <= val_value <= 80):
        color = "Pastel Violet"
        s = gTTS(text="Pastel Violet", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (56 <= hue_value <= 64) and (86 <= sat_value <= 106) and (69 <= val_value <= 89):
        color = "Pastel Yellow"
        s = gTTS(text="Pastel Yellow", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (35 <= hue_value <= 43) and (90 <= sat_value <= 110) and (75 <= val_value <= 95):
        color = "Peach"
        s = gTTS(text="Peach", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (62 <= hue_value <= 70) and (65 <= sat_value <= 85) and (44 <= val_value <= 64):
        color = "Pear"
        s = gTTS(text="Pear", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (42 <= hue_value <= 50) and (36 <= sat_value <= 56) and (79 <= val_value <= 99):
        color = "Pearl"
        s = gTTS(text="Pearl", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (55 <= hue_value <= 63) and (90 <= sat_value <= 110) and (35 <= val_value <= 55):
        color = "Peridot"
        s = gTTS(text="Peridot", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (169 <= hue_value <= 179) and (88 <= sat_value <= 108) and (14 <= val_value <= 34):
        color = "Pine Green"
        s = gTTS(text="Pine Green", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (346 <= hue_value <= 354) and (90 <= sat_value <= 110) and (78 <= val_value <= 98):
        color = "Pink"
        s = gTTS(text="Pink", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (92 <= hue_value <= 100) and (32 <= sat_value <= 52) and (51 <= val_value <= 71):
        color = "Pistachio"
        s = gTTS(text="Pistachio", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (36 <= hue_value <= 44) and (0 <= sat_value <= 15) and (79 <= val_value <= 99):
        color = "Platinum"
        s = gTTS(text="Platinum", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (303 <= hue_value <= 311) and (25 <= sat_value <= 45) and (31 <= val_value <= 51):
        color = "Plum"
        s = gTTS(text="Plum", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (7 <= hue_value <= 15) and (90 <= sat_value <= 110) and (51 <= val_value <= 71):
        color = "Portland Orange"
        s = gTTS(text="Portland Orange", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (hue_value <= 5) and (50 <= sat_value <= 70) and (17 <= val_value <= 37):
        color = "Prune"
        s = gTTS(text="Prune", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (20 <= hue_value <= 28) and (90 <= sat_value <= 110) and (45 <= val_value <= 65):
        color = "Pumpkin"
        s = gTTS(text="Pumpkin", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (266 <= hue_value <= 274) and (39 <= sat_value <= 59) and (31 <= val_value <= 51):
        color = "Purple Heart"
        s = gTTS(text="Purple Heart", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (333 <= hue_value <= 341) and (81 <= sat_value <= 101) and (67 <= val_value <= 57):
        color = "Raspberry"
        s = gTTS(text="Raspberry", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (29 <= hue_value <= 37) and (21 <= sat_value <= 41) and (29 <= val_value <= 49):
        color = "Raw Umber"
        s = gTTS(text="Raw Umber", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (hue_value <= 5) and (90 <= sat_value <= 110) and (40 <= val_value <= 60):
        color = "Red"
        s = gTTS(text="Red", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (75 <= hue_value <= 84) and (7 <= sat_value <= 27) and (14 <= val_value <= 34):
        color = "Rifle Green"
        s = gTTS(text="Rifle Green", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (349 <= hue_value <= 357) and (90 <= sat_value <= 110) and (10 <= val_value <= 30):
        color = "Rose Wood"
        s = gTTS(text="Rose wood", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (215 <= hue_value <= 223) and (90 <= sat_value <= 110) and (10 <= val_value <= 30):
        color = "Royal Blue"
        s = gTTS(text="Royal Blue", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (333 <= hue_value <= 341) and (76 <= sat_value <= 96) and (67 <= val_value <= 57):
        color = "Ruby"
        s = gTTS(text="Ruby", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (14 <= hue_value <= 22) and (76 <= sat_value <= 96) and (29 <= val_value <= 49):
        color = "Rust"
        s = gTTS(text="Rust", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (20 <= hue_value <= 28) and (90 <= sat_value <= 110) and (40 <= val_value <= 60):
        color = "Safety Orange"
        s = gTTS(text="Safety Orange", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (41 <= hue_value <= 49) and (80 <= sat_value <= 100) and (47 <= val_value <= 67):
        color = "Saffron"
        s = gTTS(text="Saffron", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (10 <= hue_value <= 18) and (90 <= sat_value <= 110) and (61 <= val_value <= 81):
        color = "Salmon"
        s = gTTS(text="Salmon", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (41 <= hue_value <= 49) and (25 <= sat_value <= 45) and (53 <= val_value <= 73):
        color = "Sand"
        s = gTTS(text="Sand", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (39 <= hue_value <= 47) and (63 <= sat_value <= 83) and (24 <= val_value <= 44):
        color = "Sand Dune"
        s = gTTS(text="Sand Dune", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (48 <= hue_value <= 56) and (72 <= sat_value <= 92) and (49 <= val_value <= 69):
        color = "Sandstorm"
        s = gTTS(text="Sandstorm", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (218 <= hue_value <= 226) and (76 <= sat_value <= 96) and (12 <= val_value <= 32):
        color = "Sapphire"
        s = gTTS(text="Sapphire", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (hue_value <= 5) and (33 <= sat_value <= 53) and (4 <= val_value <= 24):
        color = "Seal Brown"
        s = gTTS(text="Seal Brown", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (21 <= hue_value <= 29) and (90 <= sat_value <= 110) and (87 <= val_value <= 107):
        color = "Seashell"
        s = gTTS(text="Seashell", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (26 <= hue_value <= 34) and (60 <= sat_value <= 80) and (16 <= val_value <= 36):
        color = "Sepia"
        s = gTTS(text="Sepia", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (33 <= hue_value <= 41) and (9 <= sat_value <= 29) and (35 <= val_value <= 55):
        color = "Shadow"
        s = gTTS(text="Shadow", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (hue_value <= 5) and (0 <= sat_value <= 10) and (65 <= val_value <= 85):
        color = "Silver"
        s = gTTS(text="Silver", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (13 <= hue_value <= 21) and (80 <= sat_value <= 100) and (32 <= val_value <= 52):
        color = "Sinopia"
        s = gTTS(text="Sinopia", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (193 <= hue_value <= 201) and (61 <= sat_value <= 81) and (63 <= val_value <= 83):
        color = "Sky Blue"
        s = gTTS(text="Sky Blue", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (315 <= hue_value <= 325) and (39 <= sat_value <= 59) and (53 <= val_value <= 73):
        color = "Sky Magenta"
        s = gTTS(text="Sky Magenta", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (hue_value <= 5) and (90 <= sat_value <= 110) and (89 <= val_value <= 109):
        color = "Snow"
        s = gTTS(text="Snow", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (75 <= hue_value <= 84) and (90 <= sat_value <= 110) and (39 <= val_value <= 59):
        color = "Spring Bud"
        s = gTTS(text="Spring Bud", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (203 <= hue_value <= 211) and (34 <= sat_value <= 54) and (39 <= val_value <= 59):
        color = "Steel Blue"
        s = gTTS(text="Steel Blue", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (50 <= hue_value <= 58) and (58 <= sat_value <= 78) and (56 <= val_value <= 76):
        color = "Straw"
        s = gTTS(text="Straw", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (31 <= hue_value <= 39) and (79 <= sat_value <= 99) and (71 <= val_value <= 91):
        color = "Sunset"
        s = gTTS(text="Sunset", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (29 <= hue_value <= 37) and (90 <= sat_value <= 110) and (67 <= val_value <= 57):
        color = "Tangerine"
        s = gTTS(text="Tangerine", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (176 <= hue_value <= 184) and (90 <= sat_value <= 110) and (15 <= val_value <= 35):
        color = "Teal"
        s = gTTS(text="Teal", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (6 <= hue_value <= 14) and (60 <= sat_value <= 80) and (52 <= val_value <= 72):
        color = "Terra Cotta"
        s = gTTS(text="Terra Cotta", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (54 <= hue_value <= 62) and (90 <= sat_value <= 110) and (67 <= val_value <= 57):
        color = "Titanium Yellow"
        s = gTTS(text="Titaniium Yellow", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (159 <= hue_value <= 168) and (90 <= sat_value <= 110) and (13 <= val_value <= 33):
        color = "Tropical Rain Forest"
        s = gTTS(text="Tropical Rain Forest", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (169 <= hue_value <= 179) and (56 <= sat_value <= 76) and (41 <= val_value <= 61):
        color = "Turquoise"
        s = gTTS(text="Turquoise", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (240 <= hue_value <= 248) and (77 <= sat_value <= 97) and (20 <= val_value <= 40):
        color = "Ultamarine"
        s = gTTS(text="Ultamarine", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (212 <= hue_value <= 220) and (63 <= sat_value <= 83) and (53 <= val_value <= 73):
        color = "United Nations Blue"
        s = gTTS(text="United Nations Blue", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (44 <= hue_value <= 52) and (65 <= sat_value <= 85) and (71 <= val_value <= 91):
        color = "Vanilla"
        s = gTTS(text="Vanilla", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (270 <= hue_value <= 278) and (90 <= sat_value <= 110) and (40 <= val_value <= 60):
        color = "Violet"
        s = gTTS(text="Violet", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (35 <= hue_value <= 43) and (67 <= sat_value <= 87) and (73 <= val_value <= 93):
        color = "Wheat"
        s = gTTS(text="Wheat", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (hue_value <= 5) and (0 <= sat_value <= 10) and (90 <= val_value <= 110):
        color = "White"
        s = gTTS(text="White", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (hue_value <= 5) and (0 <= sat_value <= 10) and (86 <= val_value <= 106):
        color = "White Smoke"
        s = gTTS(text="White Smoke", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (132 <= hue_value <= 140) and (0 <= sat_value <= 18) and (39 <= val_value <= 59):
        color = "Xanadu"
        s = gTTS(text="Xanadu", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (208 <= hue_value <= 216) and (71 <= sat_value <= 91) and (22 <= val_value <= 42):
        color = "Yale Blue"
        s = gTTS(text="Yale Blue", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    elif (56 <= hue_value <= 64) and (90 <= sat_value <= 110) and (40 <= val_value <= 60):
        color = "Yellow"
        s = gTTS(text="Yellow", lang='en')
        tsname = "name.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)
    else:
        color = "Undefined"

    pixel_center_bgr = frame[cy, cx]
    cv2.putText(frame, color, (10, 50), 0, 1, (255, 0, 0), 2)
    cv2.circle(frame, (cx, cy), 5, (255, 0, 0), 3)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
