from machine import Pin, SoftI2C, ADC
from ssd1306 import SSD1306_I2C
from time import sleep

i2c = SoftI2C(scl=Pin(10), sda=Pin(11))
display = SSD1306_I2C(128, 64, i2c, addr=0x3C)

adc = ADC(0) # GP26

while True:
    value = adc.read_u16() # 2 ^ 16, 0 ~ 65535

    display.fill(0)
    display.text('DeviceMart', 0, 0)
    display.text('ADC', 0, 15)

    display.text(str(value), 0, 40)
    display.text('/ 65535', 40, 40)

    display.text(str('%.2f' % ((value / 65535) * 3.3)), 0, 55)
    display.text('V', 40, 55)

    display.show()
    sleep(0.3)