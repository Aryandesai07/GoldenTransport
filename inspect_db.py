import sqlite3

conn = sqlite3.connect("golden_transport.db")
cur = conn.cursor()
cur.execute("PRAGMA table_info(orders)")
rows = cur.fetchall()
print("PRAGMA table_info(orders):")
for r in rows:
    print(r)
print("db_columns_count =", len([r for r in rows if r[1] != 'id']))
print("db_columns_names =", [r[1] for r in rows if r[1] != 'id'])
conn.close()
