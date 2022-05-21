from machine import Pin, I2C
import ssd1306
from time import sleep

class OLED:
    def display(Message1,Message2,Message3):
        #i2c = I2C(-1, scl=Pin(22), sda=Pin(21)) #For ESP32: pin initializing
        i2c = I2C(scl=Pin(0), sda=Pin(4))  #For ESP8266: pin initializing
         
        oled_width = 128
        oled_height = 64
        oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

        oled.text(Message1, 0, 0)
        oled.text(Message2, 0, 16)
        oled.text(Message3, 0, 32)
                
        oled.show()
