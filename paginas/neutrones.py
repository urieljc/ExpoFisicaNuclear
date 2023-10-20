# Definir los tipos de neutrones y sus propiedades
        tipos_neutrones = ['Neutrón libre', 'Neutrón térmico', 'Neutrón rápido', 'Neutrón epitermal', 'Neutrón rápido de alta energía']
        probabilidades_interaccion = [0.99, 0.95, 0.85, 0.6, 0.2]

        # Crear la gráfica
        fig, ax = plt.subplots()
        ax.barh(tipos_neutrones, probabilidades_interaccion, color='skyblue')
        ax.set_xlabel('Probabilidad de Interacción')
        ax.set_title('Tipos de Neutrones y Sus Propiedades')

        # Mostrar la gráfica en Streamlit
        st.pyplot(fig)