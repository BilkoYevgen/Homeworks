from django.urls import path
from .views import *

urlpatterns = [
    path("books/", get_books)
]