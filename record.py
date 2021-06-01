from picamera import PiCamera
from time import sleep
from datetime import datetime

subject = input("Subject: ")

camera = PiCamera()
now = datetime.now()
filename = 'films/%s,%s.h264' % (subject, now.strftime('%Y-%m-%d,%H:%M:%S'))

camera.resolution = (648, 486)
camera.framerate = 30
camera.brightness = 100 #Enter an integer 0-100

while(1):
    go = input("Start? (Y/n) ")
    if go == "n":
        exit()
    elif go == "Y" or go == "y" or go == "":
        break
    else:
        print("Please enter \"y\", \"n\" or nothing")

camera.start_recording(filename)
print("Recording Started!")
camera.wait_recording(7500) #7500 -> 2:05:00
camera.stop_recording()
