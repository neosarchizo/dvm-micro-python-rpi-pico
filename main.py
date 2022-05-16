from machine import SoftI2C, Pin
from ssd1306 import SSD1306_I2C
from time import sleep

i2c = SoftI2C(scl=Pin(10), sda=Pin(11))
display = SSD1306_I2C(128, 64, i2c, addr=0x3C)

pirSensor = Pin(27, Pin.IN, Pin.PULL_UP)

display.fill(0)
display.text("DeviceMart", 0, 0)
display.text("PIR", 0, 15)
display.show()

def on_rising(ps):
    for _ in range(5):
        display.fill(0)
        display.text("DeviceMart", 0, 0)
        display.text("PIR", 0, 15)
        display.text("Someone here!!!", 0, 40)
        display.show()
        sleep(0.5)

        display.fill(0)
        display.text("DeviceMart", 0, 0)
        display.text("PIR", 0, 15)
        display.show()
        sleep(0.5)

pirSensor.irq(on_rising, Pin.IRQ_RISING)