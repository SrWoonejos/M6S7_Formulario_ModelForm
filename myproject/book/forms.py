from django import forms

class BookForm(forms.Form):
    titulo = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Título'}),
        label="Título"
    )
    autor = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Autor'}),
        label="Autor"
    )
    valor = forms.IntegerField(
        required=True,
        min_value=1,
        max_value=10000,
        widget=forms.NumberInput(attrs={'placeholder': 'Valor'}),
        label="Valor (entre 1 y 10000)"
    )
