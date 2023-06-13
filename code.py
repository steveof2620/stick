# Write your code here :-)
# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time
import board
import neopixel
from analogio import AnalogIn
from adafruit_simplemath import map_range

NUMPIXELS = 10  # Circuit Playground Express has 10 pixels
pixels = neopixel.NeoPixel(board.NEOPIXEL, NUMPIXELS, auto_write=False)  # CPX NeoPixels
potentiometer = AnalogIn(board.A1)  # potentiometer connected to A1, power & ground

def show_value(val):            # Show value 0-9 on CPX NeoPixels
    for i in range(val):
        pixels[i] = (50, 0, 0)  # Red
    for i in range(val, NUMPIXELS):
        pixels[i] = (0, 0, 0)
    pixels.show()

while True:
    remapped_value = int(map_range(potentiometer.value, 0, 65520, 0, 100))
    show_value(int(potentiometer.value / 65520 * NUMPIXELS))  # Show on NeoPixels
    print((potentiometer.value,))# Print value
    print ((remapped_value,))

    time.sleep(0.25)                   # Wait a bit before checking all again


