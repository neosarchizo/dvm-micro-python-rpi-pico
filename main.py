from machine import Pin, PWM
from time import sleep

servo1 = PWM(Pin(0))
servo1.freq(50)

def setAngle(angle):
    global servo1
    a = int(((((angle + 90) * 2) / 180) + 0.5) / 20 * 65535)
    servo1.duty_u16(a)

while True:
    setAngle(-90)
    sleep(1)

    setAngle(-45)
    sleep(1)

    setAngle(0)
    sleep(1)

    setAngle(45)
    sleep(1)

    setAngle(90)
    sleep(1)