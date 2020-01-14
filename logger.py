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

LOG_FILE = 'sys_log'

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

while True:
    try:
        data = open(LOG_FILE, 'r').readlines()[-2:]
    except:
        print(f'[ERROR] can\'t find {LOG_FILE}')
        sys.exit(1)
   
    if len(data) < 2:
        print('[ERROR] unable to process log (needs to have >= 2 lines)')
        sys.exit(1)

    data = list(map(lambda s: s[:-1]+' ', data))
    str_len = max(map(len,data))
    data = list(map(lambda s: s.ljust(str_len,' '), data))

    draw.rectangle((0,0,width-2,height-2), outline=2, fill=0)
    draw.text((5, 7), "recent logs:", font=font, fill=255)
    disp.image(image)
    disp.show()
    sleep(2)
    
    i = 0
    while i < str_len:
        
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        
        for j in range(0,13):
            draw.text((j*10,0), data[0][j], font=font, fill=255)
            draw.text((j*10,16), data[1][j], font=font, fill=255)
        
        i += 1
        data = list(map(lambda s: s[1:] + s[0], data))

        disp.image(image)
        disp.show()

        sleep(.2)

    sleep(.7)
