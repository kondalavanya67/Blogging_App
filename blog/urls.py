from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
urlpatterns = [
    path('create_story/', views.create_story, name="create_story"),
    path('blog/', views.blog_display, name='blog'),

]
