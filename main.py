from ws2812b import WS2812B
from time import sleep

pixels = WS2812B(30, 27) # pixel count, pin number Y11

while True:
    pixels.fill(255, 0, 0)
    pixels.show()
    sleep(1)
    
    pixels.fill(0, 255, 0)
    pixels.show()
    sleep(1)

    pixels.fill(0, 0, 255)
    pixels.show()
    sleep(1)
