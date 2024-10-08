import mysql.connector

mydb = mysql.connector.connect(
    host="db",
    user="test_user",
    password="test_pass",
    database="db_name"
)

mycursor = mydb.cursor()

while True:
    sql = input()
    if sql.lower() in ('exit', 'quit'):
        break
    if len(sql) <= 0:
        continue

    try:
        mycursor.execute(sql)
    except:
        print("wrong query")

    try:
        mydb.commit()
    except:
        pass

    try:
        myresult = mycursor.fetchall()
        for i in myresult:
            print(i)
    except:
        print("read failed")
