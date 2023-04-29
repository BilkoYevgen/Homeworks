from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'year', 'price']
        labels = {
            'title': 'Назва',
            'author': 'Автор',
            'year': 'Рік',
            'price': 'Ціна',
        }
