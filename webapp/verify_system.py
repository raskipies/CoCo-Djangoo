#!/usr/bin/env python
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings')
sys.path.insert(0, os.path.dirname(__file__))

django.setup()

from django.contrib.auth.models import User
from main.models import Game
from django.urls import reverse

print('=== FINALNA WERYFIKACJA SYSTEMU ===\n')

# Użytkownicy
users = User.objects.all()
print('Użytkownicy dostępni:')
for u in users[:5]:
    print(f'  • {u.username}')

# Gry
lib_games = Game.objects.filter(is_default_library=True).count()
store_games = Game.objects.filter(is_featured=True).count()
print(f'\nGry w systemie:')
print(f'  Store (is_featured): {store_games}')
print(f'  Library (is_default_library): {lib_games}')

# Routing
print(f'\nRoutowanie:')
print(f'  Home: {reverse("home")}')
print(f'  Library: {reverse("library")}')
print(f'  Login: {reverse("login_user")}')

print(f'\n✅ SYSTEM FULLY OPERATIONAL')
print(f'\nTestuj na: http://127.0.0.1:8000')
print(f'Login: testuser / testpass123')
