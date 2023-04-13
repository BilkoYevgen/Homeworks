from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from user.models import User


# Create your views here.
def get_users(request):
    item = User.objects.all()
    data = serializers.serialize('json', item)
    return JsonResponse(data, safe=False)