from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .forms import *
from .models import *
from http.client import HTTPResponse
from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView

class SignUp(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
    success_message = 'Учетная запись создана'

class Login(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('home')

class Logout(LogoutView):
    template_name = 'logout.html'
    next_page = reverse_lazy('home')

class CategoriesView(ListView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'categories'

class AboutCategoryView(DetailView):
    model = Category
    template_name = 'about_category.html'
    context_object_name = 'category'

class CreateCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'create_category.html'
    success_url = reverse_lazy('categories')

class ToDoView(ListView):
    model = ToDoList
    template_name = 'home.html'
    context_object_name = 'items'

    """def queryset(self, request):
        qs = super(ToDoList, self).queryset(request)
        return qs.filter(user=request.user)"""

def update(request, pk):
    action = ToDoList.objects.get(id=pk)
    action.active = not action.active
    action.save()
    return redirect('home')

class ToDoDetailView(DetailView):
    model = ToDoList
    template_name = 'about.html'
    context_object_name = 'item'

class ToDoCreateView(CreateView):
    model = ToDoList
    form_class = ToDoForm
    template_name = 'create.html'
    success_url = reverse_lazy('home')

class ToDoDeleteView(DeleteView):    
    model = ToDoList
    template_name = 'delete.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('home')