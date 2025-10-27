import streamlit as st
from supabase import create_client, Client
from dotenv import load_dotenv
import os

"""
streamlit_app.py
Aplicación web que muestra lecturas de sensores de un carrito seguidor de luz.
Conexión segura a Supabase usando variables de entorno.
"""

# 🔒 Cargar las variables del .env
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

# 🗄️ Crear el cliente de Supabase
supabase: Client = create_client(url, key)

# 🚗 Título de la app
st.title("Carrito Seguidor de Luz 🚗💡")
st.write("Visualización de los datos almacenados en Supabase.")


def obtener_datos():
    """Obtiene todas las lecturas de la tabla 'lecturas_luz' en Supabase.
    Returns:
        list: Lista de registros, o lista vacía si hay error.
    """
    try:
        response = supabase.table("lecturas_luz").select("*").execute()
        return response.data
    except Exception as e:
        st.error(f"❌ Error al conectar con Supabase: {e}")
        return []


# ✅ Obtener datos
data = obtener_datos()

if data:
    st.subheader("📊 Lecturas registradas")
    st.dataframe(data)

    # Mostrar estadísticas básicas
    st.write("Promedio de cada sensor:")
    izq = sum(row["sensor_izquierdo"] for row in data) / len(data)
    der = sum(row["sensor_derecho"] for row in data) / len(data)
    cen = sum(row["sensor_central"] for row in data) / len(data)

    st.metric("Sensor Izquierdo", f"{izq:.2f}")
    st.metric("Sensor Derecho", f"{der:.2f}")
    st.metric("Sensor Central", f"{cen:.2f}")
else:
    st.info("No hay registros en la tabla 'lecturas_luz'.")
