#!/usr/bin/env python3
import serial
try:
    ser = serial.Serial('/dev/serial0')  # open serial port
    print(ser.name)        
    print(ser.baudrate)
    ser.write(b'hello')     
#    ser.close()  
    rcv = ser.read(4)
    print(rcv)
except:
    print("Some error")
finally:
    if ser.isOpen():
        ser.close()  
