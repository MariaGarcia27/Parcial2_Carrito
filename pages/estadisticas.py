import streamlit as st
import pandas as pd

st.title("📊 Estadísticas del Carrito Seguidor de Luz")

st.write("Aquí puedes ver los promedios de los sensores y un pequeño gráfico de comparación.")

# Simulación de datos (esto luego puedes conectarlo con Supabase si quieres)
data = {
    "Sensor": ["Izquierdo", "Central", "Derecho"],
    "Promedio": [0.65, 0.72, 0.60]
}

df = pd.DataFrame(data)

# Mostrar tabla
st.dataframe(df)

# Mostrar gráfico de barras
st.bar_chart(df.set_index("Sensor"))
