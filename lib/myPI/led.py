import time
import RPi.GPIO as GPIO

class led:

    __pin = None

    def __init__(self,pin):
        self.__pin = pin
        
    def on(self):
        GPIO.setmode(GPIO.BCM) 
        GPIO.setup(self.__pin, GPIO.OUT)
        GPIO.output(self.__pin, GPIO.HIGH)
    
    def off(self):
        GPIO.cleanup()

