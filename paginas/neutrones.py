import streamlit as st
import base64
from streamlit_lottie import st_lottie
import json
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from scipy.integrate import solve_ivp
from astropy import constants as const
from PIL import Image
import plotly.express as px
import pandas as pd
from astropy import units as u
from astropy.time import Time
import time

def load_lottiefile(filepath:str):
            with open(filepath,"r")as f:
                return json.load(f)
def app():
        st.title("Neutrones de los Rayos Cosmicos")
        file_=open("img/neutrones.gif","rb")
        content=file_.read()
        data_url=base64.b64encode(content).decode("utf-8")
        file_.close()
        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" >',unsafe_allow_html=True
        )
        st.write("Los neutrones son una de las partículas que pueden ser producidas como resultado de la interacción de los rayos cósmicos con la atmósfera terrestre. Cuando los rayos cósmicos primarios, que generalmente consisten en núcleos atómicos altamente energéticos, chocan con los átomos en la atmósfera terrestre, pueden generar una cascada de partículas secundarias, que incluyen neutrones, entre otros. Estos neutrones secundarios pueden ser generados principalmente a través de dos procesos principales: Espalación nuclear: Durante la interacción de los rayos cósmicos con los núcleos de los átomos en la atmósfera, puede producirse la espalación nuclear, que implica el intercambio de energía entre los núcleos y la generación de nuevas partículas, como neutrones, protones y otros hadrones. Desintegración de partículas secundarias: Algunas de las partículas secundarias generadas en la cascada de partículas, como los piones, pueden desintegrarse en partículas adicionales, incluyendo neutrones, como parte de su proceso de decaimiento. Estos neutrones producidos por los rayos cósmicos en la atmósfera pueden ser detectados y estudiados para comprender mejor la naturaleza de la radiación cósmica y sus interacciones con la materia. El estudio de la radiación cósmica y los neutrones producidos por ella es importante no solo para la física de partículas, sino también para la investigación en meteorología y en la protección contra la radiación en la aviación y la exploración espacial.")
        radiacion=load_lottiefile("animations/sol.json")
        st_lottie(radiacion,height=300)
        image = Image.open('img/rayo_cosmico.jpg')
        st.image(image)
        
        video_file = open('animations/disentegracion.mp4', 'rb')
        video_bytes = video_file.read()

        st.video(video_bytes)
        
        # Generar datos de rayos cósmicos con Astropy
        time_range = np.linspace(0, 24, 100) * u.hour
        cosmic_ray_data = np.random.uniform(0, 100, size=len(time_range))

        # Crear la figura con Plotly
        fig = go.Figure()

        # Agregar los datos de rayos cósmicos al gráfico
        fig.add_trace(go.Scatter(x=time_range, y=cosmic_ray_data, mode='lines', name='Rayos Cósmicos'))

        # Configurar el diseño y las etiquetas
        fig.update_layout(title='Datos de Rayos Cósmicos Generados por Astropy',
                        xaxis_title='Tiempo (horas)',
                        yaxis_title='Intensidad de Rayos Cósmicos')

        # Mostrar el gráfico en Streamlit
        st.plotly_chart(fig)
        
        