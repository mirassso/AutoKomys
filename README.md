# AutoKomys - Aplikacja komisu samochodowego

Aplikacja webowa do zarządzania sprzedażą i zakupami samochodów w komisie. Pozwala na:  
- Dodawanie nowych transakcji (zakup/sprzedaż)  
- Wyszukiwanie samochodów po modelu, typie transakcji i dacie  
- Edytowanie danych sprzedażowych w tabeli

---

## 👀 Wygląd aplikacji

###Strona główna

<img width="791" height="748" alt="image" src="https://github.com/user-attachments/assets/8a6651ac-ddab-45c8-90a5-1bb18b99ca8c" />

###Wyszukiwanie

<img width="620" height="875" alt="image" src="https://github.com/user-attachments/assets/a5ed449f-0264-461f-b574-12f30aadcbc6" />


###Dane sprzedażowe

<img width="671" height="659" alt="image" src="https://github.com/user-attachments/assets/05510f9c-ee19-4129-8fd2-954622cd3672" />


###Dodawanie transakcji

<img width="659" height="754" alt="image" src="https://github.com/user-attachments/assets/6246ba24-b785-449c-b154-f33cf2e8bfad" />


## 📦 Wymagania

- Python 3.10 lub nowszy  
- Biblioteki Python zapisane w pliku `requirements.txt`. Instalacja:

```
pip install -r requirements.txt
```

---

## 🚀 Uruchamianie aplikacji

### 1. Standardowo przez terminal
1. Sklonuj repozytorium lub pobierz pliki:

```
git clone https://github.com/TWOJA_NAZWA/komis-samochodowy.git
cd komis-samochodowy
```

2. Zainstaluj zależności:

```
pip install -r requirements.txt
```

3. Uruchom aplikację:

```
streamlit run app.py
```

Aplikacja otworzy się w przeglądarce (np. `http://localhost:8501`).

### 2. Uruchomienie jednym kliknięciem (Windows)

- W katalogu głównym znajduje się plik `run_app.exe`.  
- Po dwukrotnym kliknięciu otworzy się aplikacja w przeglądarce.

---

## 📝 Struktura aplikacji

```
app.py                 # Główny plik aplikacji
tabs/                  # Zakładki aplikacji
  home.py              # Strona główna
  search.py            # Wyszukiwanie samochodów
  sales_data.py        # Edytowalna tabela sprzedaży
  add_data.py          # Dodawanie transakcji
data/
  sales.csv            # Plik z danymi o transakcjach
  img/                 # Zdjęcia samochodów
img/
  home.jpg             # Obrazek nagłówka strony głównej
requirements.txt       # Lista wymaganych bibliotek
start_app.bat          # Plik do uruchomienia aplikacji jednym kliknięciem
```

---

## ⚙️ Instrukcja korzystania

### Strona główna
- Wyświetla powitalny obrazek i krótkie wprowadzenie.

### Wyszukiwanie
- Pole tekstowe do wpisania modelu samochodu.  
- Lista rozwijalna podpowiada istniejące modele w bazie.  
- Filtry dodatkowe: typ transakcji i zakres dat.  
- Wyniki wyświetlane są na bieżąco, wraz ze zdjęciami samochodów.

### Dane sprzedażowe
- Edytowalna tabela wszystkich transakcji.  
- Możesz poprawiać wartości, usuwać wiersze lub dodawać nowe.  
- Po kliknięciu „Zapisz zmiany do CSV” wszystkie modyfikacje zostaną zapisane do pliku `sales.csv`.

### Dodawanie transakcji
- Możesz wpisać nowy model samochodu lub wybrać istniejący z listy.  
- Wypełnij pola: typ transakcji, wartość, data, auto wymienione, komentarz.  
- Zdjęcie samochodu pobierane jest automatycznie dla istniejących modeli lub dodajesz nazwę pliku dla nowego auta. Należy wtedy zapisać zdjęcie tego samochodu zachowując odpowiednią nazwę i format (.jpg), a następnie umieścić je w folderze `data/img/`.  
- Kliknij „Dodaj transakcję”, aby zapisać wiersz z danymi do pliku CSV.


---

## 📂 Uwagi
- Wszystkie zdjęcia samochodów powinny znajdować się w folderze `data/img/` i mieć rozszerzenie .jpg.   
- Plik CSV `data/sales.csv` musi istnieć, aby działanie zakładek było poprawne.

---

✅ Uruchomienie na innym komputerze:
1. Sklonuj repozytorium.  
2. Zainstaluj Python i wymagane biblioteki z `requirements.txt`.  
3. Uruchom plik `start_app.bat` znajdujący się w folderze głównym projektu lub wpisz skorzystaj z komendy `streamlit run app.py`.
