#çoklu değer insert etme

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345",
  database="Detection"
)

mycursor = mydb.cursor()

sql = "INSERT INTO koli (name, adress) VALUES (%s, %s)"
val = [
  ('Peterqweqw', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")


