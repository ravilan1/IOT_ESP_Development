from hcsr04 import HCSR04
from time import sleep
import os

print(os.listdir())
sensor = HCSR04(trigger_pin=12, echo_pin=14, echo_timeout_us=10000)
content=''
count,fileCount=1
while True:
    distance = sensor.distance_cm()
    if content=='':
        content='[DistanceMeasure: {"Distance":'+str(distance)+'cm\n}'
    else:
        content=content+',{"Distance":'+str(distance)+'cm\n}'
    print(content)
    sleep(1)
    count=count+1
    if count==10:
        file=open("measurements"+str(fileCount)+".txt","w")
        content=content+']'
        file.write(content)
        print(os.listdir())
        count=1
        fileCount=fileCount+1
        