#!/usr/bin/env python3

from picamera import PiCamera
from time import sleep
from datetime import datetime

camera = PiCamera()

camera.resolution = (2592, 1944)
camera.framerate = 15

dateCapture = '{0:%Y%m%d_%H%M%S}'.format(datetime.now())
fileName = '/home/pi/Pictures/{:s}.jpg'.format(dateCapture)

camera.annotate_text_size = 100
camera.annotate_text = dateCapture

camera.start_preview(alpha=200)
#camera.awb_mode = 'shade'
#camera.exposure_mode = 'night'
sleep(3)
camera.capture(fileName)

camera.stop_preview()
