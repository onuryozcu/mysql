#delete
import  mysql.connector

mydb = mysql.connector.connect(

    host="localhost",
    user = "root",
    password = "12345",
    database = "Detection"

)

mycursor = mydb.cursor()

query = "delete from koli  "

mycursor.execute(query)

mydb.commit()

print(mycursor.rowcount,"record(s) deleted")


