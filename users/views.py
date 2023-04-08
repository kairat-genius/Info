from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from .utils import *
from .forms import *
from .models import *

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DeleteView, CreateView



class RegisterUser(DataMixin,CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('news')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return context | c_def

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return context | c_def


    def get_success_url(self):
        return reverse_lazy('index')

def logout_user(request):
    logout(request)
    return redirect('login')