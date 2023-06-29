# First test for the on board LEDs

# Conventions
# constants, ALL_CAPS
# Class names, UpperCamelCase
# Vairable, lower case

import board
import neopixel
import time

# pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

# LED strip is connected to pin A7 so the potentiometer is on pin A3
strip_pin = board.A7
strip_num_of_lights = 5
strip = neopixel.NeoPixel(strip_pin, strip_num_of_lights, brightness = 0.5, auto_write=True)

# colour codes RGB
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
OFF = (0, 0, 0)

# an array of colours
colours = [RED, YELLOW, GREEN, CYAN, BLUE, PURPLE]

# infinite loop
while True:
    for i in range(len(strip)):
        strip[i] = colours[i]
        time.sleep(0.3)
    strip.fill(OFF)

