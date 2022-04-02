import machine
import time
from machine import Pin
from time import sleep

led_pin=Pin(2,Pin.OUT)

while True:
    led_pin.value(1)
    sleep(1)
    led_pin.value(0)
    sleep(1)