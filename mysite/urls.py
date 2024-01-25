"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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


import ssl
from django import views
from django.contrib import admin
from django.urls import path,re_path
from restaurants.views import  menu,meta,list_restaurants,comment, year_archive
from mysite.views import welcome,add,math

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/',menu),
    path('welcome/',welcome),
    path('restaurants_list/',list_restaurants),
    #path('comment/',comment),
    path('comment/<int:id>/', comment, name='comment'),
    path('comment/', comment, name='comment_without_id'),

    ]