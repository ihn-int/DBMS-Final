import mysql.connector
from mysql.connector import errorcode

db = mysql.connector.connect(
    host = "140.113.68.114",
    user = "manager",
    password = "toServer111550009",
    database = "db_final"
)

cursor = db.cursor()

cmd = "SHOW TABLES"
exec = cursor.execute(cmd)
rows = cursor.fetchall()

tables = []

for line in rows:
    tables.append(line[0])

for i in range(len(tables)):
    cmd = "SHOW COLUMNS FROM " + tables[i]
    exec = cursor.execute(cmd)
    rows = cursor.fetchall()
    print(tables[0])
    for line in rows:
        print(line)