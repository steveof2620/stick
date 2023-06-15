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

def select_option(option_selected):
    if option_selected == 1:
        print(f"lit pixels is {option_selected} - option one selected")
    elif option_selected == 2:
        print (f"lit pixels is {option_selected} - option two selected")
    elif option_selected == 3:
        print (f"lit pixels is {option_selected} - option three selected")
    elif option_selected == 4:
        print (f"lit pixels is {option_selected} - option four selected")
    elif option_selected == 5:
        print (f"lit pixels is {option_selected} - option five selected")
    elif option_selected == 6:
        print (f"lit pixels is {option_selected} - option six selected")
    elif option_selected == 7:
        print (f"lit pixels is {option_selected} - option seven selected")
    elif option_selected == 8:
        print (f"lit pixels is {option_selected} - option eight selected")
    elif option_selected == 9:
        print (f"lit pixels is {option_selected} - option nine selected")
    elif option_selected == 10:
        print (f"lit pixels is {option_selected} - option ten selected")

select_option(lit_pixels)

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
        select_option(lit_pixels)
    elif button_B.pressed:
        if lit_pixels > 1:
            pixels[lit_pixels - 1] = (BLACK)
            lit_pixels = lit_pixels - 1
        select_option(lit_pixels)

