from machine import Pin
from time import sleep

led = Pin(25, Pin.OUT)

while True:
    led.high()
    print('ON!')
    sleep(1)
    led.low()
    print('OFF!')
    sleep(1)