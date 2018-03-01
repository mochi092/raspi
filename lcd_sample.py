from time import sleep

import RPi.GPIO as GPIO
from myPI.lcd import LCD1620

try:
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()

    lcd = LCD1620()
    
    lcd.print("Hello","world")
    sleep(3)

    lcd.printLine1(lcd.kana_to_code("ハロー　ワールト”"))
    lcd.printLine2(lcd.kana_to_code("ハ”イハ”イ。サヨウナラ。"))
    sleep(3)

    lcd.clear()
        
except KeyboardInterrupt:
    pass

finally:
    lcd.clear()
    GPIO.cleanup()
