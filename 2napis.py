#!/usr/bin/env python3

import RPi.GPIO as GPIO
from time import sleep
import serial


GPIO.setmode(GPIO.BOARD)

GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.IN)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.IN)

try:

	while True:
		GPIO.output(8, 1)
		wynik = GPIO.input(10)
		print(wynik)
		sleep(1)
		
		GPIO.output(8,0)
		wynik = GPIO.input(10)
		print(wynik)
		sleep(1)
		
except:
	print("Some error")
finally:
	GPIO.cleanup()
