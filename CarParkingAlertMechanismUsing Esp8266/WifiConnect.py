import socket
import network
import gc
from machine import Pin
import esp

#collecting unused objects
gc.collect()


#Credentials of wifi
#ssid='***********'
#password='*********'
class WifiConnect:
    def __conWifi__(ssid,password):
        wlan=network.WLAN(network.STA_IF);
        wlan.active(True)
        print(wlan.scan());
        arrSSID=wlan.scan();
        for varSsId in arrSSID:
            print('ssid-->'+str(varSsId[0]))
            if str(varSsId[0]).find(ssid)!= -1:
                print('found signal')
                if not wlan.isconnected():
                    print('Connecting network')
                    wlan.connect(ssid,password)
                    while not wlan.isconnected():
                        pass
        print('network address',wlan.ifconfig())

    #__conWifi__('**********','***********')

    



