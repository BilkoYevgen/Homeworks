from django.urls import include, path
from .views import PurchaseAPIView, PurchaseViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'purchases', PurchaseViewSet)

urlpatterns = [
    # path('purchases/', PurchaseListView.as_view(), name='purchase_list'),
    # path('purchases/<int:id>/', PurchaseDetailView.as_view(), name='purchase_detail'),
    # path('add-purchase/', PurchaseCreateView.as_view()),
    # path('purchaselist/', PurchaseAPIView.as_view()),
    # path('<int:pk>/', PurchaseViewSet.as_view({'get': 'list'})),
    path('api/', include(router.urls)),
]