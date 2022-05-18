from machine import Pin, SoftI2C, ADC
from ssd1306 import SSD1306_I2C
from time import sleep

i2c = SoftI2C(scl=Pin(10), sda=Pin(11))
display = SSD1306_I2C(128, 64, i2c, addr=0x3C)

waterLevel = ADC(1)

while True:
    display.fill(0)
    display.text('DeviceMart', 0, 0)
    display.text('Water Level', 0, 15)

    value = waterLevel.read_u16() # 2 ^ 16, 65535

    display.text(str(value) + ' / 65535', 0, 40) # 2 ^ 16
    display.text(str(round(value * 3.3 / 65535, 2)) + ' V', 0, 55)

    if value <= 12500:
        display.text('0 cm', 60, 55)
    elif value <= 25000:
        display.text('1 cm', 60, 55)
    elif value <= 26000:
        display.text('2 cm', 60, 55)
    elif value <= 29000:
        display.text('3 cm', 60, 55)
    else:
        display.text('4 cm', 60, 55)
    
    display.show()
    sleep(1)