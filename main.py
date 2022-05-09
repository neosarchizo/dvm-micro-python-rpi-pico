from machine import Pin, Timer

led = Pin(25, Pin.OUT)

def timeout(t):
    led.toggle()

timer = Timer()
timer.init(
    period = 1000, # ms
    mode = Timer.PERIODIC, # ONE_SHOT
    callback = timeout
)