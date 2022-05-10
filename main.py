from machine import Pin, PWM
from time import sleep

buzzer = PWM(Pin(22))
buzzer.duty_u16(32768) # 2 ^ 16, 50%

buzzer.freq(200)
sleep(1)

buzzer.freq(400)
sleep(1)

buzzer.freq(600)
sleep(1)

buzzer.freq(800)
sleep(1)

buzzer.freq(1000)
sleep(1)

buzzer.deinit()
