#SELECT  işlemi yaparken fetchall() methodunu kullandık
import mysql.connector

mydb = mysql.connector.connect(

    host="localhost",
    user = "root",
    password = "12345",
    database = "Detection"

)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM koli")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)


print("")
print("")
print("SELECT FETCHONE() İLE TABLODAN DEĞERLERİN ÇEKİLMESİ...")
print("")


mycursor.execute("select name,adress from koli")
myresult2 = mycursor.fetchone()


print(myresult2) #output ('Onur', 'YZC 29')

for x in myresult2: #output Onur YZC 29
    print(x)



