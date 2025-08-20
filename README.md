# r_calculator
Calculator for the withdrawal date and expiration date of a product

# Calculadora de R y Caducidad

Calculadora web para determinar los días hasta retirada (R) y caducidad de productos a partir de la fecha de lote y la información de cada producto almacenada en una base de datos SQLite.

---

## **Contenido del proyecto**

- `index.html` - Frontend de la calculadora.
- `style.css` - Estilos del frontend.
- `script.js` - Lógica del frontend y llamadas al backend.
- `main.py` - Backend con FastAPI.
- `products.db` - Base de datos SQLite con productos y sus días de R y caducidad.
- `README.md` - Este archivo de documentación.

---

## **Requisitos**

- Python 3.9+
- FastAPI
- Uvicorn
- SQLite3
- Git (opcional, para control de versiones)

Instalación de dependencias:
```bash
pip install fastapi uvicorn python-multipart
