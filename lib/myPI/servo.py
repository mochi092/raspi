import RPi.GPIO as GPIO
import time


class SG90:

    def __init__(self,gpio_pin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(gpio_pin, GPIO.OUT)

        self.servo = GPIO.PWM(gpio_pin, 50) 
        self.servo.start(0.0)

    def changeAngle(self,angle):
        #duty =(1.0 + angle/180.0)/20.0*100.0
        #print("duty:" + str(duty))  
        
        
        # 角度:duty
        # -90:2.5, -45:4.875 , 0:7.25 , 45:9.625 , 90:12.0
        duty = {-90:25 , -45:4.875, 0:7.25, 45:9.625 , 90:12.0}
        print(duty[angle])
        self.servo.ChangeDutyCycle(duty[angle])

        #self.servo.ChangeDutyCycle(12.0) #90度
        #self.servo.ChangeDutyCycle(2.5) #-90度
        time.sleep(0.5)

    def cleanup(self):
        GPIO.cleanup()

