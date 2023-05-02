from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:id>/', UserDetailView.as_view(), name='user_detail'),
    path('add-user/', UserCreateView.as_view()),
]