from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import Purchase
from django.views.generic import ListView, DetailView, CreateView
from rest_framework import generics
from .serializers import PurchaseSerializer

class PurchaseListView(ListView):
    model = Purchase
    template_name = 'purchase/purchase_list.html'
    context_object_name = 'purchases'

class PurchaseDetailView(DetailView):
    model = Purchase
    template_name = 'purchase/purchase_detail.html'
    context_object_name = 'purchase'
    pk_url_kwarg = 'id'

class PurchaseAPIView(generics.ListAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer