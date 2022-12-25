import mysql.connector

mydb = mysql.connector.connect(

    host = "localhost",
    user ="root",
    password = "12345"

)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE Detection")


#######################################################################
#oluşturduğumuz database test etme

connect_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="Detection"
)



