# First test for the on board LEDs

# Conventions
# constants, ALL_CAPS
# Class names, UpperCamelCase
# Vairable, lower case

import board
import neopixel
import time
from analogio import AnalogIn
from adafruit_simplemath import map_range
from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation.color import (
    RED,
    YELLOW,
    ORANGE,
    GREEN,
    TEAL,
    CYAN,
    BLUE,
    PURPLE,
    MAGENTA,
    WHITE,
    BLACK,
    GOLD,
    PINK,
    AQUA,
    JADE,
    AMBER,
    OLD_LACE,
)

# on board LEDs
# pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

# LED strip is connected to pin A7 so the potentiometer is on pin A3
# Number of LEDs on strip is 35
strip_pin = board.A7
strip_num_of_lights = 35
strip = neopixel.NeoPixel(
    strip_pin, strip_num_of_lights, brightness=0.5, auto_write=True
)

potentiometer = AnalogIn(board.A3)

# an array of colours
colours = [
    RED,
    YELLOW,
    ORANGE,
    GREEN,
    TEAL,
    CYAN,
    BLUE,
    PURPLE,
    MAGENTA,
    WHITE,
    BLACK,
    GOLD,
    PINK,
    AQUA,
    JADE,
    AMBER,
    OLD_LACE,
]

blink = Blink(strip, speed=0.5, color=OLD_LACE)
colorcycle = ColorCycle(strip, 0.5, colors=colours)

# infinite loop
while True:
    # blink.animate()
    colorcycle.animate()
    pot_value = round(map_range(potentiometer.value, 100, 65535, 0, 1), 1)
    # rounded = round(remapped_pot_value, 1)
    print(
        "Raw: ",
        potentiometer.value,
        "Rounded: ",
        pot_value,
    )
    time.sleep(0.25)
# Write your code here :-)
