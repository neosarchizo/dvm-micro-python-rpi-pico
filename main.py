from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C
from dht import DHT11
from time import sleep

i2c = SoftI2C(scl=Pin(10), sda=Pin(11))
display = SSD1306_I2C(128, 64, i2c, addr=0x3C)

sleep(1)

dht = DHT11(Pin(17))

while True:
    dht.measure()

    temperature = dht.temperature()
    humidity = dht.humidity()

    display.fill(0)
    display.text('DeviceMart', 0, 0)
    display.text('DHT11', 0, 15)
    display.text(str(temperature) + ' C', 0, 40)
    display.text(str(humidity) + ' %', 55, 40)
    display.show()

    print(str(temperature) + ' C')
    print(str(humidity) + ' %')

    sleep(2)