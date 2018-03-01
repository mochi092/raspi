import time

import RPi.GPIO as GPIO  					 #importing the RPi.GPIO module
from myPI.human_sensor import DSUN_PIR

try:

	GPIO.setmode(GPIO.BCM) 				 
	GPIO.setwarnings(False)   
	GPIO.cleanup()

	human_sensor = 	DSUN_PIR(pin=4)

	while True:
		time.sleep(3)
		value=human_sensor.read()

		if value!=0:		                         #to read the value of a GPIO pin
			print ("on")                          
		else:
			print ("off")

except KeyboardInterrupt:
  pass
finally:
  GPIO.cleanup()