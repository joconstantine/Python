import sqlite3

conn = sqlite3.connect("contacts.sqlite")

check_name = input("Enter a name to check: ")

check_sql = "SELECT * FROM contacts WHERE name LIKE ?"
db_cursor = conn.cursor()

for row in db_cursor.execute(check_sql, (check_name,)):
    print(row)

conn.close()
