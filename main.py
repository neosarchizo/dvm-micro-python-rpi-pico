from ws2812b import WS2812B
from time import sleep

NUM_LEDS = 30
pixels = WS2812B(NUM_LEDS, 27)

RED = (255, 0, 0) #ff0000
ORANGE = (255, 165, 0) #ffa500
YELLOW = (255, 150, 0) #ff9500
GREEN = (0, 255, 0) #00ff00
BLUE = (0, 0, 255) #0000ff
INDIGO = (75, 0, 130) #4c0082
VIOLET = (138, 43, 226) #8a2be2

COLORS = [
    RED,
    ORANGE,
    YELLOW,
    GREEN,
    BLUE,
    INDIGO,
    VIOLET,
]

while True:
    for color in COLORS:
        for i in range(NUM_LEDS):
            pixels.set_pixel(i, color[0], color[1], color[2])
            sleep(0.01)
            pixels.show()
