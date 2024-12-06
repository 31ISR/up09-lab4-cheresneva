from django.contrib import admin
from django.urls import path
from . import views

app_name = 'communities'

urlpatterns = [
    path('', views.communities_list),
]

urlpatterns = [
    path('', views.communities_list, name="list"),
    path('<slug:slug>', views.communities_page, name="page"),
]