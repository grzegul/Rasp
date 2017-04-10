#!/usr/bin/env python3
import serial
ser = serial.Serial("/dev/serial0")
ser.write(b'UART the Font \r\n')
#ser.write(bytes[0, 4])
read = ser.read(10)
print(read)
ser.close()
