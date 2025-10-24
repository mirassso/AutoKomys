import streamlit as st
import pandas as pd
import os

def run():
    st.header("Wyszukiwanie samochodów")

    csv_file = "data/sales.csv"
    if not os.path.exists(csv_file):
        st.warning("Brak danych w bazie. Najpierw dodaj transakcje.")
        return

    df = pd.read_csv(csv_file)
    existing_models = df["model"].unique().tolist()

    # --- Pole modelu z podpowiedzią ---
    typed_model = st.text_input("Wpisz nazwę modelu:")

    # Lista rozwijalna z opcją "Dowolny"
    if typed_model:
        suggestions = [m for m in existing_models if typed_model.lower() in m.lower()]
        suggestions = ["Dowolny"] + suggestions if suggestions else ["Dowolny"]
    else:
        suggestions = ["Dowolny"] + existing_models

    selected_model = st.selectbox("Wybierz model z listy:", suggestions)

    if selected_model == "Dowolny":
        selected_model = None
    elif not suggestions or typed_model and not suggestions[1:]:
        st.info("Brak pojazdu w bazie dla podanej nazwy.")

    # --- Filtry dodatkowe ---
    st.subheader("Filtry dodatkowe")
    typ_transakcji = st.selectbox("Typ transakcji", ["Wszystkie", "Zakup", "Sprzedaż"])
    
    # Zakres dat
    min_date = pd.to_datetime(df["data"], dayfirst=True).min()
    max_date = pd.to_datetime(df["data"], dayfirst=True).max()
    date_range = st.date_input("Zakres dat", [min_date, max_date])

    if isinstance(date_range, (tuple, list)):
        if len(date_range) == 2:
            start_date, end_date = date_range
        elif len(date_range) == 1:
            start_date = end_date = date_range[0]
        else:
            start_date = min_date
            end_date = max_date
    else:
        start_date = end_date = date_range

    # --- Filtrowanie danych ---
    filtered_df = df.copy()

    if selected_model:
        filtered_df = filtered_df[filtered_df["model"] == selected_model]

    if typ_transakcji != "Wszystkie":
        filtered_df = filtered_df[filtered_df["typ_transakcji"] == typ_transakcji]

    filtered_df["data_dt"] = pd.to_datetime(filtered_df["data"], dayfirst=True)
    filtered_df = filtered_df[(filtered_df["data_dt"] >= pd.to_datetime(start_date)) &
                              (filtered_df["data_dt"] <= pd.to_datetime(end_date))]

    if filtered_df.empty:
        st.info("Brak pojazdów pasujących do wybranych filtrów.")
        return

    # --- Sortowanie wyników ---
    st.subheader("Sortowanie wyników")
    sort_column = st.selectbox("Sortuj po:", ["data", "wartosc"])
    sort_order = st.radio("Kierunek:", ["Rosnąco", "Malejąco"])
    ascending = True if sort_order == "Rosnąco" else False
    filtered_df = filtered_df.sort_values(by=sort_column, ascending=ascending)
    
    st.subheader(f"Wyniki wyszukiwania ({len(filtered_df)})")

    # --- Wyświetlanie wyników w dwóch kolumnach ---
    for idx, row in filtered_df.iterrows():
        cols = st.columns([1, 2])
        with cols[0]:
            if pd.notna(row["img_path"]) and os.path.exists(row["img_path"]):
                st.image(row["img_path"], use_container_width=True)
            else:
                st.write("Brak zdjęcia")

        with cols[1]:
            st.markdown(f"{row['model']}")
            st.write(f"{row['data']}")
            st.write(f"{row['typ_transakcji']}")
            st.write(f"${row['wartosc']}")
            if pd.notna(row["auto_wymienione"]) and row["auto_wymienione"]:
                st.write(f"Auto wymienione: {row['auto_wymienione']}")
            if pd.notna(row["komentarz"]) and row["komentarz"]:
                st.text(f"Komentarz: {row['komentarz']}")
        st.markdown("---")
