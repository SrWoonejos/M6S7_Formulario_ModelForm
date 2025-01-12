from django.shortcuts import render, redirect
from .forms import BookForm

def input_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el libro en la base de datos
            return render(request, 'book/success.html', {'form': form})
    else:
        form = BookForm()
    return render(request, 'book/inputbook.html', {'form': form})