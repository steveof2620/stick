# See Better Buttons with Debouncing:
# https://www.youtube.com/watch?v=RJamQZMya0ghttps://www.youtube.com/watch?v=RJamQZMya0g

import board
import neopixel
import digitalio
from adafruit_debouncer import Button

# libaries for animations
from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.animation.rainbowcomet import RainbowComet
from adafruit_led_animation.animation.rainbowsparkle import RainbowSparkle
from adafruit_led_animation.animation.sparkle import Sparkle
from adafruit_led_animation.animation.SparklePulse import SparklePulse
from adafruit_led_animation.sequence import AnimationSequence

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
    RAINBOW,
)

INDIGO = (63, 0, 255)
VIOLET = (127, 0, 255)
colours = [
    RED,
    MAGENTA,
    ORANGE,
    YELLOW,
    GREEN,
    JADE,
    BLUE,
    INDIGO,
    VIOLET,
    PURPLE,
]

button_A_input = digitalio.DigitalInOut(board.BUTTON_A)
button_A_input.switch_to_input(digitalio.Pull.DOWN)
button_A = Button(button_A_input, value_when_pressed=True)

button_B_input = digitalio.DigitalInOut(board.BUTTON_B)
button_B_input.switch_to_input(digitalio.Pull.DOWN)
button_B = Button(button_B_input, value_when_pressed=True)

strip_pin = board.A6
strip_num_of_lights = 35

# for the stick leds
pixel_strip = neopixel.NeoPixel(
    strip_pin, strip_num_of_lights, brightness=0.5, auto_write=True
)

#for the menu buttons
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

# for option one
colorcycle = ColorCycle(pixel_strip, speed=0.5, colors=colours)
# for option two
chase = Chase(pixel_strip, speed=0.05, color=MAGENTA)
# for option three
comet = Comet(pixel_strip, speed=0.01, color=PURPLE, tail_length=10, bounce=True)
# for option four
rainbow = Rainbow(pixel_strip, speed=0.1, period=2)
# for option five
rainbowchase = RainbowChase(pixel_strip, speed=0.05, size=5, spacing=3)
# for opton six
rainbow_comet = RainbowComet(pixel_strip, speed=0.02, bounce=True)
# for opton seven
rainbow_sparkle = RainbowSparkle(pixel_strip, speed=0.1)
# for option eight
sparkle = Sparkle(pixel_strip, speed=0.05, color=CYAN)
# for option nine
sparkle_pulse = SparklePulse(pixel_strip, speed=0.05, period=3, color=BLUE)
# for option ten
animations = AnimationSequence(
    colorcycle,
    chase,
    comet,
    rainbow,
    rainbowchase,
    rainbow_comet,
    rainbow_sparkle,
    sparkle,
    sparkle_pulse,
    advance_interval=5,
    auto_clear=True,
    random_order=True,
)

lit_pixels = 1
pixels[0] = BLUE

def select_option(option_selected):
    if option_selected == 1:
        return 1
    elif option_selected == 2:
        return 2
    elif option_selected == 3:
        return 3
    elif option_selected == 4:
        return 4
    elif option_selected == 5:
        return 5
    elif option_selected == 6:
        return 6
    elif option_selected == 7:
        return 7
    elif option_selected == 8:
        return 8
    elif option_selected == 9:
        return 9
    elif option_selected == 10:
        return 10


selected_option = select_option(lit_pixels)

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
        selected_option = select_option(lit_pixels)
    elif button_B.pressed:
        if lit_pixels > 1:
            pixels[lit_pixels - 1] = BLACK
            lit_pixels = lit_pixels - 1
        selected_option = select_option(lit_pixels)

    if selected_option == 1:
        colorcycle.animate()
    elif selected_option == 2:
        chase.animate()
    elif selected_option == 3:
        comet.animate()
    elif selected_option == 4:
        rainbow.animate()
    elif selected_option == 5:
        rainbowchase.animate()
    elif selected_option == 6:
        rainbow_comet.animate()
    elif selected_option == 7:
        rainbow_sparkle.animate()
    elif selected_option == 8:
        sparkle.animate()
    elif selected_option == 9:
        sparkle_pulse.animate()
    elif selected_option == 10:
        animations.animate()
