#update

import mysql.connector

mydb = mysql.connector.connect(

    host = "localhost",
    user = "root",
    password = "12345",
    database = "Detection"
)

mycursor = mydb.cursor()

query = "update koli set name = 'Türk' where adress = 'YZC 29'"

mycursor.execute(query)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")


mycursor = mydb.cursor()


#### select....
sql = "select * from koli order by name desc"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)