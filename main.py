from machine import Pin
from time import sleep

led1 = Pin(18, Pin.OUT)
led2 = Pin(19, Pin.OUT)
led3 = Pin(20, Pin.OUT)

leds = [led1, led2, led3]

while True:
    for led in leds:
        led.high()
        sleep(0.1)
        led.low()