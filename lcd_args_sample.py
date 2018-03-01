import time
import datetime
import sys

import RPi.GPIO as GPIO
from myPI.lcd import LCD1620

try:

    args = sys.argv

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()

    lcd = LCD1620()
    
    for i in range(5):
        lcd.print(args[1] , args[2] )
        time.sleep(3)

        lcd.clear()
        time.sleep(3)
   
        
except KeyboardInterrupt:
    pass

finally:
    lcd.clear()
    GPIO.cleanup()
