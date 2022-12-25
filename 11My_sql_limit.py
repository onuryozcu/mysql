import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345",
  database="Detection"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM koli LIMIT 5 OFFSET 2")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)