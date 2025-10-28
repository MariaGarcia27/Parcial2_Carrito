import streamlit as st
import pandas as pd
from db import supabase

st.title("📊 Estadísticas del Carrito Seguidor de Luz")
st.write("Aquí puedes ver los promedios reales de los sensores obtenidos desde Supabase y su comparación visual.")

# Función para obtener los datos de la base
def obtener_datos():
    """Obtiene las lecturas desde la tabla 'lecturas_luz'."""
    try:
        response = supabase.table("lecturas_luz").select("*").execute()
        return response.data
    except Exception as e:
        st.error(f"❌ Error al obtener datos de Supabase: {e}")
        return []

# Obtener datos
data = obtener_datos()

if data:
    # Convertir a DataFrame
    df = pd.DataFrame(data)

    # Mostrar tabla original
    st.subheader("📋 Lecturas registradas")
    st.dataframe(df)

    # Asegurar que las columnas existan y sean numéricas
    sensores = ["sensor_izquierdo", "sensor_central", "sensor_derecho"]
    for col in sensores:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Calcular promedios
    promedio_izq = df["sensor_izquierdo"].mean()
    promedio_cen = df["sensor_central"].mean()
    promedio_der = df["sensor_derecho"].mean()

    # Crear DataFrame de resumen
    resumen = pd.DataFrame({
        "Sensor": ["Izquierdo", "Central", "Derecho"],
        "Promedio": [promedio_izq, promedio_cen, promedio_der]
    })

    # Mostrar promedios
    st.subheader("📈 Promedio de Sensores")
    st.dataframe(resumen)

    # Mostrar gráfico
    st.bar_chart(resumen.set_index("Sensor"))

    # (Opcional) Gráfico de evolución
    st.subheader("📉 Evolución de las lecturas")
    st.line_chart(df[sensores])

else:
    st.info("No se encontraron registros en la tabla 'lecturas_luz'.")
