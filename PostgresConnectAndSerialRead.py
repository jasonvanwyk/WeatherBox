import psycopg2
import time
import serial
import random
import datetime

device = '/dev/ttyACM0'
ser = serial.Serial(device,9600)
time.sleep(1)

while 1:
    x = ser.read(2)
    temp = (x.decode('utf8'))
    print (temp)

