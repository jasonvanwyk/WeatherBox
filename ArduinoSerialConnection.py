import serial
device = '/dev/ttyACM0'
ser = serial.Serial(device,9600)
while 1:
        if(ser.in_waiting >0):
            line = ser.readline()
            print(line)
