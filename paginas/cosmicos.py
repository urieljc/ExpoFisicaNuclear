#importacion de librerias a utilizar
import streamlit as st
import base64
from streamlit_lottie import st_lottie
import json
import plotly.graph_objects as go

def load_lottiefile(filepath:str):
            with open(filepath,"r")as f:
                return json.load(f)


def app():
    with st.container():
            st.header("Radiacion",anchor=False)
            radiacion=load_lottiefile("animations/radiacion.json")
            st_lottie(radiacion,height=300)
            st.write("La radiación es la emisión, propagación y transferencia de energía en cualquier medio en forma de ondas electromagnéticas o partículas. Estamos expuestos a ella en nuestra vida cotidiana. Entre las fuentes de radiación más conocidas se encuentran el sol, los hornos de microondas de nuestras cocinas y las radios que escuchamos en nuestros automóviles.")
            with st.expander("Clasificacion de la Radiacion"):
                st.write("Radiación no ionizante: No tienen la suficiente energía como para romper los enlaces que unen los átomos del medio que irradian (ondas de radio y TV, microondas, luz visible, etc.)")
                st.write("Radiación ionizante: Tienen suficiente energía como para producir ionizaciones de los átomos del medio o materia que es irradiado. Van desde los rayos X hasta la radiación cósmica.")
    
    with st.container():
        st.header("Radiacion Cosmica",anchor=False)
        file_=open("img/estrella.gif","rb")
        content=file_.read()
        data_url=base64.b64encode(content).decode("utf-8")
        file_.close()
        
        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" >',unsafe_allow_html=True
        )
        st.write("La radiación cósmica es radiación ionizante que consiste en partículas de alta energía, primariamente núcleos de átomos, de origen más allá de la Tierra, y partículas generadas por la interacción con la atmósfera. La radiación cósmica primaria proviene del espacio y del Sol.La radiación cósmica secundaria abarca partículas que son creadas directamente o en reacciones en cascada entre la radiación cósmica primaria y la atmosfera. Las partículas importantes que se generan son neutrones, protones, fotones, electrones, positrones, muones y piones.")
        with st.expander("Mas sobre radiacion cosmica"):
            st.write("La radiación cósmica está compuesta por diversas partículas subatómicas que provienen del espacio exterior, incluyendo el Sol, otras estrellas, supernovas y otras fuentes celestes. Estas partículas pueden ser de origen primario, directamente emitidas por fuentes cósmicas, o de origen secundario, que son partículas generadas cuando las partículas primarias interactúan con la materia en el espacio o la atmósfera de la Tierra.")
            st.write("La radiación cósmica de fondo es una forma de radiación electromagnética que llena el universo y es remanente del Big Bang, el evento que se cree marcó el inicio del universo tal como lo conocemos. Esta radiación es uno de los principales pilares de la teoría del Big Bang y proporciona importantes evidencias sobre la naturaleza y la evolución del cosmos. Se emitió aproximadamente 380,000 años después del Big Bang, cuando el universo se enfrió lo suficiente como para que los electrones pudieran unirse a los núcleos atómicos, formando átomos estables. Antes de este punto, el universo estaba tan caliente y denso que los electrones y protones estaban libres, y formaban un plasma caliente y opaco que impedía que la luz viajara libremente.")
            st.write("Por otro lado se encuentra la radiación cósmica, que es una forma de radiación electromagnética y de partículas que proviene del espacio exterior, más allá de nuestra atmósfera terrestre. Esta radiación está compuesta por diversas partículas cargadas, como electrones, protones y núcleos atómicos, que viajan a altas velocidades y energías a través del espacio.")
            st.write("Rayos cósmicos primarios: Estos son protones, núcleos de helio y otros núcleos atómicos más pesados que son acelerados a velocidades cercanas a la velocidad de la luz por eventos violentos en el espacio, como supernovas o agujeros negros. Estas partículas cargadas son las que constituyen la mayor parte de la radiación cósmica. Rayos gamma: Son fotones de alta energía liberados en procesos nucleares extremadamente violentos, como explosiones de supernovas, colisiones de partículas aceleradas y otros eventos cósmicos energéticos.Partículas secundarias: Cuando los rayos cósmicos primarios interactúan con la atmósfera terrestre, producen una cascada de partículas secundarias, como muones, electrones y positrones. Estas partículas secundarias pueden llegar a la superficie de la Tierra y son una parte importante de la radiación cósmica que experimentamos en la superficie. Radiación electromagnética: Además de los rayos gamma, la radiación cósmica también incluye otras formas de radiación electromagnética, como la radiación ultravioleta, la radiación infrarroja y la radiación de radio, provenientes de diversas fuentes en el espacio. La composición exacta y la energía de estas partículas pueden variar significativamente, dependiendo de su origen y de su trayectoria a través del espacio.")
        st.write("La radiación cósmica es de particular interés en la investigación espacial y la exploración del universo, ya que puede tener efectos en la salud de los astronautas, en la operación de equipos electrónicos y en la formación de nubes de partículas en el espacio. También es relevante para la comprensión de la evolución y la estructura del universo, así como para estudiar fenómenos astrofísicos como las estrellas de neutrones, los agujeros negros y las galaxias activas.La radiación cósmica es uno de los factores que los astronautas y las misiones espaciales deben tomar en cuenta, cuando se diseñan las naves y los trajes espaciales, pero sobre todo, en sus posibles efectos en la salud.")
    
    with st.container():
        
        nuclear=load_lottiefile("animations/animation_lnqrrf01.json")
        ondas=load_lottiefile("animations\ondas.json")
        st.header("Tipos de Radiacion")
        st_lottie(ondas,height=500)
        st_lottie(nuclear,height=500)
        col1,col2,col3,col4=st.columns(4)
        with col1:
            with st.expander("Alfa"):
                st.write("La radiación alfa, los núcleos liberan partículas pesadas con carga positiva para hacerse más estables. Estas partículas no pueden penetrar nuestra piel y causar daño. Muchas veces basta con utilizar una simple hoja de papel para detener su paso. Sin embargo, si ingerimos o inhalamos un material que emite partículas alfa, nuestros tejidos internos pueden quedar expuestos directamente a este tipo de radiación y, en ese caso, ponemos en riesgo nuestra salud")
        with col2:
            with st.expander("Beta"):
                st.write("La radiación beta, los núcleos liberan partículas más pequeñas (electrones), más penetrantes que las partículas alfa y que pueden atravesar, entre otras cosas, 1 o 2 centímetros de agua, en función de su energía. Por lo general, podríamos detener el paso de la radiación beta con una lámina de aluminio de unos cuantos milímetros de espesor.")
        with col3:
            with st.expander("Gamma"):
                st.write("Los rayos gamma son un tipo de radiación electromagnética, similar a los rayos X. Algunos tipos de rayos gamma atraviesan el cuerpo humano sin causar daño, pero, en otras ocasiones estos rayos son absorbidos por el organismo y pueden ser perjudiciales. La intensidad de los rayos gamma puede reducirse a valores que entrañen menos riesgos mediante el uso de paredes gruesas de hormigón o plomo. Ese es el motivo por el cual las salas de radioterapia de los hospitales, en las que se trata a los pacientes con cáncer, tienen paredes tan gruesas")
        with col4:
            with st.expander("Neutrones"):
                st.write("Los neutrones son partículas relativamente grandes y uno de los principales componentes del núcleo atómico. No poseen carga y, por ende, no producen ionización directamente. No obstante, su interacción con los átomos de la materia puede hacer surgir rayos alfa, beta, gamma o X, que sí producen ionización. Los neutrones son penetrantes y solo puede detenérseles con grandes volúmenes de concreto, agua o parafina. Los neutrones pueden producirse de diferentes maneras, por ejemplo, dentro de los reactores nucleares o en las reacciones nucleares desencadenadas por partículas de alta energía en los haces de los aceleradores. Los neutrones pueden representar una fuente considerable de radiación indirectamente ionizante.")
                # Definir los datos para diferentes tipos de ondas
        frecuencias = ['Radio', 'Microondas', 'Infrarrojo', 'Visible', 'Ultravioleta', 'Rayos X', 'Rayos Gamma']
        longitudes = [10, 5, 3, 2, 1.5, 0.1, 0.01]  # Ejemplo de longitudes de onda en unidades arbitrarias

        # Crear gráfico de líneas
        fig = go.Figure(data=go.Scatter(x=frecuencias, y=longitudes, mode='lines+markers'))

        # Establecer el diseño y las etiquetas
        fig.update_layout(title='Tipos de Ondas Electromagnéticas',
                        xaxis_title='Frecuencias',
                        yaxis_title='Longitudes de Onda')

        # Mostrar el gráfico en Streamlit
        st.plotly_chart(fig)
        
        # Definir un diccionario con las características de diferentes partículas cósmicas
        particulas_cosmicas = {
            'Rayos Alfa': {
                'Carga': '+2',
                'Masa': '4 u',
                'Interacción': 'Baja penetración'
            },
            'Rayos Beta': {
                'Carga': '-1',
                'Masa': 'Muy pequeña',
                'Interacción': 'Penetra más que rayos alfa'
            },
            'Rayos Gamma': {
                'Carga': '0',
                'Masa': '0',
                'Interacción': 'Alta penetración, ionización'
            }
        }

        # Obtener la selección del usuario
        seleccion = st.selectbox('Seleccione el tipo de partícula cósmica:', list(particulas_cosmicas.keys()))

        # Mostrar las características correspondientes a la selección del usuario
        if seleccion:
            st.write(f"Características de {seleccion}:")
            st.write(f"- Carga: {particulas_cosmicas[seleccion]['Carga']}")
            st.write(f"- Masa: {particulas_cosmicas[seleccion]['Masa']}")
            st.write(f"- Interacción: {particulas_cosmicas[seleccion]['Interacción']}")
        
        
        

