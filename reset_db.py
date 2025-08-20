import os
import sqlite3

DB_NAME = "products.db"

# 1. Eliminar la base de datos anterior si existe
if os.path.exists(DB_NAME):
    os.remove(DB_NAME)
    print(f"{DB_NAME} eliminado correctamente.")

# 2. Crear una nueva base de datos
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# Crear tabla
cursor.execute("""
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    R_days INTEGER NOT NULL,
    expiry_days INTEGER NOT NULL
)
""")

# Insertar productos (lista actual)
productos = [
    ("chorizo fresco ib", 7, 15),
    ("morcilla pueblo", 7, 15),
    ("morcilla cebolla", 7, 15),
    ("morcilla cordoba", 5, 11),
    ("flamenquin pollo", 4, 9),
    ("cachopo", 5, 9),
    ("tocino fresco ib", 7, 15),
    ("puchero vacuno pollo", 4, 7),
    ("puchero cerdo pollo", 4, 7),
    ("preparado pringa", 4, 7)
]

cursor.executemany(
    "INSERT INTO products (name, R_days, expiry_days) VALUES (?, ?, ?)",
    productos
)

conn.commit()
conn.close()

print("Base de datos reiniciada con los productos actuales.")
