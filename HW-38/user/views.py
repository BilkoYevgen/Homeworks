from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .forms import *
from rest_framework import generics, viewsets, filters
from .serializers import UserSerializer
from rest_framework.pagination import PageNumberPagination
import django_filters

class UserListView(ListView):
    model = User
    template_name = 'user/user_list.html'
    context_object_name = 'users'

class UserDetailView(DetailView):
    model = User
    template_name = 'user/user_detail.html'
    context_object_name = 'user'
    pk_url_kwarg = 'id'

class UserCreateView(CreateView):
    model = User
    template_name = 'user/add_user.html'
    form_class = UserForm
    success_url = reverse_lazy('user_list')

class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CustomPaginator(PageNumberPagination):
    page_size_query_param = 'page_size'
    page_size = 10

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = {
            'first_name': ['exact', 'contains'],
            'age': ['gte', 'lte', 'gt', 'lt', 'exact']
        }
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPaginator
    filterset_class = UserFilter
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['age']