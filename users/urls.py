#Django modules
from django.urls import path
from django.views.generic import TemplateView

from users import views

urlpatterns = [

    #posts
    path(
        route='profile/<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),

    #users
    path(
        route='login/',
        view=views.login_view,
        name='login'
    ),

    path(
        route='users/logout/',
        view=views.logout_view,
        name='logout'
    ),

    path(
        route='signup/',
        view=views.signup_view,
        name='signup'
    ),

    path(
        route='users/me/profile',
        view=views.update_profile,
        name='update_profile'
    ),
]