from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'excerpt', 'body', 'published_at']

        # Blok widgets zajmuje się definicją pól w HTML. Tutaj można definiować typy wyświetlanych pół oraz zarządzać ich atrybutami.
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Game Title'}),
            'excerpt': TextInput(attrs={'class': 'form-control', 'placeholder': 'Publisher Name'}),
            'body': Textarea(attrs={'class': 'form-control', 'placeholder': 'Game Description'}),
            'published_at': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Date Of Request'}),
        }
