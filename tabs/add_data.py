import streamlit as st
import pandas as pd
import os

def run():
    st.header("Dodaj nową transakcję")

    csv_file = "data/sales.csv"
    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)
        existing_models = df["model"].unique().tolist()
    else:
        df = pd.DataFrame()
        existing_models = []

    typed_model = st.text_input("Model samochodu (wpisz lub wybierz z listy)")

    # Lista zawsze widoczna, filtrowana dynamicznie
    suggestions = [m for m in existing_models if typed_model.lower() in m.lower()] if typed_model else existing_models
    selected_model = None
    img_path = ""

    # Selectbox do wyboru istniejącego modelu
    if suggestions:
        selected_model = st.selectbox("Wybierz model z bazy (jeśli istnieje):", suggestions)
        img_path = df.loc[df["model"] == selected_model, "img_path"].iloc[0] if not df.empty else ""
    else:
        # Jeśli nie ma sugestii, traktujemy wpisany tekst jako nowy model
        selected_model = typed_model
        file_name = st.text_input("Nazwa pliku zdjęcia (np. Asea_29)")
        img_path = f"data/img/{file_name}.jpg" if file_name else ""

    typ_transakcji = st.selectbox("Typ transakcji", ["Zakup", "Sprzedaż"])
    wartosc = st.number_input("Wartość transakcji ($)", min_value=0)
    data = st.date_input("Data transakcji")
    auto_wymienione = st.text_input("Auto wymienione (jeśli dotyczy)")
    komentarz = st.text_area("Komentarz")

    # Tylko kliknięcie przycisku zapisuje transakcję
    if st.button("Dodaj transakcję"):
        if not selected_model:
            st.error("Podaj nazwę modelu lub wybierz z listy istniejący.")
        elif not img_path:
            st.error("Podaj nazwę pliku zdjęcia dla nowego modelu.")
        else:
            new_row = {
                "model": selected_model,
                "typ_transakcji": typ_transakcji,
                "wartosc": wartosc,
                "data": data.strftime("%d.%m.%Y"),
                "auto_wymienione": auto_wymienione,
                "komentarz": komentarz,
                "img_path": img_path
            }

            if not df.empty:
                df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            else:
                df = pd.DataFrame([new_row])

            df.to_csv(csv_file, index=False)
            st.success(f"Transakcja dla {selected_model} została dodana!")
            st.write(f"Ścieżka do obrazka: {img_path}")
