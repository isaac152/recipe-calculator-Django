#General import
from django.urls import reverse_lazy
from django.shortcuts import redirect
#View import 

from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView

#Forms import 
from .forms import SignUpForm

class SignUp(CreateView):
    template_name='register.html'
    success_url = reverse_lazy('users:login')
    form_class = SignUpForm
    

class Login(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('home')

class Index(TemplateView):
    template_name='index.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)