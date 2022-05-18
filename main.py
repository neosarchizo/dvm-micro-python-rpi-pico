from machine import Pin, SoftI2C, ADC
from ssd1306 import SSD1306_I2C
from time import sleep

i2c = SoftI2C(scl=Pin(10), sda=Pin(11))
display = SSD1306_I2C(128, 64, i2c, addr=0x3C)

soil = ADC(1)

while True:
    display.fill(0)
    display.text('DeviceMart', 0, 0)
    display.text('Soil', 0, 15)

    value = soil.read_u16() # 2 ^ 16, 65535

    display.text(str(value) + ' / 65535', 0, 40) # 2 ^ 16
    display.text(str(round(value * 3.3 / 65535, 2)) + ' V', 0, 55)

    if value <= 19952:
        display.text('Dry', 60, 55)
    elif value <= 35808:
        display.text('Normal', 60, 55)
    else:
        display.text('Wet', 60, 55)
    
    display.show()
    sleep(1)