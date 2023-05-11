from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from book.models import Book
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from .forms import BookForm
from rest_framework import generics, viewsets
from .serializers import BookSerializer
import django_filters


# class BookListView(ListView):
#     model = Book
#     template_name = 'book/book_list.html'
#     context_object_name = 'books'
#
# class BookDetailView(DetailView):
#     model = Book
#     template_name = 'book/book_detail.html'
#     context_object_name = 'book'
#     pk_url_kwarg = 'id'
#
# def create_book(request):
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             book = form.save()
#             return redirect('book_detail', id=book.id)
#     else:
#         form = BookForm()
#     return render(request, 'book/add_book.html', {'form': form})

# class BookAPIView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'title': ['exact', 'contains'],
            'price': ['gte', 'lte', 'gt', 'lt', 'exact']}

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilter
    search_fields = ['title', 'author']
    ordering_fields = ['price']