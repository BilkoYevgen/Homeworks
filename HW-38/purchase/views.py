from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from purchase.models import Purchase

def get_purchases(request):
    item = Purchase.objects.all()
    data = serializers.serialize('json', item)
    return JsonResponse(data, safe=False)