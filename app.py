import streamlit as st
import cohere
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configurar Cohere
co = cohere.Client(os.getenv("COHERE_API_KEY"))

# Título
st.title("CampoData AI")

# Descripción
st.markdown("""
### Asistente Productivo Inteligente

CampoData AI ayuda a productores agrícolas y ganaderos a analizar situaciones productivas mediante inteligencia artificial, transformando información climática y operativa en recomendaciones prácticas para la toma de decisiones.
""")

# Entradas
tipo_produccion = st.selectbox(
    "Tipo de producción",
    ["Agricultura", "Ganadería"]
)

actividad = st.text_input("Cultivo o actividad")

temperatura = st.number_input("Temperatura (°C)", value=20.0)
humedad = st.number_input("Humedad (%)", value=50.0)
precipitaciones = st.number_input("Precipitaciones (mm)", value=0.0)

observaciones = st.text_area(
    "Situación observada por el productor"
)

# Botón
if st.button("Generar análisis"):

    if actividad.strip() == "" or observaciones.strip() == "":
        st.warning("Completá el cultivo o actividad y la situación observada antes de generar el análisis.")
    else:
        prompt = f"""
        Actúa como un ingeniero agrónomo especializado en producción agrícola y ganadera de Uruguay.

        Analiza la siguiente situación:

        Tipo de producción: {tipo_produccion}
        Actividad: {actividad}
        Temperatura: {temperatura} °C
        Humedad: {humedad} %
        Precipitaciones: {precipitaciones} mm

        Observaciones:
        {observaciones}

        No inventes diagnósticos definitivos. Si faltan datos, indicá que el análisis es orientativo y que debe validarse con monitoreo a campo o asesoramiento técnico.

        Genera una respuesta con el siguiente formato:

        Diagnóstico:
        Riesgos detectados:
        Recomendaciones:
        Nivel de prioridad:
        """

        with st.spinner("Analizando información..."):
            respuesta = co.chat(
                model="command-a-03-2025",
                message=prompt
            )

        st.success("Análisis generado correctamente")
        st.subheader("Informe de CampoData AI")
        st.write(respuesta.text)

# Cómo funciona
st.header("¿Cómo funciona?")
st.write("""
1. Ingresa los datos del establecimiento.
2. Describe la situación observada.
3. Presiona 'Generar análisis'.
4. La IA generará recomendaciones para apoyar la toma de decisiones.
""")

st.divider()
st.caption("Proyecto académico desarrollado con Streamlit, Python y Cohere API.")