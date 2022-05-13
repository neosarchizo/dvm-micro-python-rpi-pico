from machine import UART

uart = UART(1, 115200)

uart.write('Hello DeviceMart!') # TX : Y9, RX : Y10

while True:
    if uart.any():
        text = uart.read(128)
        print(text)