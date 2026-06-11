import streamlit as st
import streamlit.components.v1 as components

# Ocultar márgenes extra de Streamlit
st.set_page_config(layout="wide")

# Abrir y leer tu archivo HTML
with open("tplaboratorio.html", "r", encoding="utf-8") as f:
    html_data = f.read()

# Mostrar el HTML (ajustá el height si te queda corto)
components.html(html_data, height=4500, scrolling=True)
