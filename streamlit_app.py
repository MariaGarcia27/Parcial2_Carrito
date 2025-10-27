import streamlit as st

st.title("Carrito seguidor de luz 💡")

# Datos simulados
lecturas = [
    {"sensor_izquierdo": 0.8, "sensor_derecho": 1.0, "sensor_central": 0.9, "direccion": "Derecha"},
    {"sensor_izquierdo": 0.5, "sensor_derecho": 0.6, "sensor_central": 0.7, "direccion": "Izquierda"}
]

st.write("Últimas lecturas del carrito:")
st.dataframe(lecturas)
