#create table
#table oluşturulduğu için hata verecektir panik edilmesine gerek yoktur.

import mysql.connector.cursor


mydb = mysql.connector.connect(

    host = "localhost",
    user = "root",
    password = "12345",
    database = "Detection"

)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE koli (id int AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255),adress VARCHAR(255))")

print(mydb)

