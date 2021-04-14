import pickle
import pytz
import sqlite3

import pytz

db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

# for row in db.execute("SELECT strftime('%Y-%m-%d %H:%M:%f', transactions.time, 'localtime') AS localtime,"
#                       " transactions.account, transactions.amount FROM transactions ORDER BY transactions.time"):
for row in db.execute("SELECT * from transactions"):
    utc_time = row[0]
    pickled_zone = row[3]
    zone = pickle.loads(pickled_zone)
    local_time = pytz.utc.localize(utc_time).astimezone(zone)
    print("{}\t{}\t{}".format(utc_time, local_time, local_time.tzinfo))

db.close()
