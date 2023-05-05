from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    # path('users/', UserListView.as_view(), name='user_list'),
    # path('users/<int:id>/', UserDetailView.as_view(), name='user_detail'),
    # path('add-user/', UserCreateView.as_view()),
    # path('userlist/', UserAPIView.as_view()),
    path('api/', include(router.urls)),
]