from django.urls import path
from .views import *

urlpatterns = [
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:id>/', BookDetailView.as_view(), name='book_detail'),
    path('add-book/', create_book, name='book_create'),
    path('booklist/', BookAPIView.as_view())
]