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
                t = datetime.datetime.now()
                con = psycopg2.connect(host="localhost",dbname="test",user="postgres",password="xxxxx")
                cur = con.cursor()
                cur.execute("INSERT INTO tbltest(inttest) VALUES(%s)", (temp,))
                #cur.execute("INSERT INTO tbltest VALUES (1)")
                con.commit()

        finally:
                if con:
                        con.close()

        print (temp)
        time.sleep(900)
