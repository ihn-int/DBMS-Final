import mysql.connector
from mysql.connector import errorcode
import hashlib

db = mysql.connector.connect(
    host = "140.113.68.114",
    user = "manager",
    password = "toServer111550009",
    database = "db_final"
)

cursor = db.cursor()



exec = cursor.execute(cmds["favorite"])
rows = cursor.fetchall()

def check_user_exist(account) -> bool:
    cmd = "SELECT account in user_table WHERE account == " + str(account)
    cursor.execute(cmd)
    cursor.fetchall()
    if cmd != "":
        return True
    
def check_user_exist(passwd, user_id) -> bool | int:
    hash = hashlib.md5(passwd.encode("utf-8")).hexdigest()
    cmd = "SELECT password in user_table WHERE user_id == " + str(user_id)
    cursor.execute(cmd)
    cursor.fetchall()
    if 
    pass