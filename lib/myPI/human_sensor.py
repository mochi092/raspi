import RPi.GPIO as GPIO

class DSUN_PIR:

    __pin = None

    def __init__(self,pin):
        self.__pin = pin
        GPIO.setup(self.__pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

    def read(self):
        return GPIO.input(self.__pin)