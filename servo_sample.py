from myPI.servo import SG90

if __name__ == '__main__':

    sg = SG90(gpio_pin=14)

    sg.changeAngle(-90)
    sg.changeAngle(-45)
    sg.changeAngle(-0)
    sg.changeAngle(45)
    sg.changeAngle(90)
    
    sg.cleanup()