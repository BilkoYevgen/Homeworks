from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from user.models import User
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .forms import *


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