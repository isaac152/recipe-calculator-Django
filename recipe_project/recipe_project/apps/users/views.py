#General import
from django.urls import reverse_lazy
from django.shortcuts import redirect

#model import
from ..recipes.models import Recipe
from ..users.models import Profile

#View import 
from django.views.generic import CreateView, ListView
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView

#Forms import 
from .forms import SignUpForm

class SignUp(CreateView):
    template_name='users/register.html'
    success_url = reverse_lazy('users:login')
    form_class = SignUpForm
    

class Login(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('home')

class Index(TemplateView):
    template_name='index.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


class Profile_ListView(ListView):
    model = Recipe
    paginate_by = 4
    template_name = "users/profile.html"
    context_object_name = "recipes"

    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)
        queryset = Recipe.objects.filter(profile_id = profile.id)
        return queryset
    

