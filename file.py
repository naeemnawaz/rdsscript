import mysql.connector as mysql
import os
import csv 
import secret
  
# Import x and y variables using 
# file_name.variable_name notation
HOST = secret.HOST
USER = secret.USER
PASSWORD = secret.PASSWORD
DATABASE = 'dbpython'
PORT = 3306


db_connection = mysql.connect(host=HOST,database=DATABASE,user=USER,password=PASSWORD)

mycursor = db_connection.cursor()
"""
with open('simple.csv','r',encoding="ascii",errors="surrogateescape") as f:
    reader = csv.reader(f)
    #reader = unicode(reader,errors='replace')
    for row in reader:
        print(row[2],row[3],row[4],row[5],row[6])
        sql = "INSERT INTO device(name,airpresure,temperature,humidity,soilmosture) VALUES(%s,%s,%s,%s,%s)"
        val = (row[2],row[3],row[4],row[5],row[6])
        mycursor.execute(sql,val)
        db_connection.commit()
    print('record inserted into database')
"""
#simple fetching data from AWS RDS database
mycursor.execute('select*from student')

for val in mycursor:
    print(val)


