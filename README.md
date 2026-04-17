# CoCo-Djangoo 🎮

Kompleksowy system platformy gamingowej zbudowany w oparciu o framework Django. Projekt łączy w sobie funkcjonalności sklepu z grami, biblioteki użytkownika, systemu newsów oraz forum społecznościowego.

## 🚀 Główne Funkcjonalności

### 🛒 Sklep z Grami (`main`)
- Przeglądanie dostępnych gier w responsywnym interfejsie.
- System zakupów z weryfikacją posiadania gry.
- Dynamiczne karty gier z cenami i opisami.
- Możliwość zgłaszania prośby o dodanie nowej gry do bazy.

### 📚 Biblioteka Użytkownika (`main`)
- Zarządzanie zakupionymi grami.
- Wyświetlanie szczegółów gier przypisanych do konta.

### 📰 System Newsów i Bugów (`news`)
- Publikacja artykułów i aktualności ze świata gier.
- **System zgłaszania błędów (Bugs):** Użytkownicy mogą zgłaszać problemy w konkretnych grach, dodawać opisy i zrzuty ekranu.
- Możliwość komentowania zgłoszonych błędów.

### 💬 Forum Społecznościowe (`forum`)
- Tworzenie postów tekstowych z załącznikami (zdjęcia/pliki).
- Interakcje: polubienia (likes) oraz system komentarzy pod postami.
- Sekcja najczęściej zadawanych pytań (FAQ).

## 🛠️ Technologia

- **Backend:** Python + Django 5.1
- **Baza danych:** SQLite3
- **Frontend:** HTML5, CSS3 (Custom styles), JavaScript (Fetch API dla transakcji)
- **Obsługa mediów:** Pillow (przetwarzanie obrazów gier i postów)

## ⚙️ Instalacja i Uruchomienie

### Wymagania
- Python 3.10+
- pip (menedżer pakietów)

### Kroki instalacji
1. **Sklonuj repozytorium**
2. **Utwórz i aktywuj środowisko wirtualne:**
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # Linux/macOS:
   source .venv/bin/activate
   ```
3. **Zainstaluj zależności:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Wykonaj migracje bazy danych:**
   ```bash
   cd webapp
   python manage.py migrate
   ```
5. **(Opcjonalnie) Zasil bazę danymi demo:**
   ```bash
   python seed_store.py
   ```
6. **Uruchom serwer deweloperski:**
   ```bash
   python manage.py runserver
   ```

Aplikacja będzie dostępna pod adresem: `http://127.0.0.1:8000/`

## 👤 Konta Testowe (jeśli użyto seeda)
- **Admin:** `admin` / `admin`
- **User:** `testuser` / `testpass123`

## 📁 Struktura Projektu
- `webapp/` - główny folder projektu Django
- `main/` - obsługa sklepu i biblioteki
- `news/` - system artykułów i bugów
- `forum/` - moduł społecznościowy
- `media/` - pliki przesłane przez użytkowników (gry, bugi, forum)
- `static/` - pliki CSS i assety graficzne

---
*Projekt stworzony w ramach nauki frameworka Django.*
