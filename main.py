#importaciones de librerias
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie

#importaciones de archivos

st.set_page_config(
    page_title="Machine Learning par deteccion de Neutrones"
)

class Multiapp:
    def __init__(self) :
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
                options=["Inicio","Radiacion Cosmica","Neutrones","Detector Cherenkov","Hyper-Kamiokade","Machine Learning"],
                default_index=0,
                styles={
                    "container":{"padding":"5!important","background-color":"black"},
                    "icon":{"color":"white","font-size":"23px"},
                    "nav-link":{"color":"white","font-size":"20px","text-aling":"left","margin":"0px","--hover-color":"blue"},
                    "nav-link-selected":{"background-color":"#1582A9"}
                }
            )
            # if app=="Inicio":
            #     pages.home.app()
    run()