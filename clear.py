#!/usr/bin/python3

from board import SCL, SDA
import busio

import adafruit_ssd1306

i2c = busio.I2C(SCL, SDA)

disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Clear display.
disp.fill(0)
disp.show()
