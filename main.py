from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C
from onewire import OneWire
from ds18x20 import DS18X20
from time import sleep

i2c = SoftI2C(scl = Pin(10), sda = Pin(11))
display = SSD1306_I2C(128, 64, i2c, addr = 0x3C)

ds = DS18X20(OneWire(Pin(16)))
rom = ds.scan()

while True:
    ds.convert_temp()
    temp = ds.read_temp(rom[0])

    display.fill(0)
    display.text('DeviceMart', 0, 0)
    display.text('Temperature', 0, 20)
    display.text(str('%.2f' % temp) + ' C', 0, 40)
    display.show()

    sleep(1)