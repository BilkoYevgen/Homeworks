from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from purchase.models import Purchase
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from rest_framework.viewsets import ModelViewSet
from .forms import *
from rest_framework import generics, viewsets
from .serializers import PurchaseSerializer
import django_filters

class PurchaseListView(ListView):
    model = Purchase
    template_name = 'purchase/purchase_list.html'
    context_object_name = 'purchases'

class PurchaseDetailView(DetailView):
    model = Purchase
    template_name = 'purchase/purchase_detail.html'
    context_object_name = 'purchase'
    pk_url_kwarg = 'id'

class PurchaseCreateView(CreateView):
    model = Purchase
    template_name = 'purchase/add_purchase.html'
    form_class = PurchaseForm
    success_url = reverse_lazy('purchase_list')

class PurchaseAPIView(generics.ListAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

class PurchaseFilter(django_filters.FilterSet):
    class Meta:
        model = Purchase
        fields = {
            'user': ['exact'],
            'book': ['exact'],
            'date': ['exact', 'lte', 'gte']
        }
'''
На жаль, пошук тут не буде працювати корректно, через використання ForeignKey, для коректної роботи потрібно
використовувати CharField або TextField!!!
 
 Дані запити, працюють
http://127.0.0.1:8000/api/purchases/?user=1
http://127.0.0.1:8000/api/purchases/?book=2
http://127.0.0.1:8000/api/purchases/?date__gte=
http://127.0.0.1:8000/api/purchases/?ordering=date
'''
class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    filterset_class = PurchaseFilter
    search_fields = ['user', 'book']
    ordering_fields = ['date']