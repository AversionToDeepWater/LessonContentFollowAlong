import mysql.connector
from config import HOST, USER, PASSWORD, DATABASE

db_connection = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    auth_plugin='mysql_native_password',
    database=DATABASE
)


print("Establishing Connection")

cursor = db_connection.cursor()
query = "SELECT * FROM art_works"

cursor.execute(query)

result = cursor.fetchall()

print("HP DATA: ", result)


print("Closing Connection")
db_connection.close()