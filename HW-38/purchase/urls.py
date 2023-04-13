from django.urls import path
from .views import *

urlpatterns = [
    path("purchases/", get_purchases)
]