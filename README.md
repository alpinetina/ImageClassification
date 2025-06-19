## Zbiór danych

Użyty zbiór danych pochodzi z Kaggle:  
🔗 [https://www.kaggle.com/datasets/muratkokludataset/pistachio-image-dataset](https://www.kaggle.com/datasets/muratkokludataset/pistachio-image-dataset)

### Przygotowanie danych:

1. Przejdź do [zestawu danych](https://www.kaggle.com/datasets/muratkokludataset/pistachio-image-dataset)
2. Kliknij **Download**
3. Wypakuj plik `.zip` na dysk
4. Zmień strukturę folderów tak, aby wyglądała następująco:

```
pistachio_dataset/
└── Pistachio_Image_Dataset/
    ├── Kirmizi_Pistachio/
    └── Siirt_Pistachio/
```

📌 **Uwaga:** Jeśli po wypakowaniu widzisz zagnieżdżenie `Pistachio_Image_Dataset/Pistachio_Image_Dataset/...`, przenieś foldery `Kirmizi_Pistachio` i `Siirt_Pistachio` o jeden poziom wyżej.

---
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
   _(model zostanie wytrenowany na danych w `pistachio_dataset/`; jeśli nie - wpisz: pistachio_dataset/Pistachio_Image_Dataset)_

### Klasyfikacja obrazu

1. W formularzu "Upload image to classify" wybierz plik obrazu
2. Kliknij **Classify** – pojawi się etykieta przypisana przez model
