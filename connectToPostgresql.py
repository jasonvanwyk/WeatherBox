import psycopg2
import time
import serial
import random
import datetime

con = None

for loop in range (0,10):
    try:
        x = random.randint(1,101)
        #t = datetime.datetime.now()
        con = psycopg2.connect("host='localhost', dbname = 'test', user='postgres', password='XXXX'")
        cur = con.cursor()
        #cur.execute("INSERT INTO tbltest VALUES (%s), (x)")
        cur.execute("INSERT INTO tbltest VALUES (1)")
        con.commit()

    finally:
        if con:
            con.close()

        print (x)
        time.sleep(1)
