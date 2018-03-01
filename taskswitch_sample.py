import RPi.GPIO as GPIO
from myPI.taskswitch import taskswitch 


try:
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()

    switch = taskswitch(14)

    while True:
        if switch.isClick():
            print("on")
        else:
            print("off")

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
