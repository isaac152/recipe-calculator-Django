#General import
from django.shortcuts import redirect
#View import 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView


class Home(LoginRequiredMixin,TemplateView):
    template_name='home.html'
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('users:index')
        return super().dispatch(request, *args, **kwargs)