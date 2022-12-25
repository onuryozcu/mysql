import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345",
  database="Detection"
)

mycursor = mydb.cursor()

sql = "UPDATE koli SET adress = %s WHERE adress = %s"
val = ("YZC 29", "YZC 23")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")