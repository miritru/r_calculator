from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta
import sqlite3

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8080"],  #origen del frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
DB_PATH = "products.db"

#Base de datos de productos
def get_product_info(product_name: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT R_days, expiry_days FROM products WHERE name = ?", (product_name.lower(),))
    result = cursor.fetchone()
    conn.close()
    if result:
        R_days, expiry_days = result
        return {"R_days": R_days, "expiry_days": expiry_days}
    return None

@app.get("/")
def root():
    return {"mensaje": "Welcome to R calculator"}

#Ruta para realizar el cálculo de fechas
@app.get("/calculate")
def calculate_R(product: str, batch_date: str):
    info = get_product_info(product)
    #Se comprueba si el producto existe
    if not info:
        return {"error": "Product not found"}

    #Se convierte date_lot (ej: '2025-08-20') a objeto datetime
    try:
        date = datetime.strptime(batch_date, "%Y-%m-%d")
    except ValueError:
        return {"error": "Date format is not valid. Use YYYY-MM-DD"}

    #Se calculan fecha de retirada y fecha de caducidad
    R_date = date + timedelta(days=info["R_days"])
    expiry_date = date + timedelta(days=info["expiry_days"])

    return {
        "product": product,
        "batch date": batch_date,
        "R days": info["R_days"],
        "R date": R_date.strftime("%Y-%m-%d"),
        "expiry days": info["expiry_days"],
        "expiry date": expiry_date.strftime("%Y-%m-%d")
    }

#Ruta para listar productos
@app.get("/products")
def get_products():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM products")
    rows = cursor.fetchall()

    conn.close()

    #Se transforma [(prod1,), (prod2,), ...] en ["prod1", "prod2", ...]
    products = [row[0] for row in rows]

    return products