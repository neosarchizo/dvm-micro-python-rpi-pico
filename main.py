from ws2812b import WS2812B
from time import sleep
from random import randint

NUM_LEDS = 30
MIN_LEN = 5
MAX_LEN = 20
NUM_FLASHES = 10

pixels = WS2812B(NUM_LEDS, 27)

COLORS = [
    [232, 100, 255],
    [200, 200, 20],
    [30, 200, 200],
    [150, 50, 10],
    [50, 200, 10],
]

flashing = []

for i in range(NUM_FLASHES):
    pos = randint(0, NUM_LEDS - 1) # 0 ~ 29
    idxColor = randint(0, len(COLORS) - 1) # 0 ~ 4
    flashLength = randint(MIN_LEN, MAX_LEN) # 5 ~ 20
    flashing.append([pos, COLORS[idxColor], flashLength, 0, 1]) # pixel position, color, flash length, current index of flash length, step direction

pixels.fill(0, 0, 0)

while True:
    pixels.show()

    for i in range(NUM_FLASHES):
        p = flashing[i][0] # pixel position
        brightness = (flashing[i][3] / flashing[i][2]) # current index of flash length / flash length
        color = (
            int(flashing[i][1][0] * brightness),
            int(flashing[i][1][1] * brightness),
            int(flashing[i][1][2] * brightness)
        )
        pixels.set_pixel(p, color[0], color[1], color[2])

        if flashing[i][2] == flashing[i][3]: # maximum brightness ??
            flashing[i][4] = -1 # step direction

        if flashing[i][3] == 0 and flashing[i][4] == -1: # end
            pos = randint(0, NUM_LEDS - 1) # 0 ~ 29
            idxColor = randint(0, len(COLORS) - 1) # 0 ~ 4
            flashLength = randint(MIN_LEN, MAX_LEN) # 5 ~ 20
            flashing[i] = [pos, COLORS[idxColor], flashLength, 0, 1] # update

        flashing[i][3] = flashing[i][3] + flashing[i][4]
        sleep(0.005)