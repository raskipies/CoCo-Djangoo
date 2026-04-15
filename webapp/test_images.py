#!/usr/bin/env python 
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings')
sys.path.insert(0, os.path.dirname(__file__))
django.setup()

from main.models import Game

print("=" * 60)
print("TESTING IMAGE URL GENERATION")
print("=" * 60)

game = Game.objects.filter(is_featured=True).first()
if game:
    print(f"\nGame: {game.title}")
    print(f"Image field value: '{game.image}'")
    print(f"Image URL (via .url): '{game.image.url if game.image else 'Empty'}'")
    print(f"Image name: '{game.image.name if game.image else 'None'}'")
    print(f"\nFile exists at: {game.image.path if game.image else 'N/A'}")
    if game.image:
        print(f"File actually exists: {os.path.exists(game.image.path)}")
else:
    print("No featured games found!")

print("\n" + "=" * 60)
print("CHECKING ALL FEATURED GAMES")
print("=" * 60)
for game in Game.objects.filter(is_featured=True):
    status = "✓" if game.image and os.path.exists(game.image.path) else "✗"
    print(f"{status} {game.title}: {game.image.name if game.image else 'NO IMAGE'}")
