## Instalacja i uruchomienie

```bash
#1. Sklonuj repozytorium
git clone https://github.com/alpinetina/ImageClassification
cd ImageClassification

#2. Stwórz i aktywuj środowisko wirtualne
python -m venv venv
source venv/bin/activate

#3. Zainstaluj zależności
pip install -r requirements.txt

#4. Uruchom aplikację Flask
python app.py
```

Aplikacja będzie dostępna pod adresem:  
**http://127.0.0.1:5000**

---
### Trenowanie modelu

1. Przejdź do strony: [http://127.0.0.1:5000](http://127.0.0.1:5000)
2. W formularzu "Train model" kliknij **Train**  
   _(model zostanie wytrenowany na danych w `pistachio_dataset/`)_

### Klasyfikacja obrazu

1. W formularzu "Upload image to classify" wybierz plik obrazu
2. Kliknij **Classify** – pojawi się etykieta przypisana przez model
