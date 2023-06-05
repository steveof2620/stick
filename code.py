# First test for the on board LEDs

# Conventions
# constants, ALL_CAPS
# Class names, UpperCamelCase
# Vairable, lower case

import board
import neopixel
import time
from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.color import RED, YELLOW, ORANGE, GREEN, TEAL, CYAN, BLUE, PURPLE, MAGENTA, WHITE, BLACK, GOLD, PINK, AQUA, JADE, AMBER, OLD_LACE

# on board LEDs
# pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

# LED strip is connected to pin A7 so the potentiometer is on pin A3
strip_pin = board.A7
strip_num_of_lights = 30
strip = neopixel.NeoPixel(strip_pin, strip_num_of_lights, brightness=0.5, auto_write=True)

blink = Blink(strip, speed=0.5, color=JADE)

# an array of colours
colours = [RED, YELLOW, ORANGE, GREEN, TEAL, CYAN, BLUE, PURPLE, MAGENTA, WHITE, BLACK, GOLD, PINK, AQUA, JADE, AMBER, OLD_LACE]

# infinite loop
while True:
    animations.animate()

