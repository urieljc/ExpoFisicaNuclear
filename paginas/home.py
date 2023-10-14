# pagina donde se muestra las caracteristicas del proyecto

#importacion de librerias a utilizar
import json
import streamlit as st
from pdf2image import convert_from_path
from streamlit_lottie import st_lottie
def app():
    def load_lottiefile(filepath:str):
        with open(filepath,"r")as f:
            return json.load(f)
    nuclear=load_lottiefile("animations/animation_lnqicyrw.json")
    st_lottie(nuclear,height=200)
    st.title("Presentacion de proyecto")
    st.header("titulo del articulo",anchor=False)
    st.subheader("titulo tradicido del articulo",anchor=False)
    with st.container():
        st.subheader("aqui se muestra el pdf",anchor=False)
        
        pdf_path = "doc/Juan_Bazan.pdf"

        # Función para mostrar las páginas del PDF como imágenes
        def render_pdf(pdf_path):
            images = convert_from_path(pdf_path)
            return images

        # Mostrar el PDF
        images = render_pdf(pdf_path)
        if images:
            page_number = st.slider('Selecciona una página', 1, len(images), 1)
            st.image(images[page_number - 1], caption=f"Página {page_number}", use_column_width=True)
        
    with st.container():
        st.subheader("Resumen del Articulo",anchor=False)
        st.write("resumen del articulo")
    
            