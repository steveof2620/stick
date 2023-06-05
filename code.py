# First test for the on board LEDs

# Conventions
# constants, ALL_CAPS
# Class names, UpperCamelCase
# Vairable, lower case

import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

# colour codes RGB
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
OFF = (0, 0, 0)

pixels.fill((OFF))

# infinite loop
while True:
    pass
