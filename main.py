#importacion de librerias a utilizar
import streamlit as st
from streamlit_option_menu import option_menu
#importacion de paginas externas
import paginas.home,paginas.cosmicos,paginas.neutrones,paginas.cherenkov ,paginas.kamiokande# noqa: E401

st.set_page_config(
    page_title="Machine Learning para deteccion de Neutrino"
)

class MultiApp:
    def __init__(self):
        self.apps=[]
    def add_app(self,title,function):
        self.apps.append({
            "title":title,
            "function":function
        })
    def run():
        with st.sidebar:
            app=option_menu(
                menu_title="Contenido",
                options=["Inicio","Radiacion Cosmica","Neutrones","Detector Cherenkov","Super-Kamiokande","Machine Learning"],  # noqa: E501
                default_index=1,
                styles={
                    "container":{"padding":"5!important","background-color":'black'},
                    "icon":{
                        "color":"white","font-size":"23px"
                    },
                    "nav-link":{
                        "color":"white","font-size":"20px","text-aling":"left","margin":"0px","--hover-color":"blue"
                    },
                    "nav-link-selected":{"background-color":"#2F6CA6"},
                }
            )
        if app=="Inicio":
            paginas.home.app()
        if app=="Radiacion Cosmica":
            paginas.cosmicos.app()
        if app=="Neutrones":
            paginas.neutrones.app()
        if app=="Detector Cherenkov":
            paginas.cherenkov.app()
        if app=="Super-Kamiokande":
            paginas.kamiokande.app()
    run()