#!/usr/bin/env python3

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.IN)

try:
	while True:
		if GPIO.input(12) == 0:
			GPIO.output(11, 1)
		else:
			GPIO.output(11,0)

		wynik = GPIO.input(12)
		print(wynik)
		sleep(1)
except:
	print("Some error")
finally:
	GPIO.cleanup()
