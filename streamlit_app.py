import streamlit as st
from supabase import create_client, Client
from dotenv import load_dotenv
import os

# 🔒 Cargar las variables del .env
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

# 🗄️ Crear el cliente de Supabase
supabase: Client = create_client(url, key)

# 🚗 Título de la app
st.title("Carrito Seguidor de Luz 🚗💡")

st.write("Visualización de los datos almacenados en Supabase.")

# ✅ Obtener los datos de la tabla 'lecturas_luz'
try:
    response = supabase.table("lecturas_luz").select("*").execute()
    data = response.data

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

except Exception as e:
    st.error(f"❌ Error al conectar con Supabase: {e}")
