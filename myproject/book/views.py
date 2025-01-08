from django.shortcuts import render
from .forms import BookForm

def input_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            # Procesar los datos del formulario
            titulo = form.cleaned_data['titulo']
            autor = form.cleaned_data['autor']
            valor = form.cleaned_data['valor']
            # Aquí puedes guardar los datos en la base de datos o hacer lo que necesites.
            return render(request, 'book/success.html', {'titulo': titulo, 'autor': autor, 'valor': valor})
    else:
        form = BookForm()
    return render(request, 'book/inputbook.html', {'form': form})
