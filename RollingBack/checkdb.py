import sqlite3


db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

# for row in db.execute("SELECT strftime('%Y-%m-%d %H:%M:%f', transactions.time, 'localtime') AS localtime,"
#                       " transactions.account, transactions.amount FROM transactions ORDER BY transactions.time"):
for row in db.execute("SELECT * from localtransactions"):
    print(row)

db.close()
