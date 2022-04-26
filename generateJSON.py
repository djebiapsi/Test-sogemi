# coding: utf-8
import json
import mysql.connector 

#Variable(s) Globale(s)
naissance_dept = {}
naissance_reg = {}



#connection to the database MySQL
conn = mysql.connector.connect(host="localhost",user="root",password="", database="test-sogemi")
cursor = conn.cursor()

#generate JSON naissance par departement
#Request
cursor.execute("""SELECT l.departement, count(p.id) FROM `people` as p INNER JOIN `lieux` as l ON p.commune = l.commune GROUP BY l.departement;""")
rows = cursor.fetchall()

for row in rows:
    naissance_dept[row[0]] = row[1]
   
#Write JSON file
with open('naissance_dept.json', 'w') as npdt:
	json.dump(naissance_dept, npdt)
npdt.close()


#generate JSON naissance par région
#Request
cursor.execute("""SELECT l.region, count(p.id) FROM `people` as p INNER JOIN `lieux` as l ON p.commune = l.commune GROUP BY l.region;""")
rows = cursor.fetchall()

for row in rows:
    naissance_reg[row[0]] = row[1]
conn.close()
   
#Write JSON file
with open('naissance_reg.json', 'w') as nprg:
	json.dump(naissance_reg, nprg)
nprg.close()


