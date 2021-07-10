#Django modules
from django.urls import path
from django.views.generic import TemplateView

from users import views

urlpatterns = [


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
        view=views.SignUpView.as_view(),
        name='signup'
    ),

    path(
        route='users/me/profile',
        view=views.UpdateProfileView.as_view(),
        name='update_profile'
    ),
    #posts
    path(
        route='<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
]