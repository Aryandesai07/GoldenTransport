import sqlite3

src = "golden_transport.db"
conn = sqlite3.connect(src)
cur = conn.cursor()

# 1) Create new table with desired schema (single lorry_name column)
cur.execute("""
CREATE TABLE IF NOT EXISTS orders_new (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    lorry_no TEXT,
    lorry_name TEXT,
    driver_name TEXT,
    driver_no TEXT,
    from_place TEXT,
    to_place TEXT,
    freight REAL,
    ton_age REAL,
    advance NUMERIC,
    balance INTEGER,
    load TEXT,
    commission REAL
)
""")

# 2) Copy data from old table to new table.
# Map add_name -> lorry_name if add_name exists; else use existing lorry_name.
cur.execute("""
INSERT INTO orders_new (date, lorry_no, lorry_name, driver_name, driver_no,
                        from_place, to_place, freight, ton_age,
                        advance, balance, load, commission)
SELECT
    date,
    lorry_no,
    COALESCE(add_name, lorry_name, '') AS lorry_name,
    driver_name,
    driver_no,
    from_place,
    to_place,
    freight,
    ton_age,
    advance,
    balance,
    load,
    commission
FROM orders
""")

# 3) Replace old table with new
cur.execute("DROP TABLE IF EXISTS orders")
cur.execute("ALTER TABLE orders_new RENAME TO orders")

conn.commit()
conn.close()
import sqlite3

src = "golden_transport.db"
conn = sqlite3.connect(src)
cur = conn.cursor()

# 1) Create new table with desired schema (single lorry_name column)
cur.execute("""
CREATE TABLE IF NOT EXISTS orders_new (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    lorry_no TEXT,
    lorry_name TEXT,
    driver_name TEXT,
    driver_no TEXT,
    from_place TEXT,
    to_place TEXT,
    freight REAL,
    ton_age REAL,
    advance NUMERIC,
    balance INTEGER,
    load TEXT,
    commission REAL
)
""")

# 2) Copy data from old table to new table.
# Map add_name -> lorry_name if add_name exists; else use existing lorry_name.
cur.execute("""
INSERT INTO orders_new (date, lorry_no, lorry_name, driver_name, driver_no,
                        from_place, to_place, freight, ton_age,
                        advance, balance, load, commission)
SELECT
    date,
    lorry_no,
    COALESCE(add_name, lorry_name, '') AS lorry_name,
    driver_name,
    driver_no,
    from_place,
    to_place,
    freight,
    ton_age,
    advance,
    balance,
    load,
    commission
FROM orders
""")

# 3) Replace old table with new
cur.execute("DROP TABLE IF EXISTS orders")
cur.execute("ALTER TABLE orders_new RENAME TO orders")

conn.commit()
conn.close()

print("Migration complete. Backup saved as golden_transport.db.bak")

print("Migration complete. Backup saved as golden_transport.db.bak")
