from ws2812b import WS2812B
from time import sleep

NUM_LEDS = 30
pixels = WS2812B(num_leds=NUM_LEDS, pin=27, delay=0)

pixels.fill(10, 10, 10)
pixels.show()

while True:
    for i in range(NUM_LEDS):
        for j in range(NUM_LEDS):
            pixels.set_pixel(j, abs(i + j) % 10, abs(i - (j + 3)) % 10, abs(i - (j + 6)) % 10)
        pixels.show()
        sleep(0.05)
