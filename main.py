from machine import SoftI2C, Pin
from ssd1306 import SSD1306_I2C

i2c = SoftI2C(scl=Pin(10), sda=Pin(11))
display = SSD1306_I2C(128, 64, i2c, addr=0x3C)

display.fill(0)
display.show()

display.pixel(5, 5, 1)

display.hline(5, 10, 20, 1)

display.rect(5, 15, 20, 10, 1)

display.text("DeviceMart", 5, 40)

display.show()