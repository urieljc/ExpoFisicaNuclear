import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import math
import base64

def app():
    st.title("Detector de Agua Cherenkov",anchor=False)
    video_file = open('animations/cherenkov.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    st.write("El detector Cherenkov es un detector de partículas que utiliza el umbral de velocidad para la producción de luz, la salida de luz dependiente de la velocidad o la dirección de la luz dependiente de la velocidad de la radiación Cherenkov, y tiene como finalidad registrar la caída de rayos cósmicos. Se basa en el llamado efecto Cherenkov (en honor a Pável Cherenkov, Premio Nobel de Física en 1958, por haberlo descubierto). Éste se produce cuando una partícula cargada se mueve en un medio transparente con velocidad mayor que la que tendría la luz en dicho medio. En esta situación se produce una perturbación electromagnética que origina una emisión de luz, análogamente a como un barco rápido crea una estela al navegar en aguas en reposo. La luz de la partícula resulta emitida dentro de los límites de una superficie de forma cónica, donde el vértice es el punto en que la partícula entró al detector y la directriz es la dirección de su movimiento. Un tanque de agua hermético y oscuro resulta un buen detector del rastro de la partícula si se le adicionan fotomultiplicadores.")
    
    st.subheader("Radiacion Cherenkov",anchor=False)
    img_cherenkov=Image.open('img/radiacion_cherenkov.jpeg')
    st.image(img_cherenkov)
    st.write("La radiación Cherenkov es un fenómeno óptico que ocurre cuando una partícula cargada, como un electrón, se mueve a través de un medio dieléctrico a una velocidad mayor que la velocidad de la luz en ese medio. Este fenómeno fue descubierto y explicado por primera vez por el físico soviético Pavel Cherenkov en 1934, quien recibió el Premio Nobel de Física en 1958 por este descubrimiento. Cuando una partícula cargada atraviesa un medio dieléctrico a una velocidad mayor que la de la luz en ese medio, genera una onda electromagnética de tipo radiación Cherenkov. Esta radiación es similar a una onda de choque óptica y se manifiesta como un cono de luz azul pálida que emana en un ángulo característico con respecto a la dirección de la partícula cargada. La apertura del cono y la intensidad de la radiación Cherenkov dependen del índice de refracción del medio y de la velocidad relativa de la partícula con respecto a la velocidad de la luz en el vacío. La radiación Cherenkov se utiliza en diversas aplicaciones científicas y tecnológicas, como en la detección de partículas subatómicas en detectores de radiación Cherenkov, así como en la industria nuclear y en la medicina para el diagnóstico y el tratamiento de enfermedades.")
    st.write("La fórmula de la radiación Cherenkov describe la apertura del cono de luz (ángulo Cherenkov) y se basa en el índice de refracción del medio, la velocidad de la partícula cargada y la velocidad de la luz en el vacío. La fórmula general es la siguiente:")
    st.latex(r''' \cos(\Theta_C) = \frac{c}{n*v} ''')
    st.write("Donde:")
    with st.container():
        col1,col2=st.columns(2)
        with col1:
            st.latex(r'''\Theta_C  ''')
            st.write("")
            st.write("")
            st.write("")
            st.divider()
        with col2:
            st.write("es el ángulo Cherenkov (el ángulo entre la dirección de la partícula cargada y la dirección de emisión de la radiación Cherenkov).")
            st.divider()
        with col1:
            st.latex(r'''c''')
            st.write("")
            st.divider()
        with col2:
            st.write(" es la velocidad de la luz en el vacío (aproximadamente 3*10^8 metros por segundo).")
            st.divider()
        with col1:
            st.latex(r'''n''')
            st.divider()
        with col2:
            st.write(" es el índice de refracción del medio en el que se encuentra la partícula cargada")
            st.divider()
        with col1:
            st.latex(r'''v''')
            st.divider()
        with col2:
            st.write(" es la velocidad de la partícula cargada.")
            st.divider()
        st.write("Esta fórmula describe cómo el ángulo Cherenkov depende del índice de refracción del medio (n) y de la velocidad de la partícula cargada (v) en relación con la velocidad de la luz en el vacío (c). Cuando la velocidad de la partícula (v) es mayor que la velocidad de la luz en el medio (c/n), se genera radiación Cherenkov en forma de un cono de luz con un ángulo .")
        
        img_cherenkov=Image.open('img/cherenkov_draw.sp.gif')
        st.image(img_cherenkov)
        
    st.subheader('Cálculo del Ángulo Cherenkov',anchor=False)

    # Definir un control deslizante para el índice de refracción del medio
    n = st.slider('Índice de Refracción (n)', 1.0, 2.0, 1.5, 0.01)

    # Definir un control deslizante para la velocidad de la partícula
    v = st.slider('Velocidad de la Partícula (v) (m/s)', 0.0, 3e8, 2e8, 1e6)

    # Calcular el ángulo Cherenkov utilizando la fórmula
    c = 3e8  # Velocidad de la luz en el vacío en m/s
    theta_c = np.arccos(c / (n * v))

    # Convertir el ángulo a grados
    theta_c_degrees = math.degrees(theta_c)

    # Mostrar el ángulo Cherenkov
    st.write(f'Ángulo Cherenkov: {theta_c_degrees} grados')


    # Calcular el rango de ángulos
    theta = np.linspace(0, 2 * np.pi, 100)

    # Calcular el ángulo crítico de Cherenkov
    theta_c = np.arccos(c / (n * v))

    # Calcular la intensidad de Cherenkov en función del ángulo
    I = np.where(theta <= theta_c, np.sin(theta), 0)  # noqa: E741

    # Crear el gráfico con Matplotlib
    fig, ax = plt.subplots()
    ax.plot(theta, I, label='Intensidad de Cherenkov', color='b')
    ax.axvline(x=theta_c, color='r', linestyle='--', label='Ángulo crítico de Cherenkov')
    ax.set_xlabel('Ángulo (radianes)')
    ax.set_ylabel('Intensidad')
    ax.set_title('Radiación de Cherenkov')
    ax.legend()

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)

    st.subheader('Cono de Luz de Cherenkov en Streamlit',anchor=False)

    # Definir el rango de ángulos para el cono
    theta = np.linspace(0, 2 * np.pi, 100)

    # Definir el ángulo crítico de Cherenkov
    theta_c_degrees = st.slider('Ángulo crítico de Cherenkov (grados)', 0, 90, 45)

    # Convertir el ángulo crítico a radianes
    theta_c = np.radians(theta_c_degrees)

    # Calcular la intensidad de Cherenkov en función del ángulo
    intensity = np.where(theta <= theta_c, np.sin(theta), 0)

    # Crear el gráfico con Matplotlib
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta, intensity, label='Intensidad de Cherenkov', color='b')
    ax.fill_between(theta, 0, intensity, color='lightblue')
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    ax.set_rlabel_position(180)
    ax.set_title('Cono de Luz de Cherenkov', va='bottom')

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)

    file_=open("img/cherenkov.gif","rb")
    content=file_.read()
    data_url=base64.b64encode(content).decode("utf-8")
    file_.close()
    st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" >',unsafe_allow_html=True
    )
