#where belirli bir koşul ile değerlerin seçilmesi
import mysql.connector

mydb = mysql.connector.connect(

    host="localhost",
    user="root",
    password = "12345",
    database = "Detection"
)

mycursor = mydb.cursor()

sql = "select * from koli where name='onur'"

mycursor.execute(sql)
myresult = mycursor.fetchall()


for x in myresult:
    print(x)