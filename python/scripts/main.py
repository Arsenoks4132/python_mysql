import mysql.connector

mydb = mysql.connector.connect(
  host="db",
  user="root",
  password="1234"
)

print(mydb)