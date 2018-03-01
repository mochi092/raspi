import picamera
import time

class ras_camera:
    def capture(self,filename):
    
        print('start capture')
        
        with picamera.PiCamera() as camera:
            camera.resolution = (1024,768)
            camera.vflip = True
            #camera.rotation = 90
            camera.start_preview()   
            time.sleep(3)
            camera.capture(filename)        
            camera.stop_preview()

        print('end capture')