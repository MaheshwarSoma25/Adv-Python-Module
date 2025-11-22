# Database Connection

import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "302503",
    database = "project",
    port = 3306,
    autocommit = False
)

# print(conn.is_connected())

cursor = conn.cursor()

cursor.execute("SHOW TABLES")
print(cursor.fetchall())
print(cursor.fetchone())
# print(cursor.fetchmany(3))


cursor.close()
conn.close()