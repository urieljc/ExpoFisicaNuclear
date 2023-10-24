import streamlit as st
from PIL import Image

def app():
    st.title("Super - Kamiokande")
    img_cherenkov=Image.open('img/kamiokande.jpg')
    st.image(img_cherenkov)
    st.write("El Super-Kamiokande es un detector de neutrinos ubicado en la Prefectura de Gifu, Japón. Es un experimento a gran escala diseñado para detectar y estudiar neutrinos procedentes del espacio exterior, así como de la atmósfera terrestre. ")
    st.write("Algunos puntos clave sobre el Super-Kamiokande son: ")
    st.write("Objetivo del experimento: El principal objetivo del Super-Kamiokande es estudiar los neutrinos provenientes de diversas fuentes, incluyendo el sol, así como los producidos por rayos cósmicos en la atmósfera terrestre. Estos estudios permiten a los científicos investigar fenómenos astrofísicos y mejorar la comprensión de la física de partículas.")
    st.write("Diseño y estructura: El detector Super-Kamiokande es un tanque cilíndrico gigante lleno de agua ultra pura y rodeado por un conjunto de detectores fotomultiplicadores sensibles a la luz. Cuando los neutrinos interactúan con el agua, producen destellos de luz, que son detectados por los fotomultiplicadores y registrados para su posterior análisis.")
    st.write("Contribuciones científicas: El Super-Kamiokande ha contribuido significativamente a la comprensión de la oscilación de neutrinos, un fenómeno que implica la transformación de un tipo de neutrino en otro durante su viaje a través del espacio. Este descubrimiento revolucionó nuestra comprensión de las propiedades de los neutrinos y les valió a los investigadores el Premio Nobel de Física en 2015.")
    img_cherenkov=Image.open('img/kamio-interior.jpg')
    st.image(img_cherenkov,width=300)
    st.subheader("Uso de Gadolinio",anchor=False)
    st.write(" En el detector Super-Kamiokande, el gadolinio se utiliza como un agente de detección de neutrones. El gadolinio es un elemento que tiene una alta sección eficaz para la captura de neutrones térmicos y rápidos, seguido de la emisión de rayos gamma. Esta propiedad permite que el Super-Kamiokande mejore su capacidad para detectar neutrones que se generan como productos secundarios de las interacciones de los neutrinos con los núcleos atómicos en el agua del detector.")
    st.write("El uso de gadolinio en el Super-Kamiokande permite la detección de neutrones con alta eficiencia y precisión. Esto es especialmente útil en la identificación de eventos de oscilación de neutrinos, así como en la identificación y separación de eventos de fondo de rayos cósmicos y otras fuentes de ruido.")
    st.write("Esta mejora en la detección de neutrones ha permitido al Super-Kamiokande aumentar su sensibilidad y precisión en la observación y estudio de los neutrinos, lo que ha llevado a avances significativos en el campo de la física de partículas y la astrofísica")
    img_cherenkov=Image.open('img/gadolinio.jpg')
    st.image(img_cherenkov,width=500)
    st.subheader("Herramientas que se utilizo para obtencion de datos de Super-Kamiokande")
    root_img=Image.open('img/root.jpg')
    st.image(root_img,width=500)
    with st.expander("ROOT"):
        st.write("ROOT es una plataforma de software desarrollada en el CERN (Organización Europea para la Investigación Nuclear) que proporciona herramientas para análisis de datos, visualización y almacenamiento de datos, especialmente diseñada para aplicaciones en física de partículas y experimentos de alta energía. Fue originalmente desarrollada por el laboratorio de física de partículas del CERN para manejar grandes conjuntos de datos producidos por experimentos de física de partículas.")
    geant4_img=Image.open('img/geant4.png')
    st.image(geant4_img,width=500)
    with st.expander("Geant4"):
        st.write("Geant4 es un conjunto de herramientas de software de simulación de eventos de alta energía y aplicación general, desarrollado y mantenido por el CERN (Organización Europea para la Investigación Nuclear). Se utiliza principalmente en la simulación de la interacción de partículas con la materia en una amplia gama de experimentos de física de partículas, física nuclear, física médica, así como en aplicaciones espaciales y de detección.")
    wcsim_img=Image.open('img/WCSim.png')
    st.image(wcsim_img,width=500)
    with st.expander("WCSim"):
        st.write("WCSim es un software de simulación utilizado para simular detectores de agua Cherenkov, como el Super-Kamiokande y otros detectores similares. Estos detectores utilizan el efecto Cherenkov para detectar partículas cargadas, como los neutrinos, que interactúan con el agua y producen radiación Cherenkov en el proceso. WCSim permite simular cómo se comportarían las partículas en estos detectores y cómo se registrarían los eventos.")
    corsika=Image.open('img/corsika.png')
    st.image(corsika,width=500)
    with st.expander("Corsika"):
        st.write("CORSIKA (Cosmic Ray Simulation for KASCADE) es un software ampliamente utilizado en la simulación de cascadas atmosféricas extendidas causadas por rayos cósmicos de alta energía. Este software es fundamental para la investigación en el campo de la astrofísica y la física de partículas, ya que ayuda a comprender la interacción de los rayos cósmicos con la atmósfera de la Tierra y el subsuelo.")