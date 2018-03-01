import RPi.GPIO as GPIO

class taskswitch:
    __pin = None

    def __init__(self,pin):
        self.__pin = pin 
        GPIO.setup(pin,GPIO.IN)   

    def isClick(self):
        return GPIO.input(self.__pin) == GPIO.HIGH