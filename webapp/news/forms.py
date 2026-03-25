from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'excerpt', 'body', 'published_at']

        # Blok widgets zajmuje się definicją pól w HTML. Tutaj można definiować typy wyświetlanych pół oraz zarządzać ich atrybutami.
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'excerpt': TextInput(attrs={'class': 'form-control', 'placeholder': 'Game Name'}),
            'body': Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe Your Bug'}),
            'published_at': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Date Of Publication'}),
        }

class RequestGameForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'excerpt', 'body']

        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Nickname'}),
            'excerpt': TextInput(attrs={'class': 'form-control', 'placeholder': 'Game Title'}),
            'body': Textarea(attrs={'class': 'form-control', 'placeholder': 'Why should we add this game?', 'rows': 4}),
        }