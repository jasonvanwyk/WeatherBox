import psycopg2
import time
import serial
import random
import datetime

device = '/dev/ttyACM0'
temp = 0

while 1:
        ser = serial.Serial(device,9600)
        line = ser.read(2)
        temp = (line.decode('utf8'))
        #print(temp)
                    
        con = None

        try:
                t_stamp = datetime.datetime.now()
                t_time = datetime.datetime.now()
                d_date = datetime.datetime.now()
                con = psycopg2.connect(host="localhost",dbname="test",user="postgres",password="xxxxx")
                cur = con.cursor()
                cur.execute("INSERT INTO tbltest VALUES (%s, %s, %s, %s)", (t_stamp, t_time, d_date, temp))
                con.commit()

        finally:
                if con:
                        con.close()

        print (temp)
        time.sleep(900)
