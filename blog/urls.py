from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from.views import create_story
urlpatterns = [
    path('create_story/', create_story, name="create_story"),

]
