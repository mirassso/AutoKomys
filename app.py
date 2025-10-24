import streamlit as st
from tabs import home, search, sales_data, add_data

# Konfiguracja aplikacji
st.set_page_config(
    page_title="AutoKomys",
    page_icon="🚗",
    layout="centered"
)

# Tytuł
st.title("AutoKomys")

tabs = ["Strona główna", "Wyszukiwanie", "Dane sprzedażowe", "Dodawanie transakcji"]
selected_tab = st.radio("Wybierz zakładkę:", tabs, horizontal=True)

# Wywołanie zakładki
if selected_tab == "Strona główna":
    home.run()
elif selected_tab == "Wyszukiwanie":
    search.run()
elif selected_tab == "Dane sprzedażowe":
    sales_data.run()
elif selected_tab == "Dodawanie transakcji":
    add_data.run()
