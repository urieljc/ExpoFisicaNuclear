import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def app():
    st.title("Desarrollo del Machine Learning",anchor=False)
    with st.container():
        st.subheader("Analisis de los Datos",anchor=False)
        st.write("Lectura de datos")
        # Cargar un archivo CSV
        file_path = 'doc\cosmic_ray_datasets_part2.csv'
        if file_path is not None:
            data = pd.read_csv(file_path)
            num_elements = data.count()
            data['Event'] = data.index + 1
            # Mostrar los datos
            st.write("Datos cargados:")
            st.write(data)
            
            # Mostrar los nombres de las columnas
            st.write("Nombres de las columnas:")
            st.write(list(data.columns))
            
            # Verificar si existen valores nulos
            st.write("¿Existen valores nulos?")
            st.write(data.isnull().values.any())

            # Mostrar los tipos de valores en las columnas
            st.write("Tipos de valores de las columnas:")
            st.write(data.dtypes)

            # Realizar análisis básico
            st.write("Resumen estadístico:")
            st.write(data.describe())
            
            # Graficar la distribución de los neutrones en comparación con otras partículas
            fig = px.scatter(data, x="Event", y=["Neutrons Effective Dose (uSv/year)","Proton Effective Dose (uSv/year)", "He ion Effective Dose (uSv/year)","Meuon+ Effective Dose (uSv/year)", "Muon- Effective Dose (uSv/year)","Electron Effective Dose (uSv/year)", "Positron Effective Dose (uSv/year)","Photon Effective Dose (uSv/year)", "Other ions Effective Dose (uSv/year)"], title="Distribución de Neutrones en Comparación con Otras Partículas")
            st.plotly_chart(fig)
            
            # Graficar los datos de Neutrons Effective Dose en Plotly y mostrar en Streamlit
            fig = px.scatter(data, x='X', y='Y', color='Neutrons Effective Dose (uSv/year)', 
                            title='Gráfico de dispersión de Neutrons Effective Dose en función de X y Y')
            st.plotly_chart(fig)
            
            # Crear el mapa de calor de intensidad con Plotly
            fig = px.density_heatmap(data, x="X", y="Y", z="Neutrons Effective Dose (uSv/year)", title="Mapa de Calor de Intensidad de Neutrones")
            st.plotly_chart(fig)
            
            # Normalizar los datos
            scaler = MinMaxScaler()
            scaled_data = pd.DataFrame(scaler.fit_transform(data.iloc[:, 2:4]), columns=data.columns[2:4])

            # Añadir la columna 'Event' al conjunto de datos normalizado
            scaled_data['Event'] = data.index + 1

            # Mostrar los datos normalizados
            st.write("Datos normalizados:")
            st.write(scaled_data)

            # Crear la curva con Plotly
            fig = px.line(scaled_data, x='Event', y=['Total Effective Dose (uSv/year)', 'Neutrons Effective Dose (uSv/year)'], title="Curva de Intensidad Normalizada")
            st.plotly_chart(fig)

    # Crear un nuevo DataFrame para las tablas necesarias para neutrones
    neutron_data = data[['Neutrons Effective Dose (uSv/year)']].copy()
    umbral=50
    # Calcular la presencia de radiación basada en la dosis efectiva de neutrones
    neutron_data['Radiación'] = neutron_data['Neutrons Effective Dose (uSv/year)'].apply(lambda x: 1 if x > umbral else 0)  # Ajusta 'umbral' según sea necesario

    # Dividir los datos en características (X) y etiquetas (y)
    X = neutron_data.drop(columns=['Radiación'])
    y = neutron_data['Radiación']

    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Crear un modelo de clasificación (Random Forest)
    model = RandomForestClassifier(n_estimators=100, random_state=42)

    # Entrenar el modelo
    model.fit(X_train, y_train)

    # Interfaz de usuario de Streamlit
    st.subheader('Predicción de Radiación basada en Dosis de Neutrones')
    st.write('Ingrese la dosis efectiva de neutrones para predecir si hay radiación.')

    neutron_dose = st.number_input('Dosis de Neutrones (uSv)', value=0.0)

    if st.button('Predecir'):
        # Predecir si hay radiación
        prediction = model.predict([[neutron_dose]])

        if prediction[0] == 1:
            st.write('Habrá radiación.')
        else:
            st.write('No habrá radiación.')

    # Opcional: Calcular la precisión del modelo en el conjunto de prueba
    # y_pred = model.predict(X_test)
    # accuracy = accuracy_score(y_test, y_pred)
    # st.write(f'Precisión del modelo en el conjunto de prueba: {accuracy:.2f}')