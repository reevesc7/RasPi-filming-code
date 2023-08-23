from sys import argv
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput
from picamera2 import Picamera2
from time import sleep
from datetime import datetime
from os.path import expanduser

#Argument parsing
parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("-t", "--time", default=7500, type=int, help="Duration (seconds) of recording")
args = vars(parser.parse_args())

#Set and display parameters
record_time = args["time"]
print("Record for", record_time, "seconds")

#Get subject ID
subject = input("Subject: ")

#Initialize camera
camera = Picamera2()
video_config = camera.create_video_configuration({"size": (640, 360)}, controls={"FrameDurationLimits": (40000, 40000)})
camera.configure(video_config)
encoder = H264Encoder(10000000)

#Create filename
now = datetime.now()
filename = expanduser('~') + "/recordings/%s,%s.mp4" % (subject, now.strftime("%Y-%m-%d,%H-%M-%S"))
output = FfmpegOutput(filename)

#Confirmation to start
while(1):
    go = input("Start? (Y/n)\n")
    if go == "n" or go == "N":
        exit()
    elif go == "Y" or go == "y" or go == "":
        break
    else:
        print("Please enter \"y\", \"n\" or nothing")

#Recording
camera.start_recording(encoder, output)
sleep(record_time)
camera.stop_recording()
