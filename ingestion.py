# coding: utf-8
import csv
import mysql.connector 

#connection to the database MySQL
conn = mysql.connector.connect(host="localhost",user="root",password="", database="test-sogemi")
cursor = conn.cursor()

with open('Instructions/data/lieux.csv', 'r') as lieux:
    #CSV data to object
    objL = list(csv.reader(lieux))
    for i in range(1, len(objL)):
        cursor.execute("""INSERT INTO `lieux` (commune, departement, region) VALUES(%s, %s, %s)""", objL[i])
lieux.close()


with open('Instructions/data/people.csv', 'r') as people:
    #CSV data to object
    objP = list(csv.reader(people))
    for i in range(1, len(objP)):
        cursor.execute("""INSERT INTO `people` (prenom, nom, date_naissance, commune) VALUES(%s, %s, %s, %s)""", objP[i])
people.close()


conn.commit()

conn.close()

