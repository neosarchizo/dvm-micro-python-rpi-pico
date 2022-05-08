from machine import Pin
from time import sleep

led = Pin(25, Pin.OUT)
key = Pin(14, Pin.IN, Pin.PULL_UP)

state = 0

def on_falling(k):
    global state
    sleep(0.01)

    if not k.value(): # pressed, 0, LOW
        state = not state
        led.value(state)

key.irq(on_falling, Pin.IRQ_FALLING)