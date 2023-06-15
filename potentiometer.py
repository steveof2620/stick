
import time
import board
import neopixel
from analogio import AnalogIn
from adafruit_simplemath import map_range

# potentiometer reads from 0 to 65535
# potentiometer connected to A1, power (3.3v) & ground
potentiometer = AnalogIn(board.A1)

POT_MAX_VALUE = 65535
NUM_OF_PIXELS = 10
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

#set auto_write to false for mapped_value
pixels = neopixel.NeoPixel(
    board.NEOPIXEL, NUM_OF_PIXELS, brightness=0.5, auto_write=False
)

# Testing the mapped_value 
def show_value(val):            # Show value 0-9 on CPX NeoPixels
    for i in range(val):
        pixels[i] = BLUE
    for i in range(val, NUM_OF_PIXELS):
        pixels[i] = BLACK
    pixels.show()

while True:
    pixels_to_light = int(potentiometer.value / (POT_MAX_VALUE / NUM_OF_PIXELS))
    mapped_value = int(map_range(potentiometer.value, 0, POT_MAX_VALUE, 0, NUM_OF_PIXELS +1))
    show_value(mapped_value)
    
    print((potentiometer.value,))
    print(pixels_to_light)
    print(mapped_value)

'''
    for i in range(0, NUM_OF_PIXELS):
        if i <= pixels_to_light:
            pixels[i] = BLUE
        else:
            pixels[i] = BLACK
'''
    # time.sleep(0.25)

