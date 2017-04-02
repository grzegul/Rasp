#!/usr/bin/env python3

from picamera import PiCamera
from time import sleep
from datetime import datetime

import tkinter as tk
from tkinter import messagebox



try: 
    camera = PiCamera()
    camera.resolution = (2592, 1944)
    camera.framerate = 15
    camera.start_preview(alpha=200)
    sleep(3)
except:
    root = tk.Tk()
    root.withdraw()
    messagebox.showwarning('Error', 'Unable to find camera!')
else:
    dateCapture = '{0:%Y%m%d_%H%M%S}'.format(datetime.now())
    fileName = '/home/pi/Pictures/{:s}.jpg'.format(dateCapture)

    camera.annotate_text_size = 100
    camera.annotate_text = dateCapture
    camera.capture(fileName)
    camera.stop_preview()


 





