#dotstar
import time
import random
import board
import adafruit_dotstar as dotstar
from adafruit_circuitplayground.express import cpx

data_pin = board.A7
clock_pin = board.A3
num_pixels = 40

# the pixel where the snake will begin from
snake_start = 0
# the pixel where the snake will end it's travel
snake_finish = 39
# the length of the snake
snake_length = 5
# sleep time (speed of snake)
sleep_time = 0

# colour code RGB
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
OFF = (0, 0, 0)

# Dotstar (clock, data, number of pixesl, brightness)
dots = dotstar.DotStar(clock_pin, data_pin, num_pixels, brightness=0.5, auto_write=False)

def reset_strip():
    dots.fill(OFF)
    dots.show()

def movement_colour():
    x, y, z = cpx.acceleration
    # colour_code = (0, 0, 0)
    R = 0
    G = 0
    B = 0

    colour_code = (R, G, B)

    if x:
        R = R + abs(int(x))
    if y:
        G = G + abs(int(y))
    if z:
        B = B + abs(int(z))

    colour_code = (R, G, B)

    return colour_code

def random_colour():
#    red_code = random.randint(0,255)
#    green_code = random.randint(0,255)
#    colour_code = (red_code, green_code, blue_code)

    #an arry of colours to randomly pick from
    colour_array = ["RED", "YELLOW", "GREEN", "BLUE", "PURPLE"]

    # randomly pick a value from the array using the randint function,
    # picks an element from zero (first item, to the last item (lengeth
    # of the array minus one to account for leading zero))
    colour_picked = colour_array[random.randint(0,len(colour_array)-1)]

    # set a colour value as something, just in case
    colour_code = (0, 0, 0)

    # assessing the colour code by the colour randomly chosen
    if colour_picked == "RED":
        colour_code = RED
    if colour_picked == "YELLOW":
        colour_code = YELLOW
    if colour_picked == "GREEN":
        colour_code = GREEN
    if colour_picked == "BLUE":
        colour_code = BLUE
    if colour_picked == "PURPLE":
        colour_code = PURPLE

    # now return the value
    return colour_code


def snake(colour, snake_start, snake_finish, snake_length, sleep_time):
    path_length = snake_finish - snake_start
    # off = (0, 0, 0)

    i=0
    while i < path_length:
        j=0
        while j < snake_length:
            active_dot = i+j+snake_start
            if active_dot <= snake_finish:
                dots[active_dot] = colour
                # dots[active_dot] = movement_colour()
                # dots.brightness = 1.0
                dots.brightness = random.randint(5,10)/10
            j+=1

        dots.show()

        if i+snake_start <= snake_finish-snake_length:
            dots[i+snake_start] = OFF

        time.sleep(sleep_time)

        i+=1

    # go backwards
    i=0
    while i*-1 < path_length:
        j=0
        while j*-1 < snake_length:
            active_dot = i+j+snake_finish
            if active_dot >= snake_start:
                dots[active_dot] = colour
                # dots[active_dot] = movement_colour()
                # dots.brightness = 1.0
                # pixels.brightness = random.randint(5,10)/10
            j-=1

        if i+snake_finish >= snake_length+snake_start:
            dots[i+snake_finish] = OFF

        time.sleep(sleep_time)
        dots.show()
        i-=1

reset_strip()

# MAIN LOOP
while True:
    # reset_strip()
    snake(RED, snake_start, snake_finish, snake_length, sleep_time)
