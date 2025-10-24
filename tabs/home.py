import streamlit as st
import os

def run():
    img_path = os.path.join("img", "home.jpg")
    if os.path.exists(img_path):
        st.image(img_path, use_container_width=True)
    else:
        st.warning("Brak obrazka home.jpg w folderze img.")
    st.write("Witamy w aplikacji komisu samochodowego Charliego Espresso 🚗")
    st.write("Wybierz zakładkę, z której chcesz skorzystać.")

