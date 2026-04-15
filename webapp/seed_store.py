#!/usr/bin/env python
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings')
sys.path.insert(0, os.path.dirname(__file__))
django.setup()

from main.models import Game, Purchase
from django.contrib.auth.models import User

# Featured games for the store
featured_games = [
    {
        'title': 'Cyberpunk 2077',
        'slug': 'cyberpunk-2077',
        'short_description': 'Immerse yourself in a dystopian metropolis driven by oppressive megacorporations.',
        'price': '199.99',
        'image': 'games/cybb.jpg',
        'is_featured': True,
    },
    {
        'title': 'The Witcher 3: Wild Hunt',
        'slug': 'the-witcher-3',
        'short_description': 'Play as Geralt of Rivia, a legendary monster hunter, in an open world filled with danger.',
        'price': '79.99',
        'image': 'games/w3.png',
        'is_featured': True,
    },
    {
        'title': 'Hades',
        'slug': 'hades',
        'short_description': 'Defy the god of the Dead in this roguelike dungeon crawler with stunning art style.',
        'price': '24.99',
        'image': 'games/hades.png',
        'is_featured': True,
    },
    {
        'title': 'Stardew Valley',
        'slug': 'stardew-valley',
        'short_description': 'Escape to the countryside and rebuild your life in this relaxing farming simulator.',
        'price': '14.99',
        'image': 'games/sv.png',
        'is_featured': True,
    },
    {
        'title': 'Hollow Knight',
        'slug': 'hollow-knight',
        'short_description': 'Explore a beautiful, mysterious kingdom as a tiny knight filled with ancient darkness.',
        'price': '14.99',
        'image': 'games/hk.png',
        'is_featured': True,
    },
]

print("=" * 60)
print("SEEDING FEATURED GAMES FOR STORE")
print("=" * 60)

created_count = 0
for game_data in featured_games:
    game, created = Game.objects.update_or_create(
        slug=game_data['slug'],
        defaults={
            'title': game_data['title'],
            'short_description': game_data['short_description'],
            'price': game_data['price'],
            'image': game_data.get('image', ''),
            'is_featured': game_data['is_featured'],
            'is_active': True,
        }
    )
    
    if created:
        print(f"✓ Created: {game.title}")
        created_count += 1
    else:
        print(f"✓ Updated: {game.title}")
        created_count += 1

print(f"\n{created_count} new games added to store!")

# Show store games
print("\n" + "=" * 60)
print("FEATURED GAMES IN STORE")
print("=" * 60)
store_games = Game.objects.filter(is_featured=True, is_active=True)
for game in store_games:
    print(f"• {game.title} - {game.price} PLN")

# Show user library (purchases)
print("\n" + "=" * 60)
print("USER PURCHASES")
print("=" * 60)
try:
    testuser = User.objects.get(username='testuser')
    purchases = Purchase.objects.filter(user=testuser)
    print(f"testuser: {purchases.count()} games")
    for purchase in purchases:
        print(f"  • {purchase.game.title}")
except User.DoesNotExist:
    print("testuser not found")

print("\n" + "=" * 60)
print("✓ STORE SEEDING COMPLETE!")
print("=" * 60)
