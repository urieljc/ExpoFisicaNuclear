import streamlit as st
from PIL import Image
import base64
from streamlit_lottie import st_lottie
from paginas.cosmicos import load_lottiefile
import networkx as nx
import matplotlib.pyplot as plt
from streamlit_d3graph import d3graph
import tensorflow as tf
from keras.preprocessing import image
import numpy as np
from translate import Translator

def app():
    st.title("Machine Learnig",anchor=False)
    img_machine=Image.open('img/machineLogo.jpg')
    st.image(img_machine)
    st.subheader("Que es Machine Learning")
    st.write("El aprendizaje automático, o machine learning en inglés, es un subcampo de la inteligencia artificial que se centra en el desarrollo de algoritmos y modelos que permiten a las computadoras aprender y mejorar automáticamente a partir de datos sin ser programadas explícitamente para realizar una tarea específica. El objetivo principal del aprendizaje automático es permitir a las máquinas aprender patrones y tomar decisiones basadas en datos, sin intervención humana directa.")
    st.write("El aprendizaje automático implica el estudio y la construcción de algoritmos y modelos estadísticos que pueden analizar datos y aprender a realizar tareas específicas, como reconocimiento de patrones, clasificación, predicción y toma de decisiones. Estos algoritmos pueden adaptarse y mejorar continuamente a medida que se les proporciona más información o datos de entrenamiento.")
    with st.container():
        with st.expander("Aprendizaje supervisado"):
            st.write("Se proporcionan conjuntos de datos etiquetados para entrenar al algoritmo, que luego puede predecir o clasificar nuevas instancias en función de los patrones aprendidos.")
        with st.expander("Aprendizaje no supervisado"):
            st.write(" El algoritmo se entrena en conjuntos de datos no etiquetados, lo que le permite descubrir patrones y estructuras ocultas en los datos sin una orientación específica.")
        with st.expander("Aprendizaje por refuerzo"):
            st.write(" El algoritmo aprende a tomar decisiones en un entorno específico para maximizar una recompensa acumulada, utilizando un proceso de prueba y error y retroalimentación del entorno")
    st.subheader("Diferencias entre IA, Machine Learning, Deep Learning")
    with st.container():
        img_diferencias=Image.open('img/diferencias.webp')
        st.image(img_diferencias)
        st.write("Inteligencia Artificial (IA): La IA se refiere al campo de la informática que se ocupa de la creación de sistemas y programas capaces de realizar tareas que normalmente requieren inteligencia humana. La IA se enfoca en la simulación de procesos de pensamiento humano y la toma de decisiones a través de algoritmos y sistemas automatizados.")
        st.write("Aprendizaje Automático (Machine Learning): El aprendizaje automático es un subconjunto de la IA que implica el estudio de algoritmos y modelos que permiten a las computadoras aprender y mejorar su rendimiento en una tarea específica a partir de datos, sin una programación explícita. El aprendizaje automático se basa en la identificación de patrones y la toma de decisiones basada en datos.")
        st.write("Aprendizaje Profundo (Deep Learning): El aprendizaje profundo es un subcampo del aprendizaje automático que utiliza redes neuronales artificiales con múltiples capas para modelar y analizar datos de manera similar a como lo hace el cerebro humano. El aprendizaje profundo es capaz de extraer características complejas y abstractas de conjuntos de datos, lo que lo hace especialmente efectivo en tareas como reconocimiento de imágenes y procesamiento del lenguaje natural.")
        
        file_=open("img/red_neuronal.gif","rb")
        content=file_.read()
        data_url=base64.b64encode(content).decode("utf-8")
        file_.close()
        st.markdown(
                f'<img src="data:image/gif;base64,{data_url}" >',unsafe_allow_html=True
        )
      
    
    st.subheader("Uso de Machine Learning en Fisica de particulas")
    datos=load_lottiefile("animations/datos.json")
    st_lottie(datos,height=500)
    st.write("El aprendizaje automático (machine learning) ha encontrado aplicaciones importantes en diversas áreas de la física, ayudando a los investigadores a abordar problemas complejos y a extraer conocimientos útiles de conjuntos de datos masivos. Aquí hay algunas áreas específicas en las que el aprendizaje automático se ha utilizado en la física:")
    with st.expander("Identificación de Partículas"):
        st.write(" El aprendizaje automático se utiliza para identificar y clasificar partículas subatómicas en colisiones de alta energía, ayudando a los físicos a distinguir y rastrear la firma de diferentes partículas en detectores de colisionadores como el Gran Colisionador de Hadrones (LHC).")
    with st.expander("Análisis de Datos de Detectores"):
        st.write("El aprendizaje automático se aplica en el análisis de grandes conjuntos de datos generados por detectores de partículas, ayudando a filtrar y procesar datos para identificar señales de interés y reducir el ruido de fondo, lo que permite un análisis más preciso de fenómenos físicos.")
    with st.expander("Generación de Eventos Simulados"):
        st.write(" El aprendizaje automático se utiliza para simular eventos de colisión de partículas y generar conjuntos de datos simulados para comprender y predecir resultados experimentales en entornos controlados, lo que ayuda a mejorar la precisión de los modelos teóricos y experimentales.")
    with st.expander("Optimización de Experimentos"):
        st.write(" El aprendizaje automático se aplica para optimizar y mejorar el diseño de experimentos en física de partículas, ayudando a los investigadores a identificar configuraciones óptimas de detectores y estrategias de detección para maximizar la detección de partículas y la recopilación de datos.")
    with st.expander("Búsquedas de Nuevas Partículas"):
        st.write(" El aprendizaje automático se utiliza para analizar grandes conjuntos de datos en busca de señales de partículas y fenómenos físicos no descubiertos, lo que ayuda a guiar la investigación y el descubrimiento de nuevas partículas y procesos fundamentales en el ámbito de la física de partículas.")
    
    st.subheader("Algoritmos de Machine Learning Propuestos por el articulo")
    with st.container():
        file_=open("img/universo.gif","rb")
        content=file_.read()
        data_url=base64.b64encode(content).decode("utf-8")
        file_.close()
        st.markdown(
                f'<img src="data:image/gif;base64,{data_url}" width="500" height="400">',unsafe_allow_html=True
        )
        st.subheader("Boosted Decision Trees")
        img_arbol=Image.open('img/arbolDesicion.png')
        st.image(img_arbol)
        st.write("Boosted Decision Trees, también conocidos como árboles de decisión potenciados, es un algoritmo de aprendizaje automático que se utiliza para problemas de regresión y clasificación. Es una técnica de ensamblaje que combina múltiples modelos de árboles de decisión débiles para formar un modelo más fuerte y robusto. Este enfoque se basa en la idea de construir una secuencia de modelos de aprendizaje débil, cada uno de los cuales se enfoca en corregir los errores del modelo anterior.")
        st.subheader(" Graph Neural Networks (GNNs")
        file_=open("img/gcn.gif","rb")
        content=file_.read()
        data_url=base64.b64encode(content).decode("utf-8")
        file_.close()
        st.markdown(
                f'<img src="data:image/gif;base64,{data_url}" width="500" height="400">',unsafe_allow_html=True
        )
        st.write("Las Graph Neural Networks (GNNs) son una clase de modelos de aprendizaje automático diseñados para el análisis de datos estructurados en forma de gráficos o redes. A diferencia de las redes neuronales convencionales que operan en datos tabulares o secuenciales, las GNNs están especialmente diseñadas para capturar las interacciones y relaciones complejas presentes en datos de tipo grafo, como redes sociales, redes de conocimiento, interacciones de proteínas y moléculas, entre otros.")
        st.subheader("Graph Convolutional Networks (GCNs)")
        img_convolucinal=Image.open('img/graphConvolucional.png')
        st.image(img_convolucinal)
        st.write("Las Graph Convolutional Networks (GCNs) son un tipo de arquitectura de redes neuronales diseñadas específicamente para trabajar con datos de tipo grafo. Estas redes son capaces de procesar datos estructurados en forma de grafo, como redes sociales, interacciones moleculares y otros tipos de relaciones complejas. A diferencia de las redes convencionales, las GCNs pueden realizar operaciones convolucionales directamente en grafos, lo que les permite capturar patrones y características importantes de los nodos y aristas en el grafo.")
    
    # Crear un grafo
    G = nx.erdos_renyi_graph(20, 0.1)

    # Añadir algunos atributos a los nodos
    for i in G.nodes:
        G.nodes[i]['label'] = f'Node {i}'

    # Visualizar el grafo en Streamlit
    pos = nx.spring_layout(G, seed=42)  # Layout del grafo

    # Dibujar el grafo
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=8, font_color='black', font_weight='bold')
    st.pyplot(plt)
    
    d3 = d3graph()
    # Load karate example
    adjmat, df = d3.import_example('karate')

    d3.graph(adjmat)
    d3.set_node_properties(color=df['label'].values)
    d3.show()

    
    file_=open("img/CNN.gif","rb")
    content=file_.read()
    data_url=base64.b64encode(content).decode("utf-8")
    file_.close()
    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" width="500" height="400">',unsafe_allow_html=True
    )
    st.subheader("Ejemplo de Red Convolucional")
    
    # Cargar el modelo pre-entrenado de TensorFlow
    model = tf.keras.applications.MobileNetV2(weights='imagenet')

    # Función para preprocesar la imagen
    def preprocess_img(img):
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        return tf.keras.applications.mobilenet_v2.preprocess_input(img)

    # Función para predecir la clase de la imagen
    def predict_img(img):
        img = preprocess_img(img)
        predictions = model.predict(img)
        return tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=1)[0][0][1]

    # Función para traducir el resultado a español
    def translate_to_spanish(text):
        translator = Translator(to_lang="es")
        translation = translator.translate(text)
        return translation

    # Interfaz de usuario de Streamlit
    st.write('Cargue una imagen para predecir su clase')

    uploaded_img = st.file_uploader("Cargar imagen", type=['png', 'jpg', 'jpeg'])

    if uploaded_img is not None:
        img = image.load_img(uploaded_img, target_size=(224, 224))
        st.image(img, caption='Imagen Cargada', use_column_width=True)
        pred = predict_img(img)
        pred_translation = translate_to_spanish(pred)
        st.write(f'Predicción: {pred_translation}')