#!/usr/bin/env python3

import RPi.GPIO as GPIO
from time import sleep
import serial


GPIO.setmode(GPIO.BOARD)

GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.IN)

try:
    ser = serial.Serial('/dev/serial0')
    print('Port name: ', ser.name)
    print('Baudrate: ', ser.baudrate)
    
    ser.write(b'hello')
    slowo = ser.read(4)
    print(slowo)

    print('Done')

except:
    print("Some error")
finally:
    GPIO.cleanup()
    ser.close()
