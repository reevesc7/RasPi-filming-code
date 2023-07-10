record_time = 7500
    #7500 seconds = 2:05:00

from picamera import PiCamera
from time import sleep
from datetime import datetime

subject = input("Subject: ")

camera = PiCamera()
now = datetime.now()
filename = 'films/%s,%s.h264' % (subject, now.strftime('%Y-%m-%d,%H-%M-%S'))

camera.resolution = (640, 360)
camera.framerate = 30

while(1):
    go = input("Start? (Y/n)\n")
    if go == "n" or go == "N":
        exit()
    elif go == "Y" or go == "y" or go == "":
        break
    else:
        print("Please enter \"y\", \"n\" or nothing")

camera.start_recording(filename)
camera.wait_recording(record_time)
camera.stop_recording()
