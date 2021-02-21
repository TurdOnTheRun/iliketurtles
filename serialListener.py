import time
import serial

ser = serial.Serial(port="/dev/ttyS0", baudrate=115200, timeout=None)

while 1:
    print('go')
    x=ser.readline()
    print(x)
