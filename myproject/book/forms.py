from django import forms

from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['titulo', 'autor', 'valor']
        labels = {
            'titulo': 'Título',
            'autor': 'Autor',
            'valor': 'Valor (entre 1 y 10,000)',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Título del libro'}),
            'autor': forms.TextInput(attrs={'placeholder': 'Nombre del autor'}),
            'valor': forms.NumberInput(attrs={'placeholder': 'Valor (1-10,000)'}),
        }