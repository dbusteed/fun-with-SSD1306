#!/usr/bin/python3

# see README.md for info

from pynput import keyboard
from random import randint
from time import sleep
import sys

from board import SCL, SDA
import busio

import adafruit_ssd1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

i2c = busio.I2C(SCL, SDA)

disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

disp.fill(0)
disp.show()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)

draw.rectangle((0,0,width,height), outline=0, fill=0)

font = ImageFont.truetype("mono.ttf", 16)

# make the course
course = "________"
while len(course) < 500:
    course += "^^" if randint(1,4) == 1 else "^"
    course += randint(3,7)*"_"

jump = 0 
score = 0
lives = 3
lives_symbol = 'ooo'

def on_press(key):
    global jump
    jump = 2 
    sleep(.5)

listener = keyboard.Listener(on_press=on_press)
listener.start()

print('press any key to jump!\n\n')

while True:
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    x = 0
    for i in range(0,13):
        if x == 1:
            if jump:
                draw.text((10,0), "@", font=font, fill=255)
                draw.text((10,16), course[i], font=font, fill=255)
                jump -= 1
            else:
                if course[i] is not '_':
                    lives -= 1

                    lives_symbol = ((3-lives)*'x') + (lives*'o')

                else:
                    draw.text((10,16), "@", font=font, fill=255)
        else:
            draw.text((x*10, 16), course[i], font=font, fill=255)
        x += 1
    
    score += 1
    draw.text((60, 0), str(score//3), font=font, fill=255) 
    draw.text((100,0), lives_symbol, font=font, fill=255)

    course = course[1:] + course[0]
    
    disp.image(image)
    disp.show()

    sleep(.04)
    
    if lives == 0:
        break

draw.rectangle((0,0,width,height), outline=0, fill=0)

draw.text((0,0), "GAME OVER!", font=font, fill=255)
draw.text((0,16), "SCORE: "+str(score//3), font=font, fill=255)

disp.image(image)
disp.show()
