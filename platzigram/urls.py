"""platzigram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views as local_views

urlpatterns = [

    path('admin/',admin.site.urls),
    #corremos nuestra paginas aqui
    path('hello-world/',local_views.hello_world),
    path('sorted-numbers/', local_views.sorted_numbers),
    path('hi/<str:name>/<int:age>',local_views.hi),

    #posts views
    path('', include(('posts.urls', 'posts'), namespace='posts')),
    
    #users views
    path('users/', include(('users.urls', 'users'), namespace='users')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
