from django.urls import path
from .views import *

urlpatterns = [
    path('purchases/', PurchaseListView.as_view(), name='purchase_list'),
    path('purchases/<int:id>/', PurchaseDetailView.as_view(), name='purchase_detail'),
    path('add-purchase/', PurchaseCreateView.as_view()),
    path('purchaselist/', PurchaseAPIView.as_view())
]