import sqlite3

conn = sqlite3.connect("products.db")
cursor = conn.cursor()

# Crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    R_days INTEGER NOT NULL,
    expiry_days INTEGER NOT NULL
)
""")

# Insertar productos
cursor.execute("INSERT OR IGNORE INTO products (name, R_days, expiry_days) VALUES ('chorizo fresco ib', 7, 15)")
cursor.execute("INSERT OR IGNORE INTO products (name, R_days, expiry_days) VALUES ('morcilla pueblo', 7, 15)")
cursor.execute("INSERT OR IGNORE INTO products (name, R_days, expiry_days) VALUES ('morcilla cebolla', 7, 15)")
cursor.execute("INSERT OR IGNORE INTO products (name, R_days, expiry_days) VALUES ('morcilla cordoba', 5, 11)")
cursor.execute("INSERT OR IGNORE INTO products (name, R_days, expiry_days) VALUES ('morcilla cadiz', 7, 15)")
cursor.execute("INSERT OR IGNORE INTO products (name, R_days, expiry_days) VALUES ('flamenquin pollo', 4, 9)")
cursor.execute("INSERT OR IGNORE INTO products (name, R_days, expiry_days) VALUES ('cachopo', 5, 9)")
cursor.execute("INSERT OR IGNORE INTO products (name, R_days, expiry_days) VALUES ('tocino fresco ib', 7, 15)")
cursor.execute("INSERT OR IGNORE INTO products (name, R_days, expiry_days) VALUES ('puchero vacuno pollo', 4, 7)")
cursor.execute("INSERT OR IGNORE INTO products (name, R_days, expiry_days) VALUES ('puchero cerdo pollo', 4, 7)")
cursor.execute("INSERT OR IGNORE INTO products (name, R_days, expiry_days) VALUES ('preparado pringa', 4, 7)")

conn.commit()
conn.close()

print("Database created and initialized successfully!")
