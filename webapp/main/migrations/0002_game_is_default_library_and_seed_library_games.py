from django.db import migrations, models


def seed_default_library_games(apps, schema_editor):
    Game = apps.get_model('main', 'Game')

    default_games = [
        {
            'title': 'Dragon Age: Origins',
            'slug': 'dragon-age-origins-library',
            'short_description': 'Classic fantasy RPG with rich party-based storytelling.',
            'price': '79.99',
            'is_default_library': True,
            'is_featured': False,
            'is_active': True,
        },
        {
            'title': 'The Outlast Trials',
            'slug': 'the-outlast-trials-library',
            'short_description': 'Co-op survival horror set in a disturbing experiment facility.',
            'price': '119.99',
            'is_default_library': True,
            'is_featured': False,
            'is_active': True,
        },
        {
            'title': 'Elden Ring',
            'slug': 'elden-ring-library',
            'short_description': 'Open-world action RPG focused on exploration and challenging combat.',
            'price': '249.99',
            'is_default_library': True,
            'is_featured': False,
            'is_active': True,
        },
        {
            'title': 'Rimworld',
            'slug': 'rimworld-library',
            'short_description': 'Story generator colony sim where every run is unique.',
            'price': '139.99',
            'is_default_library': True,
            'is_featured': False,
            'is_active': True,
        },
    ]

    for game_data in default_games:
        game, created = Game.objects.get_or_create(
            slug=game_data['slug'],
            defaults=game_data,
        )
        if not created:
            game.is_default_library = True
            game.is_featured = False
            game.is_active = True
            game.save(update_fields=['is_default_library', 'is_featured', 'is_active'])


def unseed_default_library_games(apps, schema_editor):
    Game = apps.get_model('main', 'Game')
    slugs = [
        'dragon-age-origins-library',
        'the-outlast-trials-library',
        'elden-ring-library',
        'rimworld-library',
    ]
    Game.objects.filter(slug__in=slugs).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='is_default_library',
            field=models.BooleanField(default=False),
        ),
        migrations.RunPython(seed_default_library_games, unseed_default_library_games),
    ]
