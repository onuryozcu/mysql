#drop table
import mysql.connector

mydb = mysql.connector.connect(

    host = "localhost",
    user = "root",
    password = "12345",
    database = "Detection"

)

mycursor = mydb.cursor()

query = "drop table if exists koli"

mycursor.execute(query)