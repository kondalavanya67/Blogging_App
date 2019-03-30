from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

app_name='registration'

urlpatterns = [
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('profile/',views.show_profile,name='show_profile'),
]
