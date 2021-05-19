from picamera import PiCamera
from time import sleep
from datetime import datetime

subject = input("Subject: ")

camera = PiCamera()
now = datetime.now()
filename = 'films/%s,%s.h264' % (subject, now.strftime('%Y-%m-%d,%H:%M:%S'))

camera.resolution = (640, 360)
camera.framerate = 15

#camera.start_preview()
#sleep(2)

go = input("Press Enter to start")
if go:
    #camera.stop_preview()
    exit()
else:
    camera.start_recording(filename)
    #camera.stop_preview()

    camera.wait_recording(20) #7500 -> 2:05:00
    camera.stop_recording()
