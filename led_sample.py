import time

import RPi.GPIO as GPIO
from myPI.led import led 


try:
    GPIO.setmode(GPIO.BCM) 

    led = led(pin=21)
    
    led.on()

    time.sleep(1)

    led.off()

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
