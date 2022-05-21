from hcsr04 import HCSR04
from MQTTServer_Publish import MQTTConfig
#from Email_Config import Email
from time import sleep
from WifiConnect import WifiConnect
from machine import Pin
import os
import ubinascii
from buzzer import BUZZER
from oled import OLED
from utility import Utility
from lm35 import LM35

print(os.listdir())
p5 = machine.Pin(5, machine.Pin.OUT)
led= machine.Pin(2, machine.Pin.OUT)
#laser=machine.Pin(15, machine.Pin.OUT)
sensor = HCSR04(trigger_pin=12, echo_pin=14, echo_timeout_us=10000)
wifiConnect=WifiConnect.__conWifi__('*********','*********')
content=''
count=1
fileCount=1
while True:
    distance = sensor.distance_cm()
    print('distance is ---->',distance)
    if(distance<3.79):
        flag='alert'
        MQTTConfig._main_(mqtt_broker="192.168.0.104", clientid=ubinascii.hexlify(machine.unique_id()),message="Alert")
        OLED.display('Hi Ravi','Obstacle - '+str(distance),str(Utility.getCurrentLocalTime()))
        led.value(1)
        #laser.on()
        BUZZER.createBuzzer(p5,500,50,flag)
        led.value(0)
        #laser.off()
    if content=='':
        content='[DistanceMeasure: {"Distance":'+str(distance)+'cm\n}'
    else:
        content=content+',{"Distance":'+str(distance)+'cm\n}'
    sleep(1)
    count=count+1
    print('count is',count)
    OLED.display('Hi Ravi','Room Temp: - '+LM35.lm(),str(Utility.getCurrentLocalTime()))
    if count==300:
        file=open("measurements"+str(fileCount)+".txt","w")
        content=content+']'
        #MQTTConfig._main_(mqtt_broker="192.168.0.104", clientid=ubinascii.hexlify(machine.unique_id()),message=content)
        print(content)
        file.write(content)
        print('before buzzer')
        flag='fullalert'
        #BUZZER.createBuzzer(p5,1047,50,flag)
        print(os.listdir())
        content=''
        count=1
        fileCount=fileCount+1