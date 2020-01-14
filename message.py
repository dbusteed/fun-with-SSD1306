#!/usr/bin/python3

# see README.md for info

from time import sleep
import sys

from board import SCL, SDA
import busio

import adafruit_ssd1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

if len(sys.argv) < 2:
    print('[ERROR] no parameter given. try again with `./custom.py "hello there!"`')
    sys.exit(1)

i2c = busio.I2C(SCL, SDA)

disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

disp.fill(0)
disp.show()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)

draw.rectangle((0,0,width,height), outline=0, fill=0)

font = ImageFont.truetype("mono.ttf", 32)

msg = sys.argv[1]

if len(msg) > 6:
    i = 0
    msg += '     '
    while i < len(msg)-4:
        
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        
        for j in range(0,5):
            draw.text((j*25, 0), msg[j], font=font, fill=255) 
        
        i += 1

        msg = msg[1:] + msg[0]
        
        disp.image(image)
        disp.show()

        sleep(.6)

else:    
    draw.text((0,0), msg, font=font, fill=255)

    disp.image(image)
    disp.show()

    sleep(1)

    draw.rectangle((0,0,width,height), outline=0, fill=0)
    disp.image(image)
    disp.show()
