import mysql.connector

mydb = mysql.connector.connect(
    host="db",
    user="root",
    password="1234",
    database="mysql_db"
)

mycursor = mydb.cursor()

while True:
    sql = input()
    if len(sql) == 0:
        continue
    if sql.lower() in ('exit', 'quit'):
        break

    mycursor.execute(sql)
    try:
        mydb.commit()
    except:
        pass

    try:
        myresult = mycursor.fetchall()
        for i in myresult:
            print(i)
    except:
        pass
