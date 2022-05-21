import dht
import machine
import time

print("Starting DHT11.")
d = dht.DHT11(machine.Pin(4,machine.Pin.PULL_UP))
d.measure()

while True:
    print("Measuring.")
    
    retry = 0
    while retry < 3:
        try:
            d.measure()
            break
        except:
            retry = retry + 1
            print(".", end = "")

    print("")

    if retry < 3:
        print("Temperature: %3.1f °C" % d.temperature())
        print("   Humidity: %3.1f %% RH" % d.humidity())

    time.sleep(5)