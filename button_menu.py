# See Better Buttons with Debouncing:
# https://www.youtube.com/watch?v=RJamQZMya0ghttps://www.youtube.com/watch?v=RJamQZMya0g

import board
import neopixel
import digitalio
from adafruit_debouncer import Button


button_A_input = digitalio.DigitalInOut(board.BUTTON_A)
button_A_input.switch_to_input(digitalio.Pull.DOWN)
button_A = Button(button_A_input, value_when_pressed = True)

button_B_input = digitalio.DigitalInOut(board.BUTTON_B)
button_B_input.switch_to_input(digitalio.Pull.DOWN)
button_B = Button(button_B_input, value_when_pressed = True)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

lit_pixels = 1
pixels[0] = BLUE

while True:
    # ensure the buttons are updated before checking the state.
    button_A.update()
    button_B.update()
    if button_A.pressed:
        if lit_pixels < 10:
            pixels[lit_pixels] = BLUE
            lit_pixels += 1
        else:
            pixels.fill(BLACK)
            lit_pixels = 1
            pixels[lit_pixels - 1] = BLUE
    elif button_B.pressed:
        if lit_pixels > 1:
            pixels[lit_pixels - 1] = (BLACK)
            lit_pixels = lit_pixels - 1

    # which option has been pressed
    if lit_pixels == 1:
        print(f"lit pixels is {lit_pixels} - option one selected")
    elif lit_pixels == 2:
        print (f"lit pixels is {lit_pixels} - option two selected")
    elif lit_pixels == 3:
        print (f"lit pixels is {lit_pixels} - option three selected")
    elif lit_pixels == 4:
        print (f"lit pixels is {lit_pixels} - option four selected")
    elif lit_pixels == 5:
        print (f"lit pixels is {lit_pixels} - option five selected")
    elif lit_pixels == 6:
        print (f"lit pixels is {lit_pixels} - option six selected")
    elif lit_pixels == 7:
        print (f"lit pixels is {lit_pixels} - option seven selected")
    elif lit_pixels == 8:
        print (f"lit pixels is {lit_pixels} - option eight selected")
    elif lit_pixels == 9:
        print (f"lit pixels is {lit_pixels} - option nine selected")
    elif lit_pixels == 10:
        print (f"lit pixels is {lit_pixels} - option ten selected")
