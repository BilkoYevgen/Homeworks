from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from book.models import Book


# Create your views here.
def get_books(request):
    item = Book.objects.all()
    data = serializers.serialize('json', item)
    return JsonResponse(data, safe=False)