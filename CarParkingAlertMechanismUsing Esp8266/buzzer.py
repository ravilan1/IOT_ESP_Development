# How to make some sound with MicroPython
# Example 1: Make a single note sound
# Author: George Bantique,
#         TechToTinker Youtube channel
#		  techtotinker.blogspot.com
# Date: September 18, 2020

# Import the machine module for GPIO and PWM
import machine
# Import the time module to add some delays
import time


class BUZZER:
    
    # Create a regular GPIO object from pin 23
    def createBuzzer(pin,frq,duty,flag):
        # Create a new object and attach the pwm driver
        print(pin)
        buzzer = machine.PWM(pin)

        # Set a pwm frequency
        buzzer.freq(frq)#1047
        # Set the pwm duty value
        # this serves as volume control
        if(flag=='alert'):
            j=2
        else:
            j=3
        i=1
        while(i<j):
            print(i)
            # Max volume is a duty value of 512
            buzzer.duty(duty)#50
            # Let the sound ring for a certain duration
            time.sleep(10)#50
            #buzzer.duty(0)
            # Turn off the pulse by setting the duty to 0
            i=i+1

        # And disconnect the pwm driver to the GPIO pin
        buzzer.deinit()
        
    #createBuzzer(pin=p5,frq=1047,duty=50)
