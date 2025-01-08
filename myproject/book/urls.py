from django.urls import path
from .views import input_book

urlpatterns = [
    path('inputbook/', input_book, name='input_book'),
]
