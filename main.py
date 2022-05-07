from machine import Pin

led = Pin(25, Pin.OUT)
key = Pin(14, Pin.IN, Pin.PULL_UP)

while True:
    if not key.value(): # pressed, 0, LOW
        led.high()
    else: # released, 1, HIGH
        led.low()