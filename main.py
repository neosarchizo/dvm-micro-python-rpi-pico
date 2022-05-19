from hcsr04 import HCSR04
from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C
from time import sleep

i2c = SoftI2C(scl=Pin(10), sda=Pin(11))
display = SSD1306_I2C(128, 64, i2c, addr=0x3C)

sonar = HCSR04(Pin(4, Pin.OUT), Pin(5, Pin.IN))

while True:
    distance = sonar.getDistance()

    display.fill(0)
    display.text('DeviceMart', 0, 0)
    display.text('Distance', 0, 15)
    display.text(str(distance) + ' cm', 0, 35)
    display.show()

    print(str(distance) + ' cm')
    sleep(0.5)