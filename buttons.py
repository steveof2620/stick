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

press_count_A = 0
press_count_B = 0

while True:
    # ensure the buttons are updated before checking the state.
    button_A.update()
    button_B.update()

    if button_A.pressed:
        press_count_A += 1
        # print with 'f' statement to allow for parsing of values within {}
        print(f"Button A press {press_count_A} times")
        pixels.fill(RED)
    elif button_A.released:
        pixels.fill(BLACK)
    elif button_B.pressed:
        press_count_B += 1
        print(f"Button B press {press_count_B} times")
        pixels.fill(BLUE)
    elif button_B.released:
        pixels.fill(BLACK)
