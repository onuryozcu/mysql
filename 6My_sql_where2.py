import mysql.connector

mydb = mysql.connector.connect(

    host="localhost",
    user="root",
    password="12345",
    database ="Detection"

)

mycursor = mydb.cursor()

sql = "select * from koli where adress like '%way%' "

mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)


##########################
print("""

EXAMPLE 2

""")

mycursor = mydb.cursor()

sql = "SELECT * FROM koli WHERE adress = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)