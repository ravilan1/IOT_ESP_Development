import machine
from time import sleep_ms 
adc = machine.ADC(0)

class LM35:
    def lm():
        #while True:
        val=adc.read()
        v_mv=val*(3100/1024)
        t=v_mv/10
        print(str(t)+' degrees')
            #sleep_ms(1000)
        return str(t)
