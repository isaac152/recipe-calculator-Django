from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

from django.urls import path
from .views import SignUp,Login,Index,Profile_ListView

urlpatterns = [
    path(
        route='',
        name='index',
        view=Index.as_view()
    ),

    #User managment
    path(
        route='signup/',
        name='signup',
        view=SignUp.as_view()
    ),
    path(
        route='login/',
        name='login',
        view=Login.as_view()

    ),
        path(
        route='logout/',
        name='logout',
        view= login_required(LogoutView.as_view(
            next_page=None
        )),
    ),
    path(
        route= 'profile/',
        name='profile',
        view=login_required(Profile_ListView.as_view())
    ),
]