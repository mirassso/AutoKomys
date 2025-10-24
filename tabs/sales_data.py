import streamlit as st
import pandas as pd
import os

def run():
    st.header("Dane sprzedażowe")

    csv_file = "data/sales.csv"
    if not os.path.exists(csv_file):
        st.warning("Brak danych w bazie. Najpierw dodaj transakcje.")
        return

    df = pd.read_csv(csv_file)

    st.info("Możesz edytować tabelę, usuwać wiersze i zmieniać wartości. Po zakończeniu możesz zapisać zmiany do pliku CSV.")

    # Wyświetlenie edytowalnej tabeli
    edited_df = st.data_editor(
        df,
        num_rows="dynamic",  # pozwala dodawać/usuwac wiersze
        use_container_width=True
    )

    # Zapis do CSV po kliknięciu przycisku
    if st.button("Zapisz zmiany do CSV"):
        edited_df.to_csv(csv_file, index=False)
        st.success("Plik CSV został zaktualizowany!")
