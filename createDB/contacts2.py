import sqlite3

db = sqlite3.connect("contacts.sqlite")

new_email = "anotherupdate@update.com"
phone = input("Please enter the phone number ")

# update_sql = "UPDATE contacts set email = '{}' where phone = {}".format(new_email, phone)
update_sql = "UPDATE contacts set email = ? where phone = ?"
print(update_sql)

update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email, phone))
print("{} rows updated".format(update_cursor.rowcount))

update_cursor.connection.commit()
update_cursor.close()

for name, phone, email in db.execute("SELECT * FROM  contacts"):
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

db.close()
