import streamlit as st
import pandas as pd

# Estilos CSS para cambiar el color de fondo, tipo de letra y tamaño del texto
page_bg_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400;700&display=swap');
    
    .stApp {
        background-color: #E0FFFF;  /* Azul agua bajito */
        font-family: 'Roboto Mono', monospace;
    }
    .header-container {
        background-color: black;  /* Contenedor negro */
        color: white;  /* Texto blanco */
        padding: 10px;
        display: flex;
        align-items: center;
    }
    .header-container img {
        width: 50px;  /* Ajusta el tamaño de la imagen según tus necesidades */
        margin-right: 10px;
    }
    .header-container b {
        font-size: 28px;  /* Ajusta el tamaño del texto del título */
        font-weight: 700;  /* Tipo de letra más elegante */
    }
    .stMarkdown, .stDataFrame {
        font-size: 20px;  /* Ajusta el tamaño del texto para otras secciones */
    }
    .stSlider {
        font-size: 24px;  /* Ajusta el tamaño del texto para el control deslizante */
    }
    .stSelectbox {
        font-size: 20px;  /* Ajusta el tamaño del texto para el cuadro de selección */
        box-shadow: 3px 3px 8px rgba(0, 0, 0, 0.3);  /* Agrega sombra al cuadro de selección */
    }
</style>
"""

# Insertar el CSS en la aplicación
st.markdown(page_bg_css, unsafe_allow_html=True)

# Añadir el título en el contenedor negro
header_html = """
<div class="header-container">
    <b>BioBackHack</b>
</div>
"""
st.markdown(header_html, unsafe_allow_html=True)

# Descripción de la aplicación
st.markdown("**Revoluciona tu bienestar, hackea tu biología**")


# Añadir lista de desplegables
options = ["Enterococcus faecium", "Staphylococcus aureus", "Klebsiella pneumoniae", 
           "Acinetobacter baumannii", "Pseudomonas aeruginosa", "Enterobacter species"]
selection = st.selectbox("Selecciona una opción:", options)

# Mostrar la selección
st.write(f'**Seleccionaste:** {selection}')

# Creación del DataFrame
df = pd.DataFrame({
    'números': [1, 2, 3, 4],
    'cuadrados': [1, 4, 9, 16]
})
# Mostrar el DataFrame con un label
st.markdown("**Aquí hay un DataFrame:**")
st.write(df)

# Mostrar gráfico de líneas del DataFrame con un label

st.markdown("**Gráfica de resultados**")
st.line_chart(df)
