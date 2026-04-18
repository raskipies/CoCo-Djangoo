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
   cd CoCo-Djangoo
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

## 👤 Tworzenie konta administratora
1. **Upewnij się, że jesteś w folderze z plikiem manage.py:**
   ```bash
   cd webapp
   ```
2. **Uruchom komendę tworzenia użytkownika:**
   ```bash
   # Windows:
   python manage.py createsuperuser
   # Linux / macOS:
   python3 manage.py createsuperuser
   ```
3. **Postępuj zgodnie z instrukcjami w terminalu:**
- Username: Wpisz nazwę administratora (np. admin) i naciśnij Enter.
- Email address: Możesz zostawić puste i nacisnąć Enter.
- Password: Wpisz hasło. WAŻNE: Podczas wpisywania hasła w terminalu znaki nie będą widoczne!
- Password (again): Powtórz hasło i naciśnij Enter.

## 🛠️ Jak wejść do Panelu Administratora?
1. **Uruchom serwer: Upewnij się, że jesteś w folderze webapp w terminalu i masz włączone środowisko wirtualne, a następnie wpisz:**
   ```bash
   python manage.py runserver
   ```
2. **Otwórz przeglądarkę: Wpisz adres lokalny aplikacji: http://127.0.0.1:8000/**

3. **Przejdź do panelu: Dopisz na końcu adresu /admin, aby uzyskać:**
- http://127.0.0.1:8000/admin

4. **Zaloguj się: Użyj danych konta superużytkownika (instrukcja tworzenia konta znajduje się powyżej).**

## 📁 Struktura Projektu
- `webapp/` - główny folder projektu Django
- `main/` - obsługa sklepu i biblioteki
- `news/` - system artykułów i bugów
- `forum/` - moduł społecznościowy
- `media/` - pliki przesłane przez użytkowników (gry, bugi, forum)
- `static/` - pliki CSS i assety graficzne

---
*Projekt stworzony w ramach nauki frameworka Django.*
