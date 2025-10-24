import streamlit as st
from tabs import home, search, sales_data, add_data

# Konfiguracja aplikacji
st.set_page_config(
    page_title="AutoKomys",
    page_icon="🚗",
    layout="centered"
)

st.title("🚗 AutoKomys - Charlie Espresso")

# --- Zakładki ---
tab1, tab2, tab3, tab4 = st.tabs([
    "🏠 Strona główna",
    "🔍 Wyszukiwanie",
    "📊 Dane sprzedażowe",
    "➕ Dodawanie transakcji"
])

with tab1:
    home.run()

with tab2:
    search.run()

with tab3:
    sales_data.run()

with tab4:
    add_data.run()
