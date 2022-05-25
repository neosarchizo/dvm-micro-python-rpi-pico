import lcd_gfx
from machine import SPI
from st7735 import ST7735
from time import sleep
from bmp import BMP

spi = SPI(1, baudrate=8000000, polarity=0, phase=0)
display = ST7735(spi, rst=13, ce=9, dc=12)
display.reset()
display.begin()

while True:
    display._bground = 0xffff
    display.fill_screen(display._bground)
    display.pixel(5, 5, display.rgb_to_565(0, 255, 0))
    lcd_gfx.drawLine(5, 10, 80, 10, display, display.rgb_to_565(0, 0, 255))
    lcd_gfx.drawRect(5, 20, 80, 40, display, display.rgb_to_565(255, 255, 0))
    lcd_gfx.drawCircle(40, 90, 20, display, display.rgb_to_565(0, 255, 255))
    display.p_string(10, 130, "Hello DeviceMart!", display.rgb_to_565(255, 0, 0))
    sleep(3)

    BMP('logo.bmp', display, 0, 0, 1)
    sleep(3)