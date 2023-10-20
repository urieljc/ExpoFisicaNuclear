# pagina donde se muestra las caracteristicas del proyecto

#importacion de librerias a utilizar
import json
import streamlit as st
from pdf2image import convert_from_path
from streamlit_lottie import st_lottie
import streamlit_scrollable_textbox as stx

def app():
    def load_lottiefile(filepath:str):
        with open(filepath,"r")as f:
            return json.load(f)
    nuclear=load_lottiefile("animations/animation_lnqicyrw.json")
    st_lottie(nuclear,height=200)
    st.title("Using Machine Learning to Improve Neutron Identiﬁcation in Water Cherenkov Detectors")  # noqa: E501
    st.header("Uso del Machine Learning para mejorar la identificación de neutrones en detectores de agua Cherenkov ",anchor=False)  # noqa: E501
    st.subheader("Univ: Bazan Panozo Juan Carlos",anchor=False)
    with st.container():
        st.subheader("Aticulo: ",anchor=False)
        
        pdf_path = "doc/Juan_Bazan.pdf"

        # Función para mostrar las páginas del PDF como imágenes
        def render_pdf(pdf_path):
            images = convert_from_path(pdf_path)
            return images

        # Mostrar el PDF
        images = render_pdf(pdf_path)
        if images:
            page_number = st.slider('Selecciona una página', 1, len(images), 1)
            st.image(images[page_number - 1], caption=f"Página {page_number}", use_column_width=True)  # noqa: E501
        
    with st.container():
        st.subheader("Resumen del Articulo",anchor=False)
        stx.scrollableTextbox("Los detectores de agua Cherenkov, como Super-Kamiokande y la próxima generación de Hyper-Kamiokande, añaden gadolinio al agua para mejorar la detección de neutrones. Al detectar neutrones además de los leptones en las interacciones de neutrinos, cabe esperar una mejor separación entre neutrinos y antineutrinos, así como una reducción de los fondos en las búsquedas de desintegración de protones. La señal de neutrones en sí sigue siendo pequeña y puede confundirse con la espalación de muones y otras fuentes de fondo. En este trabajo se emplean técnicas de aprendizaje automático para optimizar la capacidad de detección de captura de neutrones en el nuevo detector Cherenkov de agua intermedia (IWCD) para Hyper-K. En particular, se desarrollan y comparan modelos de árboles de decisión potenciados (XGBoost), redes convolucionales gráficas (GCN) y redes neuronales convolucionales gráficas dinámicas (DGCNN) con un enfoque basado en la probabilidad estadística. y se comparan con un enfoque estadístico basado en la verosimilitud, logrando un aumento de hasta el 10% en la precisión de la clasificación. También se diseñan rasgos característicos a partir de los conjuntos de datos y se analizan mediante SHAP (SHapley Additive exPlanations) para conocer los factores clave que influyen en los resultados de los tipos de sucesos. El conjunto de datos utilizado en esta investigación consistió en aproximadamente 1,6 millones de eventos simulados de cañones de partículas, divididos casi por igual entre la captura de neutrones y una fuente de electrones de fondo.",height=300)  # noqa: E501
    
            