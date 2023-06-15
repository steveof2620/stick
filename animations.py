# Animations. See https://learn.adafruit.com/circuitpython-led-animations

import board
import neopixel
import time
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

strip_pin = board.A6
strip_num_of_lights = 35

pixel_strip = neopixel.NeoPixel(strip_pin, strip_num_of_lights, brightness=0.5, auto_write=True)

colorcycle = ColorCycle(pixel_strip, 0.5, colors=colours)
chase = Chase(pixel_strip, speed=0.1, color=MAGENTA, size=3, spacing=6)
comet = Comet(pixel_strip, speed=0.01, color=PURPLE, tail_length=10, bounce=True)
rainbow = Rainbow(pixel_strip, speed=0.1, period=2)
rainbowchase = RainbowChase(pixel_strip, speed=0.1, size=5, spacing=3)
rainbow_comet = RainbowComet(pixel_strip, speed=0.03, bounce=True)
rainbow_sparkle = RainbowSparkle(pixel_strip, speed=0.1)
sparkle = Sparkle(pixel_strip, speed=0.05, color=AMBER)
sparkle_pulse = SparklePulse(pixel_strip, speed=0.05, period=3, color=JADE)

animations = AnimationSequence(colorcycle, chase, comet, advance_interval=5, auto_clear=True, random_order=True)

while True:
    sparkle_pulse.animate()
    # sparkle.animate()
    # rainbow_sparkle.animate()
    # rainbow_comet.animate()
    # rainbowchase.animate()
    # rainbow.animate()
    # colorcycle.animate()
    # chase.animate()
    # comet.animate()
    # animations.animate()